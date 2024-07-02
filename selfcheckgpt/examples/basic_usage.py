from selfcheckgpt import SelfCheckGPT

def example_llm_generate(prompt: str) -> str:
    # This is a placeholder for an actual LLM generation function
    return "This is a generated response based on the prompt: " + prompt

def main():
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

if __name__ == "__main__":
    main()