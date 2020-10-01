from .Graphics import Tkinter

class TextPad(Tkinter.Text):
	def __init__(self, *args, **kwargs):
		Tkinter.Text.__init__(self, *args, **kwargs)
		self._pack()


	def _pack(self):
		self.pack(expand = True, fill = "both")
		return



if __name__ == '__main__':
	root = Tkinter.Tk(className = " Test TextPad")
	TextPad(root)
	root.mainloop()