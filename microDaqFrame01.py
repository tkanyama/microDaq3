# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
from time import sleep
import time
import threading

import numpy as np
import matplotlib
matplotlib.interactive( True )
matplotlib.use( 'WXAgg' )
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg
from matplotlib.figure import Figure

import matplotlib.pyplot as plt

import socket
import struct
import FGControl

import nidaqmx
import nidaqmx.system

import NIDaqTest03_ao as AO
from TubuHosei import *

commonData='gbrc'

# import microDAQ as MD

###########################################################################
## Class microDaqFrame
###########################################################################

class microDaqFrame ( wx.Frame ):

    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"microDAQ System", pos = wx.Point( 710,280 ), size = wx.Size( 1200,760 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

        self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )

        self.m_menubar1 = wx.MenuBar( 0 )
        self.m_menu1 = wx.Menu()
        self.m_menuItem1 = wx.MenuItem( self.m_menu1, wx.ID_ANY, u"MyMenuItem", wx.EmptyString, wx.ITEM_NORMAL )
        self.m_menu1.AppendItem( self.m_menuItem1 )

        self.m_menuItem2 = wx.MenuItem( self.m_menu1, wx.ID_ANY, u"MyMenuItem", wx.EmptyString, wx.ITEM_NORMAL )
        self.m_menu1.AppendItem( self.m_menuItem2 )

        self.m_menubar1.Append( self.m_menu1, u"MyMenu" )

        self.m_menu2 = wx.Menu()
        self.m_menuItem3 = wx.MenuItem( self.m_menu2, wx.ID_ANY, u"MyMenuItem", wx.EmptyString, wx.ITEM_NORMAL )
        self.m_menu2.AppendItem( self.m_menuItem3 )

        self.m_menuItem4 = wx.MenuItem( self.m_menu2, wx.ID_ANY, u"MyMenuItem", wx.EmptyString, wx.ITEM_NORMAL )
        self.m_menu2.AppendItem( self.m_menuItem4 )

        self.m_menubar1.Append( self.m_menu2, u"MyMenu" )

        self.m_menu3 = wx.Menu()
        self.m_menuItem5 = wx.MenuItem( self.m_menu3, wx.ID_ANY, u"MyMenuItem", wx.EmptyString, wx.ITEM_NORMAL )
        self.m_menu3.AppendItem( self.m_menuItem5 )

        self.m_menuItem6 = wx.MenuItem( self.m_menu3, wx.ID_ANY, u"MyMenuItem", wx.EmptyString, wx.ITEM_NORMAL )
        self.m_menu3.AppendItem( self.m_menuItem6 )

        self.m_menubar1.Append( self.m_menu3, u"MyMenu" )

        self.SetMenuBar( self.m_menubar1 )

        bSizer1 = wx.BoxSizer( wx.VERTICAL )

        self.Title_panel1 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,40 ), wx.TAB_TRAVERSAL )
        self.Title_panel1.SetMinSize( wx.Size( -1,40 ) )
        self.Title_panel1.SetMaxSize( wx.Size( -1,40 ) )

        TitleSizer = wx.BoxSizer( wx.VERTICAL )

        self.m_staticText60 = wx.StaticText( self.Title_panel1, wx.ID_ANY, u"microDAQ 計測システム", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText60.Wrap( -1 )
        self.m_staticText60.SetFont( wx.Font( 24, 70, 90, 90, False, wx.EmptyString ) )

        TitleSizer.Add( self.m_staticText60, 1, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )


        self.Title_panel1.SetSizer( TitleSizer )
        self.Title_panel1.Layout()
        bSizer1.Add( self.Title_panel1, 1, wx.EXPAND |wx.ALL, 5 )

        self.Main_panel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,700 ), wx.TAB_TRAVERSAL )
        self.Main_panel.SetMinSize( wx.Size( -1,700 ) )

        MainPanelSizer = wx.BoxSizer( wx.HORIZONTAL )

        self.m_panel10 = wx.Panel( self.Main_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        self.m_panel10.SetMaxSize( wx.Size( 300,-1 ) )

        bSizer141 = wx.BoxSizer( wx.VERTICAL )

        self.microDaq_Control_panel = wx.Panel( self.m_panel10, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), wx.STATIC_BORDER|wx.TAB_TRAVERSAL )
        self.microDaq_Control_panel.SetMaxSize( wx.Size( 300,200 ) )

        bSizer14 = wx.BoxSizer( wx.VERTICAL )

        microDAQSizer1 = wx.BoxSizer( wx.HORIZONTAL )

        bSizer15 = wx.BoxSizer( wx.VERTICAL )

        self.microDAQText1 = wx.StaticText( self.microDaq_Control_panel, wx.ID_ANY, u"microDAQ\nController", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.microDAQText1.Wrap( -1 )
        self.microDAQText1.SetMaxSize( wx.Size( 70,-1 ) )

        bSizer15.Add( self.microDAQText1, 0, wx.ALL|wx.EXPAND, 5 )

        self.m_staticline71 = wx.StaticLine( self.microDaq_Control_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
        bSizer15.Add( self.m_staticline71, 0, wx.EXPAND |wx.ALL, 5 )

        self.microDAQ_Comannd = wx.TextCtrl( self.microDaq_Control_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.microDAQ_Comannd.SetMaxSize( wx.Size( 50,-1 ) )

        bSizer15.Add( self.microDAQ_Comannd, 0, wx.ALL|wx.EXPAND, 5 )


        microDAQSizer1.Add( bSizer15, 1, wx.EXPAND, 5 )

        microDAQSiser2 = wx.GridSizer( 5, 2, 0, 0 )

        self.microDAQText2 = wx.StaticText( self.microDaq_Control_panel, wx.ID_ANY, u"Sample Frq", wx.DefaultPosition, wx.Size( 60,-1 ), 0 )
        self.microDAQText2.Wrap( -1 )
        self.microDAQText2.SetFont( wx.Font( 9, 70, 90, 90, False, wx.EmptyString ) )
        self.microDAQText2.SetMaxSize( wx.Size( 65,25 ) )

        microDAQSiser2.Add( self.microDAQText2, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.microDAQ_SampleFreq = wx.TextCtrl( self.microDaq_Control_panel, wx.ID_ANY, u"1000", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.microDAQ_SampleFreq.SetMaxSize( wx.Size( 60,-1 ) )

        microDAQSiser2.Add( self.microDAQ_SampleFreq, 0, wx.ALL, 5 )

        self.microDAQText3 = wx.StaticText( self.microDaq_Control_panel, wx.ID_ANY, u"Sample N", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.microDAQText3.Wrap( -1 )
        self.microDAQText3.SetFont( wx.Font( 9, 70, 90, 90, False, wx.EmptyString ) )
        self.microDAQText3.SetMaxSize( wx.Size( 60,25 ) )

        microDAQSiser2.Add( self.microDAQText3, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.microDAQ_SampleN = wx.TextCtrl( self.microDaq_Control_panel, wx.ID_ANY, u"4096", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.microDAQ_SampleN.SetMaxSize( wx.Size( 60,-1 ) )

        microDAQSiser2.Add( self.microDAQ_SampleN, 1, wx.ALL, 5 )

        self.microDAQText4 = wx.StaticText( self.microDaq_Control_panel, wx.ID_ANY, u"St Unit No", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.microDAQText4.Wrap( -1 )
        self.microDAQText4.SetFont( wx.Font( 9, 70, 90, 90, False, wx.EmptyString ) )
        self.microDAQText4.SetMaxSize( wx.Size( 60,-1 ) )

        microDAQSiser2.Add( self.microDAQText4, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.microDAQ_StUnit = wx.TextCtrl( self.microDaq_Control_panel, wx.ID_ANY, u"1", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.microDAQ_StUnit.SetMaxSize( wx.Size( 60,-1 ) )

        microDAQSiser2.Add( self.microDAQ_StUnit, 1, wx.ALL, 5 )

        self.microDAQText5 = wx.StaticText( self.microDaq_Control_panel, wx.ID_ANY, u"Ed Unit No", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.microDAQText5.Wrap( -1 )
        self.microDAQText5.SetFont( wx.Font( 9, 70, 90, 90, False, wx.EmptyString ) )
        self.microDAQText5.SetMaxSize( wx.Size( 60,-1 ) )

        microDAQSiser2.Add( self.microDAQText5, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.microDAQ_EdUnit = wx.TextCtrl( self.microDaq_Control_panel, wx.ID_ANY, u"12", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.microDAQ_EdUnit.SetMaxSize( wx.Size( 60,-1 ) )

        microDAQSiser2.Add( self.microDAQ_EdUnit, 1, wx.ALL, 5 )

        self.microDAQ_GraphUnitNo1 = wx.StaticText( self.microDaq_Control_panel, wx.ID_ANY, u"Graph Unit", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.microDAQ_GraphUnitNo1.Wrap( -1 )
        self.microDAQ_GraphUnitNo1.SetFont( wx.Font( 9, 70, 90, 90, False, wx.EmptyString ) )

        microDAQSiser2.Add( self.microDAQ_GraphUnitNo1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.microDAQ_GraphUnitNo = wx.TextCtrl( self.microDaq_Control_panel, wx.ID_ANY, u"1", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.microDAQ_GraphUnitNo.SetMaxSize( wx.Size( 60,-1 ) )

        microDAQSiser2.Add( self.microDAQ_GraphUnitNo, 0, wx.ALL, 5 )


        microDAQSizer1.Add( microDAQSiser2, 1, wx.EXPAND, 5 )

        microDAQSizer3 = wx.BoxSizer( wx.VERTICAL )

        self.microDAQ_ZeroStartButton = wx.Button( self.microDaq_Control_panel, wx.ID_ANY, u"Zero Start", wx.DefaultPosition, wx.DefaultSize, 0 )
        microDAQSizer3.Add( self.microDAQ_ZeroStartButton, 1, wx.ALL|wx.EXPAND, 5 )

        self.m_staticline1 = wx.StaticLine( self.microDaq_Control_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
        microDAQSizer3.Add( self.m_staticline1, 0, wx.ALL|wx.EXPAND, 5 )

        self.microDAQ_ReadyButton = wx.Button( self.microDaq_Control_panel, wx.ID_ANY, u"Ready", wx.DefaultPosition, wx.DefaultSize, 0 )
        microDAQSizer3.Add( self.microDAQ_ReadyButton, 1, wx.ALL|wx.EXPAND, 5 )

        self.m_staticline7 = wx.StaticLine( self.microDaq_Control_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
        microDAQSizer3.Add( self.m_staticline7, 0, wx.EXPAND |wx.ALL, 5 )

        self.microDAQ_StartButton = wx.Button( self.microDaq_Control_panel, wx.ID_ANY, u"Start", wx.DefaultPosition, wx.DefaultSize, 0 )
        microDAQSizer3.Add( self.microDAQ_StartButton, 1, wx.ALL|wx.EXPAND, 5 )


        microDAQSizer1.Add( microDAQSizer3, 1, wx.EXPAND, 5 )


        bSizer14.Add( microDAQSizer1, 1, wx.EXPAND, 5 )

        self.microDAQ_gauge = wx.Gauge( self.microDaq_Control_panel, wx.ID_ANY, 100, wx.DefaultPosition, wx.DefaultSize, wx.GA_HORIZONTAL )
        self.microDAQ_gauge.SetValue( 0 )
        self.microDAQ_gauge.SetMinSize( wx.Size( -1,10 ) )

        bSizer14.Add( self.microDAQ_gauge, 0, wx.ALL|wx.EXPAND, 5 )


        self.microDaq_Control_panel.SetSizer( bSizer14 )
        self.microDaq_Control_panel.Layout()
        bSizer14.Fit( self.microDaq_Control_panel )
        bSizer141.Add( self.microDaq_Control_panel, 1, wx.EXPAND|wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_panel7 = wx.Panel( self.m_panel10, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.STATIC_BORDER|wx.TAB_TRAVERSAL )
        self.m_panel7.SetMinSize( wx.Size( -1,150 ) )
        self.m_panel7.SetMaxSize( wx.Size( -1,150 ) )

        bSizer10 = wx.BoxSizer( wx.HORIZONTAL )

        bSizer12 = wx.BoxSizer( wx.VERTICAL )

        self.m_staticText8 = wx.StaticText( self.m_panel7, wx.ID_ANY, u"チューブ補正", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText8.Wrap( -1 )
        self.m_staticText8.SetMinSize( wx.Size( 100,-1 ) )

        bSizer12.Add( self.m_staticText8, 0, wx.ALL, 5 )

        self.TubeHoseiCheck = wx.CheckBox( self.m_panel7, wx.ID_ANY, u"On", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.TubeHoseiCheck.SetValue(True)
        bSizer12.Add( self.TubeHoseiCheck, 0, wx.ALL, 5 )


        bSizer10.Add( bSizer12, 1, wx.EXPAND, 5 )

        gSizer2 = wx.GridSizer( 3, 2, 0, 0 )

        self.m_staticText9 = wx.StaticText( self.m_panel7, wx.ID_ANY, u"f0", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText9.Wrap( -1 )
        gSizer2.Add( self.m_staticText9, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )

        self.TubuHosei_f0_text = wx.TextCtrl( self.m_panel7, wx.ID_ANY, u"98.6", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.TubuHosei_f0_text.SetMaxSize( wx.Size( 70,-1 ) )

        gSizer2.Add( self.TubuHosei_f0_text, 0, wx.ALL, 5 )

        self.m_staticText10 = wx.StaticText( self.m_panel7, wx.ID_ANY, u"h", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText10.Wrap( -1 )
        gSizer2.Add( self.m_staticText10, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )

        self.TubuHosei_h_text = wx.TextCtrl( self.m_panel7, wx.ID_ANY, u"0.274", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.TubuHosei_h_text.SetMaxSize( wx.Size( 70,-1 ) )

        gSizer2.Add( self.TubuHosei_h_text, 0, wx.ALL, 5 )

        self.m_staticText11 = wx.StaticText( self.m_panel7, wx.ID_ANY, u"c", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText11.Wrap( -1 )
        gSizer2.Add( self.m_staticText11, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )

        self.TubuHosei_c_text = wx.TextCtrl( self.m_panel7, wx.ID_ANY, u"1.034", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.TubuHosei_c_text.SetMaxSize( wx.Size( 70,-1 ) )

        gSizer2.Add( self.TubuHosei_c_text, 0, wx.ALL, 5 )


        bSizer10.Add( gSizer2, 1, wx.EXPAND, 5 )


        self.m_panel7.SetSizer( bSizer10 )
        self.m_panel7.Layout()
        bSizer10.Fit( self.m_panel7 )
        bSizer141.Add( self.m_panel7, 1, wx.EXPAND |wx.ALL, 5 )

        self.WhiteNoise_Contol_panel = wx.Panel( self.m_panel10, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,500 ), wx.STATIC_BORDER|wx.TAB_TRAVERSAL )
        self.WhiteNoise_Contol_panel.SetMinSize( wx.Size( -1,500 ) )
        self.WhiteNoise_Contol_panel.SetMaxSize( wx.Size( -1,300 ) )

        ConsoleSizer1 = wx.BoxSizer( wx.VERTICAL )

        self.ConsoleBox = wx.TextCtrl( self.WhiteNoise_Contol_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,400 ), wx.HSCROLL|wx.TE_MULTILINE )
        self.ConsoleBox.SetMinSize( wx.Size( -1,420 ) )

        ConsoleSizer1.Add( self.ConsoleBox, 1, wx.ALL|wx.EXPAND, 5 )


        self.WhiteNoise_Contol_panel.SetSizer( ConsoleSizer1 )
        self.WhiteNoise_Contol_panel.Layout()
        bSizer141.Add( self.WhiteNoise_Contol_panel, 1, wx.ALL|wx.EXPAND, 5 )


        self.m_panel10.SetSizer( bSizer141 )
        self.m_panel10.Layout()
        bSizer141.Fit( self.m_panel10 )
        MainPanelSizer.Add( self.m_panel10, 1, wx.EXPAND |wx.ALL, 5 )

        self.Graph_panel = wx.Panel( self.Main_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.STATIC_BORDER|wx.TAB_TRAVERSAL )
        MainPanelSizer.Add( self.Graph_panel, 1, wx.ALL|wx.EXPAND, 5 )


        self.Main_panel.SetSizer( MainPanelSizer )
        self.Main_panel.Layout()
        bSizer1.Add( self.Main_panel, 1, wx.ALL|wx.EXPAND, 5 )


        self.SetSizer( bSizer1 )
        self.Layout()
        self.micoroDAQ_timer1 = wx.Timer()
        self.micoroDAQ_timer1.SetOwner( self, wx.ID_ANY )

        # Connect Events
        self.microDAQ_Comannd.Bind( wx.EVT_TEXT, self.CommadExec )
        self.microDAQ_ZeroStartButton.Bind( wx.EVT_BUTTON, self.MIcroDAQ_ZeroStart )
        self.microDAQ_ReadyButton.Bind( wx.EVT_BUTTON, self.microDAQ_Ready )
        self.microDAQ_StartButton.Bind( wx.EVT_BUTTON, self.microDAQ_Start )
        self.Bind( wx.EVT_TIMER, self.microDAQ_Measure, id=wx.ID_ANY )


# ここから上をwxFormBuilderからコピペすること。


        self.microDAQ_StartButton.Enabled = False
        self.microDAQ_ReadyButton.Enabled = False

#         self.AO_SinWaveStartButton.Enabled = True
#         self.AO_SinWaveStopButton.Enabled = False
#
#         self.AO_NoiseStartButton.Enabled = True
#         self.AO_NoiseStopButton.Enabled = False


        self.GraphDataExist = False

        self.ZeroFlag= False
        self._ReadyFlag = False

        self.figure = Figure(  None )    # Figure（グラフの台紙）オブジェクトを生成
        self._Ch_n = self.ChannelChange(32)
#         print(self._Ch_n)

    def __del__( self ):
        pass

    # Virtual event handlers, overide them in your derived class




#             ReDim Ch_N(Ch_number - 1)
#             For i As Integer = 1 To Ch_number
#                 Dim kk As Integer
#                 If i <= 16 Then
#                     If i < 9 Then
#                         kk = CInt(i * 2)
#                     Else
#                         kk = CInt((i - 8.5) * 2)
#                     End If
#                 Else
#                     If (i - 16) < 9 Then
#                         kk = CInt((i - 16) * 2) + 16
#                     Else
#                         kk = CInt((i - 16 - 8.5) * 2) + 16
#                     End If
#                 End If
#                 Ch_N(i - 1) = kk - 1
#             Next

    def ChannelChange(self,n):
        # 測定番号並び替えマトリックス（旧システムとの互換性のため）

        Ch_n=[]
        for j in range(n):
            i=j+1
            if i<=16:
                if i < 9 :
                    kk = int(i*2)
                else:
                    kk = int((i-8.5)*2)
            else:
                if (i-16)<9:
                    kk = int((i-16)*2)+16
                else:
                    kk = int((i-16-8.5)*2)+16
            Ch_n.append(kk-1)

        return Ch_n

    def CommadExec( self, event ):

        command=self.microDAQ_Comannd.Value
#         print(command)

        if command == 'Zero':
#             data = self.data1
            self.InitData=np.zeros((32,self._UnitN))

            for i in range(self._UnitN):

                for j in range(32):

                    # 平均値の計算

                    self.InitData[j,i]=np.average(self.data1[:,j,i])

            self._microDAQ_Close()
            self.ZeroFlag = True
            self.microDAQ_ReadyButton.Enabled=True

        elif command == 'Measure':
            self.micro_data = self.data1
            self._microDAQ_Close()
#             t=np.arange(self.microN)/self.microFreq
            Ch=32

#             # データの並び替え（旧システムにあわせるため）
#             d1 = np.zeros((self._SampleN,Ch,self._UnitN))
#             for j in range(self._UnitN):
#                 for i in range(Ch):
#                     d1[:,i,j]=self.micro_data[:,self._Ch_n[i],j]
#
#             self.micro_data = d1


            tb=TubuHosei(self._f0,self._h,self._c,1.0/self._SampleFreq)

            for j in range(self._UnitN):
                for i in range(Ch):
                    x=self.micro_data[:,i,j]-self.InitData[i,j]
                    x=x*self.Coe
                    if self._TubuHoseiFlag :
                        x = tb.Hosei(x)

                    self.micro_data[:,i,j]=x

    #                 x=x-np.average(x)

            self.PlotGraphWindow(self.Graph_panel,n1=8,m1=4,data=self.micro_data,
                                 Freq=self._SampleFreq,SampleN=self._SampleN)
    #             plt.subplot(8,4,i+1)
    #             plt.plot(t,x)
    #
    #         plt.show()

            self.microDAQ_ReadyButton.Enabled=True
            self.microDAQ_StartButton.Enabled=False
            self.microDAQ_Done = True



    def MIcroDAQ_ZeroStart( self, event ):
#         event.Skip()
        Freq=float(self.microDAQ_SampleFreq.Value)
        N=3000
        ST=int(self.microDAQ_StUnit.Value)
        ED=int(self.microDAQ_EdUnit.Value)
#         Coe=0.030413

        self._microDAQ(StartUnitNo = ST,EndUnitNo=ED,SampleFreq=Freq,SampleN = N)
        self._microDAQ_Ready()
        sleep(0.5)
        self.command = 'Zero'
        self.BarN = N
        self._microDAQ_Start()


#         self.InitData=np.zeros((32,ED-ST+1))
#         for i in range(ED-ST+1):
#             for j in range(32):
#                 self.InitData[j,i]=np.average(data[:,j,i])
#
#         self._microDAQ_Close()
#
#         self.microDAQ_ReadyButton.Enabled=True
# #         print(self.InitData[:,0])

    def microDAQ_Ready( self, event ):
#         event.Skip()
        if self.ZeroFlag:
            self.microFreq=float(self.microDAQ_SampleFreq.Value)
            self.microN=int(self.microDAQ_SampleN.Value)
            self.microST=int(self.microDAQ_StUnit.Value)
            self.microED=int(self.microDAQ_EdUnit.Value)
            self.Coe=0.030413

            self._microDAQ(StartUnitNo = self.microST,EndUnitNo=self.microED,
                                  SampleFreq=self.microFreq,SampleN = self.microN)
            self._microDAQ_Ready()
            self.microDAQ_Comannd.Value = ''

            sleep(0.5)
            self.microDAQ_StartButton.Enabled=True
            self.microDAQ_ReadyButton.Enabled=False
        else:
            pass


    def microDAQ_Start( self, event ):
#         event.Skip()
        if self._ReadyFlag:
            self.command = 'Measure'
            self.BarN = self.microN
            self.microDAQ_Done = False
            self._microDAQ_Start()
        else:
            pass

#
#         self._microDAQ_Close()
#         t=np.arange(self.microN)/self.microFreq
#         Ch=32
#         for j in range(self._UnitN):
#             for i in range(Ch):
#                 x=self.micro_data[:,i,j]-self.InitData[i,j]
#                 x=x*self.Coe
#                 self.micro_data[:,i,j]=x
# #                 x=x-np.average(x)
#
#         self.PlotGraphWindow(self.Graph_panel1,n1=9,m1=4,data=self.micro_data,
#                              Freq=self._SampleFreq,SampleN=self._SampleN)
# #             plt.subplot(8,4,i+1)
# #             plt.plot(t,x)
# #
# #         plt.show()
#
#         self.microDAQ_ReadyButton.Enabled=True
#         self.microDAQ_StartButton.Enabled=False


    def microDAQ_Measure( self, event ):

        buf1 = self._buf_size*self._Nbuf    # 読み込みバッファ

        for j in range(len(self._host)):

            try:
                b=self._mySocket[j].recv(buf1)
            except(OSError,socket.timeout):
                pass
#                 print('timeout1')

#                     if j==0:
#                         print(step,j,len(b),b[0],b[1],b[2],b[67],b[68],b[len(b)-2],b[len(b)-1])

            # microDAQモジュール毎にデータを追加
            self.data[j].extend(b)

            # データ数をカウント（６７バイトで１ステップ）
            if j==0:
                self.step +=int(len(b)/67)
                self.microDAQ_gauge.Value = int(self.step/self.BarN * 100)

        # データ数を超えたら読み込み中止
        if int(self.step)>=self._SampleN:
            self.microDAQ_gauge.Value = 100
            self.micoroDAQ_timer1.Stop()
            self.flag=False

            self.t2 = time.time()

            # ファンクションジェネレーターの矩形波の停止
            self.FG.FGStop()

            sleep(1.0)  # 時間調整（重要）

            # microDAQモジュールの測定停止コマンドの送信
            for i in range(len(self._host)):
                try:
                    self._mySocket[i].send(self._StopCMD[0].encode())
                    sleep(0.5)
                    a=self._mySocket[i].recv(1024)
                    a=a[len(a)-2:len(a)]
    #                 print(i,a.decode())
                except (OSError,socket.timeout):
                    print('timeout2')

    #         for i in range(len(host)):
    #             mySocket[i].close()

            # 3次元配列の作成（データはゼロ）
            self.data1= np.zeros((self._SampleN,32,self._UnitN))

            # 読み込み配列を16ビット整数に変換して3次元配列に組み込み
            for i in range(len(self._host)):
                offset1=0
    #             dd1=[]
                dd1 = np.zeros((self._SampleN,32))  # zeroの次元配列の生成
                d=bytearray(self.data[i])           # 読み込み配列をバイト配列に変換

                # 67バイト毎に32個の16ビット整数に変換
                for j in range(self._SampleN):
                    offset1 +=3             # はじめの3ビットは読み飛ばし

                    # 16ビットSignedInt（ビックエンディアン）に変換
                    dd = struct.unpack_from('>32H', d, offset1)

                    # チャンネルの並び替え（旧システムと合わすため）
                    dd2 = []
                    for k in range(32):
                        dd2.append(dd[self._Ch_n[k]])

                    # 2次元配列に組み込み
                    dd1[j,:]=dd2

                    offset1 +=64    # オフセットを 64バイト加算


                # 2次元配列を3次元配列に組み込み
                self.data1[:,:,i] = dd1


            self._Mtime=self.t2-self.t1
#             print(self._Mtime)

            self._ReadyFlag = False
            self.microDAQ_gauge.Value = 0

            self.microDAQ_Comannd.Value = self.command

#             return self.data1   # 3次元配列をリターン









    def _microDAQ(self, StartUnitNo = 1,EndUnitNo=12,SampleFreq=1000.0,SampleN = 10000):

        self._buf_size=670
        self._Nbuf = 3

        self._StartUnitNo= StartUnitNo
        self._EndUnitNo = EndUnitNo
        self._SampleFreq = SampleFreq
        self._SampleN = SampleN
        self._UnitN = self._EndUnitNo - self._StartUnitNo + 1
        self._host=[]
        self._port=[]
        self._Step = 0
        self._Mtime = 0
        self._ReadyFlag = False

        # バッファサイズの設定
        RBuffer=1024*256
        SBuffer=1024*256

#         self.intTime = 0.01

        # microDAQモジュールのIPアドレスとポート番号を設定
        for i in range(self._UnitN):
            n = 180 + i + self._StartUnitNo
            self._host.append('192.168.1.'+str(n))
            self._port.append(101)

        self._mySocket=[]
        for i in range(len(self._host)):
            # microDAQモジュール毎に通信ソケットを生成
            self._mySocket.append(socket.socket(socket.AF_INET, socket.SOCK_STREAM))

        # 通信ソケットのバッファサイズを設定
        for i in range(len(self._host)):
                self._mySocket[i].setsockopt(
                socket.SOL_SOCKET,
                socket.SO_SNDBUF,
                SBuffer)

                self._mySocket[i].setsockopt(
                socket.SOL_SOCKET,
                socket.SO_RCVBUF,
                RBuffer)


#         for i in range(len(self._host)):
#             print(self._mySocket[i].getsockopt(socket.SOL_SOCKET,socket.SO_RCVBUF))
#             print(self._mySocket[i].getsockopt(socket.SOL_SOCKET,socket.SO_SNDBUF))

        # microDAQモジュールの通信ソケットに接続
        for i in range(len(self._host)):
            self._mySocket[i].connect((self._host[i],self._port[i]))
            self._mySocket[i].settimeout(0.1)

        # microDAQモジュールの測定開始コマンドの作成
        self._StartCMD=[]
        self._StartCMD.append(chr(62)+chr(80)+chr(17)+chr(67)+chr(60))
        self._StartCMD.append(chr(62)+chr(84)+chr(17)+chr(71)+chr(60))
        self._StartCMD.append(chr(62)+chr(80)+chr(17)+chr(67)+chr(60))
        self._StartCMD.append(chr(62)+chr(84)+chr(17)+chr(71)+chr(60))

        # microDAQモジュールの測定終了コマンドの作成
        self._StopCMD=[]
        self._StopCMD.append(chr(62)+chr(84)+chr(1)+chr(87)+chr(60))

        # ファンクションジェネレーターの設定と初期化
        self.FG = FGControl.FGC('COM5')
        self.FG.FGInit()


        self.microDAQ_gauge.Value = 0



    def _microDAQ_Ready(self):
        # microDAQモジュールの測定開始コマンドの送信

        self.microDAQ_gauge.Value = 0

        for j in range(len(self._StartCMD)):
            for i in range(len(self._host)):
                self._mySocket[i].send(self._StartCMD[j].encode())
                a=self._mySocket[i].recv(1024)
#                 print(i,a.decode())

            sleep(0.5)

        self._ReadyFlag = True

    def _microDAQ_Start(self):
        # microDAQモジュールの測定スタート

        if self._ReadyFlag: # Ready関数が実行された後に読み込み開始

            self.t1 = time.time()
            # ファンクションジェネレーターの矩形波の発信（サンプリング信号）
            self.FG.FGStart(self._SampleFreq)

            self.step=0

            # 読み込み配列の初期化
            self.data=[]

            for i in range(len(self._host)):
                # 読み込み配列を2次元配列に
                self.data.append([])

            sleep(0.2)  # 時間調整（重要）

            # データの読み込み開始
            self.flag=True
#             i=0
#             buf1 = self._buf_size*self._Nbuf    # 読み込みバッファ

            self._f0 = float(self.TubuHosei_f0_text.Value)
            self._h = float(self.TubuHosei_h_text.Value)
            self._c = float(self.TubuHosei_c_text.Value)
            self._TubuHoseiFlag = self.TubeHoseiCheck.Value

            self.microDAQ_gauge.Value = 0
            self.micoroDAQ_timer1.Start(10)


#             while flag:
#                 i+=1
#     #             t2=time.time()
#     #             sleep(0.010)
#                 for j in range(len(self._host)):
#
#                     try:
#                         b=self._mySocket[j].recv(buf1)
#                     except(OSError,socket.timeout):
#                         print('timeout1')
#
# #                     if j==0:
# #                         print(step,j,len(b),b[0],b[1],b[2],b[67],b[68],b[len(b)-2],b[len(b)-1])
#
#                     # microDAQモジュール毎にデータを追加
#                     self.data[j].extend(b)
#
#                     # データ数をカウント（６７バイトで１ステップ）
#                     if j==0:
#                         step +=int(len(b)/67)
#                         self.microDAQ_gauge.Value = int(step/self._SampleN * 100)
#
#                 # データ数を超えたら読み込み中止
#                 if int(step)>=self._SampleN:
#                     flag=False
#                     self.microDAQ_gauge.Value = 100
#
#             t2 = time.time()
#
#             # ファンクションジェネレーターの矩形波の停止
#             self.FG.FGStop()
#
#             sleep(1.0)  # 時間調整（重要）
#
#             # microDAQモジュールの測定停止コマンドの送信
#             for i in range(len(self._host)):
#                 try:
#                     self._mySocket[i].send(self._StopCMD[0].encode())
#                     sleep(0.5)
#                     a=self._mySocket[i].recv(1024)
#                     a=a[len(a)-2:len(a)]
#     #                 print(i,a.decode())
#                 except (OSError,socket.timeout):
#                     print('timeout2')
#
#     #         for i in range(len(host)):
#     #             mySocket[i].close()
#
#             # 3次元配列の作成（データはゼロ）
#             self.data1= np.zeros((self._SampleN,32,self._UnitN))
#
#             # 読み込み配列を16ビット整数に変換して3次元配列に組み込み
#             for i in range(len(self._host)):
#                 offset1=0
#     #             dd1=[]
#                 dd1 = np.zeros((self._SampleN,32))  # zeroの次元配列の生成
#                 d=bytearray(self.data[i])           # 読み込み配列をバイト配列に変換
#
#                 # 67バイト毎に32個の16ビット整数に変換
#                 for j in range(self._SampleN):
#                     offset1 +=3             # はじめの3ビットは読み飛ばし
#
#                     # 16ビットSignedInt（ビックエンディアン）に変換
#                     dd = struct.unpack_from('>32H', d, offset1)
#                     # 2次元配列に組み込み
#                     dd1[j,:]=dd
#
#                     offset1 +=64    # オフセットを 64バイト加算
#
#
#                 # 2次元配列を3次元配列に組み込み
#                 self.data1[:,:,i] = dd1
#
#
#             self._Mtime=t2-t1
#             print(self._Mtime)
#
#             self._ReadyFlag = False
#             self.microDAQ_gauge.Value = 0
#
#             return self.data1   # 3次元配列をリターン
#
#         else:
#             self.data1=np.zeros((1,1,1))
#             self.microDAQ_gauge.Value = 0
#
#             return self.data1


    def _microDAQ_Close(self):

        for i in range(len(self._host)):
            self._mySocket[i].close()


    def PlotGraphWindow(self, panel1 = wx.Panel,n1=2,m1=2,data=None,Freq=1000.0,SampleN=1000):
        '''
        Windowのpanelにグラフを描画する関数
        '''

#         if self.GraphDataExist:
#             self.EraseGraphWindow(panel1)

#         print(self.radiobutton_1.GetValue())
#         from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg
#         from matplotlib.figure import Figure
#         self.figure = Figure(  None )    # Figure（グラフの台紙）オブジェクトを生成
        self.figure.clf(keep_observers=False)
        self.figure.set_facecolor( (0.8,0.8,0.8) )  # Figureの表面色を設定

        #panel2にFigureを貼り付けcanvasを生成
        self.canvas = FigureCanvasWxAgg( panel1, -1, self.figure )
        self.canvas.SetSize( tuple( self.Graph_panel.GetClientSize() ) ) # canvasのサイズをpanel2に合わせる。
#         print(self.canvas.Size,self.canvas.Position)

        self.canvas.SetBackgroundColour( wx.Colour( 100,0,255 ) ) # Canvasの背景色を設定（これは不要？）
        self.n=n1
        self.m=m1
#         self.MakeWaveData(self.n * self.m)
#         self.MakeWaveData(7)

        self.y = data[:,:,int(self.microDAQ_GraphUnitNo.Value)-1]
        self.x = np.arange(SampleN)/Freq
        Draw_Graph(self.figure,self.n,self.m,self.x,self.y)

        self.GraphDataExist = True

    def EraseGraphWindow(self, panel1 = wx.Panel):
        '''
        Windowのpanelのグラフを消去する関数
        '''
#         print(self.radiobutton_1.GetValue())
        from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg
        from matplotlib.figure import Figure
        self.figure = Figure(  None )    # Figure（グラフの台紙）オブジェクトを生成
        self.figure.set_facecolor( (1.0,1.0,1.0) )  # Figureの表面色を設定

        #panel2にFigureを貼り付けcanvasを生成
        self.canvas = FigureCanvasWxAgg( panel1, -1, self.figure )
        self.canvas.SetSize( tuple( panel1.GetClientSize() ) ) # canvasのサイズをpanel2に合わせる。

        self.GraphDataExist = False


    def PrintEventHandler(self,event):
        self.PlotGraphPDF()

    def PlotGraphPDF(self):
        '''
        PDFにグラフを描画する関数
        '''
        from matplotlib.backends.backend_pdf import FigureCanvasPdf
        from matplotlib.backends.backend_pdf import PdfPages    # PDFを作成するモジュールの読込
        import os

        if self.GraphDataExist:
            iDir=os.getcwd()                #カレントディレクトリーの読込
            iFile='test.pdf'
            openFileDialog = wx.FileDialog(self, "PDFファイルの保存", iDir, iFile,
                                                  "PDF files (*.pdf)|*.pdf",
                                                   wx.FD_SAVE|wx.FD_OVERWRITE_PROMPT)

            _filename = ''
            openFileDialog.ShowModal()
            _filename = openFileDialog.GetPath()
            if _filename != '' :
    #         from matplotlib.figure import Figure
    #         if event == wx.EVT_BUTTON:
    #             print(event)

    #         self.figure = Figure(  None )    # Figure（グラフの台紙）オブジェクトを生成
                self.figure.set_size_inches(298./25.4, 210./25.4, True)
                self.figure.set_dpi(600)
                self.figure.set_facecolor( (0.7,0.7,1.0) )  # Figureの表面色を設定

                pdf1 = PdfPages(_filename)
                self.canvas = FigureCanvasPdf( self.figure )    # Canvas（グラフ）オブジェクトをfigure上に生成

        #         Draw_Graph(self.figure)

                pdf1.savefig(self.figure)
                pdf1.close()
            else:
                print('Print Cancel')
        else:
            dlg = wx.MessageDialog(self, '作図データがありません', '警告', wx.OK | wx.ICON_WARNING)
            dlg.ShowModal()
            dlg.Destroy()



#         def selectMenu(self,event):
#             id1 = event.GetId()
#             print('MenuSelected! ' + str(id))
#             if id1 == ID_EXIT or id1 == wx.ID_EXIT :
#                 self.MainExit()
#             elif id1 == ID_PLOT:
#                 self.PlotGraphWindow()
#             elif id1 == ID_PRINT:
#                 self.PlotGraphPDF()
#             elif id1 == ID_CLEAR:
#                 self.EraseGraphWindow()
#     #             self.canvas.figure.clf()
#
#         def ExitHandler(self,event):
#             self.MainExit()
#
#         def MainExit(self):
#             dlg = wx.MessageDialog(self, message = u"終了します。よろしいですか？", caption = u"終了確認", style = wx.YES_NO)
#             result = dlg.ShowModal()
#             if result == wx.ID_YES:
#     #             self.Close(force=False)
#                 wx.Exit()
#
#         def MakeWaveData(self,n=1):
#             import numpy as np
#             amp = []  # 振幅
#             freq = [] # 周波数
#             nn = 4096         # 信号のデータ数
#             smpl = 1000       # 信号のサンプリング周波数(Hz)
#             dt = 1.0 / smpl     # 信号の時間軸分解能(s)
#             self.y = np.zeros((n,nn))
#
#             for i in range(n ):
#                 amp.append((i+1)*0.5)
#                 freq.append((i+1)*0.5)
#
#             self.x = np.arange(nn) * dt  # 波形グラフの時間データの作成
#             import random
#             for i in range(n):
#                 c = random.randint(1,5)
#                 self.y[i,:] = amp[i]*np.sin(freq[i] * 2 * np.pi * self.x) + 0.5*amp[i]*np.cos(c*freq[i] * 2 * np.pi * self.x)







def draw(sb,x,y,title):
    sb.plot(x,y)
    sb.axes.set_ylim((-np.max(y)*1.5,np.max(y)*1.5))
    sb.axes.set_xlim((0,np.max(x)))
    sb.axes.set_title(title,size =8,loc='left')
    sb.axes.set_xlabel('Freq(Hz)',size =8,labelpad=0)
    sb.axes.set_ylabel('P(Pa)',size =8,labelpad=-3)
    sb.axes.tick_params(labelsize=6,direction='in',pad=3)
    sb.axes.grid(color='k', linestyle='-.', linewidth=0.3)



def Draw_Graph(figure1,n,m,x,y):
#     import numpy as np
    h1=figure1.get_figheight()
    w1=figure1.get_figwidth()
    sb2 = []  # サブプロットオブジェクト配列の生成

    ch=np.shape(y)[1]
    for i in range(ch):
        sb2.append(figure1.add_subplot( n , m , i + 1 ))

    a4x = 297         # A4の幅(mm)
    a4y = 210         # A4の高さ(mm)
    mleft = 15        # 左余白(mm)
    mright = 15       # 右余白(mm)
    mtop = 10         # 上余白(mm)
    mbottom = 10      # 下余白(mm)
    mx = 15           # グラフ間のスペースの幅(mm)
    my = 10           # グラフ間のスペースの高さ(mm)
        # ひとつのグラフの幅(mm)を計算
    if m>1:
        xx = (a4x - mleft - mright - mx * ( m - 1 ) )/m
    else:
        xx = a4x - mleft - mright

    # ひとつのグラフの高さ(mm)を計算
    if n>1:
        yy = (a4y - mbottom - mtop - my * (n - 1) )/n
    else:
        yy = a4y - mbottom - mtop

    figure1.subplots_adjust(left=mleft/a4x, bottom=mbottom/a4y, right=(a4x-mright)/a4x, top=(a4y-mtop)/a4y,
                    wspace=mx/xx, hspace=my/yy)

#     x = np.arange(nn) * dt  # 波形グラフの時間データの作成
#     import random

    for i in range(ch):
        draw(sb2[i] , x , y[:,i],'[ch'+str(i+1)+']')



if __name__ == '__main__':
    app = wx.App()
#     fx = 800
#     fy = 800
#     s1=wx.Size(fx,fy)
    frame = microDaqFrame(None)
    frame.Show()
    app.MainLoop()
