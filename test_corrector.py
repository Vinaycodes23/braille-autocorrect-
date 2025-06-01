# test_corrector.py
import unittest
from braille_utils import convert_qwerty_to_braille
from braille_corrector import suggest_word

class TestBrailleAutoCorrect(unittest.TestCase):
    def test_convert_qwerty_to_braille_hello(self):
        # Test "hello" with new keys: D,W,O (h), D,O (e), D,W,Q (l), D,W,Q (l), D,Q,O (o)
        key_sequence = ['D,W,O', 'D,O', 'D,W,Q', 'D,W,Q', 'D,Q,O']
        expected = "hello"
        result = convert_qwerty_to_braille(key_sequence)
        self.assertEqual(result, expected, f"Expected {expected}, but got {result}")

    def test_convert_qwerty_to_braille_test(self):
        # Test "test" with new keys: W,Q,K,O (t), D,O (e), W,Q,K (s), W,Q,K,O (t)
        key_sequence = ['W,Q,K,O', 'D,O', 'W,Q,K', 'W,Q,K,O']
        expected = "test"
        result = convert_qwerty_to_braille(key_sequence)
        self.assertEqual(result, expected, f"Expected {expected}, but got {result}")

    def test_convert_qwerty_to_braille_invalid_keys(self):
        # Test invalid keys
        key_sequence = ['X,Y,Z', 'D,O']
        expected = "Error: Invalid key in sequence"
        result = convert_qwerty_to_braille(key_sequence)
        self.assertEqual(result, expected, f"Expected {expected}, but got {result}")

    def test_suggest_word_valid_word(self):
        # Test a valid word (should return None)
        input_text = "hello"
        expected = None
        result = suggest_word(input_text)
        self.assertEqual(result, expected, f"Expected {expected}, but got {result}")

    def test_suggest_word_close_match(self):
        # Test a word close to "hello" (e.g., "hell?" should suggest "hello")
        input_text = "hell?"
        expected = ['hello']
        result = suggest_word(input_text)
        self.assertEqual(result, expected, f"Expected {expected}, but got {result}")

    def test_suggest_word_invalid_input(self):
        # Test invalid input from convert_qwerty_to_braille
        input_text = "Error: Invalid key in sequence"
        expected = ["Invalid input; try valid keys: D, W, Q, K, O, P"]
        result = suggest_word(input_text)
        self.assertEqual(result, expected, f"Expected {expected}, but got {result}")

    def test_suggest_word_no_match(self):
        # Test a word with no close matches
        input_text = "xyz"
        expected = None
        result = suggest_word(input_text)
        self.assertEqual(result, expected, f"Expected {expected}, but got {result}")
    
    def test_convert_qwerty_to_braille_contraction(self):
    # Test contraction "the" with W,O
        key_sequence = ['W,O']
        expected = "the"
        result = convert_qwerty_to_braille(key_sequence)
        self.assertEqual(result, expected, f"Expected {expected}, but got {result}")

if __name__ == '__main__':
    unittest.main()