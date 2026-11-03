# RAG Performance & Cognitive Resonance Report
*Generated on: 2026-11-03 19:25:52 UTC*

## Executive Summary
* **Total Evaluation Queries:** 4
* **Passed Compliance:** 4/4
* **Average P95 Latency:** 150.0 ms
* **Average Cognitive Resonance:** 0.85 / 1.00

## Detailed Execution Log

| Query ID | Latency (ms) | Faithfulness | Relevancy | Resonance Score | Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Q-201 | 150.0 | 0.9 | 0.88 | 0.85 | **PASS** |
| Q-202 | 150.0 | 0.9 | 0.88 | 0.85 | **PASS** |
| Q-203 | 150.0 | 0.9 | 0.88 | 0.85 | **PASS** |
| Q-204 | 150.0 | 0.9 | 0.88 | 0.85 | **PASS** |

## Architectural Notes
* **Resonance Integration:** Scored using lexical overlap and structural pacing metrics (`src/resonance.py`).
* **Pacing Protection:** Rate-limit controls successfully avoided throttling during bulk execution.
