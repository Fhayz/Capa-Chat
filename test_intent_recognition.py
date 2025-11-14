import sys
import os

# Add the parent directory to the path so we can import the module
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from modules.intent_recognition import recognize_intent, get_joke

def test_recognize_intent():
    """Test cases for the recognize_intent function"""
    
    # Test greeting intents
    assert recognize_intent("hello") == "greeting"
    assert recognize_intent("Hi there!") == "greeting"
    assert recognize_intent("Good morning!") == "greeting"
    
    # Test farewell intents
    assert recognize_intent("bye") == "farewell"
    assert recognize_intent("See you later!") == "farewell"
    assert recognize_intent("I have to go now, goodbye") == "farewell"
    
    # Test joke intents
    assert recognize_intent("tell me a joke") == "joke"
    assert recognize_intent("make me laugh") == "joke"
    assert recognize_intent("do you know any funny jokes?") == "joke"
    
    # Test weather intents
    assert recognize_intent("what's the weather like?") == "weather"
    assert recognize_intent("is it going to rain today?") == "weather"
    
    # Test help intents
    assert recognize_intent("help me") == "help"
    assert recognize_intent("what can you do?") == "help"
    
    # Test time intents
    assert recognize_intent("what time is it?") == "time"
    assert recognize_intent("current time") == "time"
    
    # Test unknown intent
    assert recognize_intent("random message") == "unknown"
    
    print("All intent recognition tests passed! ✅")

def test_get_joke():
    """Test that get_joke returns a string"""
    joke = get_joke()
    assert isinstance(joke, str), "Joke should be a string"
    assert len(joke) > 0, "Joke should not be empty"
    # Check that it returns your specific joke
    assert "ocean" in joke.lower() or "waves" in joke.lower(), "Should include the ocean joke"
    print("Joke function test passed! ✅")
    print(f"Sample joke: {joke}")

if __name__ == "__main__":
    test_recognize_intent()
    test_get_joke()