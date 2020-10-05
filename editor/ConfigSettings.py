from .ScrollBar import Scrollbar
from .LineNumber import LineMain
from .StationeryFunctions import StationeryFunctions
from .PopUpMenu import Popup
from .FindAndReplace import FindReplaceFunctions

class Connect:
	def __init__(self, pad):
		self.pad = pad
		self.modules_connections()


	def modules_connections(self):
		Scrollbar(self.pad)
		# LineMain(self.pad)
		# StationeryFunctions(self.pad)
		# Popup(self.pad)
		# FindReplaceFunctions(self.pad)
		return