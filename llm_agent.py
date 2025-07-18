# LLM_agent.py
"""
Conversational agent using LLM-based intent detection and direct handling for jokes/calculations.
"""

from modules import tools, llm_intents
from modules.memory import Memory

def main():
    print("Agent: Hi! I am your LLM-powered assistant. How can I help you today?")
    memory = Memory()

    from modules import intents  # For regex-based entity extraction

    while True:
        user_input = input("\nYou: ")

        if user_input.lower() in ["exit", "quit", "bye"]:
            print("Agent: Goodbye! Have a nice day.")
            break

        # Extract user name if mentioned
        user_name = intents.extract_name(user_input)
        if user_name:
            memory.update("user_name", user_name)
            print(f"Agent: Hi {user_name}! How can I help you today?")
            continue

        # Get LLM intent and possible direct response
        intent, llm_response = llm_intents.parse_intent_llm(user_input)

        # If LLM handled joke or calculation, print and skip structured flow
        if llm_response:
            print(f"Agent: {llm_response}")
            continue

        # Structured handling for other intents
        if intent == "greeting":
            name = memory.get("user_name")
            if name:
                print(f"Agent: Hi {name}! How can I help you today?")
            else:
                print("Agent: Hello! What can I do for you today?")

        elif intent == "get_weather":
            city = intents.extract_city(user_input)
            if not city:
                city = memory.get("user_city")
            else:
                memory.update("user_city", city)

            if city:
                response = tools.get_weather(city)
                print(f"Agent: {response}")
            else:
                print("Agent: May I know which city you would like the weather update for?")

        elif intent == "set_reminder":
            text, time = intents.extract_reminder(user_input)
            if text and time:
                response = tools.set_reminder(text, time)
                print(f"Agent: {response}")
            else:
                print("Agent: Please provide both the reminder text and time (e.g., 'Remind me to call mom at 7 PM').")

        elif intent == "get_news":
            topic = intents.extract_topic(user_input)
            response = tools.get_news(topic)
            print(f"Agent: {response}")

        elif intent == "ask_name":
            name = memory.get("user_name")
            if name:
                print(f"Agent: Your name is {name}.")
            else:
                print("Agent: I don't know your name yet. Could you please tell me your name?")

        elif intent == "ask_city":
            city = memory.get("user_city")
            if city:
                print(f"Agent: Your city is {city}.")
            else:
                print("Agent: I don't know your city yet. Could you please tell me your city?")

        else:
            print("Agent: Sorry, I didn't understand that. I can provide weather updates, set reminders, and share news. Try asking something like 'What’s the weather in Delhi?' or 'Remind me to call mom at 7 PM'.")

if __name__ == "__main__":
    main()