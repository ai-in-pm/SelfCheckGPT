import unittest
from consistency_checkers.qa_checker import QAChecker

class TestQAChecker(unittest.TestCase):
    def setUp(self):
        self.checker = QAChecker()

    def test_check_consistency(self):
        sentences = ["Paris is the capital of France."]
        samples = [
            "France is a country in Western Europe. Its capital is Paris.",
            "The Eiffel Tower is located in Paris, the capital city of France.",
        ]
        scores = self.checker.check_consistency(sentences, samples)
        
        self.assertEqual(len(scores), 1)
        self.assertTrue(0 <= scores[0] <= 1)

    def test_empty_input(self):
        scores = self.checker.check_consistency([], [])
        self.assertEqual(scores, [])

    def test_inconsistent_sentence(self):
        sentences = ["London is the capital of France."]
        samples = [
            "Paris is the capital city of France.",
            "France's capital is Paris, located on the Seine river.",
        ]
        scores = self.checker.check_consistency(sentences, samples)
        
        self.assertEqual(len(scores), 1)
        self.assertGreater(scores[0], 0.5)  # Expect high inconsistency

    def test_generate_question(self):
        sentence = "The sky is blue."
        question = self.checker.generate_question(sentence)
        self.assertIsInstance(question, str)
        self.assertTrue(len(question) > 0)

if __name__ == '__main__':
    unittest.main()