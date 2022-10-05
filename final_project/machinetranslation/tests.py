import unittest

from translator import english_to_french, french_to_english

class TestEnglishToFrench(unittest.TestCase): 
    def test1(self): 

        self.assertEqual(english_to_french('Hello'), 'Bonjour')  # test when Hello is given Bonjour should be output

class TestFrenchToEnglish(unittest.TestCase): 
    def test1(self): 
       
        self.assertEqual(french_to_english('Bonjour'), 'Hello')  # test when Bonjour is given Hello should be output


unittest.main()