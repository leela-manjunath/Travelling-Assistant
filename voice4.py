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

# def run_voice_assistant():
#     speak("Hi, Welcome to TravelGuru where you can find information about Guntur and Vijayawada.")
#     while True:
#         speak("How can I assist you today?")
#         query = listen()
#         if query:
#             handle_query(query)
#         else:
#             speak("Please try again.")
        
#         speak("Do you want to ask about another category or city? Say 'exit' to stop.")
#         query = listen()
#         if query and "exit" in query:
#             speak("Thank you for using TravelGuru. Have a nice day!")
#             break

# if __name__ == "__main__":
#     run_voice_assistant()



import speech_recognition as sr
import pyttsx3

# Initialize the pyttsx3 engine
engine = pyttsx3.init()

# Set the speaking speed (increase to make it faster)
engine.setProperty('rate', 180)  # Default is around 200, lowering makes it slower, raising makes it faster

def speak(text):
    """Convert text to speech using pyttsx3."""
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

# Data structure for cities and their respective categories
city_data = {
    "Guntur": {
        "hotels": [
            "Hotel V Royal Park", "The Capital Hotel", "Geetha Regency", 
            "Hotel Siddhartha", "Hotel Swagatam", "Hotel Vajra", 
            "The Taj Gateway", "Hotel Sindoori", "Hotel Ilapuram", "Hotel Akshaya"
        ],
        "hospitals": [
            "Ramesh Hospitals", "Amaravathi Hospitals", "Siddhartha Hospitals", 
            "Katuri Medical College", "Homi Bhabha Cancer Hospital", "Care Hospitals", 
            "NRI General Hospital", "St. Joseph’s General Hospital", "Apollo Hospitals", "Manipal Hospitals"
        ],
        "tourist_spots": [
            "Kondaveedu Fort", "Uppalapadu Bird Sanctuary", "Amaravati Stupa", 
            "Kotappakonda", "Gundala Matha Shrine", "Suryalanka Beach", 
            "Ethipothala Falls", "Mangalagiri Temple", "Chandavaram Buddhist Site", "Kolleru Lake"
        ],
        "temples": [
            "Sri Panakala Lakshmi Narasimha Swamy Temple", "Kotappakonda Temple", 
            "Amareswara Swamy Temple", "Shivalayam Temple", "ISKCON Guntur", 
            "Pedda Anjaneya Swamy Temple", "Durga Temple", "Sri Uma Maheswara Temple", "Ramalingeswara Swamy Temple", "Venugopala Swamy Temple"
        ],
        "churches": [
            "St. Mary’s Church", "Bethesda Church", "Sacred Heart Church", 
            "Zion Church", "Immanuel Church", "Bethel Church", 
            "Calvary Baptist Church", "St. Luke’s Church", "Holy Cross Church", "Faith Tabernacle Church"
        ]
    },
    "Vijayawada": {
        "hotels": [
            "Hotel Park Iris", "Hotel DV Manor", "Hotel Midcity", "Fortune Murali Park", "The Gateway Hotel", 
            "Hotel Southern Grand", "Novotel Vijayawada Varun", "Treebo Trend", "Haritha Berm Park", "Minerva Grand"
        ],
        "hospitals": [
            "Ramesh Hospitals", "Andhra Hospitals", "Manipal Hospitals", 
            "Aayush Hospitals", "Sentini Hospitals", "Trust Hospitals", 
            "Sunshine Hospital", "Susruta Hospital", "Care Hospitals", "Vijaya Super Speciality Hospital"
        ],
        "tourist_spots": [
            "Prakasam Barrage", "Kanaka Durga Temple", "Bhavani Island", 
            "Undavalli Caves", "Rajiv Gandhi Park", "Mangalagiri Hills", 
            "VMC Disney Land", "Besant Road", "Victoria Museum", "Gunadala Matha Shrine"
        ],
        "temples": [
            "Kanaka Durga Temple", "Sri Subramanya Swamy Temple", 
            "Mangalagiri Temple", "ISKCON Vijayawada", "Gunadala Mary Matha Shrine", 
            "Sri Ramalingeswara Temple", "Sri Nandikeswara Temple", "Paritala Anjaneya Swamy Temple", "Sri Lakshmi Narasimha Swamy Temple", "Shivalayam Temple"
        ],
        "churches": [
            "St. Peter's Cathedral", "Christ Lutheran Church", "St. Paul's Church", 
            "Centenary Baptist Church", "Zion Church", "Methodist Church", 
            "Bethel Church", "Immanuel Church", "Holy Spirit Church", "Mount Zion Church"
        ]
    },
    "Tirupati": {
        "hotels": ["Hotel Bliss", "Fortune Select Grand Ridge", "Minerva Grand", "Pai Viceroy", "Sri Sai Residency", 
                   "Marasa Sarovar Premiere", "Kences Hotel", "Renigunta Residency", "Hotel Harsha Residency", "Bhimas Deluxe Hotel"],
        "hospitals": ["SVIMS Hospital", "Sri Venkateswara Institute of Medical Sciences", "BIRRD Hospital", "Padmavathi Hospital", 
                      "RUIA Hospital", "Balaji Institute of Surgery", "Chandamama Hospital", "MNR Medical College Hospital", "Amara Hospital", "Govindaraja Swamy Hospital"],
        "tourist_spots": ["Sri Venkateswara Temple", "Talakona Waterfalls", "Sri Kapileswara Swamy Temple", "Chandragiri Fort", 
                          "Sri Govindaraja Swamy Temple", "TTD Gardens", "Silathoranam", "Sri Venkateswara Zoological Park", "Akasaganga Teertham", "Srivari Padalu"],
        "temples": ["Sri Venkateswara Temple", "Kapila Theertham", "Padmavathi Temple", "Sri Govindaraja Swamy Temple", "Sri Kodandarama Swamy Temple",
                    "Sri Kalyana Venkateswara Swamy Temple", "Sri Varahaswami Temple", "Sri Bedi Anjaneyaswami Temple", "Sri Anjaneyaswami Temple", "Sri ISKCON Temple"],
        "churches": ["St. Paul’s Lutheran Church", "St. Mary's Church", "Holy Cross Church", "Sacred Heart Cathedral", "Bethany Christian Church",
                     "Christ the King Church", "Bethesda Gospel Ministries Church", "Zion Church", "Faith Tabernacle Church", "Bible Mission Church"]
    },
    "Visakhapatnam": {
        "hotels": ["Novotel Visakhapatnam", "Dolphin Hotel", "The Gateway Hotel", "Hotel Daspalla", "Green Park Hotel", 
                   "Fairfield by Marriott", "Hotel Akshaya", "Best Western Ramachandra", "The Park Visakhapatnam", "Fortune Inn Sree Kanya"],
        "hospitals": ["Care Hospital", "Apollo Hospital", "Seven Hills Hospital", "Queens NRI Hospital", "Indus Hospital", 
                      "King George Hospital", "Ramakrishna Hospital", "Lalitha Super Speciality Hospital", "OMNI RK Hospital", "Aayush Hospitals"],
        "tourist_spots": ["Rama Krishna Beach", "Kailasagiri", "Borra Caves", "INS Kurusura Submarine Museum", "Araku Valley", 
                          "Yarada Beach", "Dolphin’s Nose", "Simhachalam Temple", "Rishikonda Beach", "Indira Gandhi Zoological Park"],
        "temples": ["Simhachalam Temple", "Sri Kanaka Maha Lakshmi Temple", "ISKCON Temple Visakhapatnam", "Varaha Lakshmi Narasimha Temple", 
                    "Venkojipalem Sai Baba Temple", "Kali Temple", "Sri Sampath Vinayaka Temple", "Sri Venkateswara Swamy Temple", "Sri Lakshmi Ganapathi Temple", "Sri Nookambika Ammavari Temple"],
        "churches": ["St. Paul's Church", "Ross Hill Church", "All Saints' Church", "Calvary Baptist Church", "Emmanuel Lutheran Church",
                     "Holy Cross Church", "Christ the King Church", "Bethel AG Church", "Bethany Church", "Grace Church"]
    },
    "Tadepalligudem": {
        "hotels": ["Hotel SSR Residency", "Hotel Sri Kanya", "Manjeera Hotel", "Hotel Bhavani Residency", "Hotel Vijaya Residency", 
                   "Hotel Rajahamsa", "Hotel Grand", "Ravi Teja Residency", "Hotel Sai Leela Residency", "Anjaneya Residency"],
        "hospitals": ["Naveen Hospital", "Sai Lakshmi Hospitals", "Sri Venkata Sai Hospital", "Ravi Teja Hospital", "Vijaya Hospitals", 
                      "Anantha Lakshmi Hospital", "Abhishek Hospital", "Prasad Super Speciality", "Star Hospitals", "Amrutha Hospital"],
        "tourist_spots": ["Polavaram Project", "Perupalem Beach", "Dindi", "Guntupalli Caves", "Tadepalligudem Central Park", 
                          "Kolleru Lake", "Kotaiah Park", "Vempadu Forest", "Bhimavaram Temple", "Sri Mavullamma Temple"],
        "temples": ["Sri Vasavi Kanyakaparameswari Temple", "Sri Venkateswara Swamy Temple", "Sri Rama Temple", "Sri Kanaka Durga Temple", "Sri Sai Baba Temple", 
                    "Sri Anjaneya Swamy Temple", "ISKCON Temple Tadepalligudem", "Sri Varadaraja Swamy Temple", "Sri Nagendra Swamy Temple", "Sri Radha Krishna Temple"],
        "churches": ["St. John’s Church", "Sacred Heart Church", "Bethesda Church", "Faith Baptist Church", "Calvary Baptist Church", 
                     "Bethel Church", "Holy Spirit Church", "Zion Church", "Mount Zion Church", "Immanuel Church"]
    },
    "Tadpatri": {
        "hotels": ["Hotel Nandi", "Hotel Anand", "Sri Sai Lodge", "Manasa Residency", "Hotel Sai Priya", 
                   "Hotel Vasantha", "Sri Harsha Lodge", "Hotel Sindhu", "Hotel Niharika", "Swagath Residency"],
        "hospitals": ["SVS Hospital", "Laxmi Hospitals", "Medicare Hospital", "Gayatri Hospital", "Sai Ram Hospitals", 
                      "Nirmala Hospitals", "Vijaya Super Speciality Hospital", "Vasan Eye Care", "Chaitanya Hospital", "Balaji Hospital"],
        "tourist_spots": ["Chintala Venkataramana Temple", "Bugga Ramalingeswara Temple", "Belum Caves", "Yogi Vemana Park", "Gandikota Fort", 
                          "Ahobilam Temple", "Sri Ranganatha Swamy Temple", "Puttaparthi", "Penukonda Fort", "Vontimitta Temple"],
        "temples": ["Sri Chintala Venkataramana Temple", "Bugga Ramalingeswara Temple", "Sri Ranganatha Swamy Temple", "Ahobilam Temple", "Sri Rama Temple", 
                    "ISKCON Tadpatri", "Sri Sai Baba Temple", "Sri Lakshmi Narasimha Temple", "Sri Anjaneya Swamy Temple", "Sri Padmavathi Temple"],
        "churches": ["St. Joseph’s Church", "St. Mary's Church", "Holy Family Church", "Faith Tabernacle Church", "Bethel Church", 
                     "Bethesda Church", "Calvary Church", "Immanuel Church", "Christ the King Church", "Zion Church"]
    },
    "Tanuku": {
        "hotels": ["Hotel Yesh Park", "Hotel Vasishta Inn", "Hotel Sri Kanya", "Hotel Blue Moon", "Hotel Green Land", 
                   "Hotel Navayuga", "Hotel Ratnam Residency", "Hotel Chaitanya Residency", "Sai Priya Residency", "Hotel Palavelli"],
        "hospitals": ["Vasishta Hospital", "Sai Krishna Super Speciality Hospital", "Sri Venkateswara Hospital", "Gowthami Hospital", "Viswas Hospitals", 
                      "Sree Hospitals", "Manasa Hospital", "Vijaya Super Speciality Hospital", "Anuradha Hospital", "Sai Ram Hospitals"],
        "tourist_spots": ["Perupalem Beach", "Kolleru Lake", "Polavaram Project", "Bhimavaram Temple", "Dindi Resorts", 
                          "Sri Mavullamma Temple", "Pattiseema", "Guntupalli Caves", "Kotaiah Park", "Palakollu Beach"],
        "temples": ["Sri Vasavi Kanyakaparameswari Temple", "Sri Venkateswara Swamy Temple", "Sri Sai Baba Temple", "Sri Anjaneya Swamy Temple", "Sri Rama Temple", 
                    "Sri Kanaka Durga Temple", "Sri ISKCON Temple", "Sri Bhavani Shankara Temple", "Sri Lakshmi Narayana Temple", "Sri Radha Krishna Temple"],
        "churches": ["St. John’s Church", "Sacred Heart Church", "Bethesda Church", "Faith Baptist Church", "Calvary Baptist Church", 
                     "Bethel Church", "Holy Spirit Church", "Zion Church", "Mount Zion Church", "Immanuel Church"]
    },
    "Tenali": {
        "hotels": ["Hotel Sai International", "Hotel Venkateswara Residency", "Sri Lakshmi Residency", "Hotel Radha Krishna", "Hotel Grand Residency", 
                   "Hotel Prasanth Residency", "Hotel Krishna Residency", "Raghavendra Residency", "Hotel Swagath Residency", "Sri Sai Lodge"],
        "hospitals": ["NRI General Hospital", "Tenali Government Hospital", "Anu Hospitals", "Siddhartha Hospital", "Balaji Hospital", 
                      "KIMS Hospitals", "Nikhil Hospitals", "Amaravathi Hospitals", "Sri Ram Hospitals", "St. Joseph's Hospital"],
        "tourist_spots": ["Kondaveedu Fort", "Uppalapadu Bird Sanctuary", "Amaravati Stupa", "Chandavaram Buddhist Site", "Mangalagiri Temple", 
                          "Ethipothala Falls", "Gundala Matha Shrine", "Suryalanka Beach", "Guntur Central Park", "Kolleru Lake"],
        "temples": ["Sri Panakala Lakshmi Narasimha Swamy Temple", "Sri Rama Temple", "Sri Venkateswara Swamy Temple", "Sri Sai Baba Temple", "ISKCON Tenali", 
                    "Sri Kanaka Durga Temple", "Sri Anjaneya Swamy Temple", "Sri Padmavathi Temple", "Sri ISKCON Temple", "Sri Lakshmi Narayana Temple"],
        "churches": ["St. John’s Church", "Sacred Heart Church", "Bethesda Church", "Faith Baptist Church", "Calvary Baptist Church", 
                     "Bethel Church", "Holy Spirit Church", "Zion Church", "Mount Zion Church", "Immanuel Church"]
    },
    "Uravakonda": {
        "hotels": ["Sri Sai Residency", "Raja Deluxe Lodge", "Hotel Shree Ram", "Naveen Residency", "Hotel SSS Residency", 
                   "Ananya Residency", "Raghavendra Lodge", "Ganesh Lodge", "Royal Deluxe Lodge", "Bhavana Residency"],
        "hospitals": ["SVS Hospital", "Sai Hospital", "Lakshmi Hospital", "Gayatri Hospital", "Sri Venkateswara Hospital", 
                      "Ramesh Hospitals", "Anjali Hospitals", "Naveen Hospitals", "Narayana Hospitals", "Sree Rama Hospitals"],
        "tourist_spots": ["Ranganatha Swamy Temple", "Puttaparthi", "Penukonda Fort", "Belum Caves", "Thimmamma Marrimanu", 
                          "Ahobilam Temple", "Yogi Vemana Park", "Gandikota Fort", "Horsley Hills", "Sri Kadiri Lakshmi Narasimha Swamy Temple"],
        "temples": ["Sri Ranganatha Swamy Temple", "ISKCON Temple", "Sri Sai Baba Temple", "Sri Venkateswara Swamy Temple", "Sri Rama Temple", 
                    "Sri Lakshmi Narayana Temple", "Sri Anjaneya Swamy Temple", "Durga Temple", "Sri Padmavathi Temple", "Sri Lakshmi Narasimha Temple"],
        "churches": ["St. Joseph’s Church", "Faith Tabernacle Church", "Sacred Heart Church", "Zion Church", "Calvary Baptist Church", 
                     "Bethesda Church", "Bethel Church", "Mount Zion Church", "Immanuel Church", "Christ the King Church"]
    },
    "Vinukonda": {
        "hotels": ["Hotel VSR Residency", "Sri Balaji Lodge", "Annapurna Lodge", "Hotel Varalakshmi Residency", "Sri Krishna Lodge", 
                   "Sri Sai Lodge", "Sri Durga Residency", "Sri Lakshmi Narayana Residency", "Sri Venkateswara Residency", "Sai Balaji Lodge"],
        "hospitals": ["Sai Super Speciality Hospital", "Balaji Hospitals", "Naveen Hospitals", "Lakshmi Hospital", "Sri Venkateswara Hospital", 
                      "Krishna Hospitals", "Anu Hospital", "Sree Hospital", "Amaravathi Hospital", "Pranav Hospitals"],
        "tourist_spots": ["Vinukonda Hill", "Kondaveedu Fort", "Kotappakonda Temple", "Ethipothala Falls", "Chandavaram Buddhist Site", 
                          "Suryalanka Beach", "Gundala Matha Shrine", "Guntur Central Park", "Amaravati Stupa", "Kolleru Lake"],
        "temples": ["Sri Panakala Lakshmi Narasimha Swamy Temple", "Sri Rama Temple", "ISKCON Vinukonda", "Sri Anjaneya Swamy Temple", "Sri Venkateswara Swamy Temple", 
                    "Sri Kanaka Durga Temple", "Sri Lakshmi Narayana Temple", "Sri Sai Baba Temple", "Sri ISKCON Temple", "Sri Padmavathi Temple"],
        "churches": ["St. Mary’s Church", "Bethesda Church", "Faith Baptist Church", "Calvary Baptist Church", "Bethel Church", 
                     "Zion Church", "Mount Zion Church", "Immanuel Church", "Holy Spirit Church", "Sacred Heart Church"]
    },
    "Vizianagaram": {
        "hotels": ["Hotel MVR Residency", "Hotel Vytla Residency", "Hotel Grand Alliance", "Sri Srinivasa Lodge", "Hotel Ashoka", 
                   "Hotel Prasanthi Residency", "Lakshmi Residency", "Hotel Mahendra", "Mayura Residency", "Hotel Jaya Residency"],
        "hospitals": ["Maharaja Hospital", "NRI Hospital", "Raghavendra Hospitals", "Srinivasa Hospitals", "Ramesh Hospitals", 
                      "Sree Lakshmi Hospitals", "Apollo Hospitals", "Krishna Hospitals", "Sai Hospitals", "Manipal Hospitals"],
        "tourist_spots": ["Vizianagaram Fort", "Bobbili Fort", "Ramanarayanam", "Kumili Waterfall", "Ganta Stambham", 
                          "Thotlakonda Buddhist Complex", "Simhachalam", "Thousand Pillar Temple", "Sangam Sarovar", "Punyagiri Temple"],
        "temples": ["Sri Punyagiri Temple", "Sri Lakshmi Narasimha Swamy Temple", "Sri Rama Temple", "Sri Venkateswara Swamy Temple", "ISKCON Vizianagaram", 
                    "Sri Sai Baba Temple", "Sri Anjaneya Swamy Temple", "Sri Varadaraja Swamy Temple", "Durga Temple", "Sri Padmavathi Temple"],
        "churches": ["St. John’s Church", "Sacred Heart Church", "Zion Church", "Bethesda Church", "Bethel Church", 
                     "Faith Baptist Church", "Holy Spirit Church", "Mount Zion Church", "Immanuel Church", "Calvary Baptist Church"]
    },
    "Kovvur": {
        "hotels": ["Hotel Grand Kovvur", "Sri Venkateswara Residency", "Hotel Lakshmi", "Sri Sai Lodge", "Nandini Residency", 
                   "Sai Lakshmi Lodge", "Hotel Sri Surya Residency", "Ganesh Lodge", "Sri Durga Residency", "Ravi Teja Lodge"],
        "hospitals": ["Ravi Teja Hospital", "Sri Balaji Hospitals", "Naveen Hospitals", "Sri Sai Ram Hospitals", "Vijaya Hospitals", 
                      "Sree Lakshmi Hospitals", "Krishna Hospitals", "Sri Venkateswara Hospital", "Care Hospitals", "Narayana Hospitals"],
        "tourist_spots": ["Godavari River Bridge", "Polavaram Project", "Perupalem Beach", "Dindi Resorts", "Guntupalli Caves", 
                          "Papi Kondalu", "Kolleru Lake", "Sri Mavullamma Temple", "Pattiseema", "Narsapuram Beach"],
        "temples": ["Sri Vasavi Kanyakaparameswari Temple", "Sri Venkateswara Swamy Temple", "Sri Kanaka Durga Temple", "Sri Anjaneya Swamy Temple", "Sri Sai Baba Temple", 
                    "Sri Rama Temple", "ISKCON Kovvur", "Sri Varadaraja Swamy Temple", "Durga Temple", "Sri Lakshmi Narayana Temple"],
        "churches": ["St. John’s Church", "Sacred Heart Church", "Zion Church", "Bethel Church", "Faith Tabernacle Church", 
                     "Holy Spirit Church", "Bethesda Church", "Calvary Baptist Church", "Mount Zion Church", "Immanuel Church"]
    },
    "Kurnool": {
        "hotels": ["Hotel DVR Mansion", "Sri Durga Residency", "Hotel Rajavihar", "Hotel Suraj Grand", "Hotel Mourya Inn", 
                   "Hotel Trishul Grand", "Hotel Athidhi", "Haritha Hotel", "Hotel New Regency", "The Mourya Inn"],
        "hospitals": ["Vijaya Hospital", "Care Hospital", "Sai Krishna Super Speciality Hospital", "Apollo Hospital", "Manipal Hospital", 
                      "Sree Rama Hospitals", "Sunshine Hospital", "Narayana Hospital", "Nirmala Hospital", "Lakshmi Hospital"],
        "tourist_spots": ["Belum Caves", "Konda Reddy Fort", "Oravakallu Rock Garden", "Mahanandi Temple", "Ahobilam Temple", 
                          "Yaganti Temple", "Rollapadu Wildlife Sanctuary", "Srisailam", "Mantralayam", "Adoni Fort"],
        "temples": ["Sri Mahanandi Temple", "Sri Lakshmi Narasimha Swamy Temple", "Sri Ranganatha Swamy Temple", "ISKCON Kurnool", "Sri Sai Baba Temple", 
                    "Sri Anjaneya Swamy Temple", "Sri Lakshmi Narayana Temple", "Sri Venkateswara Swamy Temple", "Durga Temple", "Sri Shivalayam Temple"],
        "churches": ["St. John’s Church", "Sacred Heart Church", "Zion Church", "Bethesda Church", "Faith Tabernacle Church", 
                     "Bethel Church", "Holy Spirit Church", "Immanuel Church", "Calvary Baptist Church", "Mount Zion Church"]
    },
    "Macherla": {
        "hotels": ["Sri Sai Residency", "Hotel Lakshmi Residency", "Hotel Geetha", "Sri Krishna Lodge", "Macherla Lodge", 
                   "Haritha Hotel", "Sri Durga Residency", "Annapurna Residency", "Hotel Nandini", "Rajadhani Lodge"],
        "hospitals": ["Sri Sai Hospital", "Krishna Hospitals", "Sri Venkateswara Hospital", "Lakshmi Hospital", "Naveen Hospitals", 
                      "Anu Hospitals", "Pranav Hospital", "Sri Rama Hospital", "Sree Hospitals", "Vijaya Hospitals"],
        "tourist_spots": ["Nagarjuna Sagar Dam", "Ethipothala Falls", "Sri Mallikarjuna Swamy Temple", "Kotappakonda", "Chandavaram Buddhist Site", 
                          "Amaravati Stupa", "Kolleru Lake", "Dindi Resorts", "Macherla Fort", "Bhattiprolu Stupa"],
        "temples": ["Sri Mallikarjuna Swamy Temple", "Sri Rama Temple", "ISKCON Macherla", "Sri Lakshmi Narayana Temple", "Sri Anjaneya Swamy Temple", 
                    "Sri Venkateswara Swamy Temple", "Durga Temple", "Sri Sai Baba Temple", "Sri Padmavathi Temple", "Sri Varadaraja Swamy Temple"],
        "churches": ["St. Mary’s Church", "Zion Church", "Faith Tabernacle Church", "Calvary Baptist Church", "Sacred Heart Church", 
                     "Bethel Church", "Mount Zion Church", "Immanuel Church", "Holy Spirit Church", "Bethesda Church"]
    },
    "Machilipatnam": {
        "hotels": ["Hotel Padmavathi", "Hotel Koneru", "Hotel Vasavi Residency", "Hotel Garuda", "Hotel Vijaya Residency", 
                   "Haritha Beach Resort", "Krishna Residency", "Sri Sai Residency", "Gowtham Grand Hotel", "Hotel Lakshmi Residency"],
        "hospitals": ["Area Hospital Machilipatnam", "Manipal Hospital", "Care Hospital", "Krishna Hospitals", "Lakshmi Hospital", 
                      "Sree Lakshmi Hospitals", "Sri Venkateswara Hospital", "Sai Hospitals", "Narayana Hospitals", "Ramesh Hospitals"],
        "tourist_spots": ["Manginapudi Beach", "Machilipatnam Port", "Panduranga Swamy Temple", "Dattashram", "Hamsaladeevi Beach", 
                          "Kuchipudi Village", "Gudivada Stupa", "Undavalli Caves", "Sri Subrahmanya Swamy Temple", "Krishna River Delta"],
        "temples": ["Panduranga Swamy Temple", "Sri Rama Temple", "Sri Venkateswara Swamy Temple", "Sri Anjaneya Swamy Temple", "Sri Sai Baba Temple", 
                    "Sri Lakshmi Narayana Temple", "ISKCON Machilipatnam", "Sri Durga Temple", "Sri Padmavathi Temple", "Sri Varadaraja Swamy Temple"],
        "churches": ["St. Mary’s Church", "Zion Church", "Sacred Heart Church", "Faith Tabernacle Church", "Calvary Baptist Church", 
                     "Bethel Church", "Holy Spirit Church", "Mount Zion Church", "Immanuel Church", "Bethesda Church"]
    },
    "Madanapalle": {
        "hotels": ["Hotel Balaji Residency", "Sri Sai Residency", "Hotel GVS Residency", "Sri Venkateswara Residency", "Haritha Hotel", 
                   "Hotel MNR Grand", "Hotel Athidhi", "Hotel Padmavathi", "Sri Durga Lodge", "Hotel Sai Krishna Residency"],
        "hospitals": ["CSI Hospital", "Raghavendra Hospitals", "Sri Venkateswara Hospital", "Lakshmi Hospital", "Pranav Hospitals", 
                      "Sree Hospitals", "Krishna Hospitals", "Sai Hospitals", "Narayana Hospitals", "Anu Hospitals"],
        "tourist_spots": ["Horsley Hills", "Kaigal Waterfalls", "Kurabalakota", "Gurramkonda Fort", "Thimmamma Marrimanu", 
                          "Sri Venkateswara Swamy Temple", "Chittoor Fort", "Madanapalle Lake", "Kalyani Dam", "Malleshwara Swamy Temple"],
        "temples": ["Sri Mallikarjuna Swamy Temple", "Sri Rama Temple", "Sri Lakshmi Narasimha Swamy Temple", "ISKCON Madanapalle", "Sri Venkateswara Swamy Temple", 
                    "Sri Sai Baba Temple", "Sri Anjaneya Swamy Temple", "Sri Durga Temple", "Sri Padmavathi Temple", "Sri Varadaraja Swamy Temple"],
        "churches": ["St. John’s Church", "Faith Tabernacle Church", "Sacred Heart Church", "Zion Church", "Bethesda Church", 
                     "Bethel Church", "Mount Zion Church", "Holy Spirit Church", "Calvary Baptist Church", "Immanuel Church"]
    },
    "Mandapeta": {
        "hotels": ["Hotel Sri Sai Residency", "Sri Krishna Lodge", "Sri Lakshmi Narayana Residency", "Hotel Annapurna", "Haritha Residency", 
                   "Hotel Sai Krishna Residency", "Sri Durga Residency", "Sri Venkateswara Residency", "Sri Nandini Residency", "Hotel Srinivasa Residency"],
        "hospitals": ["Sri Sai Hospital", "Krishna Hospitals", "Sri Venkateswara Hospital", "Lakshmi Hospital", "Naveen Hospitals", 
                      "Pranav Hospital", "Anu Hospitals", "Sree Hospitals", "Vijaya Hospitals", "Sai Hospitals"],
        "tourist_spots": ["Kadiyam Nursery", "Rajahmundry Godavari Bridge", "Dowleswaram Barrage", "Kolleru Lake", "Dindi Resorts", 
                          "Draksharamam Temple", "Annavaram Temple", "Pattiseema", "Korukonda Temple", "Ryali Jagan Mohini Kesava Swamy Temple"],
        "temples": ["Sri Rama Temple", "Sri Lakshmi Narasimha Swamy Temple", "Sri Venkateswara Swamy Temple", "ISKCON Mandapeta", "Sri Sai Baba Temple", 
                    "Sri Anjaneya Swamy Temple", "Sri Durga Temple", "Sri Padmavathi Temple", "Sri Varadaraja Swamy Temple", "Sri Lakshmi Narayana Temple"],
        "churches": ["St. Mary’s Church", "Zion Church", "Faith Tabernacle Church", "Sacred Heart Church", "Bethel Church", 
                     "Bethesda Church", "Mount Zion Church", "Immanuel Church", "Holy Spirit Church", "Calvary Baptist Church"]
    },
    "Mangalagiri": {
        "hotels": ["Hotel Sankar Residency", "Sri Sai Lodge", "Sri Lakshmi Narayana Lodge", "Haritha Hotel", "Sri Krishna Residency", 
                   "Sri Durga Residency", "Sri Venkateswara Residency", "Annapurna Residency", "Sri Nandini Residency", "Sri Sai Krishna Lodge"],
        "hospitals": ["Krishna Hospitals", "NRI Hospitals", "Sri Sai Hospital", "Lakshmi Hospital", "Sri Venkateswara Hospital", 
                      "Pranav Hospitals", "Anu Hospitals", "Sree Hospitals", "Vijaya Hospitals", "Sai Hospitals"],
        "tourist_spots": ["Sri Lakshmi Narasimha Swamy Temple", "Undavalli Caves", "Amaravati Stupa", "Kondaveedu Fort", "Ethipothala Falls", 
                          "Suryalanka Beach", "Prakasam Barrage", "Bhavani Island", "Mangalgiri Hill", "Krishna River"],
        "temples": ["Sri Lakshmi Narasimha Swamy Temple", "Sri Rama Temple", "Sri Venkateswara Swamy Temple", "ISKCON Mangalagiri", "Sri Sai Baba Temple", 
                    "Sri Anjaneya Swamy Temple", "Sri Durga Temple", "Sri Padmavathi Temple", "Sri Lakshmi Narayana Temple", "Sri Varadaraja Swamy Temple"],
        "churches": ["St. Mary’s Church", "Zion Church", "Faith Tabernacle Church", "Sacred Heart Church", "Calvary Baptist Church", 
                     "Bethel Church", "Holy Spirit Church", "Mount Zion Church", "Immanuel Church", "Bethesda Church"]
    },
    "Markapur": {
        "hotels": ["Hotel Sri Sai Residency", "Sri Lakshmi Narayana Residency", "Sri Krishna Lodge", "Haritha Residency", "Sri Durga Residency", 
                   "Sri Venkateswara Residency", "Hotel Annapurna", "Sri Nandini Residency", "Hotel Sai Krishna Residency", "Sri Krishna Residency"],
        "hospitals": ["Sri Sai Hospital", "Krishna Hospitals", "Sri Venkateswara Hospital", "Lakshmi Hospital", "Naveen Hospitals", 
                      "Pranav Hospital", "Anu Hospitals", "Sree Hospitals", "Vijaya Hospitals", "Sai Hospitals"],
        "tourist_spots": ["Srisailam Dam", "Sundipenta Reservoir", "Cumbum Lake", "Gandikota Fort", "Brahmam Sagar", 
                          "Rollapadu Wildlife Sanctuary", "Sri Mallikarjuna Temple", "Nallamala Forest", "Ahobilam Temple", "Belum Caves"],
        "temples": ["Sri Mallikarjuna Swamy Temple", "Sri Lakshmi Narasimha Swamy Temple", "Sri Rama Temple", "Sri Venkateswara Swamy Temple", "ISKCON Markapur", 
                    "Sri Sai Baba Temple", "Sri Anjaneya Swamy Temple", "Sri Durga Temple", "Sri Padmavathi Temple", "Sri Varadaraja Swamy Temple"],
        "churches": ["St. Mary’s Church", "Zion Church", "Faith Tabernacle Church", "Sacred Heart Church", "Bethel Church", 
                     "Bethesda Church", "Mount Zion Church", "Immanuel Church", "Holy Spirit Church", "Calvary Baptist Church"]
    },
    "Nagari": {
        "hotels": ["Hotel Balaji Residency", "Sri Sai Lodge", "Sri Krishna Residency", "Haritha Hotel", "Sri Lakshmi Narayana Residency", 
                   "Hotel Venkateswara Residency", "Sri Durga Residency", "Annapurna Residency", "Sri Sai Krishna Residency", "Sri Nandini Residency"],
        "hospitals": ["Sri Sai Hospital", "Krishna Hospitals", "Sri Venkateswara Hospital", "Lakshmi Hospital", "Naveen Hospitals", 
                      "Pranav Hospital", "Anu Hospitals", "Sree Hospitals", "Vijaya Hospitals", "Sai Hospitals"],
        "tourist_spots": ["Nagari Hills", "Kailasa Kona Waterfalls", "Srikalahasti Temple", "Tirupati", "Chandragiri Fort", 
                          "Nagari Fort", "Kaigal Falls", "Kalyani Dam", "Sri Padmavathi Ammavari Temple", "Punganoor Lake"],
        "temples": ["Sri Venkateswara Swamy Temple", "Sri Lakshmi Narasimha Swamy Temple", "Sri Rama Temple", "ISKCON Nagari", "Sri Sai Baba Temple", 
                    "Sri Anjaneya Swamy Temple", "Sri Durga Temple", "Sri Padmavathi Temple", "Sri Varadaraja Swamy Temple", "Sri Lakshmi Narayana Temple"],
        "churches": ["St. Mary’s Church", "Zion Church", "Faith Tabernacle Church", "Sacred Heart Church", "Bethel Church", 
                     "Bethesda Church", "Mount Zion Church", "Immanuel Church", "Holy Spirit Church", "Calvary Baptist Church"]
    },
    "Nandyala": {
        "hotels": ["Sri Sai Residency", "Sri Lakshmi Narayana Residency", "Sri Krishna Lodge", "Haritha Residency", "Sri Durga Residency", 
                   "Sri Venkateswara Residency", "Hotel Annapurna", "Sri Nandini Residency", "Hotel Sai Krishna Residency", "Sri Krishna Residency"],
        "hospitals": ["Sri Sai Hospital", "Krishna Hospitals", "Sri Venkateswara Hospital", "Lakshmi Hospital", "Naveen Hospitals", 
                      "Pranav Hospital", "Anu Hospitals", "Sree Hospitals", "Vijaya Hospitals", "Sai Hospitals"],
        "tourist_spots": ["Mahanandi Temple", "Ahobilam Temple", "Belum Caves", "Oravakallu Rock Garden", "Gandikota Fort", 
                          "Srisailam Dam", "Rollapadu Wildlife Sanctuary", "Mallikarjuna Temple", "Nallamala Hills", "Yaganti Temple"],
        "temples": ["Mahanandi Temple", "Sri Lakshmi Narasimha Swamy Temple", "Sri Rama Temple", "ISKCON Nandyala", "Sri Venkateswara Swamy Temple", 
                    "Sri Sai Baba Temple", "Sri Anjaneya Swamy Temple", "Sri Durga Temple", "Sri Padmavathi Temple", "Sri Varadaraja Swamy Temple"],
        "churches": ["St. Mary’s Church", "Zion Church", "Faith Tabernacle Church", "Sacred Heart Church", "Bethel Church", 
                     "Bethesda Church", "Mount Zion Church", "Immanuel Church", "Holy Spirit Church", "Calvary Baptist Church"]
    },
    "Narasaraopet": {
        "hotels": ["Hotel Sri Sai Residency", "Sri Lakshmi Narayana Residency", "Sri Krishna Lodge", "Haritha Residency", "Sri Durga Residency", 
                   "Sri Venkateswara Residency", "Hotel Annapurna", "Sri Nandini Residency", "Hotel Sai Krishna Residency", "Sri Krishna Residency"],
        "hospitals": ["Sri Sai Hospital", "Krishna Hospitals", "Sri Venkateswara Hospital", "Lakshmi Hospital", "Naveen Hospitals", 
                      "Pranav Hospital", "Anu Hospitals", "Sree Hospitals", "Vijaya Hospitals", "Sai Hospitals"],
        "tourist_spots": ["Kondaveedu Fort", "Ethipothala Falls", "Kotappakonda Temple", "Suryalanka Beach", "Chandavaram Buddhist Site", 
                          "Gundala Matha Shrine", "Guntur Central Park", "Amaravati Stupa", "Kolleru Lake", "Mangalagiri Hill"],
        "temples": ["Sri Lakshmi Narasimha Swamy Temple", "Sri Rama Temple", "Sri Venkateswara Swamy Temple", "ISKCON Narasaraopet", "Sri Sai Baba Temple", 
                    "Sri Anjaneya Swamy Temple", "Sri Durga Temple", "Sri Padmavathi Temple", "Sri Varadaraja Swamy Temple", "Sri Lakshmi Narayana Temple"],
        "churches": ["St. Mary’s Church", "Zion Church", "Faith Tabernacle Church", "Sacred Heart Church", "Bethel Church", 
                     "Bethesda Church", "Mount Zion Church", "Immanuel Church", "Holy Spirit Church", "Calvary Baptist Church"]
    },
    "Narsipatnam": {
        "hotels": ["Sri Sai Residency", "Hotel Krishna Residency", "Sri Lakshmi Narayana Lodge", "Hotel Annapurna Residency", "Haritha Hotel", 
                   "Sri Krishna Lodge", "Sri Durga Residency", "Sri Venkateswara Residency", "Sri Sai Krishna Residency", "Sri Nandini Residency"],
        "hospitals": ["Sri Sai Hospital", "Krishna Hospitals", "Sri Venkateswara Hospital", "Lakshmi Hospital", "Naveen Hospitals", 
                      "Pranav Hospital", "Anu Hospitals", "Sree Hospitals", "Vijaya Hospitals", "Sai Hospitals"],
        "tourist_spots": ["Lambasingi", "Borra Caves", "Ananthagiri Hills", "Tyda Jungle Bells", "Araku Valley", 
                          "Katiki Waterfalls", "Simhachalam Temple", "Thotlakonda Buddhist Complex", "Yarada Beach", "Dolphin's Nose"],
        "temples": ["Sri Lakshmi Narasimha Swamy Temple", "Sri Rama Temple", "ISKCON Narsipatnam", "Sri Venkateswara Swamy Temple", "Sri Sai Baba Temple", 
                    "Sri Anjaneya Swamy Temple", "Sri Durga Temple", "Sri Padmavathi Temple", "Sri Lakshmi Narayana Temple", "Sri Varadaraja Swamy Temple"],
        "churches": ["St. Mary’s Church", "Zion Church", "Faith Tabernacle Church", "Sacred Heart Church", "Bethel Church", 
                     "Bethesda Church", "Mount Zion Church", "Immanuel Church", "Holy Spirit Church", "Calvary Baptist Church"]
    },
    "Nellore": {
        "hotels": ["Hotel Minerva Grand", "Hotel Athidhi", "Hotel Yesh Park", "Hotel DR Uttam", "Hotel Shivam International", 
                   "Hotel Leo", "Sri Durga Residency", "Haritha Hotel", "Sri Sai Residency", "Sri Krishna Lodge"],
        "hospitals": ["Apollo Hospital", "Narayanadri Hospitals", "Krishna Hospitals", "Sri Venkateswara Hospital", "Lakshmi Hospital", 
                      "Pranav Hospital", "Anu Hospitals", "Sree Hospitals", "Vijaya Hospitals", "Sai Hospitals"],
        "tourist_spots": ["Sri Ranganathaswamy Temple", "Pulicat Lake", "Mypadu Beach", "Udayagiri Fort", "Penchalakona Temple", 
                          "Nelapattu Bird Sanctuary", "Krishna Mandir", "Jonnawada Temple", "Barah Shaheed Dargah", "Venkatagiri Fort"],
        "temples": ["Sri Ranganathaswamy Temple", "Sri Lakshmi Narasimha Swamy Temple", "Sri Rama Temple", "ISKCON Nellore", "Sri Venkateswara Swamy Temple", 
                    "Sri Sai Baba Temple", "Sri Anjaneya Swamy Temple", "Sri Durga Temple", "Sri Padmavathi Temple", "Sri Varadaraja Swamy Temple"],
        "churches": ["St. Joseph’s Cathedral", "Zion Church", "Faith Tabernacle Church", "Sacred Heart Church", "Calvary Baptist Church", 
                     "Bethel Church", "Holy Spirit Church", "Mount Zion Church", "Immanuel Church", "Bethesda Church"]
    },
    "Nidadavole": {
        "hotels": ["Hotel Sri Sai Residency", "Sri Lakshmi Narayana Lodge", "Sri Krishna Residency", "Haritha Hotel", "Sri Durga Residency", 
                   "Sri Venkateswara Residency", "Hotel Annapurna", "Sri Nandini Residency", "Hotel Sai Krishna Residency", "Sri Krishna Lodge"],
        "hospitals": ["Sri Sai Hospital", "Krishna Hospitals", "Sri Venkateswara Hospital", "Lakshmi Hospital", "Naveen Hospitals", 
                      "Pranav Hospital", "Anu Hospitals", "Sree Hospitals", "Vijaya Hospitals", "Sai Hospitals"],
        "tourist_spots": ["Godavari River", "Dindi Resorts", "Dowleswaram Barrage", "Kadiyam Nurseries", "Pattiseema", 
                          "Sri Lakshmi Narasimha Swamy Temple", "Annavaram Temple", "Rajahmundry Bridge", "Kolleru Lake", "Kotilingala Ghat"],
        "temples": ["Sri Lakshmi Narasimha Swamy Temple", "Sri Rama Temple", "ISKCON Nidadavole", "Sri Venkateswara Swamy Temple", "Sri Sai Baba Temple", 
                    "Sri Anjaneya Swamy Temple", "Sri Durga Temple", "Sri Padmavathi Temple", "Sri Varadaraja Swamy Temple", "Sri Lakshmi Narayana Temple"],
        "churches": ["St. Mary’s Church", "Zion Church", "Faith Tabernacle Church", "Sacred Heart Church", "Bethel Church", 
                     "Bethesda Church", "Mount Zion Church", "Immanuel Church", "Holy Spirit Church", "Calvary Baptist Church"]
    },
    "Nuzvid": {
        "hotels": ["Hotel Sri Sai Residency", "Sri Krishna Residency", "Sri Lakshmi Narayana Lodge", "Haritha Hotel", "Sri Durga Residency", 
                   "Sri Venkateswara Residency", "Sri Nandini Residency", "Hotel Annapurna", "Hotel Sai Krishna Residency", "Sri Krishna Lodge"],
        "hospitals": ["Sri Sai Hospital", "Krishna Hospitals", "Sri Venkateswara Hospital", "Lakshmi Hospital", "Naveen Hospitals", 
                      "Pranav Hospital", "Anu Hospitals", "Sree Hospitals", "Vijaya Hospitals", "Sai Hospitals"],
        "tourist_spots": ["Kolleru Lake", "Eluru Buddha Park", "Kolleru Bird Sanctuary", "Dowleswaram Barrage", "Rajahmundry Bridge", 
                          "Pattiseema", "Sri Lakshmi Narasimha Swamy Temple", "Dindi Resorts", "Kotilingala Ghat", "Kadiyam Nurseries"],
        "temples": ["Sri Lakshmi Narasimha Swamy Temple", "Sri Rama Temple", "ISKCON Nuzvid", "Sri Venkateswara Swamy Temple", "Sri Sai Baba Temple", 
                    "Sri Anjaneya Swamy Temple", "Sri Durga Temple", "Sri Padmavathi Temple", "Sri Varadaraja Swamy Temple", "Sri Lakshmi Narayana Temple"],
        "churches": ["St. Mary’s Church", "Zion Church", "Faith Tabernacle Church", "Sacred Heart Church", "Bethel Church", 
                     "Bethesda Church", "Mount Zion Church", "Immanuel Church", "Holy Spirit Church", "Calvary Baptist Church"]
    },
    "Ongole": {
        "hotels": ["Hotel Central Park", "Vijaya Durga Residency", "Haritha Hotel", "Hotel Apsara", "Swagat Lodge", 
                   "Sri Sai Residency", "Sri Lakshmi Narayana Lodge", "Hotel RRR Residency", "Sri Krishna Residency", "Hotel Adithya"],
        "hospitals": ["Sri Sai Hospital", "Raja Hospitals", "Apollo Hospital", "Surya Hospital", "Swarna Hospitals", 
                      "Anu Hospitals", "Krishna Hospitals", "Sree Hospitals", "Vijaya Hospitals", "Sai Hospitals"],
        "tourist_spots": ["Kothapatnam Beach", "Vodarevu Beach", "Chirala Beach", "Bhavanasi Lake", "Chennakesava Swamy Temple", 
                          "Sri Shirdi Sai Baba Temple", "Cumbum Lake", "Markapur Reservoir", "Gundla Brahmeswaram", "Kandaleru Dam"],
        "temples": ["Sri Chennakesava Swamy Temple", "Sri Rama Temple", "Sri Venkateswara Swamy Temple", "ISKCON Ongole", "Sri Lakshmi Narasimha Swamy Temple", 
                    "Sri Sai Baba Temple", "Sri Anjaneya Swamy Temple", "Sri Durga Temple", "Sri Varadaraja Swamy Temple", "Sri Lakshmi Narayana Temple"],
        "churches": ["St. Mary's Church", "Zion Church", "Faith Tabernacle Church", "Sacred Heart Church", "Bethel Church", 
                     "Bethesda Church", "Mount Zion Church", "Immanuel Church", "Holy Spirit Church", "Calvary Baptist Church"]
    },
    "Palakollu": {
        "hotels": ["Sri Krishna Residency", "Sri Lakshmi Narayana Lodge", "Haritha Hotel", "Hotel Minerva", "Sri Sai Residency", 
                   "Hotel Sarovar", "Hotel Subramaniyam", "Swagat Lodge", "Hotel Annapurna", "Hotel Grand Palace"],
        "hospitals": ["Sri Sai Hospital", "Anu Hospitals", "Sree Hospitals", "Vijaya Hospitals", "Sai Hospitals", 
                      "Krishna Hospitals", "Sri Venkateswara Hospital", "Lakshmi Hospital", "Naveen Hospitals", "Pranav Hospital"],
        "tourist_spots": ["Perupalem Beach", "Ksheera Ramalingeswara Swamy Temple", "Dindi Resorts", "Godavari River", "Konaseema", 
                          "Kolleru Lake", "Rajahmundry Bridge", "Pattiseema", "Sri Lakshmi Narasimha Swamy Temple", "Annavaram Temple"],
        "temples": ["Ksheera Ramalingeswara Swamy Temple", "Sri Lakshmi Narasimha Swamy Temple", "Sri Rama Temple", "ISKCON Palakollu", "Sri Sai Baba Temple", 
                    "Sri Anjaneya Swamy Temple", "Sri Durga Temple", "Sri Padmavathi Temple", "Sri Varadaraja Swamy Temple", "Sri Lakshmi Narayana Temple"],
        "churches": ["St. Mary's Church", "Zion Church", "Faith Tabernacle Church", "Sacred Heart Church", "Bethel Church", 
                     "Bethesda Church", "Mount Zion Church", "Immanuel Church", "Holy Spirit Church", "Calvary Baptist Church"]
    },
    "Palasa": {
        "hotels": ["Sri Krishna Residency", "Hotel Surya Palace", "Sri Lakshmi Narayana Lodge", "Haritha Hotel", "Sri Sai Residency", 
                   "Hotel Golden Inn", "Hotel Sea Breeze", "Swagat Lodge", "Hotel Annapurna", "Hotel Royal Plaza"],
        "hospitals": ["Sri Sai Hospital", "Anu Hospitals", "Sree Hospitals", "Vijaya Hospitals", "Sai Hospitals", 
                      "Krishna Hospitals", "Sri Venkateswara Hospital", "Lakshmi Hospital", "Naveen Hospitals", "Pranav Hospital"],
        "tourist_spots": ["Baruva Beach", "Tekkali", "Mandasa Fort", "Ramatheertham", "Kaviti Palm Plantations", 
                          "Srikurmam Temple", "Arasavalli Sun Temple", "Ponduru", "Chandragiri Fort", "Rampa Waterfalls"],
        "temples": ["Sri Ramatheertham Temple", "Sri Rama Temple", "Sri Venkateswara Swamy Temple", "ISKCON Palasa", "Sri Sai Baba Temple", 
                    "Sri Anjaneya Swamy Temple", "Sri Durga Temple", "Sri Padmavathi Temple", "Sri Varadaraja Swamy Temple", "Sri Lakshmi Narayana Temple"],
        "churches": ["St. Mary's Church", "Zion Church", "Faith Tabernacle Church", "Sacred Heart Church", "Bethel Church", 
                     "Bethesda Church", "Mount Zion Church", "Immanuel Church", "Holy Spirit Church", "Calvary Baptist Church"]
    },
    "Peddapuram": {
        "hotels": ["Hotel Sri Sai Residency", "Sri Krishna Residency", "Sri Lakshmi Narayana Lodge", "Haritha Hotel", "Sri Durga Residency", 
                   "Hotel Sarovar", "Hotel Subramaniyam", "Swagat Lodge", "Hotel Annapurna", "Hotel Grand Palace"],
        "hospitals": ["Sri Sai Hospital", "Anu Hospitals", "Sree Hospitals", "Vijaya Hospitals", "Sai Hospitals", 
                      "Krishna Hospitals", "Sri Venkateswara Hospital", "Lakshmi Hospital", "Naveen Hospitals", "Pranav Hospital"],
        "tourist_spots": ["Pithapuram Temple", "Godavari River", "Kolleru Lake", "Konaseema", "Annavaram Temple", 
                          "Rajahmundry Bridge", "Pattiseema", "Sri Lakshmi Narasimha Swamy Temple", "Dowleswaram Barrage", "Kadiyam Nurseries"],
        "temples": ["Sri Lakshmi Narasimha Swamy Temple", "Sri Rama Temple", "ISKCON Peddapuram", "Sri Venkateswara Swamy Temple", "Sri Sai Baba Temple", 
                    "Sri Anjaneya Swamy Temple", "Sri Durga Temple", "Sri Padmavathi Temple", "Sri Varadaraja Swamy Temple", "Sri Lakshmi Narayana Temple"],
        "churches": ["St. Mary's Church", "Zion Church", "Faith Tabernacle Church", "Sacred Heart Church", "Bethel Church", 
                     "Bethesda Church", "Mount Zion Church", "Immanuel Church", "Holy Spirit Church", "Calvary Baptist Church"]
    },
    "Pithapuram": {
        "hotels": ["Sri Krishna Residency", "Sri Lakshmi Narayana Lodge", "Haritha Hotel", "Sri Sai Residency", "Hotel Subramaniyam", 
                   "Swagat Lodge", "Hotel Annapurna", "Hotel Grand Palace", "Hotel Sarovar", "Hotel Rajahamsa"],
        "hospitals": ["Sri Sai Hospital", "Anu Hospitals", "Sree Hospitals", "Vijaya Hospitals", "Sai Hospitals", 
                      "Krishna Hospitals", "Sri Venkateswara Hospital", "Lakshmi Hospital", "Naveen Hospitals", "Pranav Hospital"],
        "tourist_spots": ["Kukkuteswara Swamy Temple", "Draksharamam", "Godavari River", "Annavaram Temple", "Rajahmundry Bridge", 
                          "Pattiseema", "Sri Lakshmi Narasimha Swamy Temple", "Dowleswaram Barrage", "Kolleru Lake", "Konaseema"],
        "temples": ["Kukkuteswara Swamy Temple", "Sri Lakshmi Narasimha Swamy Temple", "Sri Rama Temple", "ISKCON Pithapuram", "Sri Venkateswara Swamy Temple", 
                    "Sri Sai Baba Temple", "Sri Anjaneya Swamy Temple", "Sri Durga Temple", "Sri Padmavathi Temple", "Sri Varadaraja Swamy Temple"],
        "churches": ["St. Mary's Church", "Zion Church", "Faith Tabernacle Church", "Sacred Heart Church", "Bethel Church", 
                     "Bethesda Church", "Mount Zion Church", "Immanuel Church", "Holy Spirit Church", "Calvary Baptist Church"]
    },
     "Proddatur": {
        "hotels": ["Sri Krishna Residency", "Sri Lakshmi Narayana Lodge", "Haritha Hotel", "Hotel Sai Krishna", "Hotel Mourya Inn", 
                   "Swagat Lodge", "Hotel Annapurna", "Hotel Sai Residency", "Hotel Grand Plaza", "Hotel Royal Fort"],
        "hospitals": ["Siddhartha Hospitals", "Sri Sai Hospital", "Anu Hospitals", "Krishna Hospitals", "Sri Venkateswara Hospital", 
                      "Sree Hospitals", "Pranav Hospital", "Vijaya Hospitals", "Naveen Hospitals", "Sai Hospitals"],
        "tourist_spots": ["Gandikota Fort", "Belum Caves", "Yaganti", "Sri Lankamalleswara Sanctuary", "Brahmamgari Matham", 
                          "Vontimitta Temple", "Siddhavatam Fort", "Gadanki Falls", "Proddatur Clock Tower", "Ahobilam Temple"],
        "temples": ["Sri Sai Baba Temple", "Sri Lakshmi Narasimha Swamy Temple", "ISKCON Proddatur", "Sri Rama Temple", "Sri Venkateswara Swamy Temple", 
                    "Sri Anjaneya Swamy Temple", "Sri Durga Temple", "Sri Padmavathi Temple", "Sri Varadaraja Swamy Temple", "Sri Lakshmi Narayana Temple"],
        "churches": ["St. Mary's Church", "Zion Church", "Faith Tabernacle Church", "Sacred Heart Church", "Bethel Church", 
                     "Bethesda Church", "Mount Zion Church", "Immanuel Church", "Holy Spirit Church", "Calvary Baptist Church"]
    },
    "Punganur": {
        "hotels": ["Sri Krishna Residency", "Sri Lakshmi Narayana Lodge", "Haritha Hotel", "Sri Sai Residency", "Hotel Mourya Inn", 
                   "Hotel Sai Krishna", "Hotel Subramaniyam", "Swagat Lodge", "Hotel Annapurna", "Hotel Grand Palace"],
        "hospitals": ["Sri Sai Hospital", "Anu Hospitals", "Krishna Hospitals", "Sri Venkateswara Hospital", "Lakshmi Hospital", 
                      "Sree Hospitals", "Pranav Hospital", "Vijaya Hospitals", "Naveen Hospitals", "Sai Hospitals"],
        "tourist_spots": ["Horsley Hills", "Kalyani Dam", "Sri Kalyana Venkateswara Swamy Temple", "Madanapalle", "Chandragiri Fort", 
                          "Talakona Waterfalls", "Kanipakam", "Sri Lakshmi Narasimha Swamy Temple", "Pushpagiri", "Pulicat Lake"],
        "temples": ["Sri Kalyana Venkateswara Swamy Temple", "Sri Rama Temple", "ISKCON Punganur", "Sri Venkateswara Swamy Temple", "Sri Sai Baba Temple", 
                    "Sri Anjaneya Swamy Temple", "Sri Durga Temple", "Sri Padmavathi Temple", "Sri Varadaraja Swamy Temple", "Sri Lakshmi Narayana Temple"],
        "churches": ["St. Mary's Church", "Zion Church", "Faith Tabernacle Church", "Sacred Heart Church", "Bethel Church", 
                     "Bethesda Church", "Mount Zion Church", "Immanuel Church", "Holy Spirit Church", "Calvary Baptist Church"]
    },
    "Puttur": {
        "hotels": ["Sri Krishna Residency", "Sri Lakshmi Narayana Lodge", "Hotel Srinivasa Residency", "Sri Sai Residency", "Hotel Subramaniyam", 
                   "Hotel Annapurna", "Hotel Grand Palace", "Swagat Lodge", "Sri Durga Residency", "Hotel Mourya Inn"],
        "hospitals": ["Sri Sai Hospital", "Anu Hospitals", "Krishna Hospitals", "Sri Venkateswara Hospital", "Sree Hospitals", 
                      "Pranav Hospital", "Vijaya Hospitals", "Naveen Hospitals", "Sai Hospitals", "Lakshmi Hospital"],
        "tourist_spots": ["Sri Venkateswara Swamy Temple", "Talakona Waterfalls", "Horsley Hills", "Chandragiri Fort", "Pushpagiri", 
                          "Kanipakam", "Sri Kalyana Venkateswara Swamy Temple", "Sri Lakshmi Narasimha Swamy Temple", "Pulicat Lake", "Kalyani Dam"],
        "temples": ["Sri Venkateswara Swamy Temple", "Sri Sai Baba Temple", "Sri Kalyana Venkateswara Swamy Temple", "ISKCON Puttur", "Sri Rama Temple", 
                    "Sri Anjaneya Swamy Temple", "Sri Durga Temple", "Sri Padmavathi Temple", "Sri Varadaraja Swamy Temple", "Sri Lakshmi Narayana Temple"],
        "churches": ["St. Mary's Church", "Zion Church", "Faith Tabernacle Church", "Sacred Heart Church", "Bethel Church", 
                     "Bethesda Church", "Mount Zion Church", "Immanuel Church", "Holy Spirit Church", "Calvary Baptist Church"]
    },
    "Rajahmundry": {
        "hotels": ["River Bay Resort", "Hotel Shelton", "Sri Krishna Residency", "Hotel Anand Regency", "Haritha Hotel", 
                   "Sri Lakshmi Narayana Lodge", "Hotel Jetty Grand", "Hotel Aditya Palace", "Hotel River Breeze", "Hotel Sai Krishna"],
        "hospitals": ["Apollo Hospitals", "Anu Hospitals", "Sree Hospitals", "Vijaya Hospitals", "Lakshmi Hospital", 
                      "Sri Venkateswara Hospital", "Krishna Hospitals", "Sai Hospitals", "Pranav Hospital", "Sri Sai Hospital"],
        "tourist_spots": ["Papi Kondalu", "Godavari River", "Dowleswaram Barrage", "Kadiyam Nurseries", "Rajahmundry Bridge", 
                          "Annavaram Temple", "Pattiseema", "Sir Arthur Cotton Museum", "Kolleru Lake", "Sri Lakshmi Narasimha Swamy Temple"],
        "temples": ["Sri Lakshmi Narasimha Swamy Temple", "Sri Venkateswara Swamy Temple", "ISKCON Rajahmundry", "Sri Rama Temple", "Sri Sai Baba Temple", 
                    "Sri Anjaneya Swamy Temple", "Sri Durga Temple", "Sri Padmavathi Temple", "Sri Varadaraja Swamy Temple", "Sri Lakshmi Narayana Temple"],
        "churches": ["St. Mary's Church", "Zion Church", "Faith Tabernacle Church", "Sacred Heart Church", "Bethel Church", 
                     "Bethesda Church", "Mount Zion Church", "Immanuel Church", "Holy Spirit Church", "Calvary Baptist Church"]
    },
    "Rajampet": {
        "hotels": ["Sri Krishna Residency", "Sri Lakshmi Narayana Lodge", "Haritha Hotel", "Hotel Sai Krishna", "Hotel Subramaniyam", 
                   "Hotel Annapurna", "Hotel Grand Palace", "Swagat Lodge", "Sri Durga Residency", "Hotel Mourya Inn"],
        "hospitals": ["Sri Sai Hospital", "Anu Hospitals", "Krishna Hospitals", "Sri Venkateswara Hospital", "Sree Hospitals", 
                      "Pranav Hospital", "Vijaya Hospitals", "Naveen Hospitals", "Sai Hospitals", "Lakshmi Hospital"],
        "tourist_spots": ["Sri Venkateswara Swamy Temple", "Ahobilam", "Gandikota Fort", "Belum Caves", "Yaganti", 
                          "Brahmamgari Matham", "Siddhavatam Fort", "Vontimitta Temple", "Siddheswaram", "Talakona Waterfalls"],
        "temples": ["Sri Venkateswara Swamy Temple", "Sri Sai Baba Temple", "ISKCON Rajampet", "Sri Lakshmi Narasimha Swamy Temple", "Sri Rama Temple", 
                    "Sri Anjaneya Swamy Temple", "Sri Durga Temple", "Sri Padmavathi Temple", "Sri Varadaraja Swamy Temple", "Sri Lakshmi Narayana Temple"],
        "churches": ["St. Mary's Church", "Zion Church", "Faith Tabernacle Church", "Sacred Heart Church", "Bethel Church", 
                     "Bethesda Church", "Mount Zion Church", "Immanuel Church", "Holy Spirit Church", "Calvary Baptist Church"]
    }

}

# Function to search for information based on city and category
def search_city_info(city, category):
    if city in city_data and category in city_data[city]:
        results = city_data[city][category]
        speak(f"Here are some {category} in {city}: {', '.join(results)}")
    else:
        speak(f"Sorry, I don't have data for {category} in {city}.")

# Function to process user query
def handle_query(query):
    # Extract the city and category from the query
    for city in city_data.keys():
        if city.lower() in query.lower():
            if "hotel" in query.lower():
                search_city_info(city, "hotels")
            elif "hospital" in query.lower():
                search_city_info(city, "hospitals")
            elif "tourist" in query.lower() or "spot" in query.lower():
                search_city_info(city, "tourist_spots")
            elif "temple" in query.lower():
                search_city_info(city, "temples")
            elif "church" in query.lower():
                search_city_info(city, "churches")
            else:
                speak(f"Sorry, I didn't understand what you are looking for in {city}.")
            return
    speak("Sorry, I couldn't find the city or category you asked for.")

def run_voice_assistant():
    # Only speak this once at the start
    speak("Hi, Welcome to TravelGuru where you can find information.")
    
    # Start a continuous loop for handling queries until user says 'exit'
    while True:
        query = listen()
        if query:
            # Check if the user wants to exit
            if "exit" in query:
                speak("Thank you for using TravelGuru. Have a nice day!")
                break
            # Handle the user's query
            handle_query(query)
        else:
            speak("Please try again.")

if __name__ == "__main__":
    run_voice_assistant()

