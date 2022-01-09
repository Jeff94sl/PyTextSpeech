from PySide2.QtWidgets import QSlider, QHBoxLayout, QFormLayout, QLabel
from PySide2.QtCore import Qt

class Slider(QSlider):
	"""docstring for Slider"""
	def __init__(self):
		super(Slider, self).__init__()
		self.setTickPosition(self.NoTicks)
		self.setOrientation(Qt.Horizontal)


class SliderGrop(QHBoxLayout):
	"""docstring for SliderGrop"""
	def __init__(self):
		super(SliderGrop, self).__init__()
		
		self.form = QFormLayout()
		self.label_volume = QLabel(self.tr("Volumen"))
		self.label_rate = QLabel("Velocidad")
		self.label_pitch = QLabel("Tono")
		self.slider_volume = Slider()
		self.slider_rate = Slider()
		self.slider_pitch = Slider()

		self.slider_volume.setMaximum(100)
		self.slider_rate.setMaximum(200)
		self.slider_pitch.setMaximum(200)

		self.form.addRow(self.label_volume,self.slider_volume)
		self.form.addRow(self.label_rate,self.slider_rate)
		self.form.addRow(self.label_pitch,self.slider_pitch)

		self.addLayout(self.form)
		
