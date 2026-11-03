# RAG Performance & Cognitive Resonance Report
*Generated on: 2026-11-03 19:37:38 UTC*

## Executive Summary
* **Total Evaluation Queries:** 2
* **Passed Compliance:** 2/2
* **Average P95 Latency:** 150.0 ms
* **Average Cognitive Resonance:** 0.88 / 1.00

## Detailed Execution Log

| Query ID | Latency (ms) | Faithfulness | Relevancy | Resonance Score | Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Q-201 | 150.0 | 0.85 | 0.85 | 0.88 | **PASS** |
| Q-202 | 150.0 | 0.85 | 0.85 | 0.88 | **PASS** |

## Architectural Notes
* **Resonance Integration:** Scored using lexical overlap and structural pacing metrics (`src/resonance.py`).
* **Pacing Protection:** Rate-limit controls successfully avoided throttling during bulk execution.
