# import speech_recognition as sr
# import pyttsx3

# # Initialize the pyttsx3 engine
# engine = pyttsx3.init()

# # Set the speaking speed (increase to make it faster)
# engine.setProperty('rate', 180)  # Default is around 200, lowering makes it slower, raising makes it faster

# def speak(text):
#     """Convert text to speech using pyttsx3."""
#     engine.say(text)
#     engine.runAndWait()

# def listen():
#     """Listen for user input and convert speech to text."""
#     recognizer = sr.Recognizer()
#     with sr.Microphone() as source:
#         print("Listening...")
#         recognizer.adjust_for_ambient_noise(source)  # Adjusts for background noise
#         audio = recognizer.listen(source)
    
#     try:
#         query = recognizer.recognize_google(audio)
#         print(f"You said: {query}")
#         return query.lower()
#     except sr.UnknownValueError:
#         speak("Sorry, I didn't catch that. Please say that again.")
#         return None
#     except sr.RequestError:
#         speak("Sorry, there seems to be an issue with the speech recognition service.")
#         return None

# # Data structure for cities and their respective categories
# city_data = {
#     "Guntur": {
#         "hotels": [
#             "Hotel V Royal Park", "The Capital Hotel", "Geetha Regency", 
#             "Hotel Siddhartha", "Hotel Swagatam", "Hotel Vajra", 
#             "The Taj Gateway", "Hotel Sindoori", "Hotel Ilapuram", "Hotel Akshaya"
#         ],
#         "hospitals": [
#             "Ramesh Hospitals", "Amaravathi Hospitals", "Siddhartha Hospitals", 
#             "Katuri Medical College", "Homi Bhabha Cancer Hospital", "Care Hospitals", 
#             "NRI General Hospital", "St. Joseph’s General Hospital", "Apollo Hospitals", "Manipal Hospitals"
#         ],
#         "tourist_spots": [
#             "Kondaveedu Fort", "Uppalapadu Bird Sanctuary", "Amaravati Stupa", 
#             "Kotappakonda", "Gundala Matha Shrine", "Suryalanka Beach", 
#             "Ethipothala Falls", "Mangalagiri Temple", "Chandavaram Buddhist Site", "Kolleru Lake"
#         ],
#         "temples": [
#             "Sri Panakala Lakshmi Narasimha Swamy Temple", "Kotappakonda Temple", 
#             "Amareswara Swamy Temple", "Shivalayam Temple", "ISKCON Guntur", 
#             "Pedda Anjaneya Swamy Temple", "Durga Temple", "Sri Uma Maheswara Temple", "Ramalingeswara Swamy Temple", "Venugopala Swamy Temple"
#         ],
#         "churches": [
#             "St. Mary’s Church", "Bethesda Church", "Sacred Heart Church", 
#             "Zion Church", "Immanuel Church", "Bethel Church", 
#             "Calvary Baptist Church", "St. Luke’s Church", "Holy Cross Church", "Faith Tabernacle Church"
#         ]
#     },
#     "Vijayawada": {
#         "hotels": [
#             "Hotel Park Iris", "Hotel DV Manor", "Hotel Midcity", "Fortune Murali Park", "The Gateway Hotel", 
#             "Hotel Southern Grand", "Novotel Vijayawada Varun", "Treebo Trend", "Haritha Berm Park", "Minerva Grand"
#         ],
#         "hospitals": [
#             "Ramesh Hospitals", "Andhra Hospitals", "Manipal Hospitals", 
#             "Aayush Hospitals", "Sentini Hospitals", "Trust Hospitals", 
#             "Sunshine Hospital", "Susruta Hospital", "Care Hospitals", "Vijaya Super Speciality Hospital"
#         ],
#         "tourist_spots": [
#             "Prakasam Barrage", "Kanaka Durga Temple", "Bhavani Island", 
#             "Undavalli Caves", "Rajiv Gandhi Park", "Mangalagiri Hills", 
#             "VMC Disney Land", "Besant Road", "Victoria Museum", "Gunadala Matha Shrine"
#         ],
#         "temples": [
#             "Kanaka Durga Temple", "Sri Subramanya Swamy Temple", 
#             "Mangalagiri Temple", "ISKCON Vijayawada", "Gunadala Mary Matha Shrine", 
#             "Sri Ramalingeswara Temple", "Sri Nandikeswara Temple", "Paritala Anjaneya Swamy Temple", "Sri Lakshmi Narasimha Swamy Temple", "Shivalayam Temple"
#         ],
#         "churches": [
#             "St. Peter's Cathedral", "Christ Lutheran Church", "St. Paul's Church", 
#             "Centenary Baptist Church", "Zion Church", "Methodist Church", 
#             "Bethel Church", "Immanuel Church", "Holy Spirit Church", "Mount Zion Church"
#         ]
#     }
# }

# # Function to search for information based on city and category
# def search_city_info(city, category):
#     if city in city_data and category in city_data[city]:
#         results = city_data[city][category]
#         speak(f"Here are some {category} in {city}: {', '.join(results)}")
#     else:
#         speak(f"Sorry, I don't have data for {category} in {city}.")

# # Function to process user query
# def handle_query(query):
#     # Extract the city and category from the query
#     for city in city_data.keys():
#         if city.lower() in query.lower():
#             if "hotel" in query.lower():
#                 search_city_info(city, "hotels")
#             elif "hospital" in query.lower():
#                 search_city_info(city, "hospitals")
#             elif "tourist" in query.lower() or "spot" in query.lower():
#                 search_city_info(city, "tourist_spots")
#             elif "temple" in query.lower():
#                 search_city_info(city, "temples")
#             elif "church" in query.lower():
#                 search_city_info(city, "churches")
#             else:
#                 speak(f"Sorry, I didn't understand what you are looking for in {city}.")
#             return
#     speak("Sorry, I couldn't find the city or category you asked for.")


# # def ask_for_details(state):
# #     """Ask the user what details they want (restaurants, tourist places, or famous food)."""
# #     speak(f"What would you like to know about {state}? Say 1 for restaurants, 2 for tourist places, or 3 for famous food.")
# #     choice = listen()

# #     # If listen() returns None, prompt the user again
# #     if choice is None:
# #         speak("I didn't understand that. Please say 1 for restaurants, 2 for tourist places, or 3 for famous food.")
# #         return ask_for_details(state)  # Ask again
    
# #     if "restaurants" in choice or "1" in choice:
# #         return 'restaurants'
# #     elif "tourist places" in choice or "2" in choice:
# #         return 'tourist_places'
# #     elif "famous food" in choice or "3" in choice:
# #         return 'famous_food'
# #     else:
# #         speak("Invalid choice, defaulting to tourist places.")
# #         return 'tourist_places'

# # def provide_info(state, detail):
# #     """Provide the requested information about the state."""
# #     info = states_info.get(state, {}).get(detail, "No information available.")
# #     speak(info)

# def run_voice_assistant():
#     speak("Hi,Welcome to TravelGuru where you can find information about destinations, bookings, and travel tips.")
#     while True:
#         # Ask for the state and provide its history
        
#         # state = ask_state()
#         if state:
#             speak(f"Here is a brief history of {state}: {states_info[state]['history']}")
            
#             # Ask what they want to know about
#             detail = ask_for_details(state)
            
#             # Provide the relevant information
#             provide_info(state, detail)

#         # Check if user wants to exit
#         speak("Do you want to ask about another state? Say 'exit' to stop.")
#         if "exit" in listen():
#             speak("Have a nice day,Bye!")
#             break
# if __name__ == "__main__":
#     run_voice_assistant() 