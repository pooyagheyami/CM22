# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import input04

###########################################################################
## Class Input
###########################################################################

class MyPanel1 ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY,  pos = wx.DefaultPosition, size = wx.Size( 142,188 ), style = wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		VBz = wx.BoxSizer( wx.VERTICAL )
		
		Hbz1 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.Text = wx.StaticText( self, wx.ID_ANY, u"حساب:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Text.Wrap( -1 )
		Hbz1.Add( self.Text, 1, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.btn1 = wx.Button( self, wx.ID_ANY, u"...", wx.DefaultPosition, wx.DefaultSize, wx.BU_EXACTFIT )
		Hbz1.Add( self.btn1, 0, wx.ALL, 5 )
		
		
		VBz.Add( Hbz1, 0, wx.EXPAND, 5 )
		
		cBox1Choices = [ u"صندوق", u"کارتخوان", u"تنخواه", u"برداشت" ]
		self.cBox1 = wx.ComboBox( self, wx.ID_ANY, u"صندوق", wx.DefaultPosition, wx.DefaultSize, cBox1Choices, 0 )
		self.cBox1.SetSelection( 0 )
		VBz.Add( self.cBox1, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.btnin = wx.Button( self, wx.ID_ANY, u"دریافت ...", wx.DefaultPosition, wx.DefaultSize, 0 )
		VBz.Add( self.btnin, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.btnout = wx.Button( self, wx.ID_ANY, u"پرداخت ...", wx.DefaultPosition, wx.DefaultSize, 0 )
		VBz.Add( self.btnout, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		self.SetSizer( VBz )
		self.Layout()
		
		self.Centre( wx.BOTH )

		self.Racc = u"صندوق"
		# Connect Events
		self.btn1.Bind( wx.EVT_BUTTON, self.slctacc )
		self.cBox1.Bind( wx.EVT_COMBOBOX, self.chosacc )
		self.btnin.Bind( wx.EVT_BUTTON, self.Oninput )
		self.btnout.Bind( wx.EVT_BUTTON, self.Onoutput )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def slctacc( self, event ):
		event.Skip()
	
	def chosacc( self, event ):
		#print self.cBox1.GetStringSelection()
		self.Racc = self.cBox1.GetStringSelection()
	
	def Oninput( self, event ):
		self.r = wx.Frame(self,style = wx.CAPTION|wx.CLOSE_BOX|wx.FRAME_FLOAT_ON_PARENT|wx.TAB_TRAVERSAL)
		lbl =  [u'دريافتي',self.Racc,u'مبلغ',u'بحروف',
                        u'در تاريخ',u'از حساب',u'بابت',u'به شماره قبض']
		txt = [u'دريافت گرديد',u'انصراف',u'چاپ رسيد',u'ثبت در سند']
		lst = [u'ريال',u'تومان']
		self.pnl = input04.MyPanel1(self.r,lbl,lst,txt)
		self.r.SetTitle(u'ورود اطلاعات')
		self.r.SetSize((523,305))
		self.r.Show()
	
	def Onoutput( self, event ):
		self.s = wx.Frame(self,style = wx.CAPTION|wx.CLOSE_BOX|wx.FRAME_FLOAT_ON_PARENT|wx.TAB_TRAVERSAL)
		lbl =  [u'پرداختي',self.Racc,u'مبلغ',u'بحروف',
                        u'در تاريخ',u'به حساب',u'بابت',u'به شماره قبض']
		txt = [u'پرداخت گرديد',u'انصراف',u'چاپ رسيد',u'ثبت در سند']
		lst = [u'ريال',u'تومان']
		self.pnl = input04.MyPanel1(self.s,lbl,lst,txt)
		self.s.SetTitle(u'ورود اطلاعات')
		self.s.SetSize((523,305))
		self.s.Show()
	

