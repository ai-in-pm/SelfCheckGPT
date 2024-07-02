from typing import List
from transformers import pipeline

class QAChecker:
    def __init__(self):
        self.qa_pipeline = pipeline("question-answering", model="distilbert-base-cased-distilled-squad")

    def generate_question(self, sentence: str) -> str:
        # This is a placeholder. In a real implementation, you'd use a question generation model.
        return f"What is the main idea of '{sentence}'?"

    def check_consistency(self, sentences: List[str], samples: List[str]) -> List[float]:
        inconsistency_scores = []
        for sentence in sentences:
            question = self.generate_question(sentence)
            sentence_scores = []
            for sample in samples:
                result = self.qa_pipeline(question=question, context=sample)
                sentence_scores.append(1 - result['score'])  # Convert confidence to inconsistency
            inconsistency_scores.append(sum(sentence_scores) / len(sentence_scores))
        return inconsistency_scores