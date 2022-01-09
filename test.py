import unittest
from engines.speak import QSpeak

class MyTestCase(unittest.TestCase):
    def test_something(self):
        speek = QSpeak()
        result = speek.readtext('Ok')
        self.assertEqual(result, True)


if __name__ == '__main__':
    unittest.main()
