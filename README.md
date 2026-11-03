# RAG Performance & Resonance Bench

A lightweight, practical testing tool for evaluating RAG (Retrieval-Augmented Generation) systems. It measures core retrieval metrics while also checking how naturally and accurately AI responses align with human intent.

## What It Solves
When building RAG systems, checking strict factual correctness isn't enough. We also need to know if the model sounds natural, stays on track, and handles pacing cleanly without hitting API rate limits.

## Core Features
* **3-Metric Core Evaluation:** Focuses on Faithfulness, Relevancy, and Bias to keep testing fast and reliable.
* **Cognitive Resonance Analyzer (`src/resonance.py`):** Goes beyond cold numbers to check tone consistency and how organically the response matches human intent.
* **API Rate-Limit Protection:** Built with intentional pacing to ensure smooth testing runs without breaking third-party API limits.
* **Automated CI/CD:** Runs tests automatically on every push via GitHub Actions.

## Project Structure
* `src/`: Core logic including metrics and the resonance analyzer.
* `datasets/`: Sample data sets for testing queries.
* `tests/`: Streamlined test suite for continuous validation.
* `.github/workflows/`: Automated CI pipeline configuration.

## Quick Start
1. Clone the repository and install dependencies.
2. Run the test suite locally:
   ```bash
   python -m pytest -v
