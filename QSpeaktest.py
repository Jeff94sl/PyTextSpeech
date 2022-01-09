from PySide2.QtCore import QLocale
from engines.speak import QSpeak

def test_say():
    sp = QSpeak()
    sp.say('Ok')
