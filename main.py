# main.py

from modules.input_processing import clean_input
from modules.intent_recognition import recognize_intent
from modules.response_generation import generate_response

def main():
    print("Welcome to the Chatbot! Type 'exit' to quit.\n")
    while True:
        user_input = input("You: ")

        if user_input.lower().strip() in ["exit", "quit"]:
            print("Bot: Goodbye!")
            break

        # Step 1: Clean/process input
        cleaned = clean_input(user_input)

        # Step 2: Recognize intent
        intent = recognize_intent(cleaned)

        # Step 3: Generate response
        bot_reply = generate_response(intent)

        print(f"Bot: {bot_reply}")

if __name__ == "__main__":
    main()
