from typing import List, Callable

class PromptChecker:
    def __init__(self, llm_function: Callable[[str], str]):
        self.llm_function = llm_function

    def check_consistency(self, sentences: List[str], samples: List[str]) -> List[float]:
        inconsistency_scores = []
        for sentence in sentences:
            sentence_scores = []
            for sample in samples:
                prompt = f"""
                Context: {sample}
                Sentence: {sentence}
                Is the sentence supported by the context above?
                Answer Yes or No:
                """
                response = self.llm_function(prompt).strip().lower()
                score = 1.0 if response == "no" else 0.0 if response == "yes" else 0.5
                sentence_scores.append(score)
            inconsistency_scores.append(sum(sentence_scores) / len(sentence_scores))
        return inconsistency_scores