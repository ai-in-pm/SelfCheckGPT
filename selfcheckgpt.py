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
