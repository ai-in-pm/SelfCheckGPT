import re
from typing import List

def split_into_sentences(text: str) -> List[str]:
    """
    Split the input text into sentences.
    This is a simple implementation and might not cover all edge cases.
    For more robust sentence splitting, consider using libraries like nltk or spacy.
    """
    # Split on period followed by space and uppercase letter
    sentences = re.split(r'(?<=[.!?])\s+(?=[A-Z])', text)
    # Remove any leading/trailing whitespace
    sentences = [s.strip() for s in sentences if s.strip()]
    return sentences

def preprocess_text(text: str) -> str:
    """
    Preprocess the input text by removing extra whitespace and normalizing.
    """
    # Remove extra whitespace
    text = re.sub(r'\s+', ' ', text).strip()
    # Normalize quotes
    text = re.sub(r'[""]', '"', text)
    # Normalize apostrophes
    text = re.sub(r'['']', "'", text)
    return text