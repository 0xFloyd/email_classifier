import unittest
from email_classifier_function import email_classifier, censor

class TestEmailClassifier(unittest.TestCase):
    '''Unit tests for email classifier function'''

    # tests classifier when given correct input
    def test_email_classifier(self):
        classified_words = ["is", "test"]
        email_text = "This is a test."
        self.assertEqual(email_classifier(classified_words, email_text), (True, "This ** a ****."))
   
    # tests classifier if list and string type not function parameters
    def test_email_classifier_type(self):
       classified_words = "is test"
       email_text = 123456789
       self.assertRaises(TypeError, email_classifier(classified_words, email_text))
    
    # test censor function when given correct input
    def test_censor(self):
        word = "censorfunction"
        self.assertEqual(censor(word), "**************")
    
    # test censor function if string type not function parameter
    def test_censor_type(self):
       word = 111
       self.assertRaises(TypeError, censor(word))