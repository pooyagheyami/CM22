# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.dataview as DV

###########################################################################
## Class MyPanel1
###########################################################################

class MyPanel1 ( wx.Panel ):
	
	def __init__( self, parent,listdata,lfild ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 190,380 ), style = wx.TAB_TRAVERSAL )

		
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer4 = wx.BoxSizer( wx.VERTICAL )

		self.DVLColumn =[]

		self.dVLCtrl1 = DV.DataViewListCtrl( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		for title in range(len(lfild)):
                        
                    self.DVLColumn.append( self.dVLCtrl1.AppendTextColumn( lfild[-1*(title+1)] ) )
                    
                    #print lfild[-1*(title+1)]
                    
		
		bSizer4.Add( self.dVLCtrl1, 5, wx.ALL|wx.EXPAND, 5 )
		
		for itemvalues in listdata:
                    self.dVLCtrl1.AppendItem(itemvalues)

                    
		bSizer1.Add( bSizer4, 5, wx.EXPAND, 5 )
		
		bSizer5 = wx.BoxSizer( wx.HORIZONTAL )
		
				
		self.m_button1 = wx.Button( self, wx.ID_ANY, u"انتخاب", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer5.Add( self.m_button1, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		self.m_button2 = wx.Button( self, wx.ID_ANY, u"انصراف", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer5.Add( self.m_button2, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		
		bSizer1.Add( bSizer5, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer1 )
		self.Layout()
		
		# Connect Events
		self.Bind( wx.dataview.EVT_DATAVIEW_ITEM_ACTIVATED, self.onselect1, id = wx.ID_ANY )
		
		self.m_button1.Bind( wx.EVT_BUTTON, self.onselect )
		self.m_button2.Bind( wx.EVT_BUTTON, self.oncancel )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def oncancel( self, event ):
                q = self.GetParent()
                q.Close()
                
	def onselect1( self, event ):
		
		a= self.dVLCtrl1.GetSelectedRow()
		#print a
		#print self.dVLCtrl1.GetTextValue(a,0)
		#print self.dVLCtrl1.GetTextValue(a,1)
		self.retdata()
		q = self.GetParent()
                q.Close()
		
	def onselect( self, event ):
               
                b = self.dVLCtrl1.GetSelectedRow()
                #print b
                #print self.dVLCtrl1.GetValue(b,0)
                #print self.dVLCtrl1.GetValue(b,1)
                self.retdata()
                q = self.GetParent()
                q.Close()
                
        def retdata(self):
                r = self.dVLCtrl1.GetSelectedRow()
                data = []
                for d in range(len(self.DVLColumn)):
                        if r == -1:
                                data.append(' ')
                        else:
                                data.append( unicode(self.dVLCtrl1.GetValue(r,d)) )
                return data        
                #q = self.GetParent()
                #q.Close()
	

