# Python 2.7.13
# test with wxPython under Python 2.7.x
import wx

class TK_App(wx.App):
	def OnInit(self):
		self.frame = Frame(parent=None, title='Hello World Test')
		self.frame.Show()
		self.SetTopWindow(self.frame)
		return(True)

if __name__ == '__main__':
	app = TK_App()
	app.MainLoop()
  
