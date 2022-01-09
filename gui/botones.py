from PySide2.QtWidgets import QHBoxLayout, QPushButton


class Boton(QHBoxLayout):
    """docstring for Boton"""

    def __init__(self):
        super(Boton, self).__init__()

        self.btnSpeak = QPushButton("Hablar")
        self.btnPause = QPushButton("Pausar")
        self.btnResume = QPushButton("Reanudar")
        self.btnStop = QPushButton("Detener")

        self.addWidget(self.btnSpeak)
        self.addWidget(self.btnPause)
        self.addWidget(self.btnResume)
        self.addWidget(self.btnStop)
