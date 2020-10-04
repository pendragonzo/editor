from .ScrollBar import Scrollbar

class Connect:
	def __init__(self, pad):
		self.pad = pad
		self.modules_connections()


	def modules_connections(self):
		Scrollbar(self.pad)
		return