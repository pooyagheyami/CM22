# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
from wx import MessageBox,OK,YES_NO,ICON_WARNING,ICON_INFORMATION
import Utility.Adaad2 as adad
import Utility.calfar01 as calfar01
import Utility.calcu as ca
from Config.Init import *
import Database.CDataGet as DG
import srclist as sr
import accsrch

###########################################################################
## Class MyPanel1
###########################################################################

class MyPanel1 ( wx.Panel ):
	
	def __init__( self, parent, lbl ,lst , txt ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 523,305 ), style = wx.TAB_TRAVERSAL )

		self.SetLayoutDirection(2)
		self.nmbr = adad.Adaad(1,u'')
		self.iCash = DG.GetData(u'',u'')
		self.jCash = DG.SetData(u'',u'')
		Vsz1 = wx.BoxSizer( wx.VERTICAL )
		
		Hsz1 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.labl1 = wx.StaticText( self, wx.ID_ANY, lbl[0], wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labl1.Wrap( -1 )
		self.labl1.SetFont( wx.Font( 16, 70, 90, 90, False, wx.EmptyString ) )
		
		Hsz1.Add( self.labl1, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.labl2 = wx.StaticText( self, wx.ID_ANY, lbl[1], wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labl2.Wrap( -1 )
		self.labl2.SetFont( wx.Font( 16, 70, 90, 90, False, wx.EmptyString ) )
		
		Hsz1.Add( self.labl2, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.Hbtn = wx.BitmapButton( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		Hsz1.Add( self.Hbtn, 1, wx.ALIGN_RIGHT|wx.ALL|wx.SHAPED, 5 )
		
		
		Vsz1.Add( Hsz1, 1, wx.EXPAND, 5 )
		
		Hsz2 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.labl3 = wx.StaticText( self, wx.ID_ANY, lbl[2], wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labl3.Wrap( -1 )
		Hsz2.Add( self.labl3, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.fld1 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		Hsz2.Add( self.fld1, 0, wx.ALIGN_CENTER, 5 )
		
		self.Cbtn = wx.BitmapButton( self, wx.ID_ANY, wx.Bitmap( UTILITY_PATH+u"calculator.bmp", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		Hsz2.Add( self.Cbtn, 0, wx.ALIGN_CENTER_VERTICAL|wx.TOP|wx.BOTTOM, 5 )
		
		choice1Choices = lst
		self.choice1 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, choice1Choices, 0 )
		self.choice1.SetSelection( 0 )
		Hsz2.Add( self.choice1, 0, wx.ALIGN_CENTER, 5 )
		
		self.labl4 = wx.StaticText( self, wx.ID_ANY, lbl[3], wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labl4.Wrap( -1 )
		Hsz2.Add( self.labl4, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.fld2 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		Hsz2.Add( self.fld2, 1, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		
		Vsz1.Add( Hsz2, 1, wx.EXPAND, 5 )
		
		Hsz3 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.labl5 = wx.StaticText( self, wx.ID_ANY, lbl[4], wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labl5.Wrap( -1 )
		Hsz3.Add( self.labl5, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.idate = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		Hsz3.Add( self.idate, 0, wx.ALIGN_CENTER_VERTICAL|wx.TOP|wx.BOTTOM|wx.LEFT, 5 )
		
		self.dbtn = wx.BitmapButton( self, wx.ID_ANY, wx.ArtProvider.GetBitmap( wx.ART_GO_DOWN, wx.ART_BUTTON ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		Hsz3.Add( self.dbtn, 0, wx.ALIGN_CENTER_VERTICAL|wx.TOP|wx.BOTTOM, 5 )
		
		self.labl6 = wx.StaticText( self, wx.ID_ANY, lbl[5], wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labl6.Wrap( -1 )
		Hsz3.Add( self.labl6, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.fld3 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		Hsz3.Add( self.fld3, 1, wx.ALIGN_CENTER, 5 )
		
		self.btn1 = wx.Button( self, wx.ID_ANY, u"...", wx.DefaultPosition, wx.Size( 25,25 ), 0 )
		Hsz3.Add( self.btn1, 0, wx.ALIGN_CENTER|wx.ALL, 1 )
		
		
		Vsz1.Add( Hsz3, 1, wx.EXPAND, 5 )
		
		Hsz4 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.labl7 = wx.StaticText( self, wx.ID_ANY, lbl[6], wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labl7.Wrap( -1 )
		Hsz4.Add( self.labl7, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.fld4 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		Hsz4.Add( self.fld4, 1, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.labl8 = wx.StaticText( self, wx.ID_ANY, lbl[7], wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labl8.Wrap( -1 )
		Hsz4.Add( self.labl8, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.fld5 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		Hsz4.Add( self.fld5, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		
		Vsz1.Add( Hsz4, 1, wx.EXPAND, 5 )
		
		Hsz5 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.labl11 = wx.CheckBox( self, wx.ID_ANY, txt[2], wx.DefaultPosition, wx.DefaultSize, 0 )
		Hsz5.Add( self.labl11, 1, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.labl12 = wx.CheckBox( self, wx.ID_ANY, txt[3], wx.DefaultPosition, wx.DefaultSize, 0 )
		Hsz5.Add( self.labl12, 1, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.btn2 = wx.Button( self, wx.ID_ANY, txt[1], wx.DefaultPosition, wx.DefaultSize, 0 )
		Hsz5.Add( self.btn2, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.btn3 = wx.Button( self, wx.ID_ANY, txt[0], wx.DefaultPosition, wx.DefaultSize, 0 )
		Hsz5.Add( self.btn3, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		
		Vsz1.Add( Hsz5, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( Vsz1 )
		self.Layout()

		# Initial Panel And Prameter
		self.Pcal1 = wx.PopupTransientWindow(self.GetTopLevelParent(),wx.SIMPLE_BORDER)
                self.pnl = calfar01.MyPanel2(self.Pcal1,-1,-1)

                self.pnl.Bind(wx.EVT_BUTTON,self.Onbind,source=None)
                
		self.cur = 0
		self.txtcur = u'ريال'
		self.isnd = 0
		# Connect Events
		self.fld1.Bind( wx.EVT_TEXT, self.amont )
		self.Cbtn.Bind( wx.EVT_BUTTON, self.calcu )
		self.choice1.Bind( wx.EVT_CHOICE, self.curncy )
		self.idate.Bind( wx.EVT_TEXT, self.chgdate )
		self.dbtn.Bind( wx.EVT_BUTTON, self.dat )
		self.btn1.Bind( wx.EVT_BUTTON, self.acsrch )
		self.labl11.Bind( wx.EVT_CHECKBOX, self.prn )
		self.labl12.Bind( wx.EVT_CHECKBOX, self.insnd )
		self.btn2.Bind( wx.EVT_BUTTON, self.cancl )
		self.btn3.Bind( wx.EVT_BUTTON, self.takit )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def amont( self, event ):
                iamnt = event.GetEventObject().GetValue()
                
                if ',' in iamnt:
                    d = iamnt.replace(',','')
                else:
                    d = iamnt
		self.fld2.SetValue(self.nmbr.num2txt(int(d))+' '+self.txtcur)
	
	def calcu( self, event ):
		dlg = wx.Dialog(self,-1)
                pnl = ca.MyPanel1(dlg)
                dlg.SetSize((176,252))
                
                dlg.ShowModal()
                adad = self.nmbr.Rondtxtnum(pnl.getValue())
                                
                self.fld1.SetValue(self.nmbr.Digigrop(int(adad),','))

                self.Refresh()
                self.Layout()

                dlg.Destroy()
	
	def curncy( self, event ):
		cur =  event.GetEventObject().GetSelection()
		self.txtcur =  event.GetEventObject().GetStringSelection()
		iamnt = self.fld1.GetValue()
		if ',' in iamnt:
                    d = iamnt.replace(',','')
                else:
                    d = iamnt
                    
		if cur == 1:
                    nwamnt = self.nmbr.Ril2Tmn(int(d))
                    self.fld1.SetValue(self.nmbr.Digigrop(nwamnt,','))
                if cur == 0:
                    nwamnt = self.nmbr.Tmn2Ril(int(d))
                    self.fld1.SetValue(self.nmbr.Digigrop(nwamnt,','))    
                                       
	
	def chgdate( self, event ):
		event.Skip()

        def dat( self, event ):
		self.Pcal1.SetSize((280,190))
		btn = event.GetEventObject()
                pos = btn.ClientToScreen( (0,0) )
                sz =  btn.GetSize()
                self.Pcal1.Position(pos, (0, sz[1]))
                
                self.Pcal1.Popup()
	def Onbind(self, event):
                #print event
                #print event.GetEventObject().GetLabel()
                r = event.GetEventObject().GetLabel()
                mydate = self.pnl.Zdate(event)
                self.idate.SetValue(mydate)
                
                                   
	
	def acsrch( self, event ):
		self.lstmoin = self.iCash.ShwAcc()
		iwin = wx.Dialog(self,-1)
		pnl = accsrch.MyPanel2(iwin,self.lstmoin)
		iwin.SetSize((270,440))
		iwin.ShowModal()

		self.icust = pnl.retdata()
		#print icust
		self.fld3.SetValue(self.icust[0][1])

		self.Refresh()
		self.Layout() 
		iwin.Destroy()
	
	def prn( self, event ):
		event.Skip()
	
	def insnd( self, event ):
		self.isnd = 1
	
	def cancl( self, event ):
		q = self.GetParent()
                q.Close()
	
	def takit( self, event ):
                #print self.chkghbz()
                if self.chkghbz() == 1:
                        idata = self.Getdata()
                        self.SetData(idata)
                        if self.isnd == 1:
                                import Database.insnd2 as IS
                                IS.Input2_Document(idata)
                                MessageBox(u'درآخرين سند ثبت شد',u'اعلان',OK | ICON_INFORMATION)
                        MessageBox(u'قبض با موفقيت ثبت شد',u'اعلان',OK | ICON_INFORMATION)
                        q = self.GetParent()
                        q.Close()
                        
	def Getdata( self ):
                f1 = self.fld5.GetValue()
                f2 = self.idate.GetValue()
                f3 = self.labl1.GetLabel()
                f4 = self.fld3.GetValue()
                f41 = self.icust[0][0]
                f5 = self.fld4.GetValue()
                f51 = hex(int(f1))[2:]+'-'+hex(int(f2[-5:-3]+f2[-2:]))[2:]
                iamnt = self.fld1.GetValue()
		if ',' in iamnt:
                    d = iamnt.replace(',','')
                else:
                    d = iamnt
                f6 = d
                f61 = self.choice1.GetSelection()
                return [f1,f2,f3,f4,f41,f5,f51,f6,f61]
                
        def SetData( self , data ):
                #self.iCash
                #print data
                thisdata = [data[0],data[1],'1000001',data[4],data[6],int(data[7])]
                data2 = [data[6],data[5]]
                self.jCash.InCash1('Cnum , Cdate, Ctype, Cacc, Cdes, Amount',thisdata)
                self.jCash.InCDes1('Cdes, Cdescpt',data2)
                #print 'OK'
                
        def chkghbz( self ):
                if self.fld1.GetValue() == '':
                        MessageBox(u'مبلغ قبض را مشخص کنيد',u'خطا',OK | ICON_WARNING)
                        return 0
                if self.idate.GetValue() == '':
                        MessageBox(u'تاريخ را مشخص کنيد',u'خطا',OK | ICON_WARNING)
                        return 0
                if self.fld3.GetValue() == '':
                        MessageBox(u'حساب را انتخاب کنيد',u'خطا',OK | ICON_WARNING)
                        return 0
                if self.fld4.GetValue() == '':
                        MessageBox(u'شرح را بنويسيد',u'خطا',OK | ICON_WARNING)
                        return 0
                if self.fld5.GetValue() == '':
                        MessageBox(u'شماره قبض را مشخص کنيد',u'خطا',OK | ICON_WARNING)
                        return 0
                return 1

