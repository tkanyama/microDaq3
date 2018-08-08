# -*- coding: utf-8 -*-
import wx
import wx.xrc

from time import sleep
import time
import threading

import numpy as np
import matplotlib
matplotlib.interactive( True )
matplotlib.use( 'WXAgg' )
import matplotlib.pyplot as plt
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg
from matplotlib.figure import Figure



from microDaqFrame01 import *
from NIDaqFrame01 import *
from CurveFit01 import *
from TubuHosei import *
from win32ui import IDR_MAINFRAME


commonData='gbrc'
microDAQFlag = False
NIDaqFlag = False

# メニューIDの設定
ID_PLOT = 101
ID_PRINT =102
ID_EXIT = 103
ID_CLEAR = 104
ID_COPY = 201
ID_PASTE =202


###########################################################################
## Class MyFrame2
###########################################################################

class MainFrame ( wx.Frame ):

    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Main Control", pos = wx.Point( 5,20 ), size = wx.Size( 700,1020 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

        self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )

        self.m_menubar2 = wx.MenuBar( 0 )
        self.m_menu4 = wx.Menu()
        self.m_menuItem7 = wx.MenuItem( self.m_menu4, wx.ID_ANY, u"終了", wx.EmptyString, wx.ITEM_NORMAL )
        self.m_menu4.AppendItem( self.m_menuItem7 )

        self.m_menubar2.Append( self.m_menu4, u"File" )

        self.SetMenuBar( self.m_menubar2 )

        bSizer15 = wx.BoxSizer( wx.HORIZONTAL )

        bSizer111 = wx.BoxSizer( wx.VERTICAL )

        bSizer121 = wx.BoxSizer( wx.HORIZONTAL )

        bSizer2 = wx.BoxSizer( wx.VERTICAL )

        bSizer6 = wx.BoxSizer( wx.HORIZONTAL )

        self.microDAQ_FrameStartButton = wx.Button( self, wx.ID_ANY, u"microDAQ", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer6.Add( self.microDAQ_FrameStartButton, 1, wx.ALL|wx.EXPAND, 5 )


        bSizer2.Add( bSizer6, 1, wx.EXPAND, 5 )

        bSizer9 = wx.BoxSizer( wx.HORIZONTAL )

        self.microDAQ_ZeroButton = wx.Button( self, wx.ID_ANY, u"Zero Start", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.microDAQ_ZeroButton.SetMaxSize( wx.Size( 60,-1 ) )

        bSizer9.Add( self.microDAQ_ZeroButton, 1, wx.ALL|wx.EXPAND, 5 )

        self.microDAQ_ReadyButton = wx.Button( self, wx.ID_ANY, u"Ready", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.microDAQ_ReadyButton.SetMaxSize( wx.Size( 60,-1 ) )

        bSizer9.Add( self.microDAQ_ReadyButton, 1, wx.ALL|wx.EXPAND, 5 )

        self.microDAQ_StartButton = wx.Button( self, wx.ID_ANY, u"Start", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.microDAQ_StartButton.SetMaxSize( wx.Size( 60,-1 ) )

        bSizer9.Add( self.microDAQ_StartButton, 1, wx.ALL|wx.EXPAND, 5 )


        bSizer2.Add( bSizer9, 1, wx.EXPAND, 5 )


        bSizer121.Add( bSizer2, 1, wx.EXPAND, 5 )

        bSizer4 = wx.BoxSizer( wx.VERTICAL )

        bSizer7 = wx.BoxSizer( wx.HORIZONTAL )

        self.NIDaq_FrameStartButton = wx.Button( self, wx.ID_ANY, u"NIDaq", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer7.Add( self.NIDaq_FrameStartButton, 1, wx.ALL|wx.EXPAND, 5 )


        bSizer4.Add( bSizer7, 1, wx.EXPAND, 5 )

        bSizer11 = wx.BoxSizer( wx.HORIZONTAL )

        self.NIDaq_SinStartButton = wx.Button( self, wx.ID_ANY, u"Sin Start", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.NIDaq_SinStartButton.SetMaxSize( wx.Size( 50,-1 ) )

        bSizer11.Add( self.NIDaq_SinStartButton, 1, wx.ALL|wx.EXPAND, 5 )

        self.NIDaq_SInStopButton = wx.Button( self, wx.ID_ANY, u"Sin Stop", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.NIDaq_SInStopButton.SetMaxSize( wx.Size( 50,-1 ) )

        bSizer11.Add( self.NIDaq_SInStopButton, 1, wx.ALL|wx.EXPAND, 5 )

        self.NIDaq_WNStartButton = wx.Button( self, wx.ID_ANY, u"White\nNoise\nStart", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.NIDaq_WNStartButton.SetFont( wx.Font( 8, 70, 90, 90, False, wx.EmptyString ) )
        self.NIDaq_WNStartButton.SetMaxSize( wx.Size( 50,-1 ) )

        bSizer11.Add( self.NIDaq_WNStartButton, 1, wx.ALL|wx.EXPAND, 5 )

        self.NIDaq_WNStopButton = wx.Button( self, wx.ID_ANY, u"White\nNoise\nStop", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.NIDaq_WNStopButton.SetFont( wx.Font( 8, 70, 90, 90, False, wx.EmptyString ) )
        self.NIDaq_WNStopButton.SetMaxSize( wx.Size( 50,-1 ) )

        bSizer11.Add( self.NIDaq_WNStopButton, 1, wx.ALL|wx.EXPAND, 5 )

        self.NIDaq_AIStartButton = wx.Button( self, wx.ID_ANY, u"AI Start", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.NIDaq_AIStartButton.SetMaxSize( wx.Size( 50,-1 ) )

        bSizer11.Add( self.NIDaq_AIStartButton, 1, wx.ALL|wx.EXPAND, 5 )

        self.NIDaq_AIStopButton = wx.Button( self, wx.ID_ANY, u"AI Stop", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.NIDaq_AIStopButton.SetMaxSize( wx.Size( 50,-1 ) )

        bSizer11.Add( self.NIDaq_AIStopButton, 1, wx.ALL|wx.EXPAND, 5 )


        bSizer4.Add( bSizer11, 1, wx.EXPAND, 5 )


        bSizer121.Add( bSizer4, 1, wx.EXPAND, 5 )

        bSizer5 = wx.BoxSizer( wx.VERTICAL )

        bSizer8 = wx.BoxSizer( wx.HORIZONTAL )

        self.End_Buttton = wx.Button( self, wx.ID_ANY, u"終了", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer8.Add( self.End_Buttton, 1, wx.ALL|wx.EXPAND, 5 )


        bSizer5.Add( bSizer8, 1, wx.EXPAND, 5 )

        bSizer12 = wx.BoxSizer( wx.HORIZONTAL )

        self.Comon_StartButton = wx.Button( self, wx.ID_ANY, u"microDAQ + AI Start", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer12.Add( self.Comon_StartButton, 1, wx.ALL|wx.EXPAND, 5 )


        bSizer5.Add( bSizer12, 1, wx.EXPAND, 5 )


        bSizer121.Add( bSizer5, 1, wx.EXPAND, 5 )


        bSizer111.Add( bSizer121, 1, wx.EXPAND, 5 )

        bSizer13 = wx.BoxSizer( wx.VERTICAL )

        bSizer151 = wx.BoxSizer( wx.VERTICAL )

        bSizer16 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_panel4 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.STATIC_BORDER|wx.TAB_TRAVERSAL )
        self.m_panel4.SetMaxSize( wx.Size( -1,220 ) )

        gSizer2 = wx.GridSizer( 4, 2, 0, 0 )

        self.m_staticText6 = wx.StaticText( self.m_panel4, wx.ID_ANY, u"Unit No.", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText6.Wrap( -1 )
        gSizer2.Add( self.m_staticText6, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )

        Unit_ChiceChoices = [ u"1", u"2", u"3", u"4", u"5", u"6", u"7", u"8", u"9", u"10", u"11", u"12" ]
        self.Unit_Chice = wx.Choice( self.m_panel4, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, Unit_ChiceChoices, 0 )
        self.Unit_Chice.SetSelection( 0 )
        self.Unit_Chice.SetMaxSize( wx.Size( 80,-1 ) )

        gSizer2.Add( self.Unit_Chice, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_staticText111 = wx.StaticText( self.m_panel4, wx.ID_ANY, u"f0", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText111.Wrap( -1 )
        gSizer2.Add( self.m_staticText111, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )

        self.f0_Text = wx.TextCtrl( self.m_panel4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.f0_Text.SetMaxSize( wx.Size( 70,-1 ) )

        gSizer2.Add( self.f0_Text, 0, wx.ALL, 5 )

        self.m_staticText12 = wx.StaticText( self.m_panel4, wx.ID_ANY, u"h", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText12.Wrap( -1 )
        gSizer2.Add( self.m_staticText12, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )

        self.h_Text = wx.TextCtrl( self.m_panel4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.h_Text.SetMaxSize( wx.Size( 70,-1 ) )

        gSizer2.Add( self.h_Text, 0, wx.ALL, 5 )

        self.m_staticText13 = wx.StaticText( self.m_panel4, wx.ID_ANY, u"c", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText13.Wrap( -1 )
        gSizer2.Add( self.m_staticText13, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )

        self.c_Text = wx.TextCtrl( self.m_panel4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.c_Text.SetMaxSize( wx.Size( 70,-1 ) )

        gSizer2.Add( self.c_Text, 0, wx.ALL, 5 )


        self.m_panel4.SetSizer( gSizer2 )
        self.m_panel4.Layout()
        gSizer2.Fit( self.m_panel4 )
        bSizer16.Add( self.m_panel4, 1, wx.EXPAND |wx.ALL, 5 )

        self.m_panel3 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.STATIC_BORDER|wx.TAB_TRAVERSAL )
        self.m_panel3.SetMaxSize( wx.Size( -1,220 ) )

        bSizer161 = wx.BoxSizer( wx.VERTICAL )

        self.m_panel51 = wx.Panel( self.m_panel3, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        self.m_panel51.SetMaxSize( wx.Size( -1,25 ) )

        bSizer18 = wx.BoxSizer( wx.VERTICAL )

        self.m_staticText14 = wx.StaticText( self.m_panel51, wx.ID_ANY, u"サイン波による周波数応答", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText14.Wrap( -1 )
        bSizer18.Add( self.m_staticText14, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


        self.m_panel51.SetSizer( bSizer18 )
        self.m_panel51.Layout()
        bSizer18.Fit( self.m_panel51 )
        bSizer161.Add( self.m_panel51, 1, wx.EXPAND |wx.ALL, 5 )

        gSizer1 = wx.GridSizer( 5, 2, 0, 0 )

        self.m_staticText1 = wx.StaticText( self.m_panel3, wx.ID_ANY, u"Start Freq", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText1.Wrap( -1 )
        gSizer1.Add( self.m_staticText1, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.StartFreq = wx.TextCtrl( self.m_panel3, wx.ID_ANY, u"5", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.StartFreq.SetMaxSize( wx.Size( 60,-1 ) )

        gSizer1.Add( self.StartFreq, 0, wx.ALL, 5 )

        self.m_staticText2 = wx.StaticText( self.m_panel3, wx.ID_ANY, u"End Freq", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText2.Wrap( -1 )
        gSizer1.Add( self.m_staticText2, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )

        self.End_Freq = wx.TextCtrl( self.m_panel3, wx.ID_ANY, u"200", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.End_Freq.SetMaxSize( wx.Size( 60,-1 ) )

        gSizer1.Add( self.End_Freq, 0, wx.ALL, 5 )

        self.m_staticText3 = wx.StaticText( self.m_panel3, wx.ID_ANY, u"Freq Pitch", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText3.Wrap( -1 )
        gSizer1.Add( self.m_staticText3, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )

        self.Freq_Pitch = wx.TextCtrl( self.m_panel3, wx.ID_ANY, u"5", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.Freq_Pitch.SetMaxSize( wx.Size( 60,-1 ) )

        gSizer1.Add( self.Freq_Pitch, 0, wx.ALL, 5 )

        self.m_staticText5 = wx.StaticText( self.m_panel3, wx.ID_ANY, u"Recent Freq", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText5.Wrap( -1 )
        gSizer1.Add( self.m_staticText5, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )

        self.Recent_Freq = wx.TextCtrl( self.m_panel3, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.Recent_Freq.SetMaxSize( wx.Size( 60,-1 ) )

        gSizer1.Add( self.Recent_Freq, 0, wx.ALL, 5 )

        self.Sweep_StartButton = wx.Button( self.m_panel3, wx.ID_ANY, u"Start", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.Sweep_StartButton.SetMaxSize( wx.Size( 70,-1 ) )

        gSizer1.Add( self.Sweep_StartButton, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

        self.Sweep_StopButton = wx.Button( self.m_panel3, wx.ID_ANY, u"Stop", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.Sweep_StopButton.SetMaxSize( wx.Size( 70,-1 ) )

        gSizer1.Add( self.Sweep_StopButton, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


        bSizer161.Add( gSizer1, 1, wx.EXPAND, 5 )


        self.m_panel3.SetSizer( bSizer161 )
        self.m_panel3.Layout()
        bSizer161.Fit( self.m_panel3 )
        bSizer16.Add( self.m_panel3, 1, wx.EXPAND |wx.ALL, 5 )

        self.m_panel5 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.STATIC_BORDER|wx.TAB_TRAVERSAL )
        self.m_panel5.SetMaxSize( wx.Size( -1,220 ) )

        bSizer20 = wx.BoxSizer( wx.VERTICAL )

        self.m_panel6 = wx.Panel( self.m_panel5, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        self.m_panel6.SetMinSize( wx.Size( -1,25 ) )
        self.m_panel6.SetMaxSize( wx.Size( -1,25 ) )

        bSizer22 = wx.BoxSizer( wx.VERTICAL )

        self.m_staticText15 = wx.StaticText( self.m_panel6, wx.ID_ANY, u"ホワイトノイズによる周波数応答", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText15.Wrap( -1 )
        bSizer22.Add( self.m_staticText15, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


        self.m_panel6.SetSizer( bSizer22 )
        self.m_panel6.Layout()
        bSizer22.Fit( self.m_panel6 )
        bSizer20.Add( self.m_panel6, 1, wx.EXPAND |wx.ALL, 5 )

        gSizer3 = wx.GridSizer( 6, 2, 0, 0 )

        self.m_staticText7 = wx.StaticText( self.m_panel5, wx.ID_ANY, u"総データ数", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText7.Wrap( -1 )
        gSizer3.Add( self.m_staticText7, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )

        self.All_DataN = wx.TextCtrl( self.m_panel5, wx.ID_ANY, u"16384", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.All_DataN.SetMaxSize( wx.Size( 60,-1 ) )

        gSizer3.Add( self.All_DataN, 0, wx.ALL, 5 )

        self.m_staticText8 = wx.StaticText( self.m_panel5, wx.ID_ANY, u"分析データ数", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText8.Wrap( -1 )
        gSizer3.Add( self.m_staticText8, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )

        self.Anal_DataN = wx.TextCtrl( self.m_panel5, wx.ID_ANY, u"1024", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.Anal_DataN.SetMaxSize( wx.Size( 60,-1 ) )

        gSizer3.Add( self.Anal_DataN, 0, wx.ALL, 5 )

        self.m_staticText9 = wx.StaticText( self.m_panel5, wx.ID_ANY, u"オーバーラップ", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText9.Wrap( -1 )
        gSizer3.Add( self.m_staticText9, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )

        self.Over_RapN = wx.TextCtrl( self.m_panel5, wx.ID_ANY, u"512", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.Over_RapN.SetMaxSize( wx.Size( 60,-1 ) )

        gSizer3.Add( self.Over_RapN, 0, wx.ALL, 5 )

        self.m_staticText10 = wx.StaticText( self.m_panel5, wx.ID_ANY, u"繰り返し回数", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText10.Wrap( -1 )
        gSizer3.Add( self.m_staticText10, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )

        self.RepeatN = wx.TextCtrl( self.m_panel5, wx.ID_ANY, u"10", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.RepeatN.SetMaxSize( wx.Size( 60,-1 ) )

        gSizer3.Add( self.RepeatN, 0, wx.ALL, 5 )

        self.m_staticText11 = wx.StaticText( self.m_panel5, wx.ID_ANY, u"回数", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText11.Wrap( -1 )
        gSizer3.Add( self.m_staticText11, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )

        self.RepeatI = wx.TextCtrl( self.m_panel5, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.RepeatI.SetMaxSize( wx.Size( 60,-1 ) )

        gSizer3.Add( self.RepeatI, 0, wx.ALL, 5 )

        self.White_Noise_StartButton = wx.Button( self.m_panel5, wx.ID_ANY, u"Start", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.White_Noise_StartButton.SetMaxSize( wx.Size( 70,-1 ) )

        gSizer3.Add( self.White_Noise_StartButton, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

        self.White_Noise_StopButton = wx.Button( self.m_panel5, wx.ID_ANY, u"Stop", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.White_Noise_StopButton.SetMaxSize( wx.Size( 70,-1 ) )

        gSizer3.Add( self.White_Noise_StopButton, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


        bSizer20.Add( gSizer3, 1, wx.EXPAND, 5 )


        self.m_panel5.SetSizer( bSizer20 )
        self.m_panel5.Layout()
        bSizer20.Fit( self.m_panel5 )
        bSizer16.Add( self.m_panel5, 1, wx.EXPAND |wx.ALL, 5 )


        bSizer151.Add( bSizer16, 1, wx.EXPAND, 5 )

        self.botton_panel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        self.botton_panel.SetMinSize( wx.Size( -1,35 ) )

        bSizer23 = wx.BoxSizer( wx.HORIZONTAL )

        self.Save_button = wx.Button( self.botton_panel, wx.ID_ANY, u"Save", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer23.Add( self.Save_button, 0, wx.ALL, 5 )

        self.Load_button = wx.Button( self.botton_panel, wx.ID_ANY, u"Load", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer23.Add( self.Load_button, 0, wx.ALL, 5 )

        self.m_staticText16 = wx.StaticText( self.botton_panel, wx.ID_ANY, u"Start Point(%)", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText16.Wrap( -1 )
        bSizer23.Add( self.m_staticText16, 0, wx.ALL, 5 )

        self.StartPoint = wx.TextCtrl( self.botton_panel, wx.ID_ANY, u"5", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.StartPoint.SetMaxSize( wx.Size( 40,-1 ) )

        bSizer23.Add( self.StartPoint, 0, wx.ALL, 5 )

        self.m_staticText17 = wx.StaticText( self.botton_panel, wx.ID_ANY, u"End Point(%)", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText17.Wrap( -1 )
        bSizer23.Add( self.m_staticText17, 0, wx.ALL, 5 )

        self.m_textCtrl14 = wx.TextCtrl( self.botton_panel, wx.ID_ANY, u"100", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_textCtrl14.SetMaxSize( wx.Size( 40,-1 ) )

        bSizer23.Add( self.m_textCtrl14, 0, wx.ALL, 5 )

        self.CurveFit_button = wx.Button( self.botton_panel, wx.ID_ANY, u"Curve Fit", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer23.Add( self.CurveFit_button, 0, wx.ALL, 5 )


        self.botton_panel.SetSizer( bSizer23 )
        self.botton_panel.Layout()
        bSizer23.Fit( self.botton_panel )
        bSizer151.Add( self.botton_panel, 1, wx.EXPAND |wx.ALL, 5 )

        self.Main_panel1 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.STATIC_BORDER|wx.TAB_TRAVERSAL )
        self.Main_panel1.SetMinSize( wx.Size( -1,700 ) )

        bSizer151.Add( self.Main_panel1, 1, wx.EXPAND |wx.ALL, 5 )


        bSizer13.Add( bSizer151, 1, wx.EXPAND, 5 )


        bSizer111.Add( bSizer13, 1, wx.EXPAND, 5 )


        bSizer15.Add( bSizer111, 1, wx.EXPAND, 5 )


        self.SetSizer( bSizer15 )
        self.Layout()
        self.MainLoop_timer1 = wx.Timer()
        self.MainLoop_timer1.SetOwner( self, wx.ID_ANY )

        # Connect Events
        self.microDAQ_FrameStartButton.Bind( wx.EVT_BUTTON, self.microDAQ_FrameStart )
        self.microDAQ_ZeroButton.Bind( wx.EVT_BUTTON, self.microDAQ_ZeroStart )
        self.microDAQ_ReadyButton.Bind( wx.EVT_BUTTON, self.microDAQ_Ready )
        self.microDAQ_StartButton.Bind( wx.EVT_BUTTON, self.microDAQ_Start )
        self.NIDaq_FrameStartButton.Bind( wx.EVT_BUTTON, self.NIDaq_FrameStart )
        self.NIDaq_SinStartButton.Bind( wx.EVT_BUTTON, self.NIDaq_SinStart )
        self.NIDaq_SInStopButton.Bind( wx.EVT_BUTTON, self.NIDaq_SinStop )
        self.NIDaq_WNStartButton.Bind( wx.EVT_BUTTON, self.NIDaq_WhiteNoiseStart )
        self.NIDaq_WNStopButton.Bind( wx.EVT_BUTTON, self.NIDaq_WhiteNoiseStop )
        self.NIDaq_AIStartButton.Bind( wx.EVT_BUTTON, self.NIDaq_AIStart )
        self.NIDaq_AIStopButton.Bind( wx.EVT_BUTTON, self.NIDaq_AIStop )
        self.End_Buttton.Bind( wx.EVT_BUTTON, self.Main_end )
        self.Comon_StartButton.Bind( wx.EVT_BUTTON, self.microDAQ_AI_Start )
        self.Unit_Chice.Bind( wx.EVT_CHOICE, self.Unit_Change )
        self.Sweep_StartButton.Bind( wx.EVT_BUTTON, self.Sweep_Start )
        self.Sweep_StopButton.Bind( wx.EVT_BUTTON, self.Sweep_Stop )
        self.White_Noise_StartButton.Bind( wx.EVT_BUTTON, self.White_Noise_Start )
        self.White_Noise_StopButton.Bind( wx.EVT_BUTTON, self.White_Noise_Stop )
        self.Save_button.Bind( wx.EVT_BUTTON, self.Data_Save )
        self.Load_button.Bind( wx.EVT_BUTTON, self.Data_Load )
        self.CurveFit_button.Bind( wx.EVT_BUTTON, self.DoCurveFit )
        self.Bind( wx.EVT_TIMER, self.Main_Loop1, id=wx.ID_ANY )






#     ここから上を「wxFormBilder」からコピペ

        self.mode = 0
        self.figure = Figure(  None )    # Figure（グラフの台紙）オブジェクトを生成

        self.cp=[]
        exec('self.cp.append(self.f0_Text)')
#         self.cp.append(self.f0_Text)
        self.cp.append(self.h_Text)
        self.cp.append(self.c_Text)

        for i in range(3):
            self.cp[i].Value =str(i)

#         print(self.__dict__)

    def __del__( self ):
        pass


    # Virtual event handlers, overide them in your derived class
    def microDAQ_FrameStart( self, event ):

#    microDAQコントロールフレームを作成して表示するボタンの処理

        self._microDAQFrame = microDaqFrame(None)
        self._microDAQFrame.Show()


    def NIDaq_FrameStart( self, event ):

#    NIDaqコントロールフレームを作成して表示するボタン処理

        self._NIDaqFrame = NIDaqFrame(None)
        self._NIDaqFrame.Show()

    def Main_end( self, event ):

#    プログラムの終了処理ボタン処理

        self.MainExit()


    def MainExit(self):

#    プログラムの終了処理

        dlg = wx.MessageDialog(self, message = u"終了します。よろしいですか？",
                                caption = u"終了確認", style = wx.YES_NO)
        result = dlg.ShowModal()
        if result == wx.ID_YES:
#             self.Close(force=False)
            wx.Exit()


    def microDAQ_ZeroStart( self, event ):

#    microDAQのゼロ測定スタートボタン処理

        self._microDAQFrame.MIcroDAQ_ZeroStart(event)

    def microDAQ_Ready( self, event ):

#    microDAQの測定準備ボタン処理

        self._microDAQFrame.microDAQ_Ready(event)

    def microDAQ_Start( self, event ):

#    microDAQの測定スタートボタン処理

        self._microDAQFrame.microDAQ_Start(event)

    def NIDaq_SinStart( self, event ):

#    NIDaqのサイン波スタートボタン処理

        self._NIDaqFrame.SinWaveStart(event)

    def NIDaq_SinStop( self, event ):

#    NIDaqのサイン波ストップボタン処理

        self._NIDaqFrame.SinWaveStop(event)

    def NIDaq_WhiteNoiseStart( self, event ):

#    NIDaqのホワイトノイズ　スタートボタン処理

        self._NIDaqFrame.WhiteNoiseStart(event)

    def NIDaq_WhiteNoiseStop( self, event ):

#    NIDaqのホワイトノイズ　ストップボタン処理

        self._NIDaqFrame.WhiteNoiseStop(event)

    def NIDaq_AIStart( self, event ):

#    NIDaqの測定開始ボタン処理

        self._NIDaqFrame.AI_Srart(event)

    def NIDaq_AIStop( self, event ):

#    NIDaqの測定停止ボタン処理

        self._NIDaqFrame.AI_Stop(event)

    def microDAQ_AI_Start( self, event ):
        self._NIDaqFrame.AI_ExtSample.Value = True
        Freq = float(self._microDAQFrame.microDAQ_SampleFreq.Value)
        SampleN = int(self._microDAQFrame.microDAQ_SampleN.Value)
        self._NIDaqFrame.AI_SampleFreq.Value = str(Freq)
        self._NIDaqFrame.AI_SampleN.Value = str(SampleN)
        self._NIDaqFrame.AI_Srart(event)
        self._microDAQFrame.microDAQ_Start(event)

    def Sweep_Start( self, event ):

        if self._microDAQFrame.ZeroFlag :
            self.WaveMode=1
            self.mode = 1
            self.done = False
            self.R_Freq = float( self.StartFreq.Value )
            self.P_Freq = float( self.Freq_Pitch.Value)
            self.E_Freq = float( self.End_Freq.Value)
            self._MaxFreq = self.E_Freq

            self.FreqN = int((self.E_Freq-self.R_Freq)/self.P_Freq) + 1
            self.ChN = 32
            self.UnitN = int(self._microDAQFrame.microDAQ_GraphUnitNo.Value)-1
            self.G_Freq=np.zeros(self.FreqN)
            self.G_Amp = np.zeros((self.FreqN,self.ChN))
            self.G_Phase = np.zeros((self.FreqN,self.ChN))

            self._TubeHoseiFlag = self._microDAQFrame.TubeHoseiCheck.Value

            self.Count = 0

            for i in range(self.FreqN):
                self.G_Freq[i]= self.R_Freq + self.P_Freq * i
                for j in range(self.ChN):
                    self.G_Amp[i,j]=1.0
                    self.G_Phase[i,j]=0.0

            self.PlotGraphWindow(freq=self.G_Freq,amp=self.G_Amp,phase=self.G_Phase)
            self.Recent_Freq.Value = str(self.R_Freq)
            self.MainLoop_timer1.Start(100)


        else:
            dlg = wx.MessageDialog(self, message = u"Zero測定をしてください！！", caption = u"エラー", style = wx.YES_NO)
            result = dlg.ShowModal()
            if result == wx.ID_YES:
                pass



    def Data_Save( self, event ):
        event.Skip()

    def Data_Load( self, event ):
        event.Skip()

    def DoCurveFit( self, event ):
        event.Skip()



    def Main_Loop1( self, event ):

        if self.WaveMode ==1:

            if self.mode == 1:
                if self.done :
                    if self._microDAQFrame._ReadyFlag:
                        self.mode = 2
                        self.done = False
                        sleep(0.5)
                else:
                    self.microDAQ_Ready(wx.Event)
                    self.done =True
                    sleep(0.5)

            elif self.mode == 2:
                if self.done:
                    if self._microDAQFrame.microDAQ_Done and self._NIDaqFrame.NIDaq_done:
                        self._NIDaqFrame.SinWaveStop(wx.Event)
                        self.mode = 3
                        self.done = False
                        sleep(0.5)
                else:
                    self._NIDaqFrame.AO_SinFreq.Value = str(self.R_Freq)
                    self._NIDaqFrame.SinWaveStart(wx.Event)
                    self.microDAQ_AI_Start(wx.Event)
                    self.done =True
                    sleep(0.5)

            elif self.mode == 3:
                self.MainLoop_timer1.Stop()
                self.NIData = self._NIDaqFrame.NIDaq_data
                self.microData = self._microDAQFrame.micro_data
                (x,y)=self.Calc_Amp_Phase(self.NIData[:,0], self.microData[:,:,self.UnitN])
                self.G_Amp[self.Count,:]=x
                self.G_Phase[self.Count,:]=y
#                 self.EraseGraphWindow()
                self.PlotGraphWindow(freq=self.G_Freq,amp=self.G_Amp,phase=self.G_Phase,CalcFlag=False)

                self.Count += 1
                self.R_Freq += self.P_Freq
                self.Recent_Freq.Value = str(self.R_Freq)

                if self.R_Freq>self.E_Freq:
                    self.MainLoop_timer1.Stop()
                    if self._TubeHoseiFlag==False:
                        self.PlotGraphWindow(freq=self.G_Freq,amp=self.G_Amp,phase=self.G_Phase,CalcFlag=True)
                        np.save('freq',self.G_Freq)
                        np.save('amp',self.G_Amp)

                    self.mode =0

                else:
                    self.mode = 1
                    self.MainLoop_timer1.Start(100)

        elif self.WaveMode ==2:

            if self.mode == 1:
                if self.done :
                    if self._microDAQFrame._ReadyFlag:
                        self.mode = 2
                        self.done = False
                        sleep(0.5)
                else:
                    self.microDAQ_Ready(wx.Event)
                    self.done =True
                    sleep(0.5)

            elif self.mode == 2:
                if self.done:
                    if self._microDAQFrame.microDAQ_Done and self._NIDaqFrame.NIDaq_done:
                        self._NIDaqFrame.WhiteNoiseStop(wx.Event)
                        self.mode = 3
                        self.done = False
                        sleep(0.5)
                else:
    #                 self._NIDaqFrame.AO_SinFreq.Value = str(self.R_Freq)
    #                 self._NIDaqFrame.SinWaveStart(wx.Event)
                    self._NIDaqFrame.WhiteNoiseStart(wx.Event)
                    self.microDAQ_AI_Start(wx.Event)
                    self.done =True
                    sleep(0.5)

            elif self.mode == 3:
                self.MainLoop_timer1.Stop()
                self.NIData = self._NIDaqFrame.NIDaq_data
                self.microData = self._microDAQFrame.micro_data
                x=self.NIData[:,0]
                y=self.microData[:,:,self.UnitN]

#                 if self._TubeHoseiFlag:
#                     tb=TubuHosei(98.6,0.274,1.034,0.001)
#
#                     for j in range(self.ChN):
#                         y[:,j] = tb.Hosei(y[:,j])

                n1=0
                n2=self._Anal_DataN

                Win = np.hanning(n2)
                print(Win.shape)
                while True:

                    self.Count +=1

                    for i in range(self.ChN):
                        x1 = x[n1 : n2]
                        y1 = y[n1 : n2,i]
#                         print(x1.shape)

                        x1 = np.fft.fft(x1 * Win)
                        y1 = np.fft.fft(y1 * Win)


                        if self.Count == 1:
                            self.G_Trans[:,i] =  (y1*np.conj(x1))/(x1*np.conj(x1))
                        else:
                            self.G_Trans[:,i] = (self.G_Trans[:,i] * (self.Count-1) + (y1*np.conj(x1))/(x1*np.conj(x1)))/self.Count


                    n1 = n1 + self._Over_RapN
                    n2 = n2 + self._Over_RapN

                    if n2 > self._All_DataN:

                        break


                self.G_Amp = np.abs(self.G_Trans)
                self.G_Phase = np.angle(self.G_Trans,deg = True)

#                 self.EraseGraphWindow()
                self.PlotGraphWindow(freq=self.G_Freq,amp=self.G_Amp,phase=self.G_Phase,CalcFlag=False)

                self._RepeatI += 1
                self.RepeatI.Value = str(self._RepeatI)

                if self._RepeatI >= self._RepeatN:
                    self.mode =0

                    if self._TubeHoseiFlag==False:
#                         self.EraseGraphWindow()
                        self.PlotGraphWindow(freq=self.G_Freq,amp=self.G_Amp,phase=self.G_Phase,CalcFlag=True)
                        np.save('freq',self.G_Freq)
                        np.save('amp',self.G_Amp)

                else:
                    self.MainLoop_timer1.Start(100)
                    self.mode = 1




    def White_Noise_Start( self, event ):
        if self._microDAQFrame.ZeroFlag :
            self.mode = 1
            self.WaveMode=2
            self.done = False
            self._All_DataN = int(self.All_DataN.Value)
            self._Anal_DataN = int(self.Anal_DataN.Value)
            self._Over_RapN = int(self.Over_RapN.Value)
            self._RepeatN = int(self.RepeatN.Value)
            self._MaxFreq = 200
            self._SampleFreq = float(self._microDAQFrame.microDAQ_SampleFreq.Value)
            self._Dt = 1.0/self._SampleFreq
            self._Df = 1.0/(self._Dt*self._Anal_DataN)

            self._TubeHoseiFlag = self._microDAQFrame.TubeHoseiCheck.Value

            self.ChN = 32
            self.UnitN = int(self._microDAQFrame.microDAQ_GraphUnitNo.Value)-1
            self.G_Freq=np.arange(self._Anal_DataN)*self._Df
            self.G_Trans = np.zeros((self._Anal_DataN,self.ChN)) * (0+0j)
            self.G_Amp = np.zeros((self._Anal_DataN,self.ChN))+1.0
            self.G_Phase = np.zeros((self._Anal_DataN,self.ChN))

            self._microDAQFrame.microDAQ_SampleN.Value = str(self._All_DataN)
            self._NIDaqFrame.AI_SampleN.Value = str(self._All_DataN)


            self.Count = 0
            self._RepeatI = 0
            self.RepeatI.Value = str(self._RepeatI)

            self.PlotGraphWindow(freq=self.G_Freq,amp=self.G_Amp,phase=self.G_Phase,CalcFlag=False)
            self.MainLoop_timer1.Start(100)

        else:
            dlg = wx.MessageDialog(self, message = u"Zero測定をしてください！！", caption = u"エラー", style = wx.YES_NO)
            result = dlg.ShowModal()
            if result == wx.ID_YES:
                pass



    def White_Noise_Stop( self, event ):
        self.MainLoop_timer1.Stop()
        self.mode =0



    def Calc_Amp_Phase(self,x,y):

        N=np.shape(x)[0]
        x0=np.mean(x)
        x1 = x - x0
        xrms = np.sqrt(np.sum(x1 * x1)/N)
#         print(N)
        Window1=np.hanning(N)
        FData1 = np.fft.fft(Window1 * x)/N*4.0
        p1=np.argmax(np.abs(FData1))
        amp1 = np.abs(FData1)[p1]
        phase1 = np.angle(FData1,deg = True)[p1]
#         print(amp1,phase1)
        amp=np.zeros(32)
        phase=np.zeros(32)
        for i in range(32):
            y0=np.mean(y[:,i])
            y1 = y[:,i]-y0
            yrms = np.sqrt( np.sum(y1 * y1)/N )
            FData2 = np.fft.fft(Window1 * y[:,i])/N*4.0
            p2=np.argmax(np.abs(FData2))
#             amp[i] = np.abs(FData2)[p2]/amp1
            amp[i] = yrms /xrms
            phase[i] = np.angle(FData2,deg = True)[p1]-phase1
            if phase[i]>180:
                phase[i] -= 360
            elif phase[i]<-180:
                phase[i] += 360


        print(amp[0],phase[0],phase1)


        return (amp,phase)


    def Sweep_Stop( self, event ):
        self.MainLoop_timer1.Stop()
        self.mode =0


    def Unit_Change( self, event ):
        event.Skip()


    def PlotGraphWindow(self, freq=None,amp=None,phase = None,CalcFlag = False):
        '''
        Windowのpanelにグラフを描画する関数
        '''
        panel1 = self.Main_panel1
        n1 = 4
        m1 = 2

#         print(self.radiobutton_1.GetValue())
#         from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg
#         from matplotlib.figure import Figure
#         self.figure = Figure(  None )    # Figure（グラフの台紙）オブジェクトを生成
        self.figure.clf(keep_observers=False)
        self.figure.set_facecolor( (0.8,0.8,0.8) )  # Figureの表面色を設定

        #panel2にFigureを貼り付けcanvasを生成
        self.canvas = FigureCanvasWxAgg( panel1, -1, self.figure )
        self.canvas.SetSize( tuple( panel1.GetClientSize() ) ) # canvasのサイズをpanel2に合わせる。
#         print(self.canvas.Size,self.canvas.Position)

        self.canvas.SetBackgroundColour( wx.Colour( 100,0,255 ) ) # Canvasの背景色を設定（これは不要？）


        a4x = 300         # A4の幅(mm)
        a4y = 250         # A4の高さ(mm)
        mleft = 20        # 左余白(mm)
        mright = 15       # 右余白(mm)
        mtop = 15         # 上余白(mm)
        mbottom = 15      # 下余白(mm)
        mx = 20           # グラフ間のスペースの幅(mm)
        my = 15           # グラフ間のスペースの高さ(mm)
            # ひとつのグラフの幅(mm)を計算
        if m1>1:
            xx = (a4x - mleft - mright - mx * ( m1 - 1 ) )/m1
        else:
            xx = a4x - mleft - mright

        # ひとつのグラフの高さ(mm)を計算
        if n1>1:
            yy = (a4y - mbottom - mtop - my * (n1 - 1) )/n1
        else:
            yy = a4y - mbottom - mtop

        self.figure.subplots_adjust(left=mleft/a4x, bottom=mbottom/a4y, right=(a4x-mright)/a4x, top=(a4y-mtop)/a4y,
                        wspace=mx/xx, hspace=my/yy)


        sb = []  # サブプロットオブジェクト配列の生成
        sb2 = []
        ch=4
        for i in range(ch):
            sb.append(self.figure.add_subplot( n1 , m1 , 2*i + 1 ))
#             for i in range(ch):
            sb[i].plot(freq,amp[:,i])
            sb[i].axes.set_ylim((0,3))
            sb[i].axes.set_xlim((0,self._MaxFreq))
            sb[i].axes.set_title('[ch'+str(i+1)+':amp]',size =8,loc='left')
            sb[i].axes.set_xlabel('Freq(Hz)',size =8,labelpad=0)
            sb[i].axes.set_ylabel('Amp',size =8,labelpad=0)
            sb[i].axes.tick_params(labelsize=6,direction='in',pad=3)
            sb[i].axes.grid(color='k', linestyle='-.', linewidth=0.3)


            if CalcFlag:
                if self.WaveMode == 1:
                    nmax = int(np.argmax(amp)*1.05)
#                     nmax=np.argmax(amp)
                    x0=np.array([200.0,1.0,2.0])
                    cf = CurveFit(freq[1:nmax],amp[1:nmax,i],x0)
                    r1 = cf.Calc()
                    x1 = np.arange(200)
                    y1 = cf.ydata(x1)
                    sb[i].plot(x1,y1)

                    if i==0:
                        self.f0_Text.Value = '{:.3f}'.format(r1[0])
                        self.h_Text.Value = '{:.3f}'.format(r1[1])
                        self.c_Text.Value = '{:.3f}'.format(r1[2])

                elif self.WaveMode == 2 :
                    nmax=np.argmax(amp[3:300,0])
                    x0=np.array([200.0,1.0,2.0])
                    cf = CurveFit(freq[1:nmax],amp[1:nmax,i],x0)
                    r1 = cf.Calc()
                    x1 = np.arange(200)
                    y1 = cf.ydata(x1)
                    sb[i].plot(x1,y1)

                    if i==0:
                        for j in range(3):
                            self.cp[j].Value='{:.3f}'.format(r1[j])
#                         self.f0_Text.Value = '{:.3f}'.format(r1[0])
#                         self.h_Text.Value = '{:.3f}'.format(r1[1])
#                         self.c_Text.Value = '{:.3f}'.format(r1[2])


        for i in range(ch):
            sb2.append(self.figure.add_subplot( n1 , m1 , 2*(i+1)  ))
#             for i in range(ch):
            sb2[i].plot(freq,phase[:,i])
            sb2[i].axes.set_ylim((-180,180))
            sb2[i].axes.set_xlim((0,self._MaxFreq))
            sb2[i].axes.set_title('[ch'+str(i+1)+':phase]',size =8,loc='left')
            sb2[i].axes.set_xlabel('Freq(Hz)',size =8,labelpad=0)
            sb2[i].axes.set_ylabel('Phase(deg)',size =8,labelpad=-3)
            sb2[i].axes.tick_params(labelsize=6,direction='in',pad=3)
            sb2[i].axes.grid(color='k', linestyle='-.', linewidth=0.3)

            if CalcFlag:
                if self.WaveMode == 1:
                    nmax=np.argmax(amp)
                    x0=np.array([200.0,1.0,2.0])
                    cf = CurveFit(freq[1:nmax],amp[1:nmax,i],x0)
                    r1 = cf.Calc()
                    x1 = np.arange(200)
                    y1 = cf.PhaseData(x1)
                    sb2[i].plot(x1,y1)

                elif self.WaveMode ==2:

                    nmax=np.argmax(amp[3:300,0])
                    x0=np.array([200.0,1.0,2.0])
                    cf = CurveFit(freq[1:nmax],amp[1:nmax,i],x0)
                    r1 = cf.Calc()
                    print(r1)
                    x1 = np.arange(200)
                    y1 = cf.PhaseData(x1)
                    sb2[i].plot(x1,y1)


#                 sb[i].ylim([-180,180])

    def EraseGraphWindow(self):
        '''
        Windowのpanelのグラフを消去する関数
        '''
        panel1 = self.Main_panel1
#         print(self.radiobutton_1.GetValue())
        from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg
        from matplotlib.figure import Figure
        self.figure = Figure(  None )    # Figure（グラフの台紙）オブジェクトを生成
        self.figure.set_facecolor( (1.0,1.0,1.0) )  # Figureの表面色を設定

        #panel2にFigureを貼り付けcanvasを生成
        self.canvas = FigureCanvasWxAgg( panel1, -1, self.figure )
        self.canvas.SetSize( tuple( panel1.GetClientSize() ) ) # canvasのサイズをpanel2に合わせる。

#         self.GraphDataExist = False


if __name__ == '__main__':
    app = wx.App()
    _MainFrame = MainFrame(None)
    _MainFrame.Show()
    event = wx.Event
    _MainFrame.microDAQ_FrameStart(event )
    _MainFrame.NIDaq_FrameStart(event )

    app.MainLoop()
