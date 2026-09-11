from evaluator import compute_hallucination_score

def test_high_grounding():
    score = compute_hallucination_score("Kubernetes is a container orchestrator.", "Kubernetes is an orchestrator.")
    assert score > 0.5
