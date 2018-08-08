# -*- Coding: utf-8 -*-

from serial import Serial
# from time import sleep


class FGC():

    def __init__(self,port1='COM5'):
        self._port          = port1
        self._baudrate      = 9600
        self._bytesize      = 8
        self._parity        = 'N'
        self._stopbits      = 1
        self._timeout       = None
        self._xonxoff       = False
        self._rtscts        = False
        self._writeTimeout  = None
        self._dsrdtr        = False

    def connect(self):

        try:

            self.com = Serial(
                  port = self._port,
                  baudrate = self._baudrate,
                  bytesize = self._bytesize,
                  parity = self._parity,
                  stopbits = self._stopbits,
                  timeout = self._timeout,
                  xonxoff = self._xonxoff,
                  rtscts = self._rtscts,
                  writeTimeout = self._writeTimeout,
                  dsrdtr = self._dsrdtr
                  )

            return 0

        except (OSError, Serial.SerialException):
            return 1

    def CMDSend1(self,cmd=''): # アンサー無しコマンド

        if cmd!='':
            data=cmd+'\n'
            try:

                self.com.write(data.encode())
                return 0

            except (OSError, Serial.SerialException):
                print( Serial.SerialException)
                return 1


    def CMDSend2(self,cmd): # アンサー有りコマンド

        if cmd!='':
            data=cmd+'\n'
            try:
                self.com.write(data.encode())
                a=self.com.readline()
                return a.decode()

            except (OSError, Serial.SerialException):
                print( Serial.SerialException)
                return ""


    def close(self):
        self.com.close()


    def FGInit(self):
        self.connect()
        self.CMDSend1('*RST')
        self.CMDSend1('*CLS')
        self.close()


    def FGStart(self,freq=1000,amp=5.0,dcyc=85):

        self.connect()
        self.CMDSend1('SOUR1:FUNC SQU')
        self.CMDSend1('SOUR1:AMPL '+str(amp))
        self.CMDSend1('SOUR1:FREQ '+str(freq))
        self.CMDSend1('SOUR1:SQU:DCYC '+str(dcyc))
        self.CMDSend1('SOUR1:OUTP ON')
        self.close()

    def FGSinStart(self,freq=1000,amp=5.0):

        self.connect()
        self.CMDSend1('SOUR1:FUNC SIN')
        self.CMDSend1('SOUR1:AMPL '+str(amp))
        self.CMDSend1('SOUR1:FREQ '+str(freq))
        self.CMDSend1('SOUR1:OUTP ON')
        self.close()

    def FGStop(self):

        self.connect()
        self.CMDSend1('SOUR1:OUTP OFF')
        self.close()
