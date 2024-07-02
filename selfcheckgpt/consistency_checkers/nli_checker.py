from typing import List
import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification

class NLIChecker:
    def __init__(self):
        self.tokenizer = AutoTokenizer.from_pretrained("microsoft/deberta-v3-large")
        self.model = AutoModelForSequenceClassification.from_pretrained("microsoft/deberta-v3-large")

    def check_consistency(self, sentences: List[str], samples: List[str]) -> List[float]:
        inconsistency_scores = []
        for sentence in sentences:
            sentence_scores = []
            for sample in samples:
                inputs = self.tokenizer(sample, sentence, return_tensors="pt", truncation=True, max_length=512)
                with torch.no_grad():
                    outputs = self.model(**inputs)
                logits = outputs.logits
                probs = torch.softmax(logits, dim=1)
                contradiction_prob = probs[0, 2].item()  # Assuming index 2 is for contradiction
                sentence_scores.append(contradiction_prob)
            inconsistency_scores.append(sum(sentence_scores) / len(sentence_scores))
        return inconsistency_scores