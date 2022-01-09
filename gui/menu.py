from PySide2.QtWidgets import QMenuBar, QAction


class Menu(QMenuBar):
	"""docstring for Menu"""
	def __init__(self):
		super(Menu, self).__init__()
		self.opcion = self.addMenu("Archivo")

		self.Pdf = QAction("Abrir Pdf")
		self.Texto =QAction("Abrir Texto") 

		self.opcion.addAction(self.Pdf)
		self.opcion.addAction(self.Texto)
