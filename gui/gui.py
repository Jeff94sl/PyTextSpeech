from PySide2.QtWidgets import QWidget, QVBoxLayout, QTextEdit, QMessageBox
from PySide2.QtCore import Qt, QLocale
from gui import Menu, SliderGrop, Boton, ComboGrop
from engines import QSpeak, Document


class Window(QWidget):
    """docstring for Window"""

    def __init__(self):
        super(Window, self).__init__()
        self.setWindowTitle("PyTextSpeech")
        self.resize(400, 400)

        self.volume = 0
        self.rate = 0
        self.engine = QSpeak()
        self.doc = Document()
        self.mn = Menu()
        self.text_to_read = QTextEdit()
        self.vlayout = QVBoxLayout()
        self.sliders = SliderGrop()

        self.cmbgrop = ComboGrop()

        self.lbtn = Boton()
        self.doc.parent = self
        self.lbtn.btnSpeak.clicked.connect(self.Speak)
        self.lbtn.btnPause.clicked.connect(self.Pause)
        self.lbtn.btnResume.clicked.connect(self.Resume)
        self.lbtn.btnStop.clicked.connect(self.Stop)

        self.sliders.slider_volume.valueChanged.connect(self.SliderVolume)
        self.sliders.slider_rate.valueChanged.connect(self.SliderRate)

        self.cmbgrop.cmbVoice.currentTextChanged.connect(self.Voice)
        self.cmbgrop.cmbLanguage.currentTextChanged.connect(self.Locale)

        self.mn.Pdf.triggered.connect(self.Abrir_Pdf)
        self.mn.Texto.triggered.connect(self.Abrir_Text)

        self.LoadLanguage()
        self.LoadVoices()

        self.vlayout.addWidget(self.mn)
        self.vlayout.addWidget(self.text_to_read)

        self.vlayout.addLayout(self.sliders)
        self.vlayout.addLayout(self.cmbgrop)
        self.vlayout.addLayout(self.lbtn)

        self.setLayout(self.vlayout)

    def Abrir_Pdf(self):
        text = self.doc.AbrirPDF()
        self.text_to_read.setText(text)

    def Abrir_Text(self):
        self.text_to_read.setText(self.doc.AbrirText())

    def LoadVoices(self):
        voices = self.engine.getVoices()

        for i in voices:
            self.cmbgrop.cmbVoice.addItem(i.name())

    def LoadLanguage(self):
        locales = self.engine.getLocale()

        for i in locales:
            self.cmbgrop.cmbLanguage.addItem(QLocale.countryToString(i.country()))


    def Voice(self):
        try:
            voices = self.engine.getVoices()

            self.engine.Voice(voices[self.cmbgrop.cmbVoice.currentIndex()])

        except:
            msg = QMessageBox()
            msg.setWindowTitle('Error')
            msg.setIcon(QMessageBox.Warning)
            msg.setStandardButtons(QMessageBox.Ok)
            msg.setText('Voz no disponible')
            msg.exec_()

    def Locale(self):
        try:
            locales = self.engine.getLocale()
            self.engine.Locale(locales[self.cmbgrop.cmbLanguage.currentIndex()])
        except:
            msg = QMessageBox()
            msg.setWindowTitle(self.tr('Error'))
            msg.setIcon(QMessageBox.Warning)
            msg.setStandardButtons(QMessageBox.Ok)
            msg.setText('Lenguaje no disponible')
            msg.exec_()

    def SliderVolume(self):
        self.engine.setVolume(float(self.sliders.slider_volume.value() / 100))

    def SliderRate(self):
        self.engine.setRate(self.sliders.slider_rate.value() / 100)

    def SliderPitch(self):
        self.engine.setPitch(self.sliders.slider_pitch.value() / 100)

    def Speak(self):
        self.parent.setOverrideCursor(Qt.WaitCursor)
        self.engine.say(self.text_to_read.toPlainText())
        self.parent.restoreOverrideCursor()

    def Pause(self):
        self.engine.pause()

    def Resume(self):
        self.engine.resume()

    def Stop(self):
        self.engine.stop()
