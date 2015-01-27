#!/bin/env python2

import wx 
import wx.html2 

class MyBrowser(wx.Frame): 
  def __init__(self, *args, **kwds): 
    wx.Frame.__init__(self, None, -1, size=(1920, 1080), style=wx.DEFAULT_FRAME_STYLE | wx.NO_BORDER ^ wx.SYSTEM_MENU)
    self.browser = wx.html2.WebView.New(self) 
    self.ShowFullScreen(True) 

if __name__ == '__main__': 
  app = wx.App() 
  dialog = MyBrowser(None, -1) 
  dialog.browser.LoadURL("http://yisonPylkita.com") 
  dialog.Show() 
  app.MainLoop() 

