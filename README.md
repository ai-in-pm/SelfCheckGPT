# SelfCheckGPT

SelfCheckGPT is a Python library for detecting hallucinations in large language model outputs through self-consistency checking. It provides various methods to assess the factuality and consistency of generated text.

SelfCheckGPT was inspired by the SELFCHECKGPT: Zero-Resource Black-Box Hallucination Detection for Generative Large Language Models Paper. To read the full article, visit https://arxiv.org/pdf/2303.08896

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

## Testing

We use pytest for testing. To run all tests:

```bash
pytest
```

To run tests with coverage report:

```bash
pytest --cov=selfcheckgpt
```

## Configuration

SelfCheckGPT can be configured to use various language models, including OpenAI's GPT models (like ChatGPT). To use these models, you'll need to set up your API keys.
Setting up API Keys

OpenAI API (for GPT-4o, ChatGPT-3.5, etc.):

Sign up for an account at OpenAI
Generate an API key in your account dashboard
Set the API key as an environment variable:

```
export OPENAI_API_KEY='your-api-key-here'
```

Alternatively, you can set it in your Python script:

```
import os
os.environ['OPENAI_API_KEY'] = 'your-api-key-here'
```
Other APIs:

If you're using other language model APIs, follow a similar process to obtain and set the necessary API keys.

Note: Never commit your API keys to version control. Always use environment variables or a secure configuration file that is not tracked by git.

Usage
To use SelfCheckGPT with a specific language model, you'll need to provide a function that interfaces with that model's API. Here's an example using OpenAI's GPT-3:

```
import openai
from selfcheckgpt import SelfCheckGPT

def gpt3_generate(prompt: str) -> str:
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=100
    )
    return response.choices[0].text.strip()

# Initialize SelfCheckGPT with the GPT-3 generation function
selfcheck = SelfCheckGPT(gpt3_generate)

# Use SelfCheckGPT as before
main_response = "The Earth is the third planet from the Sun."
consistency_scores = selfcheck.check_consistency(main_response, method="nli")
print(f"Consistency scores: {consistency_scores}")
```

## Contributing

We welcome contributions to SelfCheckGPT! Here's how you can contribute:

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

Please make sure to update tests as appropriate and adhere to the code style guidelines.

### Code Style

We use Black for code formatting and Flake8 for linting. Please ensure your code passes both before submitting a pull request:

```bash
black .
flake8 .
```

### Adding a New Consistency Checker

To add a new consistency checker:

1. Create a new file in `selfcheckgpt/consistency_checkers/`
2. Implement the checker class with a `check_consistency` method
3. Add appropriate tests in `tests/test_consistency_checkers/`
4. Update `selfcheckgpt/selfcheckgpt.py` to include the new checker
5. Update the README to mention the new checker in the Features section

## Citing SelfCheckGPT

If you use SelfCheckGPT in your research, please cite it as follows:

```
@software{selfcheckgpt2023,
  author = {Your Name},
  title = {SelfCheckGPT: Self-Consistency Checking for Language Model Outputs},
  year = {2023},
  url = {https://github.com/yourusername/selfcheckgpt}
}
```
