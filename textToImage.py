import text_to_image
import wx
class main(wx.Frame):
	def __init__(self):
		super().__init__(None, title="textToImage")
		self.Centre()
		p = wx.Panel(self)
		wx.StaticText(p, -1, "text")
		self.edit = wx.TextCtrl(p,-1,value="",name="")
		wx.StaticText(p, -1, "file name")
		self.edit1 = wx.TextCtrl(p,-1)
		generate = wx.Button(p,-1,label="&save")
		generate.Bind(wx.EVT_BUTTON,self.onGenerate)
		self.Show()
	def onGenerate(self,event):
		if self.edit.GetValue() == "":
			wx.MessageBox("error Please enter text","error")
			self.SetFocus(self.edit)
		else:
			encoded_image_path = text_to_image.encode(self.edit.GetValue(), f"{self.edit1.GetValue()}.png")

			self.edit.Value = ""

app=wx.App()
w=main()
w.Show()
app.MainLoop()