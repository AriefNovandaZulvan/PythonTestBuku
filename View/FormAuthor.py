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
## Class MyFrame1
###########################################################################

class FormAuthor(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=wx.EmptyString, pos=wx.DefaultPosition,
                          size=wx.Size(530, 250), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        gSizer1 = wx.GridSizer(0, 2, 0, 0)

        fgSizer1 = wx.FlexGridSizer(0, 2, 0, 0)
        fgSizer1.SetFlexibleDirection(wx.BOTH)
        fgSizer1.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        bSizer1 = wx.BoxSizer(wx.VERTICAL)

        bSizer5 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText5 = wx.StaticText(self, wx.ID_ANY, u"Author ID", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText5.Wrap(-1)
        self.m_staticText5.SetMinSize(wx.Size(100, -1))

        bSizer5.Add(self.m_staticText5, 0, wx.ALL, 5)

        self.txtAuthorID = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer5.Add(self.txtAuthorID, 0, wx.ALL, 5)

        bSizer1.Add(bSizer5, 1, wx.EXPAND, 5)

        bSizer51 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText51 = wx.StaticText(self, wx.ID_ANY, u"Nama Author", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText51.Wrap(-1)
        self.m_staticText51.SetMinSize(wx.Size(100, -1))

        bSizer51.Add(self.m_staticText51, 0, wx.ALL, 5)

        self.txtNamaAuthor = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer51.Add(self.txtNamaAuthor, 0, wx.ALL, 5)

        bSizer1.Add(bSizer51, 1, wx.EXPAND, 5)

        bSizer52 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText52 = wx.StaticText(self, wx.ID_ANY, u"Tanggal Lahir", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText52.Wrap(-1)
        self.m_staticText52.SetMinSize(wx.Size(100, -1))

        bSizer52.Add(self.m_staticText52, 0, wx.ALL, 5)

        self.txtTanggallahir = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer52.Add(self.txtTanggallahir, 0, wx.ALL, 5)

        bSizer1.Add(bSizer52, 1, wx.EXPAND, 5)

        bSizer1.AddSpacer(0)

        bSizer13 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_button1 = wx.Button(self, wx.ID_ANY, u"Add", wx.DefaultPosition, wx.Size(50, -1), 0)
        bSizer13.Add(self.m_button1, 0, wx.ALL, 5)

        self.m_button11 = wx.Button(self, wx.ID_ANY, u"Edit", wx.DefaultPosition, wx.Size(50, -1), 0)
        bSizer13.Add(self.m_button11, 0, wx.ALL, 5)

        self.m_button12 = wx.Button(self, wx.ID_ANY, u"Delete", wx.DefaultPosition, wx.Size(50, -1), 0)
        bSizer13.Add(self.m_button12, 0, wx.ALL, 5)

        self.m_button13 = wx.Button(self, wx.ID_ANY, u"Exit", wx.DefaultPosition, wx.Size(50, -1), 0)
        bSizer13.Add(self.m_button13, 0, wx.ALL, 5)

        bSizer1.Add(bSizer13, 1, wx.EXPAND, 5)

        fgSizer1.Add(bSizer1, 1, wx.EXPAND, 5)

        gSizer1.Add(fgSizer1, 1, wx.EXPAND, 5)

        fgSizer2 = wx.FlexGridSizer(0, 2, 0, 0)
        fgSizer2.SetFlexibleDirection(wx.BOTH)
        fgSizer2.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.m_dataViewListCtrl1 = wx.dataview.DataViewListCtrl(self, wx.ID_ANY, wx.DefaultPosition, wx.Size(240, 200),
                                                                0)
        fgSizer2.Add(self.m_dataViewListCtrl1, 0, wx.ALL, 5)

        gSizer1.Add(fgSizer2, 1, wx.EXPAND, 5)

        self.SetSizer(gSizer1)
        self.Layout()

        self.Centre(wx.BOTH)

        self.Show(True)

    def __del__(self):
        pass



