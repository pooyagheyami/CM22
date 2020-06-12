# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.grid
import wx.dataview
import Utility.Adaad2 as adad
from wx import MessageBox,OK,YES_NO,ICON_WARNING,ICON_INFORMATION
import  wx.lib.scrolledpanel as scrolled
import Utility.calfar01 as calfar01
import Utility.calcu as ca
import Utility.B1 as B1
from Config.Init import *
import Database.FDataGet as DG
import Specy 
import accsrch
import Fprint 
###########################################################################
## Class MyPanel2
###########################################################################

class MyPanel2 ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 508,672 ), style = wx.TAB_TRAVERSAL )

		self.iFakt = DG.GetData(u'',u'')
		self.jFakt = DG.SetData(u'',u'')
		self.inum = adad.Adaad(1,'')
		if self.iFakt.shwFno() == []:
                        self.Fnum = self.inum.n2f(1)
                else:
                        maxnum = int(self.iFakt.shwFno()[-1][0])
                        #print maxnum+1
                        self.Fnum = self.inum.n2f(maxnum+1)
		self.Frow = 9
		icomp = self.iFakt.gCmpny()
		#print icomp[0][1]
		VSz1 = wx.BoxSizer( wx.VERTICAL )
		
		Vsz11 = wx.BoxSizer( wx.VERTICAL )
		
		self.pnl1 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.RAISED_BORDER )
		Vsz12 = wx.BoxSizer( wx.VERTICAL )
		
		self.titr1 = wx.StaticText( self.pnl1, wx.ID_ANY, icomp[0][1], wx.DefaultPosition, wx.DefaultSize, 0 )
		self.titr1.Wrap( -1 )
		Vsz12.Add( self.titr1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.titr2 = wx.StaticText( self.pnl1, wx.ID_ANY, u"فاکتور فروش", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.titr2.Wrap( -1 )
		self.titr2.SetFont( wx.Font( 19, 70, 90, 90, False, wx.EmptyString ) )
		
		Vsz12.Add( self.titr2, 0, wx.ALIGN_CENTER|wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		self.pnl1.SetSizer( Vsz12 )
		self.pnl1.Layout()
		Vsz12.Fit( self.pnl1 )
		Vsz11.Add( self.pnl1, 0, wx.EXPAND |wx.ALL, 5 )
		
		
		VSz1.Add( Vsz11, 0, wx.EXPAND, 5 )
		
		self.lin1 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		VSz1.Add( self.lin1, 0, wx.EXPAND |wx.ALL, 5 )
		
		Vsz2 = wx.BoxSizer( wx.VERTICAL )
		
		self.pnl2 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.RAISED_BORDER )
		#self.pnl2 = scrolled.ScrolledPanel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.RAISED_BORDER )


		Vsz21 = wx.BoxSizer( wx.VERTICAL )
		
		HSz1 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.nbtn = wx.BitmapButton( self.pnl2, wx.ID_ANY, wx.ArtProvider.GetBitmap( wx.ART_GO_BACK, wx.ART_BUTTON ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		HSz1.Add( self.nbtn, 0, wx.ALIGN_CENTER_VERTICAL|wx.TOP|wx.BOTTOM|wx.LEFT, 5 )
		
		self.bbtn = wx.BitmapButton( self.pnl2, wx.ID_ANY, wx.ArtProvider.GetBitmap( wx.ART_GO_FORWARD, wx.ART_BUTTON ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		HSz1.Add( self.bbtn, 0, wx.ALIGN_CENTER_VERTICAL|wx.TOP|wx.BOTTOM, 5 )
		
		self.fld1 = wx.TextCtrl( self.pnl2, wx.ID_ANY, self.Fnum, wx.DefaultPosition, wx.Size( 45,-1 ), 0 )
		HSz1.Add( self.fld1, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.lbl1 = wx.StaticText( self.pnl2, wx.ID_ANY, u"شماره", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lbl1.Wrap( -1 )
		HSz1.Add( self.lbl1, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		
		Vsz21.Add( HSz1, 1, wx.EXPAND, 5 )
		
		HSz2 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.dbtn = wx.BitmapButton( self.pnl2, wx.ID_ANY, wx.ArtProvider.GetBitmap( wx.ART_GO_DOWN, wx.ART_BUTTON ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		HSz2.Add( self.dbtn, 0, wx.TOP|wx.BOTTOM|wx.LEFT, 5 )
		
		self.idate = wx.TextCtrl( self.pnl2, wx.ID_ANY, NOW, wx.DefaultPosition, wx.Size( 75,-1 ), 0 )
		HSz2.Add( self.idate, 0, wx.TOP|wx.BOTTOM|wx.RIGHT, 5 )
		
		self.lbl2 = wx.StaticText( self.pnl2, wx.ID_ANY, u"تاریخ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lbl2.Wrap( -1 )
		HSz2.Add( self.lbl2, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.btn1 = wx.Button( self.pnl2, wx.ID_ANY, u"...", wx.DefaultPosition, wx.Size( 25,-1 ), 0 )
		HSz2.Add( self.btn1, 0, wx.TOP|wx.BOTTOM|wx.LEFT, 5 )
		
		self.fld3 = wx.TextCtrl( self.pnl2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_RIGHT )
		HSz2.Add( self.fld3, 1, wx.ALIGN_CENTER|wx.TOP|wx.BOTTOM|wx.RIGHT, 5 )
		
		self.lbl3 = wx.StaticText( self.pnl2, wx.ID_ANY, u"صورتحساب", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lbl3.Wrap( -1 )
		HSz2.Add( self.lbl3, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		
		Vsz21.Add( HSz2, 1, wx.EXPAND, 5 )
		
		
		self.pnl2.SetSizer( Vsz21 )
		self.pnl2.Layout()
		Vsz21.Fit( self.pnl2 )
		Vsz2.Add( self.pnl2, 0, wx.EXPAND |wx.ALL, 5 )
		
		
		VSz1.Add( Vsz2, 0, wx.EXPAND, 5 )
		
		Vsz3 = wx.BoxSizer( wx.VERTICAL )
		
		#self.pnl3 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.RAISED_BORDER|wx.TAB_TRAVERSAL )
		self.pnl3 = scrolled.ScrolledPanel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size(500,450), wx.RAISED_BORDER )
		
		Vsz31 = wx.BoxSizer( wx.VERTICAL )
		
		HSz3 = wx.BoxSizer( wx.HORIZONTAL )

		self.clbla = []
		self.cola = [(u"مبلغ",92),(u"فی",90),(u"تعداد",50),(u"شرح کالا",210),(u"رد",19)]
		i = 0
		for col in self.cola:
                        self.clbla.append(  wx.StaticText( self.pnl3, wx.ID_ANY, col[0], wx.DefaultPosition, wx.Size( col[1],-1 ), wx.ALIGN_CENTRE|wx.DOUBLE_BORDER ) )
                        self.clbla[i].Wrap( -1 )
                        HSz3.Add( self.clbla[i], 0, wx.ALIGN_BOTTOM|wx.ALL|wx.EXPAND, 0 )
                        i = i + 1
		
		
		Vsz31.Add( HSz3, 0, wx.EXPAND, 0 )
		
		HSz4 = wx.BoxSizer( wx.HORIZONTAL )
		
		cboxChoices = [ u"به ریال", u"به تومان" ]
		self.cbox = wx.ComboBox( self.pnl3, wx.ID_ANY, u"به ریال", wx.DefaultPosition, wx.Size( 92,-1 ), cboxChoices, wx.CB_READONLY )
		self.cbox.SetSelection( 0 )
		HSz4.Add( self.cbox, 0, wx.ALIGN_BOTTOM, 0 )

                self.clblb = []
                self.colb = [(u'',90),(u'',50),(u'',210),(u'',19)]
                i = 0
		for col in self.colb:
                        self.clblb.append( wx.StaticText( self.pnl3, wx.ID_ANY, col[0], wx.DefaultPosition, wx.Size( col[1],-1 ), wx.ALIGN_CENTRE|wx.DOUBLE_BORDER ) )
                        self.clblb[i].Wrap( -1 )
                        HSz4.Add( self.clblb[i], 0, wx.ALIGN_BOTTOM|wx.EXPAND, 0 )
                        i = i + 1
                        
		
		
		Vsz31.Add( HSz4, 0, wx.EXPAND, 0 )
		
		FGSz = wx.FlexGridSizer( 0, 9, 0, 0 )
		FGSz.SetFlexibleDirection( wx.BOTH )
		FGSz.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_ALL )

		self.Amnt = []

		for i in range(4):
                        self.Amnt.append( wx.grid.Grid( self.pnl3, wx.ID_ANY, wx.DefaultPosition, wx.Size( 23,-1 ), 0 ) )

                        # Grid
                        self.Amnt[i].CreateGrid( self.Frow, 1 )
                        self.Amnt[i].EnableEditing( True )
                        self.Amnt[i].EnableGridLines( True )
                        self.Amnt[i].EnableDragGridSize( False )
                        self.Amnt[i].SetMargins( 0, 0 )

                        # Columns
                        self.Amnt[i].SetColSize( 0, 23 )
                        self.Amnt[i].EnableDragColMove( False )
                        self.Amnt[i].EnableDragColSize( True )
                        self.Amnt[i].SetColLabelSize( 0 )
                        self.Amnt[i].SetColLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )

                        # Rows
                        self.Amnt[i].EnableDragRowSize( True )
                        self.Amnt[i].SetRowLabelSize( 0 )
                        self.Amnt[i].SetRowLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )

                        # Label Appearance

                        # Cell Defaults
                        if i% 2:
                                self.Amnt[i].SetDefaultCellBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_3DLIGHT ) )
                           
                        self.Amnt[i].SetDefaultCellAlignment( wx.ALIGN_RIGHT, wx.ALIGN_CENTRE )
                        FGSz.Add( self.Amnt[i], 0, 0, 0 )
                        
                        
		
		
		self.Sgr3 = wx.grid.Grid( self.pnl3, wx.ID_ANY, wx.DefaultPosition, wx.Size( 90,-1 ), 0 )
		
		# Grid
		self.Sgr3.CreateGrid( self.Frow, 1 )
		self.Sgr3.EnableEditing( True )
		self.Sgr3.EnableGridLines( True )
		self.Sgr3.EnableDragGridSize( False )
		self.Sgr3.SetMargins( 0, 0 )
		
		# Columns
		self.Sgr3.SetColSize( 0, 90 )
		self.Sgr3.EnableDragColMove( False )
		self.Sgr3.EnableDragColSize( True )
		self.Sgr3.SetColLabelSize( 0 )
		self.Sgr3.SetColLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Rows
		self.Sgr3.EnableDragRowSize( True )
		self.Sgr3.SetRowLabelSize( 0 )
		self.Sgr3.SetRowLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Label Appearance
		
		# Cell Defaults
		self.Sgr3.SetDefaultCellAlignment( wx.ALIGN_CENTRE, wx.ALIGN_TOP )
		FGSz.Add( self.Sgr3, 0, 0, 0 )
		
		self.Sgr2 = wx.grid.Grid( self.pnl3, wx.ID_ANY, wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
		
		# Grid
		self.Sgr2.CreateGrid( self.Frow, 1 )
		self.Sgr2.EnableEditing( True )
		self.Sgr2.EnableGridLines( True )
		self.Sgr2.EnableDragGridSize( False )
		self.Sgr2.SetMargins( 0, 0 )
		
		# Columns
		self.Sgr2.SetColSize( 0, 50 )
		self.Sgr2.EnableDragColMove( False )
		self.Sgr2.EnableDragColSize( True )
		self.Sgr2.SetColLabelSize( 0 )
		self.Sgr2.SetColLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Rows
		self.Sgr2.EnableDragRowSize( True )
		self.Sgr2.SetRowLabelSize( 0 )
		self.Sgr2.SetRowLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Label Appearance
		
		# Cell Defaults
		self.Sgr2.SetDefaultCellAlignment( wx.ALIGN_CENTRE, wx.ALIGN_TOP )
		FGSz.Add( self.Sgr2, 0, 0, 0 )
		
		self.Sgr1 = wx.grid.Grid( self.pnl3, wx.ID_ANY, wx.DefaultPosition, wx.Size( 210,-1 ), 0 )
		
		# Grid
		self.Sgr1.CreateGrid( self.Frow, 1 )
		self.Sgr1.EnableEditing( True )
		self.Sgr1.EnableGridLines( True )
		self.Sgr1.EnableDragGridSize( False )
		self.Sgr1.SetMargins( 0, 0 )
		
		# Columns
		self.Sgr1.SetColSize( 0, 210 )
		self.Sgr1.EnableDragColMove( False )
		self.Sgr1.EnableDragColSize( True )
		self.Sgr1.SetColLabelSize( 0 )
		self.Sgr1.SetColLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Rows
		self.Sgr1.EnableDragRowSize( True )
		self.Sgr1.SetRowLabelSize( 0 )
		self.Sgr1.SetRowLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Label Appearance
		
		# Cell Defaults
		self.Sgr1.SetDefaultCellAlignment( wx.ALIGN_CENTRE, wx.ALIGN_TOP )
		self.m_menu1 = wx.Menu()
		self.Item1 = wx.MenuItem( self.m_menu1, wx.ID_ANY, u"انتخاب کالا", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu1.AppendItem( self.Item1 )
		
		#self.Item2 = wx.MenuItem( self.m_menu1, wx.ID_ANY, u"انتهای فاکتور", wx.EmptyString, wx.ITEM_NORMAL )
		#self.m_menu1.AppendItem( self.Item2 )
		
		self.m_menu1.AppendSeparator()
		
		self.Item3 = wx.MenuItem( self.m_menu1, wx.ID_ANY, u"کالای جدید", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu1.AppendItem( self.Item3 )
		
		#self.Item4 = wx.MenuItem( self.m_menu1, wx.ID_ANY, u"اضافات و کسورات", wx.EmptyString, wx.ITEM_NORMAL )
		#self.m_menu1.AppendItem( self.Item4 )
		
		self.Item5 = wx.MenuItem( self.m_menu1, wx.ID_ANY, u"ردیف جدید", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu1.AppendItem( self.Item5 )

		self.Sgr1.SetLayoutDirection(2)
		
		self.Sgr1.Bind( wx.EVT_RIGHT_DOWN, self.Sgr1OnContextMenu ) 
		
		FGSz.Add( self.Sgr1, 0, 0, 1 )
		
		self.rdf = wx.grid.Grid( self.pnl3, wx.ID_ANY, wx.DefaultPosition, wx.Size( 19,-1 ), 0 )
		
		# Grid
		self.rdf.CreateGrid( self.Frow, 1 )
		self.rdf.EnableEditing( True )
		self.rdf.EnableGridLines( True )
		self.rdf.EnableDragGridSize( False )
		self.rdf.SetMargins( 0, 0 )
		
		# Columns
		self.rdf.SetColSize( 0, 19 )
		self.rdf.EnableDragColMove( False )
		self.rdf.EnableDragColSize( True )
		self.rdf.SetColLabelSize( 0 )
		self.rdf.SetColLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Rows
		self.rdf.EnableDragRowSize( True )
		self.rdf.SetRowLabelSize( 0 )
		self.rdf.SetRowLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Label Appearance
		
		# Cell Defaults
		self.rdf.SetDefaultCellAlignment( wx.ALIGN_RIGHT, wx.ALIGN_TOP )
		FGSz.Add( self.rdf, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		Vsz31.Add( FGSz, 0, wx.EXPAND, 1 )
		
		HSz5 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.fld5 = wx.TextCtrl( self.pnl3, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 92,-1 ), wx.TE_RIGHT )
		HSz5.Add( self.fld5, 0, 0, 0 )
		
		self.fld4 = wx.TextCtrl( self.pnl3, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 309,-1 ), wx.TE_RIGHT )
		HSz5.Add( self.fld4, 0, 0, 0 )
		
		self.lbl4 = wx.StaticText( self.pnl3, wx.ID_ANY, u"جمع بحروف", wx.DefaultPosition, wx.Size( 60,-1 ), 0 )
		self.lbl4.Wrap( -1 )
		HSz5.Add( self.lbl4, 0, wx.EXPAND, 0 )
		
		
		Vsz31.Add( HSz5, 1, wx.EXPAND, 5 )
		
		
		self.pnl3.SetSizer( Vsz31 )
		self.pnl3.Layout()
		Vsz31.Fit( self.pnl3 )
		Vsz3.Add( self.pnl3, 1, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		VSz1.Add( Vsz3, 1, wx.EXPAND, 5 )
		
		Vsz4 = wx.BoxSizer( wx.VERTICAL )
		
		self.pnl4 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.RAISED_BORDER|wx.TAB_TRAVERSAL )
		HSz6 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.btn6 = wx.Button( self.pnl4, wx.ID_ANY, u"دریافت", wx.DefaultPosition, wx.DefaultSize, 0 )
		HSz6.Add( self.btn6, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.btn5 = wx.Button( self.pnl4, wx.ID_ANY, u"انصراف", wx.DefaultPosition, wx.DefaultSize, 0 )
		HSz6.Add( self.btn5, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.btn4 = wx.Button( self.pnl4, wx.ID_ANY, u"چاپ", wx.DefaultPosition, wx.DefaultSize, 0 )
		HSz6.Add( self.btn4, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		
		HSz6.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.cBox3 = wx.CheckBox( self.pnl4, wx.ID_ANY, u"پیش نمایش...", wx.DefaultPosition, wx.DefaultSize, 0 )
		HSz6.Add( self.cBox3, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.cBox2 = wx.CheckBox( self.pnl4, wx.ID_ANY, u"ثبت در سند", wx.DefaultPosition, wx.DefaultSize, 0 )
		HSz6.Add( self.cBox2, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		
		self.pnl4.SetSizer( HSz6 )
		self.pnl4.Layout()
		HSz6.Fit( self.pnl4 )
		Vsz4.Add( self.pnl4, 0, wx.EXPAND |wx.ALL, 5 )
		
		
		VSz1.Add( Vsz4, 0, wx.EXPAND, 5 )
		
		
		self.SetSizer( VSz1 )
		self.Layout()

		# Initial Panel And Prameter
		self.Pcal1 = wx.PopupTransientWindow(self.GetTopLevelParent(),wx.SIMPLE_BORDER)
                self.pnl = calfar01.MyPanel2(self.Pcal1,-1,-1)

                self.pnl.Bind(wx.EVT_BUTTON,self.Onbind,source=None)

		self.row = 0
		self.Totamnt = 0
		self.total = 0
		self.txtcur = u'ريال'
		self.isnd = 0
		
		# Connect Events
		self.nbtn.Bind( wx.EVT_BUTTON, self.nxt )
		self.bbtn.Bind( wx.EVT_BUTTON, self.bak )
		self.fld1.Bind( wx.EVT_TEXT, self.fknum )
		self.dbtn.Bind( wx.EVT_BUTTON, self.dat )
		self.idate.Bind( wx.EVT_TEXT, self.chgdate )
		self.btn1.Bind( wx.EVT_BUTTON, self.chrcst )
		self.fld3.Bind( wx.EVT_TEXT, self.custmr )
		self.cbox.Bind( wx.EVT_COMBOBOX, self.chscury )
		self.Sgr3.Bind( wx.EVT_KEY_DOWN, self.Dothis )
		self.Sgr2.Bind( wx.EVT_KEY_DOWN, self.Dothis )
		self.Sgr1.Bind( wx.grid.EVT_GRID_CELL_RIGHT_CLICK, self.kala )
		self.Bind( wx.EVT_MENU, self.choskala, id = self.Item1.GetId() )
		#self.Bind( wx.EVT_MENU, self.fotfkt, id = self.Item2.GetId() )
		self.Bind( wx.EVT_MENU, self.newkala, id = self.Item3.GetId() )
		#self.Bind( wx.EVT_MENU, self.addrmv, id = self.Item4.GetId() )
		self.Bind( wx.EVT_MENU, self.newrdf, id = self.Item5.GetId() )
		self.fld5.Bind( wx.EVT_TEXT, self.totl )
		self.btn6.Bind( wx.EVT_BUTTON, self.reciv )
		self.btn5.Bind( wx.EVT_BUTTON, self.cancl )
		self.btn4.Bind( wx.EVT_BUTTON, self.prnt )
		self.cBox3.Bind( wx.EVT_CHECKBOX, self.prvew )
		self.cBox2.Bind( wx.EVT_CHECKBOX, self.insnd )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def nxt( self, event ):
		self.fnum = int(self.fld1.GetValue())
		if self.fnum < 999:
                        self.Fnum = unicode(self.fnum + 1)
                self.fld1.SetValue( self.inum.n2f(self.Fnum))       
	
	def bak( self, event ):
		self.fnum = int(self.fld1.GetValue())
		if self.fnum > 1:
                        self.Fnum = unicode(self.fnum - 1)
                self.fld1.SetValue( self.inum.n2f(self.Fnum))
	
	def fknum( self, event ):
                n = int(event.GetEventObject().GetValue())
		Thisfktr = self.iFakt.ShowFkt(unicode(n))
		#print Thisfktr
		i = 0
		self.row = 0
		if len(Thisfktr) != 0:
                        self.ClearFkt()
                        self.idate.SetValue(Thisfktr[0][1])
                        self.fld3.SetValue(Thisfktr[0][2])
                        self.fld5.SetValue(self.inum.Digigrop(Thisfktr[0][3],','))
                        Thistuff = self.iFakt.ShwDfak(unicode(n))
                        if len(Thistuff) > self.Frow:
                                self.Addrow(len(Thistuff) - self.Frow)
                                self.Frow = len(Thistuff)
                        for lin in Thistuff:
                                #print lin
                                self.MakeBdy(self.row,lin)
                                self.row = self.row + 1
                        self.NewFkt = False
		else:
                        self.ClearFkt()
                        self.NewFkt = True

		self.Refresh()
                self.Layout()
	              
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
                
	def chgdate( self, event ):
		event.Skip()
	
	def chrcst( self, event ):
		self.lstmoin = self.iFakt.ShwAcc()
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
			
	def custmr( self, event ):
		event.Skip()
	
	def chscury( self, event ):
		cur =  event.GetEventObject().GetSelection()
		self.txtcur =  event.GetEventObject().GetStringSelection()[2:]
		numdata = []
		for i in range(self.Frow):
                        if self.rdf.GetCellValue(i,0) != '':
                                num  = self.getamnt(i)
                                if cur == 1:
                                        numdata.append(self.inum.Ril2Tmn(num))
                                        
                                if cur == 0:
                                        numdata.append(self.inum.Tmn2Ril(num))
                                        
                self.SetAllAmnt(numdata)
                self.setotal()
                self.fld5.SetValue(self.inum.Digigrop(self.total,','))
                self.Refresh()
                self.Layout()
        def ClearFkt( self ):
                self.idate.SetValue(NOW)
                self.fld3.SetValue('')
                self.cbox.SetSelection( 0 )
                self.rdf.ClearGrid()
                self.Sgr1.ClearGrid()
                self.Sgr2.ClearGrid()
                self.Sgr3.ClearGrid()
                self.CLSAllAmnt()
                
                self.fld5.SetValue('')
                self.Refresh()
                self.Layout()
                
        def CLSAllAmnt( self ):
                for i in range(self.Frow):
                        self.amntfill(i,0,'')
        def SetAllAmnt( self, numdata ):
                #print numdata
                #self.CLSAllAmnt()
                j = 0
                for i in range(self.Frow):
                        if self.rdf.GetCellValue(i,0) != '':
                                #print self.rdf.GetCellValue(i,0)
                                #self.Sgr3.SetCellValue(i,0,self.inum.n2f(numdata[i]))
                                self.amntfill(i,0,'')
                                self.amntfill(i,0,self.inum.n2f(numdata[j]))
                                j = j + 1
                               
                self.Refresh()
                self.Layout()                           
   
	
	def Dothis( self, event ):
		print event.GetEventObject()
                #event.Skip()
	
	def kala( self, event ):
                self.row= event.GetRow()
		self.Sgr1OnContextMenu(event)
	
	def choskala( self, event ):
		iwin = wx.Dialog(self,-1)
		pnl = MyPanel4(iwin)
		iwin.SetSize((460,220))
		iwin.ShowModal()

		idata = pnl.data
		icur = pnl.cur
		self.SetStuff(idata,icur)
			
		iwin.Destroy()
	def SetStuff( self , data , curncy):
                #print data
                if curncy == 1:
                        data[4] = self.inum.n2f( self.inum.Tmn2Ril(int(data[4])))
                        data[5] = self.inum.n2f( self.inum.Tmn2Ril(int(data[5])))
                        
                r = self.row
                self.rdf.SetCellValue(r,0,self.inum.e2f(r+1))
                self.Sgr1.SetCellValue(r,0,data[0]+data[2])
                self.Sgr2.SetCellValue(r,0,self.inum.n2f(data[3]))
                self.Sgr3.SetCellValue(r,0,self.inum.n2f(data[4]))
                self.amntfill(self.row,0,self.inum.f2e(data[5]))
                #self.row = self.row + 1
                self.setotal()
                self.fld5.SetValue(self.inum.Digigrop(self.total,','))
                self.Refresh()
                self.Layout()
                
        def MakeBdy(self,r,data):
                stfnam = self.gnrname (self.iFakt.gStfnm(data[1])[0][0])
                
                self.rdf.SetCellValue(r,0,self.inum.e2f(r+1))
                self.Sgr1.SetCellValue(r,0,stfnam+data[1])
                self.Sgr2.SetCellValue(r,0,self.inum.n2f(data[2]))
                self.Sgr3.SetCellValue(r,0,self.inum.n2f(data[3]))
                self.amntfill(self.row,0,data[4])

                self.Refresh()
                self.Layout()
        def gnrname( self , codnam ):
                name = ''
                nams = codnam.split('-')
                nams.remove('')
                #print nams
                for nam in nams:
                        n = self.iFakt.gNmcod(nam)
                        #print n
                        name = name + n[0][0] + '-'
                return name                

        def setotal( self ):
                itotal = 0
                for i in range(self.Frow):
                        if self.rdf.GetCellValue(i,0) != '':
                                itotal = itotal + self.getamnt(i)
                self.total = itotal                
        def amntfill(self,r,c,number):
                j = 1
                if number == '':
                        nm = [u'',u'',u'',u'']
                else:
                        num = self.inum.Digigrop(int(number),',')
                        nm = num.split(',')
                for i in range(3,3-len(nm),-1):
                        self.Amnt[i].SetCellValue(r,c,nm[j*(-1)])
                        j = j + 1
                #for i in range(4):
                #        self.Amnt[i].SetCellValue(r,c,nm[j*(-1)])
                #        j = j + 1        
        def getamnt(self,r):
                no = 0
                t = 0
                for i in range(3,-1,-1):
                        n = self.Amnt[i].GetCellValue(r,0)
                        if n != '':
                                no = no + int(n) * (1000**t)
                                t = t + 1
                        else:
                                no = no + 0
                return no        
	#def fotfkt( self, event ):
	#	event.Skip()
	
	def newkala( self, event ):
		iwin = wx.Dialog(self,-1)
		pnl = MyPanel5(iwin)
		iwin.SetSize((387,308))
		iwin.ShowModal()
		
		iwin.Destroy()
	
	#def addrmv( self, event ):
	#	event.Skip()
	
	def newrdf( self, event ):
		iwin = wx.Dialog(self,-1)
		pnl = MyPanel6(iwin)
		iwin.SetSize((237,134))
		iwin.ShowModal()
		r = pnl.irow
		#print r
		self.Addrow(r)
		self.Frow = self.Frow + r	
		iwin.Destroy()
	def Addrow( self , r ):
                self.rdf.AppendRows(numRows=r)
                self.Sgr1.AppendRows(numRows=r)
                self.Sgr2.AppendRows(numRows=r)
                self.Sgr3.AppendRows(numRows=r)
                for i in range(4):
                        self.Amnt[i].AppendRows(numRows=r)
                self.pnl3.SetupScrolling()
                
	def totl( self, event ):
		ltotal = event.GetEventObject().GetValue()
		#print ltotal,self.total
		#print int(ltotal.replace(',',''))
		if ltotal != '':
                        hroof = self.inum.num2txt(int(ltotal.replace(',','')))+' '+self.txtcur
		        self.fld4.SetValue(hroof)
	
	def reciv( self, event ):
                if self.chkfakt() == 1:
                        data1 = self.getdata()
                        self.jFakt.Infaktr('Fnum , Fdate, Ftype , Facc , Fdes, Amount ',data1)
                        data2 = self.GetStuff()
                        self.jFakt.InFDesc('Fdes , Fstuf , Number , Fee , Famnt',data2)
                        if self.isnd == 1:
                                import Database.insnd2 as IS
                                IS.Input_Document(data1)
                                MessageBox(u'درآخرين سند ثبت شد',u'اعلان',OK | ICON_INFORMATION)
                                
                        MessageBox(u'فاکتور با موفقيت ثبت شد',u'اعلان',OK | ICON_INFORMATION)
                        q = self.GetParent()
                        q.Close()
		
	def getdata(self):
                f1 = int(self.fld1.GetValue())
                f2 = self.idate.GetValue()
                f3 = '6200001'
                f4 = self.icust[0][0]
                self.Fdes = hex(f1)[2:]+'-'+hex(int(f2[-5:-3]+f2[-2:]))[2:]
                f5 = self.Fdes
                f6 = self.total
                return [f1,f2,f3,f4,f5,f6]
                
	def GetStuff(self):
                rdata = []
                for r in range(self.Frow):
                        if self.rdf.GetCellValue(r,0) != '':
                                f2 = self.Sgr1.GetCellValue(r,0)[:4]
                                f3 = int(self.Sgr2.GetCellValue(r,0))
                                f4 = int(self.Sgr3.GetCellValue(r,0))
                                f5 = self.getamnt(r)
                                rdata.append( (self.Fdes,f2,f3,f4,f5) )
                                self.UpStuff(f2,f3)
                return rdata        
        def UpStuff(self,Stuf,Num):
                inum = self.iFakt.gStfno(Stuf)
                thisnum = inum[0][0] - int(Num)
                #print thisnum
                self.jFakt.Stufup(" numbr = ? where Stuffs.Fstuf = '%s'"%Stuf,(thisnum,))
                
	def cancl( self, event ):
		q = self.GetParent()
                q.Close()
	
	def prnt( self, event ):
		P = wx.Frame(self,-1,style=wx.FRAME_FLOAT_ON_PARENT|wx.DEFAULT_FRAME_STYLE)
		D1 = self.getD1()
		D2 = self.getD2()
		D3 = self.getD3()
		D4 = self.getD4()
		prn = Fprint.TestPrintPanel(P,D1,D2,D3,D4)
		P.SetSize((520,700))
		P.Show()
	def getD1( self ):
                pnl1 = (self.pnl1.GetPositionTuple(),self.pnl1.GetSize())
                txt1 = (self.titr1.GetPositionTuple(),self.titr1.GetLabel())
                txt2 = (self.titr2.GetPositionTuple(),self.titr2.GetLabel())
                pnl2 = (self.pnl2.GetPositionTuple(),self.pnl2.GetSize())
                txt3 = (self.lbl1.GetPositionTuple(),self.lbl1.GetLabel())
                txt4 = (self.lbl2.GetPositionTuple(),self.lbl2.GetLabel())
                txt5 = (self.lbl3.GetPositionTuple(),self.lbl3.GetLabel())
                return [txt1,txt2,txt3,txt4,txt5,pnl1,pnl2]
        def getD2( self ):
                cols1 = self.cola
                cols2 = self.colb
                col3 = (self.cbox.GetPositionTuple(),self.cbox.GetStringSelection())
                pnl3 = (self.pnl3.GetPositionTuple(),self.pnl3.GetSize())
                return [cols1,cols2,col3,pnl3]
        def getD3( self ):
                fld1 = (self.fld1.GetPositionTuple(),self.fld1.GetValue())
                fld2 = (self.idate.GetPositionTuple(),self.idate.GetValue())
                fld3 = (self.fld3.GetPositionTuple(),self.fld3.GetValue())
                fld4 = (self.fld4.GetPositionTuple(),self.fld4.GetValue())
                fld5 = (self.fld5.GetPositionTuple(),self.fld5.GetValue())
                return [fld1,fld2,fld3,fld4,fld5]
                
        def getD4( self ):
                rdata = []
                for r in range(self.Frow):
                        if self.rdf.GetCellValue(r,0) != '':
                                grd0 = self.rdf.GetCellValue(r,0)
                                grd1 = self.Sgr1.GetCellValue(r,0)
                                grd2 = self.Sgr2.GetCellValue(r,0)
                                grd3 = self.Sgr3.GetCellValue(r,0)
                                grd4 = self.getamnt(r)
                                rdata.append( (grd0,grd1,grd2,grd3,grd4) )
                                
                return rdata
        def chkfakt( self):
                fno = int(self.fld1.GetValue())
                if self.iFakt.ShowFkt(fno) != []:
                        MessageBox(u'براي اصلاح فاکتور به قسمت اصلاحات برويد',u'خطا',OK | ICON_WARNING)
                        return 0
                if self.idate.GetValue() == '':
                        MessageBox(u'تاريخ را مشخص کنيد',u'خطا',OK | ICON_WARNING)
                        return 0
                if self.fld3.GetValue() == '':
                        MessageBox(u'لطفا يک مشتري براي فاکتور مشخص کنيد',u'خطا',OK | ICON_WARNING)
                        return 0
                if self.fld5.GetValue() == '':
                        MessageBox(u'حداقل يک کالا را ثبت کنيد',u'خطا',OK | ICON_WARNING)
                        return 0
                return 1
	
	def prvew( self, event ):
		event.Skip()
	
	def insnd( self, event ):
		self.isnd = 1
	
	def Sgr1OnContextMenu( self, event ):
		self.Sgr1.PopupMenu( self.m_menu1, event.GetPosition() )
		

###########################################################################
## Class MyPanel3
###########################################################################

class MyPanel3 ( wx.Panel ):
	
	def __init__( self, parent , data ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 387,300 ), style = wx.TAB_TRAVERSAL )

                self.iData = DG.GetData(u'',u'')
		self.newdata = self.changname(data)
		self.nmbr = adad.Adaad(1,u'')
		
		Vsz1 = wx.BoxSizer( wx.VERTICAL )
		
		Hsz1 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.fld1 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_RIGHT)
		Hsz1.Add( self.fld1, 1, wx.ALL, 5 )
		
		self.txt1 = wx.StaticText( self, wx.ID_ANY, u"جستجو کالا", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.txt1.Wrap( -1 )
		Hsz1.Add( self.txt1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		Vsz1.Add( Hsz1, 0, wx.EXPAND, 5 )
		
		Hsz2 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.DVC1 = wx.dataview.DataViewListCtrl( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.dataview.DV_HORIZ_RULES|wx.dataview.DV_ROW_LINES|wx.dataview.DV_VERT_RULES )
		self.Col1 = self.DVC1.AppendTextColumn( u"قیمت فروش", 0 ,width = 90,align=wx.ALIGN_CENTER)
		self.Col2 = self.DVC1.AppendTextColumn( u"نام کالا", 0 ,width = 220,align=wx.ALIGN_CENTER)
		self.Col3 = self.DVC1.AppendTextColumn( u"کد کالا", 0,width = 50,align= wx.ALIGN_CENTER)
		Hsz2.Add( self.DVC1, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		Vsz1.Add( Hsz2, 1, wx.EXPAND, 5 )
		
		Hsz3 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.btn1 = wx.Button( self, wx.ID_ANY, u"انتخاب", wx.DefaultPosition, wx.DefaultSize, 0 )
		Hsz3.Add( self.btn1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		Vsz1.Add( Hsz3, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		for itemvalues in self.newdata:
                    self.DVC1.AppendItem(itemvalues)
                    
		self.SetSizer( Vsz1 )
		self.Layout()
		
		# Connect Events
		self.fld1.Bind( wx.EVT_TEXT, self.srchkala )
		self.Bind( wx.dataview.EVT_DATAVIEW_ITEM_ACTIVATED, self.onslct, id = wx.ID_ANY )
		self.btn1.Bind( wx.EVT_BUTTON, self.onslct )
	
	def __del__( self ):
		pass
	
	def changname(self,data):
                newdata = []
                ND = ''
                #print data
                for D in data:
                        d =  D[1].split('-')
                        d.remove(u'')
                        for N in d:
                                ND = ND + '-' + self.iData.gNmcod(N)[0][0]
                        #print ND
                        newdata.append((D[0],ND,D[2]))
                        ND = ''
                                       
                #print newdata
                return newdata
                                
                        
	# Virtual event handlers, overide them in your derived class
	def srchkala( self, event ):
                stf = event.GetEventObject().GetValue()
                stfs = stf.split('-')
                
                for s in stfs:
                        
                        hcod= self.nmbr.txt2hex2(s)
                        self.DVC1.DeleteAllItems()
                        data = self.iData.ShwStuf(hcod)
                        self.newdata = self.changname(data)
                        
		for itemvalues in self.newdata:
                    self.DVC1.AppendItem(itemvalues)
	
	def onslct( self, event ):
                a= self.DVC1.GetSelectedRow()
                self.retdata()
		q = self.GetParent()
                q.Close()

        def retdata(self):
                a= self.DVC1.GetSelectedRow()
                data = []
                if a == -1:
                        data.append(' ')
                else:
                        data.append((unicode(self.DVC1.GetValue(a,0)),
                                     unicode(self.DVC1.GetValue(a,1)),
                                     unicode(self.DVC1.GetValue(a,2))))
                return data        
	

###########################################################################
## Class MyPanel4
###########################################################################

class MyPanel4 ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 450,200 ), style = wx.TAB_TRAVERSAL )

		self.iFakt = DG.GetData(u'',u'')
		self.jFakt = DG.SetData(u'',u'')
		Vsz1 = wx.BoxSizer( wx.VERTICAL )
		
		Hsz1 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.fld1 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_RIGHT )
		Hsz1.Add( self.fld1, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.txt1 = wx.StaticText( self, wx.ID_ANY, u"بارکد", wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
		self.txt1.Wrap( -1 )
		Hsz1.Add( self.txt1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.fld0 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		Hsz1.Add( self.fld0, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.txt0 = wx.StaticText( self, wx.ID_ANY, u"کد کالا", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.txt0.Wrap( -1 )
		Hsz1.Add( self.txt0, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		
		Vsz1.Add( Hsz1, 1, wx.EXPAND, 5 )
		
		Hsz2 = wx.BoxSizer( wx.HORIZONTAL )

		self.fld22 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 30,-1 ), wx.TE_RIGHT )
		Hsz2.Add( self.fld22, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.txt22 = wx.StaticText( self, wx.ID_ANY, u"تعداد مانده", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.txt22.Wrap( -1 )
		Hsz2.Add( self.txt22, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.btn2 = wx.Button( self, wx.ID_ANY, u"...", wx.DefaultPosition, wx.DefaultSize, wx.BU_EXACTFIT )
		Hsz2.Add( self.btn2, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.fld2 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_RIGHT )
		Hsz2.Add( self.fld2, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.txt2 = wx.StaticText( self, wx.ID_ANY, u"نام کالا", wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
		self.txt2.Wrap( -1 )
		Hsz2.Add( self.txt2, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		Vsz1.Add( Hsz2, 1, wx.EXPAND, 5 )
		
		Hsz3 = wx.BoxSizer( wx.HORIZONTAL )
		
		curcyChoices = [ u"ریال", u"تومان" ]
		self.curcy = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, curcyChoices, 0 )
		self.curcy.SetSelection( 0 )
		Hsz3.Add( self.curcy, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.calcu1 = wx.BitmapButton( self, 1000, wx.Bitmap( UTILITY_PATH+u"calculator.bmp", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		Hsz3.Add( self.calcu1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.fld4 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_RIGHT )
		Hsz3.Add( self.fld4, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.txt4 = wx.StaticText( self, wx.ID_ANY, u"فی", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.txt4.Wrap( -1 )
		Hsz3.Add( self.txt4, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.calcu2 = wx.BitmapButton( self, 1001, wx.Bitmap( UTILITY_PATH+u"calculator.bmp", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		Hsz3.Add( self.calcu2, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.fld3 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 30,-1 ), wx.TE_RIGHT )
		Hsz3.Add( self.fld3, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.txt3 = wx.StaticText( self, wx.ID_ANY, u"تعداد", wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
		self.txt3.Wrap( -1 )
		Hsz3.Add( self.txt3, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		Vsz1.Add( Hsz3, 1, wx.EXPAND, 5 )
		
		bSizer34 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.fld6 = wx.StaticText( self, wx.ID_ANY, u"<مبلغ به حروف>", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_RIGHT )
		self.fld6.Wrap( -1 )
		bSizer34.Add( self.fld6, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.txt6 = wx.StaticText( self, wx.ID_ANY, u"بحروف", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.txt6.Wrap( -1 )
		bSizer34.Add( self.txt6, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.fld5 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_RIGHT )
		bSizer34.Add( self.fld5, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.txt5 = wx.StaticText( self, wx.ID_ANY, u"مبلغ", wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
		self.txt5.Wrap( -1 )
		bSizer34.Add( self.txt5, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		Vsz1.Add( bSizer34, 1, wx.EXPAND, 5 )
		
		Hsz4 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.btn4 = wx.Button( self, wx.ID_ANY, u"انتخاب", wx.DefaultPosition, wx.DefaultSize, 0 )
		Hsz4.Add( self.btn4, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.btn3 = wx.Button( self, wx.ID_ANY, u"انصراف", wx.DefaultPosition, wx.DefaultSize, 0 )
		Hsz4.Add( self.btn3, 0, wx.ALL, 5 )
		
		self.nmbr = adad.Adaad(1,u'')
		
		Vsz1.Add( Hsz4, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.ifee = 0
		self.inum = 0
		self.iamnt = 0
		self.data = []
		self.cur = 0
		
		self.SetSizer( Vsz1 )
		self.Layout()
		
		# Connect Events
		self.fld1.Bind( wx.EVT_TEXT, self.barcodit )
		self.fld0.Bind( wx.EVT_TEXT, self.incod )
		self.btn2.Bind( wx.EVT_BUTTON, self.srchstf )
		self.curcy.Bind( wx.EVT_CHOICE, self.curncy )
		self.calcu1.Bind( wx.EVT_BUTTON, self.calcu )
		self.fld4.Bind( wx.EVT_TEXT, self.feestf )
		self.calcu2.Bind( wx.EVT_BUTTON, self.calcu )
		self.fld3.Bind( wx.EVT_TEXT, self.numstf )
		self.fld5.Bind( wx.EVT_TEXT, self.amntit )
		self.btn4.Bind( wx.EVT_BUTTON, self.onslct )
		self.btn3.Bind( wx.EVT_BUTTON, self.cancl )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def barcodit( self, event ):
                icod = event.GetEventObject().GetValue()
                if len(icod) == 13:
                        idata = self.iFakt.gStbar(icod)
                        self.fld0.SetValue(idata[0][2])
                        self.Setfld(idata)
	
	def incod( self, event ):
		icod = event.GetEventObject().GetValue()
		if len(icod)>=4:
                        idata = self.iFakt.gStuff(icod)
                        self.fld1.SetValue(idata[0][3])
                        self.Setfld(idata)
	
	def srchstf( self, event ):
                idata = self.iFakt.ShwKala()
		iwin = wx.Dialog(self,-1)
		pnl = MyPanel3(iwin,idata)
		iwin.SetSize((387,308))
		iwin.ShowModal()

		iStuff = pnl.retdata()
		#print iStuff[0][2]
		self.fld0.SetValue(iStuff[0][2])

		#ibrcd = self.iFakt.Shwbarc(unicode(iStuff[0][2]))
		#self.fld0.SetValue(iStuff[0][2])
		#self.fld1.SetValue(ibrcd[0][0])
		#self.fld2.SetValue(iStuff[0][1])
		#self.fld3.SetValue(self.nmbr.n2f(u'1'))
		#self.fld4.SetValue(self.nmbr.n2f(iStuff[0][0]))
		#print iStuff

		self.Refresh()
		self.Layout()
		
		iwin.Destroy()
	def Setfld( self , data ):
                
		#self.fld0.SetValue(data[0][2])
		#self.fld1.SetValue(data[0][3])
		name = self.gnrname(data[0][1])
		self.fld2.SetValue(name)
		self.fld3.SetValue(self.nmbr.n2f(u'1'))
		self.fld4.SetValue(self.nmbr.n2f(data[0][0]))
		self.fld22.SetValue(self.nmbr.n2f(data[0][4]))
                
	def gnrname( self , codnam ):
                name = ''
                nams = codnam.split('-')
                nams.remove('')
                #print nams
                for nam in nams:
                        n = self.iFakt.gNmcod(nam)
                        #print n
                        name = name + n[0][0] + '-'
                return name        
                        
	def curncy( self, event ):
		icur =  event.GetEventObject().GetSelection()
		ifee = int(self.fld4.GetValue())
                imablagh = int(self.fld5.GetValue())
		if icur == 1:
                        newfee = self.nmbr.Ril2Tmn(ifee)
                        newmab = self.nmbr.Ril2Tmn(imablagh)
                        self.fld4.SetValue(self.nmbr.n2f(newfee))
                        self.fld5.SetValue(self.nmbr.n2f(newmab))
                        self.fld6.SetLabel(unicode(self.nmbr.num2txt(newmab))+' '+
                                           unicode(self.curcy.GetStringSelection()))
                        self.cur = 1
                
                if icur == 0:
                        newfee = self.nmbr.Tmn2Ril(ifee)
                        newmab = self.nmbr.Tmn2Ril(imablagh)
                        self.fld4.SetValue(self.nmbr.n2f(newfee))
                        self.fld5.SetValue(self.nmbr.n2f(newmab))
                        self.fld6.SetLabel(unicode(self.nmbr.num2txt(newmab))+' '+
                                           unicode(self.curcy.GetStringSelection()))
                        self.cur = 0
                self.Refresh()
                self.Layout()       

	
	def calcu( self, event ):
		iid =  event.GetEventObject().GetId()
		dlg = wx.Dialog(self,-1)
                pnl = ca.MyPanel1(dlg)
                dlg.SetSize((176,252))
                
                dlg.ShowModal()
                adad = self.nmbr.Rondtxtnum(pnl.getValue())
                if iid == 1000:
                    self.fld4.SetValue(self.nmbr.n2f(adad))
                if iid == 1001:
                    self.fld3.SetValue(self.nmbr.n2f(adad))

                self.Refresh()
                self.Layout()

                dlg.Destroy()
	
	def feestf( self, event ):
                self.ifee = int(event.GetEventObject().GetValue())
		self.iamnt = self.ifee*self.inum
		self.fld5.SetValue(self.nmbr.n2f(self.iamnt))
	
	
	def numstf( self, event ):
                self.inum = int(event.GetEventObject().GetValue())
                self.iamnt = self.ifee*self.inum
		self.fld5.SetValue(self.nmbr.n2f(self.iamnt))
	
	def amntit( self, event ):
		self.fld6.SetLabel(self.nmbr.num2txt(self.iamnt))
		self.Refresh()
                self.Layout()
	
	def onslct( self, event ):
                self.data = self.getdata()
		q = self.GetParent()
                q.Close()
        def cancl( self, event ):
                self.data = ['','','','','','']
		q = self.GetParent()
                q.Close()
        def getdata( self ):
                f0 = self.fld0.GetValue()
                f1 = self.fld1.GetValue()
                f2 = self.fld2.GetValue()
                f3 = self.fld3.GetValue()
                f4 = self.fld4.GetValue()
                f5 = self.fld5.GetValue()
                return [f0,f1,f2,f3,f4,f5]        

###########################################################################
## Class MyPanel5
###########################################################################

class MyPanel5 ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 387,308 ), style = wx.TAB_TRAVERSAL )

		self.SetLayoutDirection(2)
		self.iData = DG.GetData(u'',u'')
		self.jData = DG.SetData(u'',u'')
		VS1 = wx.BoxSizer( wx.VERTICAL )
		
		HS2 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.lbl1 = wx.StaticText( self, wx.ID_ANY, u"نام کالا", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lbl1.Wrap( -1 )
		HS2.Add( self.lbl1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.fld1 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		HS2.Add( self.fld1, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		VS1.Add( HS2, 1, wx.EXPAND, 5 )
		
		HS3 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.lbl2 = wx.StaticText( self, wx.ID_ANY, u"کد کالا", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lbl2.Wrap( -1 )
		HS3.Add( self.lbl2, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.fld2 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		HS3.Add( self.fld2, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.btn1 = wx.Button( self, wx.ID_ANY, u"...", wx.DefaultPosition, wx.DefaultSize, wx.BU_EXACTFIT )
		HS3.Add( self.btn1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.btn2 = wx.Button( self, wx.ID_ANY, u"مشاهده کد بندی", wx.DefaultPosition, wx.DefaultSize, 0 )
		HS3.Add( self.btn2, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		VS1.Add( HS3, 1, wx.EXPAND, 5 )
		
		HS4 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.lbl3 = wx.StaticText( self, wx.ID_ANY, u"بارکد", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lbl3.Wrap( -1 )
		HS4.Add( self.lbl3, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.fld3 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		HS4.Add( self.fld3, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.lbl4 = wx.StaticText( self, wx.ID_ANY, u"تصویر", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lbl4.Wrap( -1 )
		HS4.Add( self.lbl4, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.barcode = wx.StaticBitmap( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
		HS4.Add( self.barcode, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		VS1.Add( HS4, 1, wx.EXPAND, 5 )
		
		HS5 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.btn3 = wx.Button( self, wx.ID_ANY, u"مشخصات فنی...", wx.DefaultPosition, wx.Size( 120,-1 ), 0 )
		HS5.Add( self.btn3, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.lbl5 = wx.StaticText( self, wx.ID_ANY, u"تعداد", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_RIGHT )
		self.lbl5.Wrap( -1 )
		HS5.Add( self.lbl5, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.fld4 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		HS5.Add( self.fld4, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_bpButton3 = wx.BitmapButton( self, 11, wx.Bitmap( UTILITY_PATH+u"calculator.bmp", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		HS5.Add( self.m_bpButton3, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		VS1.Add( HS5, 1, wx.EXPAND, 5 )
		
		HS6 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.btn4 = wx.Button( self, wx.ID_ANY, u"مشخصات فروش ...", wx.DefaultPosition, wx.Size( 120,-1 ), 0 )
		HS6.Add( self.btn4, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.lbl6 = wx.StaticText( self, wx.ID_ANY, u"قیمت", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_RIGHT )
		self.lbl6.Wrap( -1 )
		HS6.Add( self.lbl6, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.fld5 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		HS6.Add( self.fld5, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_bpButton4 = wx.BitmapButton( self, 12, wx.Bitmap( UTILITY_PATH+u"calculator.bmp", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		HS6.Add( self.m_bpButton4, 0, wx.ALL, 5 )
		
		
		VS1.Add( HS6, 1, wx.EXPAND, 5 )
		
		HS7 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.listbtn = wx.BitmapButton( self, wx.ID_ANY, wx.ArtProvider.GetBitmap( wx.ART_LIST_VIEW, wx.ART_BUTTON ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		self.listbtn.SetToolTipString( u"راهنمای ورود کالا و کد بندی" )
		
		HS7.Add( self.listbtn, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		HS7.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.btn5 = wx.Button( self, wx.ID_ANY, u"انصراف", wx.DefaultPosition, wx.DefaultSize, 0 )
		HS7.Add( self.btn5, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.btn6 = wx.Button( self, wx.ID_ANY, u"ثبت کالا", wx.DefaultPosition, wx.DefaultSize, 0 )
		HS7.Add( self.btn6, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		VS1.Add( HS7, 1, wx.EXPAND, 5 )
		
		self.nmbr = adad.Adaad(1,u'')
		
		self.SetSizer( VS1 )
		self.Layout()
		
		# Connect Events
		self.fld1.Bind( wx.EVT_TEXT, self.cdstuf )
		self.btn1.Bind( wx.EVT_BUTTON, self.srch )
		self.btn2.Bind( wx.EVT_BUTTON, self.codviw )
		self.fld3.Bind( wx.EVT_TEXT, self.crtbar )
		self.btn3.Bind( wx.EVT_BUTTON, self.prop1 )
		self.m_bpButton3.Bind( wx.EVT_BUTTON, self.calcu )
		self.btn4.Bind( wx.EVT_BUTTON, self.prop2 )
		self.m_bpButton4.Bind( wx.EVT_BUTTON, self.calcu )
		self.listbtn.Bind( wx.EVT_BUTTON, self.listkala )
		self.btn5.Bind( wx.EVT_BUTTON, self.cancl )
		self.btn6.Bind( wx.EVT_BUTTON, self.inkala )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def cdstuf( self , event ):
                txt = self.fld1.GetValue()
                                        
                        
	def srch( self, event ):
                idata = self.iData.ShwKala()
		iwin = wx.Dialog(self,-1)
		pnl = MyPanel3(iwin,idata)
		iwin.SetSize((387,308))
		iwin.ShowModal()
		
		iwin.Destroy()
	
	def codviw( self, event ):
                txt = self.fld1.GetValue()
                
                cods = self.IncodG(txt)
		dlg = wx.Dialog(self,-1)
                pnl = MyPanel7(dlg,cods)
                dlg.SetSize((400,110))
                
                dlg.ShowModal()

                self.Refresh()
                self.Layout()

                dlg.Destroy()
	def IncodG( self , txt ):
                stfs =  txt.split('-')
                self.lname = []
                cods  = ''
                for stf in stfs :
                        self.lname.append((stf ,  self.nmbr.txt2hex2(stf)))
                        cods = cods + '-' + self.nmbr.txt2hex2(stf)
                return cods        
                
	def crtbar( self, event ):
		if len(self.fld3.GetValue()) > 11:
                    bar = B1.EanBarCode()
                    fld = self.fld3.GetValue()
                    bar.getImage(fld,50,"png")
                    #print bar.code
                    self.BrCd = bar.code
                    
                    barcod = wx.Bitmap( UTILITY_PATH+u'barcode' + u".png" )
                    #barcod = wx.Bitmap( unicode(bar.code) + u".png" )
                    #print barcod
                    self.barcode.SetBitmap( barcod  )

                self.Refresh()
                self.Layout()
        def GtSpcCod(self,tit):
                f2 = self.fld2.GetValue()
                hd = hex(int(f2[:2]))[-1:]+hex(int(f2[2:4])+1)[-1:]
                return f2[:2]+hd+'-'+str(tit)+str(f2[-2:])
	
	def prop1( self, event ):
                txt1 = u"نام کالا"
                txt2 = self.fld1.GetValue()
                txts =  [txt1,txt2]
                self.stfcod = self.GtSpcCod('3')
                iwin = wx.Dialog(self,-1)
		#pnl = MyPanel8(iwin,txt,'','311')
		pnl = Specy.MyPanel2(iwin,txts,self.stfcod,'311')
		iwin.SetSize((333,299))
		iwin.ShowModal()
		if pnl.RetRev():
                        #pnl.savtit(idata,self.sData)
                        self.ispec = self.iData.gSpcy(self.stfcod)
                        mdata = pnl.gettit()
                        #print mdata
		        self.savtit(mdata,self.jData)
	
		iwin.Destroy()
	
	def prop2( self, event ):
                txt1 = u"نام کالا"
                txt2 = self.fld1.GetValue()
                txts =  [txt1,txt2]
                self.stfcod = self.GtSpcCod('5')
		iwin = wx.Dialog(self,-1)
		#pnl = MyPanel8(iwin,txt,'','511')
		pnl = Specy.MyPanel2(iwin,txts,self.stfcod,'511')
		iwin.SetSize((333,299))
		iwin.ShowModal()
		if pnl.RetRev():
                        #pnl.savtit(idata,self.sData)
                        self.ispec = self.iData.gSpcy(self.stfcod)
                        mdata = pnl.gettit()
                        #print mdata
		        self.savtit(mdata,self.jData)
		
		iwin.Destroy()
	def savtit(self,data,iSet):
                #print data
                #print self.ispec
                for i in range(len(data)):
                        for j in range(len(self.ispec)):
                                if data[i][1] in self.ispec[j]:
                                        idata = (data[i][2],)
                                        iSet.Specup("Spcfy = ? where Spc = '%s' and tit = '%s' "%(self.stfcod,self.ispec[j][2]),idata)
                                        break
                        else:
                                iSet.Specin('Spc , tit, Spcfy ',data[i])	

	def calcu( self, event ):
                iid =  event.GetEventObject().GetId()
		dlg = wx.Dialog(self,-1)
                pnl = ca.MyPanel1(dlg)
                dlg.SetSize((176,252))
                
                dlg.ShowModal()
                adad = self.nmbr.Rondtxtnum(pnl.getValue())
                if iid == 11:
                    self.fld4.SetValue(unicode(adad))
                if iid == 12:
                    self.fld5.SetValue(unicode(adad))

                self.Refresh()
                self.Layout()

                dlg.Destroy()
	
	def listkala( self, event ):
		event.Skip()
	
	def cancl( self, event ):
		q = self.GetParent()
                q.Close()
	
	def inkala( self, event ):
                idata = self.GetData()
                #print idata[0]
                
                isnwstuf = self.chkcod(idata)
                if isnwstuf :
                        self.jData.Stufin('Fstuf , Fbarcd , Stufname , numbr , price , Spc1 , Spc2',idata[0])
                        print self.lname
                        self.NamIns2(self.lname)
                        #self.jData.Namein2('name , code',self.lname)
                        MessageBox(u'کالاي جديد با موفقيت ثبت شد',u'اعلان',OK | ICON_INFORMATION)
                        
                nxtcod = unicode(int(idata[0][0])+1)
                #self.CLSData()
                self.fld2.SetValue(nxtcod)
                
        def NamIns2(self, data):
                
                for name in data:
                        if self.iData.gCodnm(name[0]) == []:
                                self.jData.Namein1('name , code , rpit',name+(1,))
                        else:
                                rp = self.iData.gRptcd(name[1])
                                print rp[0][0]
                                self.jData.Nameup1("rpit = ? where code = '%s'"%name[1],(rp[0][0]+1,))
                
	def GetData(self):
                f1 = self.fld1.GetValue()
                f2 = self.fld2.GetValue()
                f3 = self.fld3.GetValue()
                f13 = self.BrCd
                f4 = self.fld4.GetValue()
                f5 = self.fld5.GetValue()
                Fc = self.IncodG(f1)
                iSpc1 = self.GtSpcCod('3')
                iSpc2 = self.GtSpcCod('5')                  
                rdata = [f2,f13,Fc,f4,f5,iSpc1,iSpc2],[f1]
                #print rdata
                return rdata
        def chkcod( self , data):
                #print data[0]
                if self.iData.gStuff(data[0][0]) == []:
                        self.newstuf = 1
                else:
                        MessageBox(u'کد کالا تکراري است',u'خطا',OK | ICON_WARNING)
                        self.newstuf = 0
                if self.iData.gStbar(data[0][1]) == []:
                        self.newstuf = 1
                else:
                        MessageBox(u'بارکد تکراري است ',u'خطا',OK | ICON_WARNING)
                        self.newstuf = 0
                return self.newstuf        
                        

                
        def CLSData(self):
                #self.fld1.SetValue('')
                #self.fld2.SetValue('')
                self.fld3.SetValue('')
                self.BrCd = ''
                self.fld4.SetValue('')
                self.fld5.GetValue('')

###########################################################################
## Class MyPanel6
###########################################################################

class MyPanel6 ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 237,134 ), style = wx.TAB_TRAVERSAL )
		
		vsz1 = wx.BoxSizer( wx.VERTICAL )
		
		hsz1 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.txt1 = wx.StaticText( self, wx.ID_ANY, u"ردیف به پائین فاکتور", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.txt1.Wrap( -1 )
		hsz1.Add( self.txt1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.SCtrl1 = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), wx.SP_ARROW_KEYS, 1, 10, 1 )
		hsz1.Add( self.SCtrl1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.txt2 = wx.StaticText( self, wx.ID_ANY, u"تعداد", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.txt2.Wrap( -1 )
		hsz1.Add( self.txt2, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		vsz1.Add( hsz1, 1, wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		hsz2 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.btn1 = wx.Button( self, wx.ID_ANY, u"اضافه شود", wx.DefaultPosition, wx.DefaultSize, 0 )
		hsz2.Add( self.btn1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.btn2 = wx.Button( self, wx.ID_ANY, u"انصراف", wx.DefaultPosition, wx.DefaultSize, 0 )
		hsz2.Add( self.btn2, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		vsz1.Add( hsz2, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.irow = 1
		self.SetSizer( vsz1 )
		self.Layout()
		
		# Connect Events
		self.btn1.Bind( wx.EVT_BUTTON, self.addit )
		self.btn2.Bind( wx.EVT_BUTTON, self.cncel )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def addit( self, event ):
                #print self.redata()
                self.irow = self.redata()
		q = self.GetParent()
                q.Close()
	
	def cncel( self, event ):
                self.irow = 0
                q = self.GetParent()
                q.Close()

        def redata( self ):
                return self.SCtrl1.GetValue()
	
###########################################################################
## Class MyPanel7
###########################################################################

class MyPanel7 ( wx.Panel ):
	
	def __init__( self, parent , cods):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 500,161 ), style = wx.TAB_TRAVERSAL )
		
		Vsz1 = wx.BoxSizer( wx.VERTICAL )
		
		Hsz1 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.fld = wx.TextCtrl( self, wx.ID_ANY, cods, wx.DefaultPosition, wx.DefaultSize, 0 )
		Hsz1.Add( self.fld, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.txt = wx.StaticText( self, wx.ID_ANY, u"کد بندی داخلی نرم افزار ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.txt.Wrap( -1 )
		Hsz1.Add( self.txt, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		Vsz1.Add( Hsz1, 1, wx.EXPAND, 5 )
		
		Hsz2 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.btn = wx.Button( self, wx.ID_ANY, u"برگشت", wx.DefaultPosition, wx.DefaultSize, 0 )
		Hsz2.Add( self.btn, 0, wx.ALL, 5 )
		
		
		Vsz1.Add( Hsz2, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		self.SetSizer( Vsz1 )
		self.Layout()
		
		# Connect Events
		self.btn.Bind( wx.EVT_BUTTON, self.retit )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def retit( self, event ):
		q = self.GetParent()
                q.Close()
	
