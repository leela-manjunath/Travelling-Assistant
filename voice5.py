import speech_recognition as sr
import pyttsx3
import pandas as pd
import re

# Initialize text-to-speech engine
engine = pyttsx3.init()

# Optionally, set properties like voice and rate
engine.setProperty('rate', 180)  # Adjust speaking rate (words per minute)

voices = engine.getProperty('voices')

# Look for an Indian English voice
for voice in voices:
    print(f"Voice: {voice.name}, ID: {voice.id}, Lang: {voice.languages}")

# Optionally, set an Indian English voice (modify as per your system's voices)
for voice in voices:
    if "Indian" in voice.name or "Hindi" in voice.name:
        engine.setProperty('voice', voice.id)
        break



# Load CSV files into DataFrames
hotels_df = pd.read_csv('hotels.csv')
hospitals_df = pd.read_csv('hospitals.csv')
tourist_spots_df = pd.read_csv('tourist_spots.csv')
# temples_df = pd.read_csv('temples.csv')
churches_df = pd.read_csv('churches.csv')

# Function to get data based on category and city
def get_data(category_df, city_name):
    city_data = category_df[category_df['City'].str.lower() == city_name.lower()]
    return city_data.iloc[:, 1].tolist()  # Assumes the second column has the names

# Function to speak the output
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to capture voice input
def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)  # Adjust for ambient noise
        audio = recognizer.listen(source)

    try:
        query = recognizer.recognize_google(audio)
        print(f"You said: {query}")
        return query.lower()
    except sr.UnknownValueError:
        speak("Sorry, I did not understand that.")
        return None
    except sr.RequestError:
        speak("Sorry, I'm unable to connect to the speech recognition service.")
        return None

# Function to detect city and intent from user's query
def process_query(query):
    # Define categories and their keywords
    categories = {
        'hotel': ['hotel', 'hotels', 'accommodation'],
        'hospital': ['hospital', 'hospitals', 'medical'],
        'tourist_spot': ['tourist spot', 'tourist spots', 'places to visit', 'attraction', 'attractions'],
        # 'temple': ['temple', 'temples'],
        'church': ['church', 'churches']
    }

    intent = None
    category = None
    city = None

    # Identify category
    for key, keywords in categories.items():
        for word in keywords:
            if word in query:
                intent = key
                category = key  # For simplicity, category name matches intent
                break
        if intent:
            break

    if not intent:
        return None, None

    # Extract the city name using regex
    # This regex looks for 'in [CityName]' or 'at [CityName]'
    match = re.search(r'in\s+([A-Za-z\s]+)|at\s+([A-Za-z\s]+)', query)
    if match:
        city = match.group(1) if match.group(1) else match.group(2)
        city = city.strip()
    else:
        # Optionally, implement more sophisticated city extraction
        # For now, return None if city is not found
        return intent, None

    return intent, city

# Main function to run the voice assistant
def voice_assistant():
    speak("Hi, Welcome to TravelGuru. How can I assist you today?")

    while True:
        query = listen()
        if query:
            # Check if the user wants to exit
            if any(exit_word in query for exit_word in ["exit", "bye", "ok bye", "quit", "goodbye"]):
                speak("Thank you for using TravelGuru. Have a nice day!")
                print("Exiting Voice Assistant.")
                break

            intent, city = process_query(query)

            if intent and city:
                # Fetch data based on intent and city
                if intent == 'hotel':
                    data = get_data(hotels_df, city)
                    category_name = "hotels"
                elif intent == 'hospital':
                    data = get_data(hospitals_df, city)
                    category_name = "hospitals"
                elif intent == 'tourist_spot':
                    data = get_data(tourist_spots_df, city)
                    category_name = "tourist spots"
                # elif intent == 'temple':
                #     data = get_data(temples_df, city)
                #     category_name = "temples"
                elif intent == 'church':
                    data = get_data(churches_df, city)
                    category_name = "churches"
                else:
                    data = []
                    category_name = "unknown category"

                if data:
                    # Limit the number of items to prevent overly long responses
                    limited_data = data[:10]  # Adjust the number as needed
                    response = f"Here are some {category_name} in {city}: " + ", ".join(limited_data)
                else:
                    response = f"Sorry, I couldn't find any {category_name} in {city}."

                print(response)
                speak(response)
            else:
                speak("Sorry, I didn't understand your request. Please try again.")
        else:
            # Optional: Prompt the user again or continue silently
            pass

# Entry point
if __name__ == "__main__":
    voice_assistant()
