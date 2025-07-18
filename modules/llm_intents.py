# modules/llm_intents.py
"""
LLM-based intent extraction and direct handling of jokes and calculations for our agent.
Uses Groq LLM to parse user intent and generate responses where applicable.
"""

from dotenv import load_dotenv
import os

load_dotenv()

from groq import Groq

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def parse_intent_llm(user_input):
    """
    Uses LLM to parse and return the intent for user input.
    If the intent is 'tell_joke' or 'calculate', returns the generated response directly.
    Returns:
        tuple: (intent, response or None)
    """
    prompt = f"""
You are an assistant for a CLI conversational agent.

Your tasks:
- Identify the user's intent from:
  'greeting', 'get_weather', 'set_reminder', 'get_news',
  'ask_name', 'ask_city', 'tell_joke', 'calculate', 'unknown'.
- If intent is 'tell_joke' or 'calculate', respond with the answer directly (a joke or the calculated result) in the format:
  intent: <your response>
- Otherwise, ONLY reply with the intent keyword and nothing else.

User input: "{user_input}"
"""
    response = client.chat.completions.create(
        model="llama3-8b-8192",
        messages=[{"role": "system", "content": prompt}],
    )
    content = response.choices[0].message.content.strip()

    allowed_intents = [
        'greeting', 'get_weather', 'set_reminder', 'get_news',
        'ask_name', 'ask_city', 'tell_joke', 'calculate', 'unknown'
    ]

    # New robust parsing
    split_content = content.split(":", 1)
    potential_intent = split_content[0].strip().lower()

    if potential_intent in allowed_intents and len(split_content) > 1:
        # 'intent: generated text'
        return potential_intent, split_content[1].strip()
    elif content.lower() in allowed_intents:
        # 'intent'
        return content.lower(), None
    else:
        # fallback using keywords in user input
        if "joke" in user_input.lower():
            return "tell_joke", content
        elif any(word in user_input.lower() for word in ["calculate", "what is", "solve", "+", "-", "*", "/"]):
            return "calculate", content
        else:
            return "unknown", None