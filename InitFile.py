import wx
from Controller import ControllerAuthor

if __name__ == '__main__':
    app = wx.App()
    vAuthor = ControllerAuthor.controllerAuthor(None)
    vAuthor.Show()
    app.MainLoop()
