import hangman
from unittest import TestCase


# 'METHOD' means 'validate_input' is the name of the method.
class TestHangmanMETHODvalidate_input(TestCase):
    # 'CHECK' means what this method asserts.
    def test_input_multiple_characters_OR_input_float_CHECK_return_False(self):
        # int
        self.assertFalse(hangman.validate_input('56'))
        # correct answers
        self.assertFalse(hangman.validate_input('to'))
        # incorrect answers
        self.assertFalse(hangman.validate_input('ah'))
        # float
        self.assertFalse(hangman.validate_input('5.6'))
        # single digit float
        self.assertFalse(hangman.validate_input('5.0'))
        # single digit negative number
        self.assertFalse(hangman.validate_input('-1'))

    # Previous test catches multiple digits. This test should only check for single digits.
    def test_input_single_character_Int_CHECK_return_False(self):
        # positive
        self.assertFalse(hangman.validate_input('5'))
        # 0
        self.assertFalse(hangman.validate_input('0'))

    def test_input_single_character_uppercase_AND_lowercase_CHECK_True(self):
        # Correct guess
        self.assertTrue(hangman.validate_input('c'))
        # Correct uppercase guess
        self.assertTrue(hangman.validate_input('O'))
        # Incorrect lowercase guess
        self.assertTrue(hangman.validate_input('a'))
        # Incorrect uppercase guess
        self.assertTrue(hangman.validate_input('H'))


class TestHangmanMETHODupdate_guessed(TestCase):

# Can't get this to work. I'm probably missing something.
    # def setUp(self):
    #     words = "computers rule"
    #     guessed = '_________ ____'

    def test_character_is_first_correct_guess_in_secret_words_CHECK_returns_correct_value(self):
        words = "computers rule"
        guessed = '_________ ____'

        # first letter
        self.assertEqual(hangman.update_guessed('c', words, guessed), 'c________ ____')
        # multiple occurrences
        self.assertEqual(hangman.update_guessed('r', words, guessed), '_______r_ r___')
        # last letter
        self.assertEqual(hangman.update_guessed('e', words, guessed), '______e__ ___e')

    def test_consecutive_correct_guesses_in_secret_words_CHECK_returns_correct_value(self):
        words = "computers rule"
        guessed = '_________ ____'

        # first letter
        guessed = hangman.update_guessed('c', words, guessed)
        self.assertEqual(guessed, 'c________ ____')
        # multiple occurrences
        guessed = hangman.update_guessed('r', words, guessed)
        self.assertEqual(guessed, 'c______r_ r___')
        # last letter
        guessed = hangman.update_guessed('e', words, guessed)
        self.assertEqual(guessed, 'c_____er_ r__e')
