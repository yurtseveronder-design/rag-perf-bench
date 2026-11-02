import json
from pathlib import Path
from src.metrics import PerformanceTracker

# Load benchmark queries from the external JSON dataset
DATASET_PATH = Path(__file__).parent.parent / "datasets" / "queries.json"

with open(DATASET_PATH, "r", encoding="utf-8") as f:
    data = json.load(f)

def mock_rag_pipeline(query: str):
    """
    Simulates a RAG pipeline response returning text and generated token count.
    In a live deployment, this would make an API call to your vector store and LLM.
    """
    # Simulated processing delay
    import time
    time.sleep(0.02) 

    dummy_response = f"Context retrieved and generated answer for: {query}"
    simulated_token_count = 45  # Estimated tokens generated
    return dummy_response, simulated_token_count

def test_rag_query_latency_and_throughput():
    """Test and benchmark latency and token throughput for each query in the dataset."""
    tracker = PerformanceTracker()
    queries = data["benchmark_queries"]

    for item in queries:
        query_text = item["query"]

        # Measure execution performance using the metrics engine
        (response, token_count), latency = tracker.measure_latency(mock_rag_pipeline, query_text)
        throughput = tracker.calculate_throughput(token_count, latency)

        # Assertions to ensure performance thresholds and valid responses
        assert latency < 1.0, f"Latency too high for query ID {item['id']}: {latency:.4f}s"
        assert throughput > 0, f"Throughput calculation failed for query ID {item['id']}"
        assert len(response) > 0, f"Empty response received for query ID {item['id']}"