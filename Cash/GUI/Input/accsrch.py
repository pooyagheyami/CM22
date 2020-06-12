# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.dataview

###########################################################################
## Class MyPanel2
###########################################################################

class MyPanel2 ( wx.Panel ):
	
	def __init__( self, parent , data ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 270,440 ), style = wx.TAB_TRAVERSAL )

		#self.SetLayoutDirection(2)
		Vsz1 = wx.BoxSizer( wx.VERTICAL )
		
		Hsz1 = wx.BoxSizer( wx.HORIZONTAL )

		self.srch1 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0|wx.STATIC_BORDER )
		Hsz1.Add( self.srch1, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.Text1 = wx.StaticText( self, wx.ID_ANY, u"جستجوی حساب", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Text1.Wrap( -1 )
		Hsz1.Add( self.Text1, 0, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		#self.srch1 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0|wx.STATIC_BORDER )
		#Hsz1.Add( self.srch1, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		Vsz1.Add( Hsz1, 0, wx.EXPAND, 5 )
		
		self.DVLC1 = wx.dataview.DataViewListCtrl( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0|wx.STATIC_BORDER )
		
		self.col1 = self.DVLC1.AppendTextColumn( u"کد حساب",width=67 )
		self.col2 = self.DVLC1.AppendTextColumn( u"نام حساب" ,width=187)
		
		Vsz1.Add( self.DVLC1, 1, wx.ALL|wx.EXPAND, 5 )
		
		Vsz2 = wx.BoxSizer( wx.VERTICAL )
		
		self.btn1 = wx.Button( self, wx.ID_ANY, u"انتخاب", wx.DefaultPosition, wx.DefaultSize, 0 )
		Vsz2.Add( self.btn1, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		
		Vsz1.Add( Vsz2, 0, wx.EXPAND, 5 )

		#print data

		for itemvalues in data:
                    self.DVLC1.AppendItem(itemvalues)

		
		self.SetSizer( Vsz1 )
		self.Layout()
		
		# Connect Events
		self.srch1.Bind( wx.EVT_TEXT, self.txtsrch )
		self.srch1.Bind( wx.EVT_TEXT_ENTER, self.txtentr )
		self.Bind( wx.dataview.EVT_DATAVIEW_ITEM_ACTIVATED, self.onslct, id = wx.ID_ANY )
		self.btn1.Bind( wx.EVT_BUTTON, self.onselct )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def txtsrch( self, event ):
		event.Skip()
	
	def txtentr( self, event ):
		event.Skip()
	
	def onslct( self, event ):
                a= self.DVLC1.GetSelectedRow()
                self.retdata()
		q = self.GetParent()
                q.Close()

	
	def onselct( self, event ):
                a= self.DVLC1.GetSelectedRow()
                self.retdata()
		q = self.GetParent()
                q.Close()

	def retdata(self):
                a= self.DVLC1.GetSelectedRow()
                data = []
                if a == -1:
                        data.append(' ')
                else:
                        data.append((unicode(self.DVLC1.GetValue(a,0)),
                                     unicode(self.DVLC1.GetValue(a,1))))
                return data
                


