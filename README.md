# RAG Performance & Security Evaluation Benchmarking Engine

A robust, modular testing and benchmarking ecosystem designed to evaluate Retrieval-Augmented Generation (RAG) pipelines for latency, throughput, faithfulness, answer relevancy, and bias.

## Core Capabilities
* **Automated Evaluation Pipeline:** End-to-end orchestration connecting test datasets, model inference, and metric validation.
* **LLM Guardrails Integration:** Powered by DeepEval metrics (Faithfulness, Relevancy, Bias) backed by high-speed Groq inference.
* **Cognitive Resonance Scoring:** Analyzes lexical overlap and structural pacing to ensure generated responses match semantic intent.
* **Data-Driven Reporting:** Automatically compiles test runs into clean, actionable Markdown performance reports (`performance_report.md`).

## Tech Stack
* **Language:** Python
* **Testing Framework:** `pytest`
* **Evaluation & Metrics:** `DeepEval`, OpenAI / Groq API integrations
* **Automation & CI/CD:** Git, GitHub Actions

## Getting Started
1. Install dependencies:
   ```bash
   pip install -r requirements.txt