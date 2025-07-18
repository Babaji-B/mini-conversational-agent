# agent.py
"""
Main conversational loop for our agent.
Accepts user input, identifies intent, extracts entities, calls tools, and manages memory.
Supports multi-turn handling with last intent tracking.
"""

from modules import tools, intents
from modules.memory import Memory

def main():
    print("Agent: Hi! I am your mini assistant. How can I help you today?")
    memory = Memory()
    last_intent = None  # For multi-turn context tracking

    while True:
        user_input = input("\nYou: ")

        if user_input.lower() in ["exit", "quit", "bye"]:
            print("Agent: Goodbye! Have a nice day.")
            break

        # Check for user name and store
        user_name = intents.extract_name(user_input)
        if user_name:
            memory.update("user_name", user_name)
            print(f"Agent: Hi {user_name}! How can I help you today?")
            continue

        # Check if user is asking for their name
        if intents.is_ask_name(user_input):
            name = memory.get("user_name")
            if name:
                print(f"Agent: Your name is {name}!")
            else:
                print("Agent: I don't know your name yet. Can you please tell me?")
            continue

        # Multi-turn handling: if last intent was get_weather and user now gives city
        if last_intent == "get_weather":
            city = intents.extract_city(user_input)
            if not city:
                city = user_input.strip()  # Assume user typed only the city name
            if city:
                memory.update("user_city", city)
                response = tools.get_weather(city)
                print(f"Agent: {response}")
                last_intent = None
                
            else:
                print("Agent: I couldn't detect the city, could you please repeat?")
            continue

        # Identify intent
        intent = intents.parse_intent(user_input)

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
                last_intent = "get_weather"  # Set context for next user input

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
        
        elif intents.is_ask_city(user_input):
            city = memory.get("user_city")
            if city:
                print(f"Agent: Your city is {city}.")
            else:
                print("Agent: I don't know your city yet. Could you please tell me your city?")

        else:
            print("Agent: Sorry, I didn't understand that. I can provide weather updates, set reminders, and share news. Try asking something like 'What’s the weather in Delhi?' or 'Remind me to call mom at 7 PM'.")

if __name__ == "__main__":
    main()
