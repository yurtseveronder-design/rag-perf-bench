# RAG Performance & Cognitive Resonance Report
*Generated on: 2026-11-03 19:06:27 UTC*

## Executive Summary
* **Total Evaluation Queries:** 1
* **Passed Compliance:** 0/1
* **Average P95 Latency:** 0.0 ms
* **Average Cognitive Resonance:** 0.0 / 1.00

## Detailed Execution Log

| Query ID | Latency (ms) | Faithfulness | Relevancy | Resonance Score | Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| retrieval_01 | 0.15 | 0.9 | 0.9 | 0.85 | **PASS** |

## Architectural Notes
* **Resonance Integration:** Scored using lexical overlap and structural pacing metrics (`src/resonance.py`).
* **Pacing Protection:** Rate-limit controls successfully avoided throttling during bulk execution.
