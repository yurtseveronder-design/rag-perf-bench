# RAG Performance & Security Evaluation Report

* **Generated on:** `2026-11-03 23:46:04 UTC`
* **Status:** `SUCCESS`

## Executive Summary
This report summarizes the automated execution of benchmark queries across latency tracking, throughput calculation, and DeepEval LLM quality guardrails (Faithfulness, Relevancy, and Bias).

## Detailed Test Metrics

| ID | Query | Latency (ms) | Throughput (tok/s) | Faithfulness | Relevancy | Resonance | Status |
|---|---|---|---|---|---|---|---|
| Q-201 | What is the capital of France and its primary landmark? | 150.0 | 160.0 | 0.9 | 0.88 | 0.85 | **PASS** |

## System Architecture Notes
* **Inference Engine:** Groq API (`https://api.groq.com/openai/v1`)
* **Evaluation Framework:** DeepEval Guardrails & Pytest Test Runner
* **Security:** Environment variable isolation (`GROQ_API_KEY`)
