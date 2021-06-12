# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class MainFrame
###########################################################################

class MainFrame ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Calculator", pos = wx.DefaultPosition, size = wx.Size( 306,340 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		sizerFull = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Made by Rapzy" ), wx.VERTICAL )

		self.textControl = wx.TextCtrl( sizerFull.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 271,-1 ), wx.TE_READONLY|wx.TE_RIGHT )
		sizerFull.Add( self.textControl, 0, wx.ALL, 5 )

		sizer1 = wx.BoxSizer( wx.HORIZONTAL )

		self.button1 = wx.Button( sizerFull.GetStaticBox(), wx.ID_ANY, u"1", wx.DefaultPosition, wx.Size( 60,40 ), 0 )
		sizer1.Add( self.button1, 0, wx.ALL, 5 )

		self.button2 = wx.Button( sizerFull.GetStaticBox(), wx.ID_ANY, u"2", wx.DefaultPosition, wx.Size( 60,40 ), 0 )
		sizer1.Add( self.button2, 0, wx.ALL, 5 )

		self.button3 = wx.Button( sizerFull.GetStaticBox(), wx.ID_ANY, u"3", wx.DefaultPosition, wx.Size( 60,40 ), 0 )
		sizer1.Add( self.button3, 0, wx.ALL, 5 )

		self.buttonAddition = wx.Button( sizerFull.GetStaticBox(), wx.ID_ANY, u"+", wx.DefaultPosition, wx.Size( 60,40 ), 0 )
		sizer1.Add( self.buttonAddition, 0, wx.ALL, 5 )


		sizerFull.Add( sizer1, 1, wx.EXPAND, 5 )

		sizer2 = wx.BoxSizer( wx.HORIZONTAL )

		self.button4 = wx.Button( sizerFull.GetStaticBox(), wx.ID_ANY, u"4", wx.DefaultPosition, wx.Size( 60,40 ), 0 )
		sizer2.Add( self.button4, 0, wx.ALL, 5 )

		self.button5 = wx.Button( sizerFull.GetStaticBox(), wx.ID_ANY, u"5", wx.DefaultPosition, wx.Size( 60,40 ), 0 )
		sizer2.Add( self.button5, 0, wx.ALL, 5 )

		self.button6 = wx.Button( sizerFull.GetStaticBox(), wx.ID_ANY, u"6", wx.DefaultPosition, wx.Size( 60,40 ), 0 )
		sizer2.Add( self.button6, 0, wx.ALL, 5 )

		self.buttonSubstraction = wx.Button( sizerFull.GetStaticBox(), wx.ID_ANY, u"-", wx.DefaultPosition, wx.Size( 60,40 ), 0 )
		sizer2.Add( self.buttonSubstraction, 0, wx.ALL, 5 )


		sizerFull.Add( sizer2, 1, wx.EXPAND, 5 )

		sizer3 = wx.BoxSizer( wx.HORIZONTAL )

		self.button7 = wx.Button( sizerFull.GetStaticBox(), wx.ID_ANY, u"7", wx.DefaultPosition, wx.Size( 60,40 ), 0 )
		sizer3.Add( self.button7, 0, wx.ALL, 5 )

		self.button8 = wx.Button( sizerFull.GetStaticBox(), wx.ID_ANY, u"8", wx.DefaultPosition, wx.Size( 60,40 ), 0 )
		sizer3.Add( self.button8, 0, wx.ALL, 5 )

		self.button9 = wx.Button( sizerFull.GetStaticBox(), wx.ID_ANY, u"9", wx.DefaultPosition, wx.Size( 60,40 ), 0 )
		sizer3.Add( self.button9, 0, wx.ALL, 5 )

		self.buttonMultiplication = wx.Button( sizerFull.GetStaticBox(), wx.ID_ANY, u"*", wx.DefaultPosition, wx.Size( 60,40 ), 0 )
		sizer3.Add( self.buttonMultiplication, 0, wx.ALL, 5 )


		sizerFull.Add( sizer3, 1, wx.EXPAND, 5 )

		sizer4 = wx.BoxSizer( wx.HORIZONTAL )

		self.buttonComma = wx.Button( sizerFull.GetStaticBox(), wx.ID_ANY, u".", wx.DefaultPosition, wx.Size( 60,40 ), 0 )
		sizer4.Add( self.buttonComma, 0, wx.ALL, 5 )

		self.button0 = wx.Button( sizerFull.GetStaticBox(), wx.ID_ANY, u"0", wx.DefaultPosition, wx.Size( 60,40 ), 0 )
		sizer4.Add( self.button0, 0, wx.ALL, 5 )

		self.buttonClear = wx.Button( sizerFull.GetStaticBox(), wx.ID_ANY, u"Clear", wx.DefaultPosition, wx.Size( 60,40 ), 0 )
		sizer4.Add( self.buttonClear, 0, wx.ALL, 5 )

		self.buttonDivision = wx.Button( sizerFull.GetStaticBox(), wx.ID_ANY, u"/", wx.DefaultPosition, wx.Size( 60,40 ), 0 )
		sizer4.Add( self.buttonDivision, 0, wx.ALL, 5 )


		sizerFull.Add( sizer4, 1, wx.EXPAND, 5 )

		sizer5 = wx.BoxSizer( wx.HORIZONTAL )

		self.buttonEquals = wx.Button( sizerFull.GetStaticBox(), wx.ID_ANY, u"=", wx.DefaultPosition, wx.Size( 271,40 ), 0 )
		sizer5.Add( self.buttonEquals, 0, wx.ALL, 5 )


		sizerFull.Add( sizer5, 1, wx.EXPAND, 5 )


		self.SetSizer( sizerFull )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.button1.Bind( wx.EVT_BUTTON, self.addText )
		self.button2.Bind( wx.EVT_BUTTON, self.addText )
		self.button3.Bind( wx.EVT_BUTTON, self.addText )
		self.buttonAddition.Bind( wx.EVT_BUTTON, self.addText )
		self.button4.Bind( wx.EVT_BUTTON, self.addText )
		self.button5.Bind( wx.EVT_BUTTON, self.addText )
		self.button6.Bind( wx.EVT_BUTTON, self.addText )
		self.buttonSubstraction.Bind( wx.EVT_BUTTON, self.addText )
		self.button7.Bind( wx.EVT_BUTTON, self.addText )
		self.button8.Bind( wx.EVT_BUTTON, self.addText )
		self.button9.Bind( wx.EVT_BUTTON, self.addText )
		self.buttonMultiplication.Bind( wx.EVT_BUTTON, self.addText )
		self.buttonComma.Bind( wx.EVT_BUTTON, self.addText )
		self.button0.Bind( wx.EVT_BUTTON, self.addText )
		self.buttonClear.Bind( wx.EVT_BUTTON, self.clearNow )
		self.buttonDivision.Bind( wx.EVT_BUTTON, self.addText )
		self.buttonEquals.Bind( wx.EVT_BUTTON, self.equalsNow )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def addText( self, event ):
		event.Skip()














	def clearNow( self, event ):
		event.Skip()


	def equalsNow( self, event ):
		event.Skip()


