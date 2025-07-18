# modules/tools.py
"""
Mock tool functions for our agent.
These simulate API/tool calls.
"""

def get_weather(city):
    """
    Simulates fetching weather information for a given city.
    Input:
        city (str): The name of the city for which the weather is requested.
    Returns:
        str: A static weather info for the city.
    """
    return f"The weather in {city} is 72°F and sunny."


def set_reminder(text, time):
    """
    Simulates setting a reminder with provided text and time.
    Input:
        text (str): The content of the reminder (e.g., 'call mom').
        time (str): The time for the reminder (e.g., '7 PM').
    Returns:
        str: A confirmation string stating the reminder has been set.
    """
    return f"Reminder set: '{text}' at {time}."


def get_news(topic):
    """
    Simulates fetching top news for a given topic.
    Input:
        topic (str): The news topic requested by the user (e.g., 'AI').
    Returns:
        str: A news string containing a static headline.
    """
    return f"Top news in {topic}: 'AI is transforming the world!'"

