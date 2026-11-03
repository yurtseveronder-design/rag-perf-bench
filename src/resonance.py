
import re
from typing import Dict, Any

class CognitiveResonanceAnalyzer:
    """
    Analyzes semantic alignment, lexical overlap, and cognitive tone 
    between a user query and a generated RAG response.
    """
    def __init__(self, semantic_threshold: float = 0.4):
        self.semantic_threshold = semantic_threshold

    def evaluate_resonance(self, query: str, response: str) -> Dict[str, Any]:
        if not query or not response:
            return {"resonance_score": 0.0, "is_cognitively_resonant": False, "reason": "Empty input detected."}

        # Tokenize and clean text
        q_tokens = set(re.findall(r'\w+', query.lower()))
        r_tokens = set(re.findall(r'\w+', response.lower()))

        if not q_tokens:
            overlap_ratio = 0.0
        else:
            overlap_ratio = len(q_tokens.intersection(r_tokens)) / len(q_tokens)

        # Structural length balance check (penalize extreme verbosity or abruptness)
        length_ratio = min(len(response), len(query) * 5) / max(len(response), len(query) * 5, 1)

        # Composite resonance score
        resonance_score = round(float((overlap_ratio * 0.6) + (length_ratio * 0.4)), 2)
        is_resonant = resonance_score >= self.semantic_threshold

        return {
            "resonance_score": resonance_score,
            "is_cognitively_resonant": is_resonant,
            "lexical_overlap_ratio": round(overlap_ratio, 2),
            "structural_balance": round(length_ratio, 2)
        }