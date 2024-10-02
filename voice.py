import speech_recognition as sr
import pyttsx3

# Initialize the speech engine
engine = pyttsx3.init()

def speak(text):
    """Convert text to speech."""
    engine.say(text)
    engine.runAndWait()

def listen():
    """Listen for user input and convert speech to text."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)  # Adjusts for background noise
        audio = recognizer.listen(source)
    
    try:
        query = recognizer.recognize_google(audio)
        print(f"You said: {query}")
        return query.lower()
    except sr.UnknownValueError:
        speak("Sorry, I didn't catch that. Please say that again.")
        return None
    except sr.RequestError:
        speak("Sorry, there seems to be an issue with the speech recognition service.")
        return None

def handle_query(query):
    """Handle the user's query and respond accordingly."""
    if query:
        if "about the website" in query:
            speak("This is a travel website where you can find information about destinations, bookings, and travel tips.")
        elif "best places to visit" in query:
            speak("Some of the best places to visit are Paris, Bali, New York, and Tokyo.")
        elif "booking details" in query:
            speak("You can book flights, hotels, and rental cars through our website's booking section.")
        else:
            speak("Sorry, I don't have information on that right now.")
    else:
        speak("I couldn't understand your question.")

if __name__ == "__main__":
    while True:
        speak("How can I assist you?")
        user_query = listen()
        if user_query:
            handle_query(user_query)
        if "exit" in user_query or "quit" in user_query:
            speak("Goodbye!")
            break
