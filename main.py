#!/usr/bin/env python
import wx
from controller import *

if __name__ == "__main__":
    app = wx.App(False)
    frame = calc(None)
    frame.Show(True)
    app.MainLoop()