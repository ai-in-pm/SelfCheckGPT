from typing import List
from bert_score import BERTScorer

class BERTScoreChecker:
    def __init__(self):
        self.scorer = BERTScorer(lang="en", rescale_with_baseline=True)

    def check_consistency(self, sentences: List[str], samples: List[str]) -> List[float]:
        inconsistency_scores = []
        for sentence in sentences:
            sentence_scores = []
            for sample in samples:
                _, _, F1 = self.scorer.score([sentence], [sample])
                sentence_scores.append(1 - F1.item())  # Convert similarity to inconsistency
            inconsistency_scores.append(sum(sentence_scores) / len(sentence_scores))
        return inconsistency_scores