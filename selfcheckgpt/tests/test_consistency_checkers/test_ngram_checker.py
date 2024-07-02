import unittest
from consistency_checkers.ngram_checker import NGramChecker

class TestNGramChecker(unittest.TestCase):
    def setUp(self):
        self.checker = NGramChecker(n=3)  # Using trigrams

    def test_check_consistency(self):
        sentences = ["The quick brown fox jumps over the lazy dog."]
        samples = [
            "A quick brown fox leaps over a lazy dog.",
            "The rapid fox jumps above the sleepy hound.",
        ]
        scores = self.checker.check_consistency(sentences, samples)
        
        self.assertEqual(len(scores), 1)
        self.assertTrue(0 <= scores[0] <= 1)

    def test_empty_input(self):
        scores = self.checker.check_consistency([], [])
        self.assertEqual(scores, [])

    def test_inconsistent_sentence(self):
        sentences = ["The purple elephant flies in the sky."]
        samples = [
            "The quick brown fox jumps over the lazy dog.",
            "A fast car drives on the highway.",
        ]
        scores = self.checker.check_consistency(sentences, samples)
        
        self.assertEqual(len(scores), 1)
        self.assertGreater(scores[0], 0.5)  # Expect high inconsistency

    def test_different_n(self):
        checker2 = NGramChecker(n=2)  # Using bigrams
        sentences = ["The quick brown fox."]
        samples = ["The quick brown fox."]
        scores1 = self.checker.check_consistency(sentences, samples)
        scores2 = checker2.check_consistency(sentences, samples)
        self.assertNotEqual(scores1, scores2)

if __name__ == '__main__':
    unittest.main()