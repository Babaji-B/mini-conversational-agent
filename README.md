# Mini Conversational Agent

## Overview

A simple Python CLI conversational agent that:

* Accepts natural language input
* Identifies intent using regex
* Calls mock functions (weather, reminder, news)
* Stores user name and city in memory
* Returns clean chatbot responses

---

## Folder Structure

```bash
mini-conversational-agent/
├── agent.py               # Main conversational CLI
└── modules/
    ├── tools.py           # Mock tool functions
    ├── intents.py         # Regex-based intent detection
    └── memory.py          # Simple in-memory store
```

---

## Setup

```bash
# Create and activate virtual environment
python -m venv venv
venv\Scripts\activate  # On Windows
source venv/bin/activate  # On Mac/Linux

# Install dependencies
pip install regex
```

---

## Usage

```bash
python agent.py
```

### Example Inputs

* "Hi, I am Babaji"
* "What's the weather in Hyderabad?"
* "Remind me to call mom at 7 PM"
* "Tell me news about AI"
* Type `exit`, `quit`, or `bye` to end the session.

---

## Notes

✅ Uses **local mock functions** (no external APIs).
✅ Uses **regex for intent detection** (no LLM yet).
✅ Modular and ready for LLM upgrades in `llm_intents.py` next.


---

## LLM Extension

This project now also includes **Groq LLM-based intent detection** for advanced use:

✅ Handles jokes and basic calculations directly via LLM  
✅ Uses `llm_intents.py` for LLM-based parsing  
✅ Uses `llm_agent.py` for CLI interaction with LLM support

---

## Updated Folder Structure

```bash
mini-conversational-agent/
├── agent.py               # Main conversational CLI (regex-based)
├── llm_agent.py           # LLM-powered CLI conversational agent
└── modules/
    ├── tools.py           # Mock tool functions
    ├── intents.py         # Regex-based intent detection
    ├── llm_intents.py     # LLM-based intent detection + direct LLM responses
    └── memory.py          # Simple in-memory store
