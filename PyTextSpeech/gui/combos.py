from PySide2.QtWidgets import (QHBoxLayout, QFormLayout,
	QLabel,QComboBox)
class ComboGrop(QHBoxLayout):
	"""docstring for ComboGrop"""
	def __init__(self):
		super(ComboGrop, self).__init__()
		
		self.form = QFormLayout()
		self.labelLanguage = QLabel("Idioma")
		self.labelVoice = QLabel("Voz")
		self.cmbLanguage = QComboBox()
		self.cmbVoice = QComboBox()
		self.cmbengine = QComboBox()

		self.form.addRow(self.labelLanguage,self.cmbLanguage)
		self.form.addRow(self.labelVoice,self.cmbVoice)

		self.addLayout(self.form)

