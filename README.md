# RAG Performance & Resonance Bench

A focused benchmarking tool for evaluating the **quality and performance** of Retrieval-Augmented Generation (RAG) systems.

## What It Does

Measures how well a RAG pipeline performs across three key dimensions:
- **Performance** → Latency & Throughput
- **Quality** → Faithfulness, Answer Relevancy, and Bias (via DeepEval)
- **Cognitive Resonance** → How naturally and coherently the response aligns with the user query

## Core Features

- Cognitive Resonance Analyzer (`src/resonance.py`)
- DeepEval integration (Faithfulness, Relevancy, Bias)
- Latency and throughput tracking
- Structured Markdown performance reports
- Rate-limit aware execution
- Fully automated CI with GitHub Actions

## Project Structure