# -*- Coding: utf-8 -*-


import nidaqmx
import numpy as np
from time import sleep

class SinWave():

    '''
    サイン波形を作成するクラス

    wave = SinWave(
                timingsubobject = nidaqmx.Task.timing,
                freq=10.0,
                sampleN = 250,
                cycleN=5,
                amp = 1.0
                )
    '''
    def __init__(self,
                timingsubobject = nidaqmx.Task.timing,
                freq=10.0,
                sampleN = 250,
                cycleN=5,
                amp = 1.0):

        self._timingsubobject = timingsubobject
        self._freq = freq
        self._sampleN = sampleN
        self._cycleN = cycleN
        self._amp = amp

        if self._timingsubobject.samp_timing_type == nidaqmx.constants.SampleTimingType.ON_DEMAND:
            self._timingsubobject.samp_timing_type = nidaqmx.constants.SampleTimingType.SAMPLE_CLOCK

        self._sampleclock = (self._freq * self._sampleN) /self._cycleN
        self._samplepercycle = self._sampleN / self._cycleN
        self._timingsubobject.samp_clk_rate = self._sampleclock
        self._resultsamplerate = self._timingsubobject.samp_clk_rate
        self._resultfreq = self._resultsamplerate / (self._sampleN / self._cycleN)

        dt = 1.0 / self._resultsamplerate
        intsampleN = int(self._sampleN) - 1
        t = np.arange(intsampleN) * dt
        self._data = self._amp * np.sin(2.0 * np.pi * freq * t)


    @property
    def data(self):
        return self._data

    @property
    def resultsamplerate(self):
        return self._resultsamplerate

    @property
    def resultfreq(self):
        return self._resultfreq

class SinGenerator():

    def __init__(self,Dev ='Dev1/ao0',Freq=10.0,SampleN=4096,CycleN=2,Amp=1.0):

        self._Dev = Dev
        self._Vmin = -10
        self._Vmax = 10
        self._Freq = Freq
        self._SampleN = SampleN
        self._CycleN = CycleN
        self._Amp = Amp

        try:
            self._task = nidaqmx.Task()
            self._task.ao_channels.add_ao_voltage_chan(self._Dev,
                    min_val=self._Vmin,max_val=self._Vmax,
                    units = nidaqmx.constants.VoltageUnits.VOLTS)

            self._task.control(nidaqmx.constants.TaskMode.TASK_VERIFY)

            fGen = SinWave(timingsubobject = self._task.timing,
                                     freq = self._Freq,
                                     sampleN =self._SampleN,
                                     cycleN = self._CycleN,
                                     amp = self._Amp
                                     )
            self._resultFreq = fGen.resultfreq

            self._task.timing.cfg_samp_clk_timing(fGen.resultsamplerate,
                                            active_edge=nidaqmx.constants.Edge.RISING,
                                             sample_mode=nidaqmx.constants.AcquisitionType.CONTINUOUS,
                                              samps_per_chan=1000)

            self._task.write(fGen.data, auto_start=False, timeout=10.0)

        except(OSError,nidaqmx.errors.Error):
            print('ERROR')


    def Start(self):
        try:

            self._task.start()

        except(OSError,nidaqmx.errors.Error):
            print('ERROR')


    def Stop(self):
        try:
            self._task.stop()

        except(OSError,nidaqmx.errors.Error):
            print('ERROR')

    def Close(self):
        try:
            self._task.close()

        except(OSError,nidaqmx.errors.Error):
            print('ERROR')

    @property
    def resultFreq(self):
        return self._resultFreq

class WhiteNoise():

    '''
    ホワイトノイズを作成するクラス

    wave = WhiteNoise(
                timingsubobject = nidaqmx.Task.timing,
                maxfreq=200,
                sampleN = 2000,
                amp = 1.0
                )
    '''
    def __init__(self,
                timingsubobject = nidaqmx.Task.timing,
               maxfreq=200,
               sampleN=2000,
            amp = 1.0):

        self._timingsubobject = timingsubobject
        self._maxfreq = maxfreq
        self._sampleN = sampleN
        self._amp = amp

        if self._timingsubobject.samp_timing_type == nidaqmx.constants.SampleTimingType.ON_DEMAND:
            self._timingsubobject.samp_timing_type = nidaqmx.constants.SampleTimingType.SAMPLE_CLOCK

        self._sampleclock = self._maxfreq * 2.0
        self._timingsubobject.samp_clk_rate = self._sampleclock
        self._resultsamplerate = self._timingsubobject.samp_clk_rate

#         print(self._resultsamplerate)
#         dt = 1.0 / self._resultsamplerate
#         intsampleN = int(self._sampleN) - 1
#         t = np.arange(intsampleN) * dt
        self._data = self._amp * 2.0 * (np.random.rand(self._sampleN)-0.5)

#         print(self._data[0])#         self._data = self._amp * np.sin(2.0 * np.pi * freq * t)


    @property
    def data(self):
        return self._data

    @property
    def resultsamplerate(self):
        return self._resultsamplerate


class WhiteNoiseGenerator():

    def __init__(self,Dev ='Dev1/ao0',MaxFreq=200,SampleN=2000,Amp=1.0):

        self._Dev = Dev
        self._Vmin = -10
        self._Vmax = 10
        self._MaxFreq = MaxFreq
        self._SampleN = SampleN
        self._Amp = Amp
        self._Dt = 1.0/(self._MaxFreq*2.0)

        try:
            self._task = nidaqmx.Task()
            self._task.ao_channels.add_ao_voltage_chan(self._Dev,
                    min_val=self._Vmin,max_val=self._Vmax,
                    units = nidaqmx.constants.VoltageUnits.VOLTS)

            self._task.control(nidaqmx.constants.TaskMode.TASK_VERIFY)

#             fGen = self._Amp * 2.0 * (np.random.rand(self._SampleN)-0.5)

            fGen = WhiteNoise(timingsubobject = self._task.timing,
                                     maxfreq = self._MaxFreq,
                                     sampleN =self._SampleN,
                                     amp = self._Amp
                                     )
            self._resultsamplerate = fGen.resultsamplerate

            self._task.timing.cfg_samp_clk_timing(fGen.resultsamplerate,
                                            active_edge=nidaqmx.constants.Edge.RISING,
                                             sample_mode=nidaqmx.constants.AcquisitionType.CONTINUOUS,
                                              samps_per_chan=1000)

            self._task.write(fGen.data, auto_start=False, timeout=10.0)

        except(OSError,nidaqmx.errors.Error):
            print('ERROR')


    def Start(self):
        try:

            self._task.start()

        except(OSError,nidaqmx.errors.Error):
            print('ERROR')


    def Stop(self):
        try:
            self._task.stop()

        except(OSError,nidaqmx.errors.Error):
            print('ERROR')

    def Close(self):
        try:
            self._task.close()

        except(OSError,nidaqmx.errors.Error):
            print('ERROR')

    @property
    def resultSampleRate(self):
        return self._resultsamplerate

class VoltUpdate():
    def __init__(self,dev ='Dev1/ao0',volt=0.0):

        try:
            with nidaqmx.Task() as task:
                task.ao_channels.add_ao_voltage_chan(dev)
                task.write(volt)
                task.stop()
#                 task.close()

        except(OSError,nidaqmx.errors.Error):
            print('ERROR')


def Main():

    Dev = 'Dev1/ao0'
    Vmin = -10
    Vmax = 10
    Freq = 10.0
    SampleN = 1000
    CycleN = 1
    Amp = 1.0

    SG = SinGenerator(Dev=Dev,Freq=Freq,SampleN=SampleN,CycleN=CycleN,Amp=Amp)
    print(SG._resultFreq)
    SG.Start()
    sleep(10)
    SG.Stop()
    SG.Close()

    VoltUpdate(Dev,0.0)

    sleep(5)
#     Freq = 148.0
#     SG = SinGenerator(Dev=Dev,Freq=Freq,SampleN=SampleN,CycleN=CycleN,Amp=Amp)
#     print(SG._resultFreq)
#     SG.Start()
#     sleep(10)
#     SG.Stop()
#     SG.Close()
#
#     VoltUpdate(Dev,0.0)


    sleep(5)
    MaxFreq = 500.0
    SampleN = 4000
    Amp=1.0
    WG = WhiteNoiseGenerator(Dev=Dev,MaxFreq=MaxFreq,SampleN=SampleN,Amp=Amp)
    print(WG.resultSampleRate)
    WG.Start()
    sleep(10)
    WG.Stop()
    WG.Close()

    VoltUpdate(Dev,0.0)



if __name__ == '__main__':
    Main()

