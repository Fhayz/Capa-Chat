def recognize_intent(text: str) -> str:
    """
    Figure out what the user wants based on their message.
    This function looks for keywords in the text to decide the intent.
    
    Args:
        text: The cleaned input text from the user
        
    Returns:
        str: The detected intent like "greeting", "farewell", "joke", etc.
    """
    
    # Convert text to lowercase to make matching easier
    text_lower = text.lower()
    
    # List of words that mean greeting
    greeting_words = ["hi", "hello", "hey", "howdy", "greetings", "good morning", "good afternoon"]
    
    # List of words that mean farewell
    farewell_words = ["bye", "goodbye", "see you", "farewell", "later", "cya", "exit", "quit"]
    
    # List of words that mean joke request
    joke_words = ["joke", "funny", "laugh", "humor", "make me laugh"]
    
    # List of words for asking about weather
    weather_words = ["weather", "temperature", "forecast", "rain", "sunny", "hot", "cold"]
    
    # List of words for asking for help
    help_words = ["help", "what can you do", "options", "commands", "menu"]
    
    # List of words for asking about time
    time_words = ["time", "clock", "what time", "current time"]
    
    # Check for greeting intent
    for word in greeting_words:
        if word in text_lower:
            return "greeting"
    
    # Check for farewell intent
    for word in farewell_words:
        if word in text_lower:
            return "farewell"
    
    # Check for joke intent
    for word in joke_words:
        if word in text_lower:
            return "joke"
    
    # Check for weather intent
    for word in weather_words:
        if word in text_lower:
            return "weather"
    
    # Check for help intent
    for word in help_words:
        if word in text_lower:
            return "help"
    
    # Check for time intent
    for word in time_words:
        if word in text_lower:
            return "time"
    
    # If no specific intent is found, return "unknown"
    return "unknown"


def get_joke() -> str:
    """
    Returns a random joke from our collection.
    This function will be used by the response generation module.
    """
    jokes = [
        "How does the ocean say hi? It waves!",
        "Why don't scientists trust atoms? Because they make up everything!",
        "What do you call a fake noodle? An impasta!",
        "Why did the scarecrow win an award? He was outstanding in his field!",
        "How do you organize a space party? You planet!",
        "Why don't eggs tell jokes? They'd crack each other up!",
        "What do you call a sleeping dinosaur? A dino-snore!",
        "Why did the math book look so sad? Because it had too many problems!"
    ]
    
    # For now, we'll just return the first joke
    # Later, we can make it return a random one
    return jokes[0]  # This will return your ocean joke!


# Simple test function to see if our intent recognition works
def test_intent_recognition():
    """
    A simple test to check if our function works correctly.
    You can run this to see examples of how it works.
    """
    test_messages = [
        "hello there!",
        "goodbye my friend", 
        "tell me a joke",
        "what's the weather like?",
        "can you help me?",
        "what time is it?",
        "how are you doing today?"
    ]
    
    print("Testing intent recognition:")
    print("-" * 30)
    
    for message in test_messages:
        intent = recognize_intent(message)
        print(f"Message: '{message}'")
        print(f"Detected intent: '{intent}'")
        
        # If it's a joke intent, show the joke too
        if intent == "joke":
            print(f"Joke: '{get_joke()}'")
        print()


# This part runs only if we run this file directly
if __name__ == "__main__":
    # Run the test when this file is executed
    test_intent_recognition()
    
    # Also let the user try it out
    print("\nYou can test the intent recognition yourself!")
    print("Type a message and see what intent is detected.")
    print("Type 'quit' to exit.")
    print()
    
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["quit", "exit", "bye"]:
            print("Goodbye!")
            break
        
        intent = recognize_intent(user_input)
        print(f"Detected intent: {intent}")
        
        # If they want a joke, tell them one!
        if intent == "joke":
            print(f"Here's a joke for you: {get_joke()}")
        print()