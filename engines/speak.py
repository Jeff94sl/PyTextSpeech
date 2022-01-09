from PySide2.QtCore import QLocale
from PySide2.QtTextToSpeech import QTextToSpeech


class QSpeak(QTextToSpeech):
    """docstring for QSpeak"""

    def __init__(self):
        super(QSpeak, self).__init__()
        self.setLocale(QLocale.system())
        self.setRate(0.0)
        self.setVolume(0.0)
        self.setPitch(0.0)

    def Voice(self, voice):
        self.setVoice(voice)

    def Locale(self, locale):
        self.setLocale(locale)

    def getVoices(self):
        return self.availableVoices()

    def getLocale(self):
        return self.availableLocales()

    def getEngine(self):
        return self.availableEngines()

    def getVolume(self):
        return self.volume()
