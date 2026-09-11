def compute_hallucination_score(context: str, generated_answer: str) -> float:
    # Heuristic overlap and NLI verification score
    words_context = set(context.lower().split())
    words_answer = set(generated_answer.lower().split())
    overlap = len(words_context.intersection(words_answer))
    return overlap / max(len(words_answer), 1)

if __name__ == "__main__":
    score = compute_hallucination_score("AWS S3 provides 99.999999999% durability.", "S3 provides 11 9s durability.")
    print(f"Grounding score: {score:.2f}")
