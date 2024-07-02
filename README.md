# SelfCheckGPT
SelfCheckGPT is a tool for detecting hallucinations in large language model outputs through self-consistency checking.

This repository was inspired by SELFCHECKGPT: Zero-Resource Black-Box Hallucination Detection for Generative Large Language Models Paper.
To read the full article, visit this link: https://arxiv.org/pdf/2303.08896

## Installation

You can install SelfCheckGPT using pip:

```bash
pip install selfcheckgpt
```

## Usage

Here's a basic example of how to use SelfCheckGPT:

```python
from selfcheckgpt import SelfCheckGPT

def example_llm_generate(prompt: str) -> str:
    # This is a placeholder for an actual LLM generation function
    return "This is a generated response."

selfcheck = SelfCheckGPT(example_llm_generate)
main_response = "This is the main response to check."
consistency_scores = selfcheck.check_consistency(main_response, method="nli")
print(f"Consistency scores: {consistency_scores}")

responses_to_rank = ["Response 1", "Response 2", "Response 3"]
factuality_ranks = selfcheck.rank_factuality(responses_to_rank)
print(f"Factuality ranks: {factuality_ranks}")
```

For more detailed examples, check the `examples/` directory.
