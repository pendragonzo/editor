from .Graphics import Tkinter as tk
from .TextPad import TextPad

class TextPad_Window(tk.Tk):
	def __init__(self, *args, **kwargs):
		tk.Tk.__init__(self, *args, **kwargs)
		self._text_pad_()


	def _text_pad_(self):
		TextPad(self).pack()
		return