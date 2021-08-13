import unittest
from main import english_to_french, french_to_english
from ibm_cloud_sdk_core.api_exception import ApiException


class TestLanguageService(unittest.TestCase):
    def setUp(self):
        self.english1 = "Hello"
        self.english2 = "Goodbye"

        self.french1 = "Bonjour"
        self.french2 = "Au revoir"

        self.empty = ""

    def test_english_to_french(self):
        self.assertEqual(english_to_french(self.english1), self.french1)
        self.assertEqual(english_to_french(self.english2), self.french2)

        self.assertNotEqual(english_to_french(self.english1), self.french2)
        self.assertNotEqual(english_to_french(self.english2), self.french1)
        

    def test_french_to_english(self):
        self.assertEqual(french_to_english(self.french1), self.english1)
        self.assertEqual(french_to_english(self.french2), self.english2)

        self.assertNotEqual(french_to_english(self.french1), self.english2)
        self.assertNotEqual(french_to_english(self.french2), self.english1)
    
    def test_exception(self):
        self.assertEqual(english_to_french("")[0], 400)
        self.assertEqual(french_to_english("")[0], 400)
