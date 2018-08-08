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

commonData='gbrc'

# import microDAQ as MD

###########################################################################
## Class NIDaqFrame
###########################################################################

class NIDaqFrame ( wx.Frame ):

    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"microDAQ System", pos = wx.Point( 710,20 ), size = wx.Size( 1200,250 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

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

        self.Title_panel1 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,30 ), wx.TAB_TRAVERSAL )
        self.Title_panel1.SetMinSize( wx.Size( -1,30 ) )
        self.Title_panel1.SetMaxSize( wx.Size( -1,30 ) )

        TitleSizer = wx.BoxSizer( wx.VERTICAL )

        self.m_staticText60 = wx.StaticText( self.Title_panel1, wx.ID_ANY, u"NIDaq 計測システム", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText60.Wrap( -1 )
        self.m_staticText60.SetFont( wx.Font( 16, 70, 90, 90, False, wx.EmptyString ) )

        TitleSizer.Add( self.m_staticText60, 1, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )


        self.Title_panel1.SetSizer( TitleSizer )
        self.Title_panel1.Layout()
        bSizer1.Add( self.Title_panel1, 1, wx.ALL|wx.EXPAND, 5 )

        self.Main_panel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        MainPanelSizer = wx.BoxSizer( wx.HORIZONTAL )

        self.SinWave_Control_panel = wx.Panel( self.Main_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.STATIC_BORDER|wx.TAB_TRAVERSAL )
        self.SinWave_Control_panel.SetMaxSize( wx.Size( 270,-1 ) )

        SinWaveSizer1 = wx.BoxSizer( wx.HORIZONTAL )

        self.SinWaveText1 = wx.StaticText( self.SinWave_Control_panel, wx.ID_ANY, u"Dev1/AO\nController\n\nSin Wave\nGenerator\n", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.SinWaveText1.Wrap( -1 )
        self.SinWaveText1.SetMaxSize( wx.Size( 70,-1 ) )

        SinWaveSizer1.Add( self.SinWaveText1, 0, wx.ALL|wx.EXPAND, 5 )

        SinWaveSizer2 = wx.GridSizer( 5, 2, 0, 0 )

        self.SinWaveText2 = wx.StaticText( self.SinWave_Control_panel, wx.ID_ANY, u"Sin Freq", wx.DefaultPosition, wx.Size( 60,-1 ), 0 )
        self.SinWaveText2.Wrap( -1 )
        self.SinWaveText2.SetMaxSize( wx.Size( 60,25 ) )

        SinWaveSizer2.Add( self.SinWaveText2, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.AO_SinFreq = wx.TextCtrl( self.SinWave_Control_panel, wx.ID_ANY, u"20", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.AO_SinFreq.SetMaxSize( wx.Size( 50,-1 ) )

        SinWaveSizer2.Add( self.AO_SinFreq, 0, wx.ALL, 5 )

        self.SinWaveText3 = wx.StaticText( self.SinWave_Control_panel, wx.ID_ANY, u"Sample N", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.SinWaveText3.Wrap( -1 )
        self.SinWaveText3.SetMaxSize( wx.Size( 60,25 ) )

        SinWaveSizer2.Add( self.SinWaveText3, 0, wx.ALL, 5 )

        self.AO_SinSampleN = wx.TextCtrl( self.SinWave_Control_panel, wx.ID_ANY, u"1000", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.AO_SinSampleN.SetMaxSize( wx.Size( 50,-1 ) )

        SinWaveSizer2.Add( self.AO_SinSampleN, 1, wx.ALL, 5 )

        self.SinWaveTexxt4 = wx.StaticText( self.SinWave_Control_panel, wx.ID_ANY, u"Amp", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.SinWaveTexxt4.Wrap( -1 )
        self.SinWaveTexxt4.SetMaxSize( wx.Size( 60,-1 ) )

        SinWaveSizer2.Add( self.SinWaveTexxt4, 0, wx.ALL, 5 )

        self.AO_SinAmp = wx.TextCtrl( self.SinWave_Control_panel, wx.ID_ANY, u"1.0", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.AO_SinAmp.SetMaxSize( wx.Size( 50,-1 ) )

        SinWaveSizer2.Add( self.AO_SinAmp, 1, wx.ALL, 5 )

        self.SInWaveText5 = wx.StaticText( self.SinWave_Control_panel, wx.ID_ANY, u"Sycle N", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.SInWaveText5.Wrap( -1 )
        SinWaveSizer2.Add( self.SInWaveText5, 0, wx.ALL, 5 )

        self.AO_SinWaveCycleN = wx.TextCtrl( self.SinWave_Control_panel, wx.ID_ANY, u"2", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.AO_SinWaveCycleN.SetMaxSize( wx.Size( 50,-1 ) )

        SinWaveSizer2.Add( self.AO_SinWaveCycleN, 0, wx.ALL, 5 )


        SinWaveSizer1.Add( SinWaveSizer2, 1, wx.EXPAND, 5 )

        SinWaveSizer3 = wx.BoxSizer( wx.VERTICAL )

        self.AO_SinWaveStartButton = wx.Button( self.SinWave_Control_panel, wx.ID_ANY, u"Start", wx.DefaultPosition, wx.DefaultSize, 0 )
        SinWaveSizer3.Add( self.AO_SinWaveStartButton, 1, wx.ALL|wx.EXPAND, 5 )

        self.m_staticline2 = wx.StaticLine( self.SinWave_Control_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
        SinWaveSizer3.Add( self.m_staticline2, 0, wx.EXPAND |wx.ALL, 5 )

        self.AO_SinWaveStopButton = wx.Button( self.SinWave_Control_panel, wx.ID_ANY, u"Stop", wx.DefaultPosition, wx.DefaultSize, 0 )
        SinWaveSizer3.Add( self.AO_SinWaveStopButton, 1, wx.ALL|wx.EXPAND, 5 )


        SinWaveSizer1.Add( SinWaveSizer3, 1, wx.EXPAND, 5 )


        self.SinWave_Control_panel.SetSizer( SinWaveSizer1 )
        self.SinWave_Control_panel.Layout()
        SinWaveSizer1.Fit( self.SinWave_Control_panel )
        MainPanelSizer.Add( self.SinWave_Control_panel, 1, wx.EXPAND |wx.ALL, 5 )

        self.WhiteNoise_Contol_panel = wx.Panel( self.Main_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.STATIC_BORDER|wx.TAB_TRAVERSAL )
        self.WhiteNoise_Contol_panel.SetMaxSize( wx.Size( 270,-1 ) )

        NoiseSizer1 = wx.BoxSizer( wx.HORIZONTAL )

        self.NoiseText1 = wx.StaticText( self.WhiteNoise_Contol_panel, wx.ID_ANY, u"Dev1/AO\nController\n\nWhite\nNoise\nGenerator\n", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.NoiseText1.Wrap( -1 )
        self.NoiseText1.SetMaxSize( wx.Size( 70,-1 ) )

        NoiseSizer1.Add( self.NoiseText1, 0, wx.ALL|wx.EXPAND, 5 )

        NoiseSiser2 = wx.GridSizer( 5, 2, 0, 0 )

        self.NoiseText2 = wx.StaticText( self.WhiteNoise_Contol_panel, wx.ID_ANY, u"Max Freq", wx.DefaultPosition, wx.Size( 60,-1 ), 0 )
        self.NoiseText2.Wrap( -1 )
        self.NoiseText2.SetMaxSize( wx.Size( 60,25 ) )

        NoiseSiser2.Add( self.NoiseText2, 0, wx.ALL, 5 )

        self.AO_NoizeMaxFreq = wx.TextCtrl( self.WhiteNoise_Contol_panel, wx.ID_ANY, u"500", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.AO_NoizeMaxFreq.SetMaxSize( wx.Size( 50,-1 ) )

        NoiseSiser2.Add( self.AO_NoizeMaxFreq, 0, wx.ALL, 5 )

        self.NoiseText3 = wx.StaticText( self.WhiteNoise_Contol_panel, wx.ID_ANY, u"Sample N", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.NoiseText3.Wrap( -1 )
        self.NoiseText3.SetMaxSize( wx.Size( 60,25 ) )

        NoiseSiser2.Add( self.NoiseText3, 0, wx.ALL, 5 )

        self.AO_NoiseSampleN = wx.TextCtrl( self.WhiteNoise_Contol_panel, wx.ID_ANY, u"4000", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.AO_NoiseSampleN.SetMaxSize( wx.Size( 50,-1 ) )

        NoiseSiser2.Add( self.AO_NoiseSampleN, 1, wx.ALL, 5 )

        self.NoiseText4 = wx.StaticText( self.WhiteNoise_Contol_panel, wx.ID_ANY, u"Amp", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.NoiseText4.Wrap( -1 )
        self.NoiseText4.SetMaxSize( wx.Size( 60,-1 ) )

        NoiseSiser2.Add( self.NoiseText4, 0, wx.ALL, 5 )

        self.AO_NoiseAmp = wx.TextCtrl( self.WhiteNoise_Contol_panel, wx.ID_ANY, u"1.0", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.AO_NoiseAmp.SetMaxSize( wx.Size( 50,-1 ) )

        NoiseSiser2.Add( self.AO_NoiseAmp, 1, wx.ALL, 5 )


        NoiseSizer1.Add( NoiseSiser2, 1, wx.EXPAND, 5 )

        NoiseSiser3 = wx.BoxSizer( wx.VERTICAL )

        self.AO_NoiseStartButton = wx.Button( self.WhiteNoise_Contol_panel, wx.ID_ANY, u"Start", wx.DefaultPosition, wx.DefaultSize, 0 )
        NoiseSiser3.Add( self.AO_NoiseStartButton, 1, wx.ALL|wx.EXPAND, 5 )

        self.m_staticline3 = wx.StaticLine( self.WhiteNoise_Contol_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
        NoiseSiser3.Add( self.m_staticline3, 0, wx.EXPAND |wx.ALL, 5 )

        self.AO_NoiseStopButton = wx.Button( self.WhiteNoise_Contol_panel, wx.ID_ANY, u"Stop", wx.DefaultPosition, wx.DefaultSize, 0 )
        NoiseSiser3.Add( self.AO_NoiseStopButton, 1, wx.ALL|wx.EXPAND, 5 )


        NoiseSizer1.Add( NoiseSiser3, 1, wx.EXPAND, 5 )


        self.WhiteNoise_Contol_panel.SetSizer( NoiseSizer1 )
        self.WhiteNoise_Contol_panel.Layout()
        NoiseSizer1.Fit( self.WhiteNoise_Contol_panel )
        MainPanelSizer.Add( self.WhiteNoise_Contol_panel, 1, wx.EXPAND |wx.ALL, 5 )

        self.AI_Control_panel = wx.Panel( self.Main_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.STATIC_BORDER|wx.TAB_TRAVERSAL )
        self.AI_Control_panel.SetMaxSize( wx.Size( 270,-1 ) )

        AISizer1 = wx.BoxSizer( wx.HORIZONTAL )

        bSizer12 = wx.BoxSizer( wx.VERTICAL )

        self.AIText1 = wx.StaticText( self.AI_Control_panel, wx.ID_ANY, u"Dev1/AI\nController\n\nAnalog\nInput", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.AIText1.Wrap( -1 )
        self.AIText1.SetMaxSize( wx.Size( 70,-1 ) )

        bSizer12.Add( self.AIText1, 0, wx.ALL|wx.EXPAND, 5 )

        self.m_staticline5 = wx.StaticLine( self.AI_Control_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
        bSizer12.Add( self.m_staticline5, 0, wx.EXPAND |wx.ALL, 5 )

        self.AI_command = wx.TextCtrl( self.AI_Control_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.AI_command.SetMaxSize( wx.Size( 55,-1 ) )

        bSizer12.Add( self.AI_command, 0, wx.ALL, 5 )


        AISizer1.Add( bSizer12, 1, wx.EXPAND, 5 )

        AISizer2 = wx.GridSizer( 5, 2, 0, 0 )

        self.AIText2 = wx.StaticText( self.AI_Control_panel, wx.ID_ANY, u"Start CH", wx.DefaultPosition, wx.Size( 60,-1 ), 0 )
        self.AIText2.Wrap( -1 )
        self.AIText2.SetMaxSize( wx.Size( 60,25 ) )

        AISizer2.Add( self.AIText2, 0, wx.ALL, 5 )

        self.AI_StartCH = wx.TextCtrl( self.AI_Control_panel, wx.ID_ANY, u"1", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.AI_StartCH.SetMaxSize( wx.Size( 60,-1 ) )

        AISizer2.Add( self.AI_StartCH, 0, wx.ALL, 5 )

        self.AIText3 = wx.StaticText( self.AI_Control_panel, wx.ID_ANY, u"End CH", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.AIText3.Wrap( -1 )
        self.AIText3.SetMaxSize( wx.Size( 60,25 ) )

        AISizer2.Add( self.AIText3, 0, wx.ALL, 5 )

        self.AI_EndCH = wx.TextCtrl( self.AI_Control_panel, wx.ID_ANY, u"2", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.AI_EndCH.SetMaxSize( wx.Size( 60,-1 ) )

        AISizer2.Add( self.AI_EndCH, 1, wx.ALL, 5 )

        self.AIText4 = wx.StaticText( self.AI_Control_panel, wx.ID_ANY, u"Sample Frq", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.AIText4.Wrap( -1 )
        self.AIText4.SetMaxSize( wx.Size( 60,-1 ) )

        AISizer2.Add( self.AIText4, 0, wx.ALL, 5 )

        self.AI_SampleFreq = wx.TextCtrl( self.AI_Control_panel, wx.ID_ANY, u"1000", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.AI_SampleFreq.SetMaxSize( wx.Size( 60,-1 ) )

        AISizer2.Add( self.AI_SampleFreq, 1, wx.ALL, 5 )

        self.AIText5 = wx.StaticText( self.AI_Control_panel, wx.ID_ANY, u"Range", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.AIText5.Wrap( -1 )
        self.AIText5.SetMaxSize( wx.Size( 60,-1 ) )

        AISizer2.Add( self.AIText5, 0, wx.ALL, 5 )

        self.AI_Range = wx.TextCtrl( self.AI_Control_panel, wx.ID_ANY, u"5.0", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.AI_Range.SetMaxSize( wx.Size( 60,-1 ) )

        AISizer2.Add( self.AI_Range, 1, wx.ALL, 5 )

        self.AIText6 = wx.StaticText( self.AI_Control_panel, wx.ID_ANY, u"Sample N", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.AIText6.Wrap( -1 )
        self.AIText6.SetMaxSize( wx.Size( 60,-1 ) )

        AISizer2.Add( self.AIText6, 0, wx.ALL, 5 )

        self.AI_SampleN = wx.TextCtrl( self.AI_Control_panel, wx.ID_ANY, u"4096", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.AI_SampleN.SetMaxSize( wx.Size( 60,-1 ) )

        AISizer2.Add( self.AI_SampleN, 0, wx.ALL, 5 )


        AISizer1.Add( AISizer2, 1, wx.EXPAND, 5 )

        AISizer3 = wx.BoxSizer( wx.VERTICAL )

        self.AI_StartButton = wx.Button( self.AI_Control_panel, wx.ID_ANY, u"Start", wx.DefaultPosition, wx.DefaultSize, 0 )
        AISizer3.Add( self.AI_StartButton, 1, wx.ALL|wx.EXPAND, 5 )

        self.m_staticline4 = wx.StaticLine( self.AI_Control_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
        AISizer3.Add( self.m_staticline4, 0, wx.EXPAND |wx.ALL, 5 )

        self.AI_StopButton = wx.Button( self.AI_Control_panel, wx.ID_ANY, u"Stop", wx.DefaultPosition, wx.DefaultSize, 0 )
        AISizer3.Add( self.AI_StopButton, 1, wx.ALL|wx.EXPAND, 5 )

        self.m_staticline6 = wx.StaticLine( self.AI_Control_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
        AISizer3.Add( self.m_staticline6, 0, wx.EXPAND |wx.ALL, 5 )

        self.AI_ExtSample = wx.CheckBox( self.AI_Control_panel, wx.ID_ANY, u"ExtSample", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.AI_ExtSample.SetValue(True)
        AISizer3.Add( self.AI_ExtSample, 1, wx.ALL, 5 )


        AISizer1.Add( AISizer3, 1, wx.EXPAND, 5 )


        self.AI_Control_panel.SetSizer( AISizer1 )
        self.AI_Control_panel.Layout()
        AISizer1.Fit( self.AI_Control_panel )
        MainPanelSizer.Add( self.AI_Control_panel, 1, wx.EXPAND |wx.ALL, 5 )

        self.Graph_panel = wx.Panel( self.Main_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer141 = wx.BoxSizer( wx.VERTICAL )

        self.Graph_panel1 = wx.Panel( self.Graph_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.STATIC_BORDER|wx.TAB_TRAVERSAL )
        bSizer141.Add( self.Graph_panel1, 1, wx.EXPAND |wx.ALL, 5 )


        self.Graph_panel.SetSizer( bSizer141 )
        self.Graph_panel.Layout()
        bSizer141.Fit( self.Graph_panel )
        MainPanelSizer.Add( self.Graph_panel, 1, wx.ALL|wx.EXPAND, 5 )


        self.Main_panel.SetSizer( MainPanelSizer )
        self.Main_panel.Layout()
        MainPanelSizer.Fit( self.Main_panel )
        bSizer1.Add( self.Main_panel, 1, wx.EXPAND |wx.ALL, 5 )


        self.SetSizer( bSizer1 )
        self.Layout()

        # Connect Events
        self.AO_SinWaveStartButton.Bind( wx.EVT_BUTTON, self.SinWaveStart )
        self.AO_SinWaveStopButton.Bind( wx.EVT_BUTTON, self.SinWaveStop )
        self.AO_NoiseStartButton.Bind( wx.EVT_BUTTON, self.WhiteNoiseStart )
        self.AO_NoiseStopButton.Bind( wx.EVT_BUTTON, self.WhiteNoiseStop )
        self.AI_command.Bind( wx.EVT_TEXT, self.AI_Command )
        self.AI_StartButton.Bind( wx.EVT_BUTTON, self.AI_Srart )
        self.AI_StopButton.Bind( wx.EVT_BUTTON, self.AI_Stop )


########################################################################################################


        self.AO_SinWaveStartButton.Enabled = True
        self.AO_SinWaveStopButton.Enabled = False

        self.AO_NoiseStartButton.Enabled = True
        self.AO_NoiseStopButton.Enabled = False

        self.GraphDataExist=False

        self.figure = Figure(  None )    # Figure（グラフの台紙）オブジェクトを生成


#########################################################################################################

    def SinWaveStart( self, event ):
#         event.Skip()
#         print(commonData)
        self.Dev = 'Dev1/ao0'
#             Vmin = -10
#             Vmax = 10
        Freq = float(self.AO_SinFreq.Value)
        SampleN = int(self.AO_SinSampleN.Value)
        CycleN = int(self.AO_SinWaveCycleN.Value)
        Amp = float(self.AO_SinAmp.Value)

        self.SG = AO.SinGenerator(Dev=self.Dev,Freq=Freq,SampleN=SampleN,CycleN=CycleN,Amp=Amp)
#             print(self.SG._resultFreq)
        self.SG.Start()
        self.AO_SinWaveStartButton.Enabled=False
        self.AO_SinWaveStopButton.Enabled=True
#         self.ConsoleBox.Value = 'Sin Wave Start\n'+self.ConsoleBox.Value


    def SinWaveStop( self, event ):
#         event.Skip()
        self.SG.Stop()
        self.SG.Close()
        AO.VoltUpdate(self.Dev,0.0)
        self.SG = None
        self.AO_SinWaveStartButton.Enabled=True
        self.AO_SinWaveStopButton.Enabled=False

#         self.ConsoleBox.Value = 'Sin Wave Stop\n'+self.ConsoleBox.Value



    def WhiteNoiseStart( self, event ):
#         event.Skip()
        self.Dev = 'Dev1/ao0'
        MaxFreq = float(self.AO_NoizeMaxFreq.Value)
        SampleN = int(self.AO_NoiseSampleN.Value)
        Amp=float(self.AO_NoiseAmp.Value)
        self.WG = AO.WhiteNoiseGenerator(Dev=self.Dev,MaxFreq=MaxFreq,SampleN=SampleN,Amp=Amp)
#         print(WG.resultSampleRate)
        self.WG.Start()
        self.AO_NoiseStartButton.Enabled=False
        self.AO_NoiseStopButton.Enabled=True

#         self.ConsoleBox.Value = 'White Noise Start\n'+self.ConsoleBox.Value



    def WhiteNoiseStop( self, event ):
#         event.Skip()
        self.WG.Stop()
        self.WG.Close()
        AO.VoltUpdate(self.Dev,0.0)
        self.WG=None
        self.AO_NoiseStartButton.Enabled=True
        self.AO_NoiseStopButton.Enabled=False

#         self.ConsoleBox.Value = 'White Noise Stop\n'+self.ConsoleBox.Value

    def AI_Srart( self, event ):
#         event.Skip()

        self.NIDaq_done = False

        if self.AI_ExtSample.Value == True:
            self.AI_command.Value = ''
            self.ST1=int(self.AI_StartCH.Value)
            self.ED1=int(self.AI_EndCH.Value)
            self.Freq1=float(self.AI_SampleFreq.Value)
            self.Range1=float(self.AI_Range.Value)
            self.SampleN1=int(self.AI_SampleN.Value)
            print(self.ST1,self.ED1,self.SampleN1)
    #
            self.th = threading.Thread(target=self.AI_Ext, args=(self.ST1, self.ED1,self.Freq1,
                                                            self.Range1,self.SampleN1))
            self.th.start()



        else:
            self.AI_command.Value = ''
            self.ST1=int(self.AI_StartCH.Value)
            self.ED1=int(self.AI_EndCH.Value)
            self.Freq1=float(self.AI_SampleFreq.Value)
            self.Range1=float(self.AI_Range.Value)
            self.SampleN1=int(self.AI_SampleN.Value)
            print(self.ST1,self.ED1,self.SampleN1)
    #
            self.th = threading.Thread(target=self.AI_Int, args=(self.ST1, self.ED1,self.Freq1,
                                                            self.Range1,self.SampleN1))
            self.th.start()

#         self.th.join()

#         data=self.AI_Ext(ST = self.ST1, ED = self.ED1,Freq = self.Freq1, Range = self.Range1,
#                          SampleN = self.SampleN1)
#         d1=np.zeros(self.SampleN1,self.ED1-self.ST1+1)
#         for i in range(self.ED1-self.ST1+1):
#             d1[:,i]=data[i,:]
#
#         self.PlotGraphWindow(self.Graph_panel1,n1=1,m1=4,data=d1,
#                              Freq=self.Freq1,SampleN=self.SampleN1)

    def AI_Command( self, event ):
        command = self.AI_command.Value
        print(command)
        if command == 'OK':
#             self.GraphPlot()
#             data=self.q.get()
#             self.th.join()
            print(self.ST1,self.ED1,self.SampleN1)
#             d1=np.array([[0,0],[0,0]])
#             d1 = np.zeros((3000,2))
            self.NIDaq_data = np.zeros((self.SampleN1,self.ED1-self.ST1+1), dtype = float)
            for i in range(self.ED1-self.ST1+1):
                self.NIDaq_data[:,i]=self.data[i,:]

#             self.GraphDataExist=False
            self.PlotGraphWindow(self.Graph_panel1,n1=1,m1=1,data=self.NIDaq_data,
                                 Freq=self.Freq1,SampleN=self.SampleN1)

            self.NIDaq_done = True

    def GraphPlot(self):

        print(self.ST1,self.ED1.self.SampleN1)
        d1=np.zeros(self.SampleN1,self.ED1-self.ST1+1)
        for i in range(self.ED1-self.ST1+1):
            d1[:,i]=self.data[i,:]

        self.PlotGraphWindow(self.Graph_panel2,n1=4,m1=1,data=d1,
                                 Freq=self.Freq1,SampleN=self.SampleN1)


    def AI_Ext(self,ST=1,ED=2,Freq=1000.0,Range = 2.0,SampleN=3000):

        self.task= nidaqmx.Task()
        v_range =Range   # 0.2,1.0,2.0,5.0,10.0
        sample_freq=Freq
        self.sample_number=SampleN
        dt=1/sample_freq
        devpara="/Dev1/ai0:"+ str(ED - 1)
        rising = nidaqmx.constants.Edge.RISING
        falling = nidaqmx.constants.Edge.FALLING
        finite = nidaqmx.constants.AcquisitionType.FINITE
        task_verify = nidaqmx.constants.TaskMode.TASK_VERIFY

        self.task.ai_channels.add_ai_voltage_chan(devpara, min_val=-v_range, max_val=v_range)


    #     task.export_signals.export_signal(nidaqmx.constants.Signal.SAMPLE_CLOCK,'/Dev1/PFI4')

        self.task.timing.cfg_samp_clk_timing(sample_freq, source=u'/Dev1/PFI0',
                                        active_edge = falling,
                                         sample_mode = finite,
                                        samps_per_chan=self.sample_number)

        self.task.control(task_verify)


    #     print('N Channel N Samples Read: ')

    #     f1.FGStart(sample_freq)

        self.data = self.task.read(number_of_samples_per_channel=self.sample_number,timeout=100)
#             self.data = self.data * 200.0
        self.data = np.array(self.data) * 200.0
#         print(self.data[0,0])
        self.AI_command.Value = 'OK'
        self.task.close()
#         return self.data

    def AI_Int(self,ST=1,ED=2,Freq=1000.0,Range = 2.0,SampleN=3000):
        v_range=Range   # 0.2,1.0,2.0,5.0,10.0
        sample_freq=Freq
        sample_number=SampleN
        dt=1/sample_freq
        devpara="/Dev1/ai0:" + str(ED - 1)
    #     task.timing.cfg_samp_clk_timing(sample_freq, source=u'', active_edge=nidaqmx.constants.Edge.RISING,
    #                               sample_mode=nidaqmx.constants.AcquisitionType.FINITE, samps_per_chan=sample_number)
    #     task.ai_channels.add_ai_voltage_chan("Dev1/ai0:3")
        self.task= nidaqmx.Task()
        self.task.ai_channels.add_ai_voltage_chan(devpara, min_val=-v_range, max_val=v_range)


        self.task.export_signals.export_signal(nidaqmx.constants.Signal.SAMPLE_CLOCK,'/Dev1/PFI4')
    #     task.export_signals.ctr_out_event_output_behavior=nidaqmx.constants.ExportAction.PULSE
        self.task.timing.cfg_samp_clk_timing(sample_freq,samps_per_chan=sample_number)

    #     task.export_signals.export_signal(nidaqmx.constants.Signal.SAMPLE_CLOCK,'/Dev1/PFI4')
    #     task.timing.cfg_burst_handshaking_timing_export_clock(sample_freq, 'Dev1/ctr0')
    #     task.export_signals.ExportSignals(12487,'Dev1/port1/line0')

        print('N Channel N Samples Read: ')
        self.data = self.task.read(number_of_samples_per_channel=sample_number,timeout=100)

        self.data=np.array(self.data)* 200.0
        self.AI_command.Value = 'OK'
        self.task.close()


    def AI_Stop( self, event ):

        self.data = self.task.read(number_of_samples_per_channel=self.sample_number,timeout=100)
        self.data = self.data * 200.0

#         print(self.data[0,0])
        self.AI_command.Value = 'OK'
#             return data



    def PlotGraphWindow(self, panel1 = wx.Panel,n1=1,m1=1,data=None,Freq=1000.0,SampleN=1000):
        '''
        Windowのpanelにグラフを描画する関数
        '''

#         if self.GraphDataExist:
#             self.EraseGraphWindow(panel1)

#         print(self.radiobutton_1.GetValue())
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

        self.y = data
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



def draw(sb,x,y):
    sb.plot(x,y)
    sb.axes.set_ylim((-np.max(y)*1.5,np.max(y)*1.5))
    sb.axes.set_xlim((0,np.max(x)))
    sb.axes.set_title('reference signal',size =8,loc='left')
    sb.axes.set_xlabel('Freq(Hz)',size =8,labelpad=0)
    sb.axes.set_ylabel('P(Pa)',size =8,labelpad=-3)
    sb.axes.tick_params(labelsize=6,direction='in',pad=3)
    sb.axes.grid(color='k', linestyle='-.', linewidth=0.3)



def Draw_Graph(figure1,n,m,x,y):
#     import numpy as np
    h1=figure1.get_figheight()
    w1=figure1.get_figwidth()
    sb2 = []  # サブプロットオブジェクト配列の生成

    ch=1
    for i in range(ch):
        sb2.append(figure1.add_subplot( n , m , i + 1 ))

    a4x = 100         # A4の幅(mm)
    a4y = 50         # A4の高さ(mm)
    mleft = 10        # 左余白(mm)
    mright = 10       # 右余白(mm)
    mtop = 10         # 上余白(mm)
    mbottom = 15      # 下余白(mm)
    mx = 10           # グラフ間のスペースの幅(mm)
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
#
# #     x = np.arange(nn) * dt  # 波形グラフの時間データの作成
#     import random

    for i in range(ch):
        draw(sb2[i] , x , y[:,i])





if __name__ == '__main__':
    app = wx.App()
#     fx = 800
#     fy = 800
#     s1=wx.Size(fx,fy)
    frame2 = NIDaqFrame(None)
    frame2.Show()
    app.MainLoop()
