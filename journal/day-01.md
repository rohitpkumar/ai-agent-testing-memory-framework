# Day 01 - First LLM API Call

## Date

24 June 2026

---

## Objective

Set up the local AI development environment and make the first successful LLM API call using the OpenAI Python SDK.

---

## What We Built

### Environment Setup

* Fixed broken Python alias configuration.
* Verified Python installation and version.
* Created a project-specific virtual environment (`.venv`).
* Activated and verified the virtual environment.
* Installed the OpenAI Python SDK.

### First AI Application

Created a simple Python script:

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

response = client.responses.create(
    model="gpt-4.1-mini",
    input="Say hello to Rohit in one short sentence."
)

print(response.output_text)
```

Successfully executed the script and received a response from the model.

### Prompt Experiment

Prompt 1:

```
Say hello to Rohit in one short sentence.
```

Response:

```
Hello, Rohit!
```

Prompt 2:

```
You are an AI career coach.
Give Rohit one AI career tip in one sentence.
```

Response:

```
Rohit, focus on building a strong foundation in machine learning algorithms and practical experience by working on real-world AI projects to stand out in the field.
```

---

## What We Learned

### Python Environment Management

* How Python aliases can break command execution.
* Difference between system Python and virtual environments.
* How to create and activate a virtual environment.

### OpenAI SDK Basics

* Installed and configured the OpenAI Python SDK.
* Used environment variables instead of hardcoding API keys.
* Connected a Python application to an LLM.

### Core AI Concepts (Observed Practically)

* A prompt is an instruction given to an LLM.
* Different prompts produce different outputs.
* LLMs generate responses based on provided instructions.
* AI applications are built on the simple flow:

```
Prompt
  ↓
Model
  ↓
Response
```

### AI QA Perspective

Traditional Software Testing:

```
Input
 ↓
Expected Exact Output
```

Example:

```
2 + 2 = 4
```

AI Testing:

```
Prompt
 ↓
Generated Response
```

Validation focuses on:

* Relevance
* Correctness
* Helpfulness
* Following instructions

rather than exact string matching.

---

## Commands Learned

### Git & Project Setup

```bash
git clone
git status
git add .
git commit
git push
```

### File & Directory Operations

```bash
pwd
ls
ls -la
mkdir
touch
cat
```

### Python Environment

```bash
which python3
python3 --version

python3 -m venv .venv

source .venv/bin/activate

pip install openai

pip show openai
```

### Environment Variables

```bash
export OPENAI_API_KEY="YOUR_KEY"

echo $OPENAI_API_KEY
```

### Debugging

```bash
alias

unalias python3

cat ~/.zshrc

cat ~/.zprofile
```

---

## Key Takeaway

Today was the first successful interaction with an LLM from code.

I can now confidently say that I have:

* Set up a Python AI development environment.
* Installed and used the OpenAI SDK.
* Managed API keys securely.
* Executed LLM API calls.
* Observed how prompt changes affect model responses.

This is the foundation for future work involving:

* AI Agents
* RAG
* Memory Systems
* Prompt Evaluations
* AI Testing Frameworks
