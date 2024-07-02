# SelfCheckGPT

SelfCheckGPT is a Python library for detecting hallucinations in large language model outputs through self-consistency checking. It provides various methods to assess the factuality and consistency of generated text.

## Features

- Multiple consistency checking methods:
  - BERTScore
  - Question-Answering (QA)
  - N-gram
  - Natural Language Inference (NLI)
  - Prompt-based
- Factuality ranking of multiple responses
- Flexible integration with different language models

## Installation

### For users

To use SelfCheckGPT in your project, you can install it using pip:

```bash
pip install selfcheckgpt
```

Alternatively, you can install from source:

```bash
git clone https://github.com/yourusername/selfcheckgpt.git
cd selfcheckgpt
pip install -r requirements.txt
pip install .
```

### For developers

If you're planning to contribute to SelfCheckGPT or run tests, install the development dependencies:

```bash
git clone https://github.com/yourusername/selfcheckgpt.git
cd selfcheckgpt
pip install -r requirements-dev.txt
```

## Usage

Here's a basic example of how to use SelfCheckGPT:

```python
from selfcheckgpt import SelfCheckGPT

def example_llm_generate(prompt: str) -> str:
    # This is a placeholder for an actual LLM generation function
    return "This is a generated response based on the prompt: " + prompt

# Initialize SelfCheckGPT
selfcheck = SelfCheckGPT(example_llm_generate)

# Check consistency of a single response
main_response = "The Earth is the third planet from the Sun and the only astronomical object known to harbor life."
consistency_scores = selfcheck.check_consistency(main_response, method="nli")
print(f"Consistency scores: {consistency_scores}")

# Rank factuality of multiple responses
responses_to_rank = [
    "The Moon is Earth's only natural satellite.",
    "Mars is a gaseous planet with rings similar to Saturn.",
    "Jupiter is the largest planet in our solar system."
]
factuality_ranks = selfcheck.rank_factuality(responses_to_rank)
print(f"Factuality ranks: {factuality_ranks}")
```

For more detailed examples, check the `examples/` directory.

## Development

To set up the development environment:

1. Install the development dependencies:
   ```bash
   pip install -r requirements-dev.txt
   ```

2. Install pre-commit hooks:
   ```bash
   pre-commit install
   ```

3. Run tests:
   ```bash
   pytest
   ```

4. Check code style:
   ```bash
   flake8 .
   black --check .
   ```

5. Generate documentation:
   ```bash
   cd docs
   make html
   ```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

Please make sure to update tests as appropriate and adhere to the code style guidelines.
