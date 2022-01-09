import pathlib
from PySide2.QtWidgets import QFileDialog
from PyPDF4 import PdfFileReader


class Document:
    """docstring for Document"""

    def __init__(self):
        super(Document, self).__init__()
        self.parent = ""

    def AbrirPDF(self):
        filename, _ = QFileDialog.getOpenFileName(self.parent, 'Abrir Pdf', f'{pathlib.Path.home()}', 'Pdf (*.pdf)')

        if filename:
            archivo = open(filename, 'rb')
            pdfread = PdfFileReader(archivo)
            numpage = pdfread.getNumPages()
            for i in range(numpage):
                page = pdfread.getPage(i)
                return page.extractText()

    def AbrirText(self):
        filename, _ = QFileDialog.getOpenFileName(self.parent, 'Abrir Text', f'{pathlib.Path.home()}',
                                                  'Texto Plano(*.txt *.py *.rb *.html *.go *.c *.cpp *.cs *.java)')
        if filename:
            archivo = open(filename, 'r')
            return archivo.read()
