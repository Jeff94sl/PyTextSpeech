import sys
from PySide2.QtWidgets import QApplication
from PySide2.QtCore import QTranslator, QLocale, QLibraryInfo
from gui import Window


if __name__ == '__main__':
	app = QApplication(sys.argv)

	traductor = QTranslator()
	traductor.load("qtbase_"+ QLocale.system().name(),
                   QLibraryInfo.location(QLibraryInfo.TranslationsPath))
	app.installTranslator(traductor)

	print(QLocale.system().name())
	win = Window()
	win.parent = app;

	win.show()

	sys.exit(app.exec_())