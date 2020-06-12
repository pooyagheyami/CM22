#In the name of God
# -*- coding: cp1256 -*-
# -*- coding: utf-8 -*-
#!usr/bin/env python

import wx
import SndRsv2


class telframe(wx.Frame):
    def __init__(self,parent):
        wx.Frame.__init__(self,parent,style=wx.CAPTION|wx.CLOSE_BOX|wx.FRAME_FLOAT_ON_PARENT|wx.SYSTEM_MENU)
        self.parent=parent
                
        panel = SndRsv2.MyPanel1(self)

        
    def closeit(self):
        self.Close(True)

def size():
    return (140,250)

def main(panel=None ):
    locale = wx.Locale(wx.LANGUAGE_ENGLISH)
    
    parent =  panel.GetParent()
    
    frame = telframe(parent )
    frame.SetTitle(u'ورود اطلاعات')
    frame.SetSize(size())
    frame.Show()
    
