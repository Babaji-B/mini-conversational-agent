# modules/intents.py
"""
Intent and entity extraction module for our agent.
Uses regex and keyword-based parsing to identify user intents and extract relevant entities.
"""

import re

def parse_intent(user_input):
    """
    Identifies the user's intent based on their input.
    Returns:
        str: One of 'greeting', 'get_weather', 'set_reminder', 'get_news', or 'unknown'.
    """
    user_input_lower = user_input.lower()

    if any(greet in user_input_lower for greet in ["hi", "hello", "hey"]):
        return "greeting"
    elif "weather" in user_input_lower:
        return "get_weather"
    elif "remind" in user_input_lower or "reminder" in user_input_lower:
        return "set_reminder"
    elif "news" in user_input_lower:
        return "get_news"
    else:
        return "unknown"

def extract_name(user_input):
    """
    Extracts the user's name from their input if provided.
    Returns:
        str or None: Extracted name or None if not found.
    """
    match = re.search(r"(?:i am|i'm|my name is)\s+(\w+)", user_input, re.IGNORECASE)
    if match:
        return match.group(1)
    return None

def extract_city(user_input):
    """
    Extracts a city name from the user's input for weather queries.
    Supports 'in <city>', 'of <city>', and '<city> city' patterns.
    Returns:
        str or None: City name or None if not found.
    """
    # Pattern: in <city>
    match = re.search(r"in\s+([A-Za-z\s]+)", user_input, re.IGNORECASE)
    if match:
        return match.group(1).strip()
    
    # Pattern: of <city>
    match = re.search(r"of\s+([A-Za-z\s]+)", user_input, re.IGNORECASE)
    if match:
        return match.group(1).strip()
    
    # Pattern: <city> city
    match = re.search(r"([A-Za-z\s]+)\s+city", user_input, re.IGNORECASE)
    if match:
        return match.group(1).strip()
    
    return None


def extract_reminder(user_input):
    """
    Extracts reminder text and time from the user's input.
    Returns:
        tuple (text, time) or (None, None) if not found.
    """
    text_match = re.search(r"remind me to\s+(.*?)\s+(?:at|on)\s+", user_input, re.IGNORECASE)
    time_match = re.search(r"(?:at|on)\s+(\d{1,2}\s*(?:am|pm)?)", user_input, re.IGNORECASE)

    text = text_match.group(1).strip() if text_match else None
    time = time_match.group(1).strip() if time_match else None

    return text, time

def extract_topic(user_input):
    """
    Extracts a topic for news queries from the user's input.
    Returns:
        str: Extracted topic or 'general' if none is found.
    """
    match = re.search(r"news(?: about| on)?\s+([A-Za-z\s]+)", user_input, re.IGNORECASE)
    if match:
        return match.group(1).strip()
    return "general"



def is_ask_name(user_input):
    """
    Checks if the user is asking for their stored name.
    Returns True if detected, else False.
    """
    patterns = [
        r"\bwhat\s+is\s+my\s+name\b",
        r"\btell\s+me\s+my\s+name\b",
        r"\bdo\s+you\s+know\s+my\s+name\b",
        r"\bwho\s+am\s+i\b"
    ]
    for pattern in patterns:
        if re.search(pattern, user_input, re.IGNORECASE):
            return True
    return False


def is_ask_city(user_input):
    """
    Checks if the user is asking for their stored city.
    Returns True if detected, else False.
    """
    patterns = [
        r"\bwhat\s+is\s+my\s+city\b",
        r"\btell\s+me\s+my\s+city\b",
        r"\bdo\s+you\s+know\s+my\s+city\b",
        r"\babout\s+my\s+city\b",
        r"\bcan\s+you\s+tell\s+me\s+about\s+my\s+city\b"
    ]
    for pattern in patterns:
        if re.search(pattern, user_input, re.IGNORECASE):
            return True
    return False

