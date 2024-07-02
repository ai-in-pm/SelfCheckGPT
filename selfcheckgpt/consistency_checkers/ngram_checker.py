from typing import List
from collections import Counter
import nltk
from nltk.util import ngrams

class NGramChecker:
    def __init__(self, n: int = 3):
        self.n = n
        nltk.download('punkt')

    def check_consistency(self, sentences: List[str], samples: List[str]) -> List[float]:
        # Create n-gram model from samples
        all_ngrams = []
        for sample in samples:
            tokens = nltk.word_tokenize(sample.lower())
            all_ngrams.extend(ngrams(tokens, self.n))
        ngram_counts = Counter(all_ngrams)

        inconsistency_scores = []
        for sentence in sentences:
            tokens = nltk.word_tokenize(sentence.lower())
            sentence_ngrams = list(ngrams(tokens, self.n))
            if not sentence_ngrams:
                inconsistency_scores.append(1.0)  # Maximum inconsistency if no n-grams
                continue
            
            ngram_scores = [1 / (ngram_counts[ng] + 1) for ng in sentence_ngrams]
            inconsistency_scores.append(sum(ngram_scores) / len(ngram_scores))

        return inconsistency_scores