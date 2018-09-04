from PySide2.QtWidgets import (QMessageBox, QFileDialog)
from PySide2.QtCore import QObject
from PyPDF2 import PdfFileReader

class Document():
	"""docstring for Document"""
	def __init__(self):
		super(Document, self).__init__()
		self.parent= ""
	
	def AbrirPDF(self):
		filename,_ = QFileDialog.getOpenFileName(self.parent,"Abrir Pdf", "/home/","Pdf (*.pdf)")

		if filename:
			archivo = open(filename,'rb')
			pdfread = PdfFileReader(archivo)
			numpage = pdfread.getNumPages()
			for i in range(numpage):
				page = pdfread.getPage(i)
				return page.extractText()

	def AbrirText(self):
		filename,_ = QFileDialog.getOpenFileName(self.parent,"Abrir Text","/home/","Texto Plano(*.txt *.py *.rb *.html *.go *.c *.cpp *.cs *.java)")
		if filename:
			archivo = open(filename,'r')
			return archivo.read()
