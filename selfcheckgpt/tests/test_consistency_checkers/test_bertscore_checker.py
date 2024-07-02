import unittest
from consistency_checkers.bertscore_checker import BERTScoreChecker

class TestBERTScoreChecker(unittest.TestCase):
    def setUp(self):
        self.checker = BERTScoreChecker()

    def test_check_consistency(self):
        sentences = ["The quick brown fox jumps over the lazy dog."]
        samples = [
            "A fast auburn canine leaps above a sluggish hound.",
            "The rapid brown fox hops over the sleepy dog.",
        ]
        scores = self.checker.check_consistency(sentences, samples)
        
        self.assertEqual(len(scores), 1)
        self.assertTrue(0 <= scores[0] <= 1)

    def test_empty_input(self):
        scores = self.checker.check_consistency([], [])
        self.assertEqual(scores, [])

    def test_inconsistent_sentence(self):
        sentences = ["The Earth is flat."]
        samples = [
            "The Earth is a spherical planet.",
            "Our planet is an oblate spheroid.",
        ]
        scores = self.checker.check_consistency(sentences, samples)
        
        self.assertEqual(len(scores), 1)
        self.assertGreater(scores[0], 0.5)  # Expect high inconsistency

if __name__ == '__main__':
    unittest.main()