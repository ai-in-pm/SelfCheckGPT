import unittest
from consistency_checkers.nli_checker import NLIChecker

class TestNLIChecker(unittest.TestCase):
    def setUp(self):
        self.checker = NLIChecker()

    def test_check_consistency(self):
        sentences = ["Water boils at 100 degrees Celsius at sea level."]
        samples = [
            "The boiling point of water is 100 degrees Celsius under normal atmospheric pressure.",
            "At sea level, water typically boils at 212 degrees Fahrenheit, which is 100 degrees Celsius.",
        ]
        scores = self.checker.check_consistency(sentences, samples)
        
        self.assertEqual(len(scores), 1)
        self.assertTrue(0 <= scores[0] <= 1)

    def test_empty_input(self):
        scores = self.checker.check_consistency([], [])
        self.assertEqual(scores, [])

    def test_inconsistent_sentence(self):
        sentences = ["The Moon is made of cheese."]
        samples = [
            "The Moon is Earth's only natural satellite and is composed mainly of rock.",
            "Lunar samples brought back by Apollo missions show the Moon is made of various types of rocks.",
        ]
        scores = self.checker.check_consistency(sentences, samples)
        
        self.assertEqual(len(scores), 1)
        self.assertGreater(scores[0], 0.5)  # Expect high inconsistency

    def test_consistent_sentence(self):
        sentences = ["The Earth orbits around the Sun."]
        samples = [
            "Our planet, Earth, revolves around the Sun in an elliptical orbit.",
            "The Solar System consists of the Sun and the celestial objects bound to it by gravity, including Earth.",
        ]
        scores = self.checker.check_consistency(sentences, samples)
        
        self.assertEqual(len(scores), 1)
        self.assertLess(scores[0], 0.5)  # Expect low inconsistency

if __name__ == '__main__':
    unittest.main()