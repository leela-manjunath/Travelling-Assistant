import speech_recognition as sr
from gtts import gTTS
import os
from playsound import playsound

# Sample state data (add more as needed)
states_info = {
    'andhra pradesh': {
        'capital': 'Amaravati',
        'history': 'Andhra Pradesh was formed in 1953 and was one of the first states to be formed on a linguistic basis.',
        'restaurants': 'Famous restaurants include Paradise, Rayalaseema Ruchulu.',
        'tourist_places': 'Famous tourist places include Tirupati, Araku Valley, and Vishakhapatnam.',
        'famous_food': 'Andhra is famous for biryani, Gongura, and Pesarattu.'
    },
    'karnataka': {
        'capital': 'Bangalore',
        'history': 'Karnataka was formed in 1956 and is known for its rich cultural heritage.',
        'restaurants': 'Famous restaurants include Mavalli Tiffin Room, Karavalli.',
        'tourist_places': 'Famous tourist places include Coorg, Mysore Palace, and Hampi.',
        'famous_food': 'Karnataka is famous for masala dosa, idli, and Bisi Bele Bath.'
    },
    # Add more states...
}

def speak(text):
    """Convert text to speech in English using gTTS."""
    tts = gTTS(text=text, lang='en')
    tts.save("response.mp3")
    playsound("response.mp3")
    os.remove("response.mp3")

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

def ask_state():
    """Ask the user to select a state and provide basic info."""
    speak("Which state would you like to visit? You can say Andhra Pradesh, Karnataka, Kerala, etc.")
    state = listen()
    if state in states_info:
        return state
    else:
        speak("Sorry, I don't have information on that state. Please choose a different state.")
        return ask_state()

def ask_for_details(state):
    """Ask the user what details they want (restaurants, tourist places, or famous food)."""
    speak(f"What would you like to know about {state}? Say 1 for restaurants, 2 for tourist places, or 3 for famous food.")
    choice = listen()

    # If listen() returns None, prompt the user again
    if choice is None:
        speak("I didn't understand that. Please say 1 for restaurants, 2 for tourist places, or 3 for famous food.")
        return ask_for_details(state)  # Ask again
    
    if "restaurants" in choice or "1" in choice:
        return 'restaurants'
    elif "tourist places" in choice or "2" in choice:
        return 'tourist_places'
    elif "famous food" in choice or "3" in choice:
        return 'famous_food'
    else:
        speak("Invalid choice, defaulting to tourist places.")
        return 'tourist_places'


def provide_info(state, detail):
    """Provide the requested information about the state."""
    info = states_info.get(state, {}).get(detail, "No information available.")
    speak(info)

if __name__ == "__main__":
    while True:
        # Ask for the state and provide its history
        state = ask_state()
        if state:
            speak(f"Here is a brief history of {state}: {states_info[state]['history']}")
            
            # Ask what they want to know about
            detail = ask_for_details(state)
            
            # Provide the relevant information
            provide_info(state, detail)

        # Check if user wants to exit
        speak("Do you want to ask about another state? Say 'exit' to stop.")
        if "exit" in listen():
            speak("Goodbye!")
            break
