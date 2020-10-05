from .Graphics import tkinter
from .ConfigSettings import Connect

class TextPad(tkinter.Text):
	def __init__(self, *args, **kwargs):
		tkinter.Text.__init__(self, *args, **kwargs)
		self.storeobj = {}
		self.Connect_External_Module_Features()
		self._pack()

	def Connect_External_Module_Features(self):
		Connect(self)
		return

	def _pack(self):
		self.pack(expand = True, fill = "both")
		return

if __name__ == '__main__':
		root = tkinter.Tk(className = "Test TextPad")
		TextPad(root)
		root.mainloop()