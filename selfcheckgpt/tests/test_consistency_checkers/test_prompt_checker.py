import unittest
from consistency_checkers.prompt_checker import PromptChecker

class TestPromptChecker(unittest.TestCase):
    def setUp(self):
        def mock_llm_function(prompt: str) -> str:
            if "Earth" in prompt and "planet" in prompt:
                return "Yes"
            elif "Moon" in prompt and "cheese" in prompt:
                return "No"
            else:
                return "Unable to determine"
        
        self.checker = PromptChecker(mock_llm_function)

    def test_check_consistency(self):
        sentences = ["The Earth is a planet in our solar system."]
        samples = [
            "The Earth is the third planet from the Sun.",
            "Our planet Earth is part of the Solar System.",
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
            "The Moon is Earth's only natural satellite.",
            "Lunar rocks were brought back by Apollo missions for study.",
        ]
        scores = self.checker.check_consistency(sentences, samples)
        
        self.assertEqual(len(scores), 1)
        self.assertGreater(scores[0], 0.5)  # Expect high inconsistency

    def test_uncertain_response(self):
        sentences = ["The speed of light is constant in a vacuum."]
        samples = [
            "Light travels at different speeds through different mediums.",
            "Einstein's theory of relativity deals with the speed of light.",
        ]
        scores = self.checker.check_consistency(sentences, samples)
        
        self.assertEqual(len(scores), 1)
        self.assertAlmostEqual(scores[0], 0.5)  # Expect uncertainty

if __name__ == '__main__':
    unittest.main()