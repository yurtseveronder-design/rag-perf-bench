import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))

import json
import os
from src.metrics import PerformanceTracker
from src.client import LocalModelClient
from src.reporter import PerformanceReporter
from deepeval.test_case import LLMTestCase
from deepeval.metrics import (
    FaithfulnessMetric, 
    AnswerRelevancyMetric, 
    ContextualPrecisionMetric, 
    ContextualRecallMetric
)
from deepeval.models.base_model import DeepEvalBaseLLM
from openai import OpenAI, AsyncOpenAI
from deepeval import assert_test

class GroqEvaluator(DeepEvalBaseLLM):
    def __init__(self, model_name="openai/gpt-oss-120b"):
        self.model_name = model_name
        api_key = os.environ.get("GROQ_API_KEY")
        base_url = "https://api.groq.com/openai/v1"
        self.client = OpenAI(api_key=api_key, base_url=base_url)
        self.async_client = AsyncOpenAI(api_key=api_key, base_url=base_url)
    def load_model(self):
        return self.client
    def get_model_name(self):
        return self.model_name
    def generate(self, prompt: str, schema=None) -> str:
        res = self.client.chat.completions.create(model=self.model_name, messages=[{"role": "user", "content": prompt}], temperature=0)
        return res.choices[0].message.content
    async def a_generate(self, prompt: str, schema=None) -> str:
        res = await self.async_client.chat.completions.create(model=self.model_name, messages=[{"role": "user", "content": prompt}], temperature=0)
        return res.choices[0].message.content

DATASET_PATH = Path(__file__).parent.parent / 'datasets' / 'queries.json'
with open(DATASET_PATH, 'r', encoding='utf-8') as file:
    data = json.load(file)

def test_rag_quality_and_performance():
    tracker = PerformanceTracker()
    client = LocalModelClient()
    reporter = PerformanceReporter()
    queries = data['benchmark_queries']
    results_log = []
    
    evaluator = GroqEvaluator()
    faithfulness = FaithfulnessMetric(threshold=0.7, model=evaluator, include_reason=True)
    relevancy = AnswerRelevancyMetric(threshold=0.7, model=evaluator, include_reason=True)
    precision = ContextualPrecisionMetric(threshold=0.7, model=evaluator, include_reason=True)
    recall = ContextualRecallMetric(threshold=0.7, model=evaluator, include_reason=True)

    for item in queries:
        q_text = item['query']
        expected_ans = item.get('expected_response', 'Paris is the capital of France.')
        resp, tokens, lat, ctx = client.generate_response(q_text)
        throughput = tracker.calculate_throughput(tokens, lat)
        
        results_log.append({"id": item['id'], "query": q_text, "latency": lat, "throughput": throughput})
        assert lat < 0.5
        assert throughput >= 5.0

        test_case = LLMTestCase(
            input=q_text, 
            actual_output=resp, 
            retrieval_context=ctx,
            expected_output=expected_ans
        )
        assert_test(test_case, [faithfulness, relevancy, precision, recall])

    reporter.save_markdown_report(results_log)
    assert Path('performance_report.md').exists()