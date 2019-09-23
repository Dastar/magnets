import wx


APP_EXIT = 1


class Example(wx.Frame):
    def __init__(self, *args, **kwargs):
        super(Example, self).__init__(*args, **kwargs)
        self.init_ui()

    def init_ui(self):
        menu_bar = wx.MenuBar()
        view_menu = wx.Menu()

        self.shst = view_menu.Append(wx.ID_ANY, 'show statusbar', 'show statusbar',
                                     kind=wx.ITEM_CHECK)
        self.shtl = view_menu.Append(wx.ID_ANY, 'show toolbar', 'show toolbar',
                                     kind=wx.ITEM_CHECK)

        view_menu.Check(self.shst.GetId(), True)
        view_menu.Check(self.shtl.GetId(), True)

        self.Bind(wx.EVT_MENU, self.toggle_status_bar, self.shst)
        self.Bind(wx.EVT_MENU, self.toggle_tool_bar, self.shtl)

        menu_bar.Append(view_menu, '&View')
        self.SetMenuBar(menu_bar)

        self.toolbar = self.CreateToolBar()
        self.toolbar.AddTool(1, 'Some Text', wx.Bitmap('icon.png'))
        self.toolbar.Realize()

        self.statusbar = self.CreateStatusBar()
        self.statusbar.SetStatusText('Ready')

        self.SetSize((400, 300))
        self.SetTitle('Simple Menu')
        self.Center()

    def toggle_status_bar(self, e):
        if self.shst.IsChecked():
            self.statusbar.Show()
        else:
            self.statusbar.Hide()

    def toggle_tool_bar(self, e):
        if self.shtl.IsChecked():
            self.toolbar.Show()
        else:
            self.toolbar.Hide()

def main():
    app = wx.App()
    ex = Example(None)
    ex.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()
