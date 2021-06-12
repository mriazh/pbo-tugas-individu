import wx
import gui
import math

save = []

class calc(gui.MainFrame):
    def __init__(self,parent):
        gui.MainFrame.__init__(self, parent)
    
    def equalsNow(self,parent):
        try:
            result = eval(self.textControl.GetValue())
            self.textControl.SetValue(str(result))
            save.clear()
        except Exception:
            print("Error")
    
    def clearNow(self, event):
        self.textControl.SetValue(str(''))
        save.clear()

    def addText(self, event):
        Button = event.GetEventObject().GetLabel()
        save.append(Button)
        self.saveNow()

    def saveNow(self):
        saved = ''.join([str(element) for element in save])
        self.textControl.SetValue(str(saved))