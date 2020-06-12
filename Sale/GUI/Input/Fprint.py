# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import Utility.Adaad2 as adad

###########################################################################
## Class MyPanel1
###########################################################################

class MyPanel1 ( wx.Panel ):
	
	def __init__( self, parent , txts , lbls , flds , grids ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 500,700 ), style = wx.TAB_TRAVERSAL )

		self.inum = adad.Adaad(1,'')
		Main = wx.BoxSizer( wx.VERTICAL )
		self.txts = txts
		self.lbls = lbls
		self.flds = flds
		self.grids = grids

		if 1:
                        self.buffer = wx.EmptyBitmap(500,700)
                        dc = wx.BufferedDC(None,self.buffer)
                        dc.SetBackground(wx.Brush(self.GetBackgroundColour()))
                        dc.Clear()
                        self.DoDrawing(dc)
		
		self.SetSizer( Main )
		self.Layout()
		#self.SetLayoutDirection(2)
		self.Bind(wx.EVT_PAINT, self.OnPaint)
		#dc1 = self.GetDC()
	
	
	def __del__( self ):
		pass

	def OnPaint(self, event):
                ############################### 
		#render = wx.RendererNative.Get()
                if 1:
                        dc = wx.BufferedPaintDC(self,self.buffer,wx.BUFFER_VIRTUAL_AREA)
                        
		#dc = wx.GCDC(wx.PaintDC(self))
		#brush = wx.Brush(wx.BLACK,wx.VERTICAL_HATCH)
		#dc.SetBrush(brush)
		#dc.SetTextForeground(wx.BLACK)
		#dc.SetFont(wx.NORMAL_FONT)
		#############################
		#self.DoDrawing(dc)
		#dc.DrawRoundedRectangle(1, 150, 105, 400,5)
		
	def DoDrawing(self, dc, printing=False):
                brush = wx.Brush(wx.BLACK,wx.TRANSPARENT)
		dc.SetBrush(brush)
		dc.SetTextForeground(wx.BLACK)
		dc.SetFont(wx.NORMAL_FONT)
                 
		self.Header(dc)
		self.Number(123,dc)
		#self.Accont(u'آقاي قيامي',self.e2f(u'1397')+"/"+self.e2f(u'01')+"/"+self.e2f(u'19'),dc)
		#lcol = [u'مبلغ',u'في',u'تعداد',u'شرح کالا',u'رديف']
		self.Collbl(dc)
		self.Minbil(self.grids,dc)
		self.Atotal(1,dc)
		
		self.footer(u'امضاء فروشنده',u'امضاء خريدار',dc)
		
	def Header(self,dc):
                dc.DrawRoundedRectangle(self.txts[5][0][0], self.txts[5][0][1],
                                        self.txts[5][1][0], self.txts[5][1][1],5)
                
                dc.DrawText(self.txts[0][1],self.txts[0][0][0],self.txts[0][0][1])
                dc.SetFont(wx.Font( 19, 70, 90, 90, False, wx.EmptyString ))
                #print self.txts[1][1],'-',self.txts[1][0]
                dc.DrawText(self.txts[1][1],self.txts[1][0][0],self.txts[1][0][1])
                #dc.DrawLine(1,50,480,50)
                dc.SetFont(wx.NORMAL_FONT)
                dc.DrawRoundedRectangle(self.txts[6][0][0], self.txts[6][0][1],
                                        self.txts[6][1][0], self.txts[6][1][1],5)
               
                w = self.txts[5][1][1]+32
                dc.DrawText(self.txts[2][1],self.txts[2][0][0],self.txts[2][0][1]+w)
                dc.DrawText(self.txts[3][1],self.txts[3][0][0],self.txts[3][0][1]+w)
                dc.DrawText(self.txts[4][1],self.txts[4][0][0],self.txts[4][0][1]+w)
                
        def Number(self,num,dc):
                w = self.txts[5][1][1]+32
                dc.SetFont(wx.NORMAL_FONT)
                dc.DrawText(self.flds[0][1],self.flds[0][0][0]+20,self.flds[0][0][1]+w+5)
                dc.DrawText(self.flds[1][1],self.flds[1][0][0]+20,self.flds[1][0][1]+w+5)
                dc.DrawText(self.flds[2][1],self.flds[2][0][0]+160,self.flds[2][0][1]+w+5)
                
                #dc.DrawText(self.flds[3][1],self.flds[3][0][0],self.flds[3][0][1]+w+30)
                #dc.DrawText(self.flds[4][1],self.flds[4][0][0],self.flds[4][0][1]+w+30)

                dc.DrawText(self.flds[3][1],self.flds[3][0][0]+100,615)
                #dc.DrawText(self.flds[4][1],self.flds[4][0][0],615)
                
                dc.DrawText(u'جمع بحروف',410,615)

           
        def Minbil(self,grids,dc):
                i = 0
                for g in grids:
                        dc.DrawText(unicode(g[0]),479,220+i*20)
                        lstf = len(g[1])
                        
                        dc.DrawText(g[1],420-(lstf*4) ,220+i*20)
                        #dc.DrawText(g[1],255,220+i*20)
                        dc.DrawText(g[2],200,220+i*20)
                        dc.DrawText(g[3],120,220+i*20)
                        dc.SetFont(wx.Font( 11, 70, 90, 90, False, wx.EmptyString ))
                        lamt = len(unicode(g[4]))
                        dc.DrawText(self.e2f(unicode(g[4])),90-((lamt-1)*8),220+i*20)

                        i = i + 1
                        dc.SetFont(wx.NORMAL_FONT)
                        dc.DrawLine(5,215+i*20,490,215+i*20)

                ltot = len(unicode( self.flds[4][1]))
                dc.SetFont(wx.Font( 10, 70, 90, 90, False, wx.EmptyString ))
                dc.DrawText(self.flds[4][1],100-((ltot-1)*8),615)

                dc.DrawLine(5,215+i*20+10,150,215+i*20+10)
                dc.DrawLine(150,215+i*20+10,490,605)
        
        
        def Collbl(self,dc):
                #print self.lbls
                col1 = self.lbls[0]
                col2 = self.lbls[1]
                #co = [36,128,229,410,565,613]
                i = 0
                t = 0
                s = 0
                brush = wx.Brush(wx.WHITE,wx.TRANSPARENT)
                dc.SetBrush(brush)
                #dc.DrawRoundedRectangle(0, 80, 630, 260,5)

                for c in col1:
                        #co = co + ((c[1]//2)-10)
                        t = ((c[1]//2)-9)+s
                        if i == 4:
                                break
                        #        s = s + 20
                        dc.DrawText(c[0],t,85+105)
                        if i == 3:
                                s = s + 30
                        
                        s = s + col1[i][1]
                        #print t ,'---', co[i]
                        #print co,'---',c[1]
                        i = i + 1
                dc.DrawRotatedText(u"رديف",t,110+105,90)        
                cols = [92,90,50,235,19]
                self.rndrec(5,80+105,cols,30,dc)

                self.colnum(5,215,92,391,dc)
                self.rndrec(5,215,cols,391,dc)
        
        
        def Atotal(self,num,dc):
                dc.DrawRoundedRectangle(5,605,92,30,5)
                dc.DrawRoundedRectangle(97,605,395,30,5)
                        
        def footer(self,txt1,txt2,dc):
                dc.DrawText(txt1,100,650)
                dc.DrawText(txt2,300,650)
                
        def colnum(self,x,y,w,h,dc):
                brush = wx.Brush(wx.WHITE,wx.TRANSPARENT)
                dc.SetBrush(brush)
                dc.SetPen(wx.Pen("BLACK",2))
                #lines = [(x+24,y,x+24,y+h),(x+48,y,x+48,y+h),(x+72,y,x+72,y+h),(x+96,y,x+96,y+h)]
                lines = [(x+23,y,x+23,y+h),(x+46,y,x+46,y+h),(x+69,y,x+69,y+h)]
                dc.DrawLineList(lines)

                dc.SetPen(wx.Pen("BLACK",0.5))
                for i in range(4):
                        l = i*23
                        lines = [(x+7+l,y,x+7+l,y+h),(x+14+l,y,x+14+l,y+h)]
                        dc.DrawLineList(lines)
        

        def rndrec(self,x,y,cols,h,dc):
                brush = wx.Brush(wx.WHITE,wx.TRANSPARENT)
                dc.SetBrush(brush)
                dc.SetPen(wx.Pen("BLACK",1.5))
                c = 0
                for i in range(len(cols)):
                        
                        dc.DrawRoundedRectangle(x+c,y,cols[i],h,5)
                        c = c + cols[i]

        def e2f(self,number):
                s = ''
                adadha = {u'0':1632 , u'1':1633 ,u'2':1634 , u'3':1635 , u'4':1636 ,u'5':1637 ,u'6':1638 ,u'7':1639 ,u'8':1640 ,u'9':1641 }

                for c in number:
                        #print c
                        s = s + unichr(adadha[c])
                
                return s
        


            
class MyPrintout(wx.Printout):
    def __init__(self, canvas):
        wx.Printout.__init__(self)
        self.canvas = canvas
        #self.log = log

    def OnBeginDocument(self, start, end):
        #self.log.WriteText("MyPrintout.OnBeginDocument\n")
        return super(MyPrintout, self).OnBeginDocument(start, end)

    def OnEndDocument(self):
        #self.log.WriteText("MyPrintout.OnEndDocument\n")
        super(MyPrintout, self).OnEndDocument()

    def OnBeginPrinting(self):
        #self.log.WriteText("MyPrintout.OnBeginPrinting\n")
        super(MyPrintout, self).OnBeginPrinting()

    def OnEndPrinting(self):
        #self.log.WriteText("MyPrintout.OnEndPrinting\n")
        super(MyPrintout, self).OnEndPrinting()

    def OnPreparePrinting(self):
        #self.log.WriteText("MyPrintout.OnPreparePrinting\n")
        super(MyPrintout, self).OnPreparePrinting()

    def HasPage(self, page):
        #self.log.WriteText("MyPrintout.HasPage: %d\n" % page)
        if page <= 2:
            return True
        else:
            return False

    def GetPageInfo(self):
        #self.log.WriteText("MyPrintout.GetPageInfo\n")
        return (1, 2, 1, 2)

    def OnPrintPage(self, page):
        #self.log.WriteText("MyPrintout.OnPrintPage: %d\n" % page)
        dc = self.GetDC()

        #-------------------------------------------
        # One possible method of setting scaling factors...

        maxX = 500 #self.canvas.getWidth()
        maxY = 700 #self.canvas.getHeight()

        # Let's have at least 50 device units margin
        marginX = 50
        marginY = 50

        # Add the margin to the graphic size
        maxX = maxX + (2 * marginX)
        maxY = maxY + (2 * marginY)

        # Get the size of the DC in pixels
        (w, h) = dc.GetSizeTuple()

        # Calculate a suitable scaling factor
        scaleX = float(w) / maxX
        scaleY = float(h) / maxY

        # Use x or y scaling factor, whichever fits on the DC
        actualScale = min(scaleX, scaleY)

        # Calculate the position on the DC for centering the graphic
        #posX = (w - (self.canvas.getWidth() * actualScale)) / 2.0
        #posY = (h - (self.canvas.getHeight() * actualScale)) / 2.0
        #####
        posX = (w - (500 * actualScale)) / 2.0
        posY = (h - (700 * actualScale)) / 2.0

        # Set the scale and origin
        dc.SetUserScale(actualScale, actualScale)
        dc.SetDeviceOrigin(int(posX), int(posY))

        #-------------------------------------------

        self.canvas.DoDrawing(dc, True)
        dc.DrawText("Page: %d" % page, marginX/2, maxY-marginY)

        return True


#----------------------------------------------------------------------

	

class TestPrintPanel(wx.Panel):
    def __init__(self, parent , pos1, pos2 , pos3 , pos4):
        wx.Panel.__init__(self, parent, -1)
        #self.log = log
        self.frame = wx.Frame(self,-1,style=wx.FRAME_FLOAT_ON_PARENT|wx.DEFAULT_FRAME_STYLE)

        self.pos1 = pos1
        self.pos2 = pos2
        self.pos3 = pos3
        self.pos4 = pos4

        self.printData = wx.PrintData()
        self.printData.SetPaperId(wx.PAPER_LETTER)
        self.printData.SetPrintMode(wx.PRINT_MODE_PRINTER)

        self.txt = self.pos1
        self.lbl = self.pos2
        self.fld = self.pos3
        self.grd = self.pos4
        
        self.box = wx.BoxSizer(wx.VERTICAL)
        self.canvas = MyPanel1(self,self.txt,self.lbl,self.fld,self.grd)
        self.SetLayoutDirection(2)
        self.box.Add(self.canvas, 1, wx.GROW)

        subbox = wx.BoxSizer(wx.HORIZONTAL)
        btn = wx.Button(self, -1, u"مشخصات صفحه")
        self.Bind(wx.EVT_BUTTON, self.OnPageSetup, btn)
        subbox.Add(btn, 1, wx.GROW | wx.ALL, 2)

        btn = wx.Button(self, -1, u"پيش نمايش")
        self.Bind(wx.EVT_BUTTON, self.OnPrintPreview, btn)
        subbox.Add(btn, 1, wx.GROW | wx.ALL, 2)

        btn = wx.Button(self, -1, u"چاپ")
        self.Bind(wx.EVT_BUTTON, self.OnDoPrint, btn)
        subbox.Add(btn, 1, wx.GROW | wx.ALL, 2)

        self.box.Add(subbox, 0, wx.GROW)

        self.SetAutoLayout(True)
        self.SetSizer(self.box)



    def OnPageSetup(self, evt):
        psdd = wx.PageSetupDialogData(self.printData)
        psdd.EnablePrinter(True)
        psdd.CalculatePaperSizeFromId()
        dlg = wx.PageSetupDialog(self, psdd)
        dlg.ShowModal()

        # this makes a copy of the wx.PrintData instead of just saving
        # a reference to the one inside the PrintDialogData that will
        # be destroyed when the dialog is destroyed
        self.printData = wx.PrintData( dlg.GetPageSetupData().GetPrintData() )

        dlg.Destroy()

    def OnPrintPreview(self, event):
        data = wx.PrintDialogData(self.printData)
        printout = MyPrintout(self.canvas )
        printout2 = None #MyPrintout(self.canvas)
        self.preview = wx.PrintPreview(printout, printout2, data)

        if not self.preview.Ok():
            self.log.WriteText("Houston, we have a problem...\n")
            return
        #frame = wx.PreviewFrame(self.preview, self, "Print Preview",
        #                            pos=self.GetPosition(),
        #                            size=self.GetSize())
        #frame.Initialize()
        #frame.Show()


        pfrm = wx.PreviewFrame(self.preview, self.frame, u"اين پيش نمايش چاپ است ")

        pfrm.Initialize()
        pfrm.SetPosition(self.frame.GetPosition())
        #pfrm.SetSize(self.frame.GetSize())
        pfrm.SetSize((300,500))
        pfrm.Show(True)



    def OnDoPrint(self, event):
        pdd = wx.PrintDialogData(self.printData)
        pdd.SetToPage(2)
        printer = wx.Printer(pdd)
        printout = MyPrintout(self.canvas)

        if not printer.Print(self.frame, printout, True):
            wx.MessageBox(u"مشکل در چاپ شدن وجود دارد\nممکن است چاپگر فعلي درست تنظيم نشده؟", u"چاپ شدن", wx.OK)
        else:
            self.printData = wx.PrintData( printer.GetPrintDialogData().GetPrintData() )
        printout.Destroy()
