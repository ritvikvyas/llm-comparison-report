# LLM Comparison Report

Compare responses from different AI models side-by-side.

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Create a `.env` file with your API keys:
```
OPENAI_API_KEY=your_key_here
ANTHROPIC_API_KEY=your_key_here
```

## Usage

Run the comparison:
```bash
python main.py
```

This will compare responses from GPT-3.5 and Claude, then save a report to `llm_comparison_report.md`.

## What it does

- Sends the same prompt to multiple AI models
- Shows responses in the terminal
- Generates a markdown report for easy comparison

