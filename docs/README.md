# APHASIA COMMUNICATION ASSISTANT

## Overview
A multimodal communication assistant that accepts text and images, infers simple intent, and produces 2–3 clear sentence suggestions for aphasic users.

## Project Structure
```
aphasia-assist/
│
├── app.py                     # Gradio app entry point
│
├── core/
│   ├── __init__.py
│   ├── prompts.py             # System prompts and templates
│   ├── tools.py               # Tool schemas and tool-calling logic
│   ├── intent.py              # Intent detection and guardrails
│   └── multimodal.py          # Image / audio preprocessing
│
├── services/
│   ├── __init__.py
│   └── llm_client.py          # OpenAI client wrapper
│
├── experiments/
│   └── prompt_playground.ipynb  # Notebook for testing prompts
│
├── requirements.txt
└── README.md
```

### Why this structure works

* `app.py`
  Pure UI and wiring. No logic clutter.

* `core/`
  Where your thinking lives. Prompts, tools, rules.

* `services/`
  Anything external. LLM APIs now. Speech later.

* `experiments/`
  Safe place to break things and learn.
---