import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))

import json
from src.metrics import PerformanceTracker
from src.client import LocalModelClient
from src.reporter import PerformanceReporter

DATASET_PATH = Path(__file__).parent.parent / 'datasets' / 'queries.json'

with open(DATASET_PATH, 'r', encoding='utf-8') as f:
    data = json.load(f)

def test_rag_live_endpoint_and_generate_report():
    tracker = PerformanceTracker()
    client = LocalModelClient()
    reporter = PerformanceReporter()
    queries = data['benchmark_queries']
    results_log = []
    MAX_LATENCY_THRESHOLD = 0.5
    MIN_THROUGHPUT_THRESHOLD = 5.0
    for item in queries:
        query_text = item['query']
        response, token_count, latency = client.generate_response(query_text)
        throughput = tracker.calculate_throughput(token_count, latency)
        results_log.append({'id': item['id'], 'query': query_text, 'latency': latency, 'throughput': throughput})
        assert latency < MAX_LATENCY_THRESHOLD
        assert throughput >= MIN_THROUGHPUT_THRESHOLD
    reporter.save_markdown_report(results_log)
    assert Path('performance_report.md').exists()
