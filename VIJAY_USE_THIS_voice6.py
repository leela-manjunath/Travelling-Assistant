###FIRST NUVVU EM CHESTHAV ANTE VSCODE LO RIGHT CLICK ICHI II FOLDER LO
# 
# RUN IN INTERACTIVE SHELL ANI UNTUNDHIADI CLICK CHEYYI CHESAKA NEEKU INTERACTIVE SHELL OPEN AYYIDI 
# 
# NENU GUI KUDA CHESANU START NOKKITHE INKA OPEN AYYIDHI 
# 
# EXIT AVVALI ANTE 'EXIT' KANI 'BYE' KANI ' QUIT' KANI CHEPPU INKA AUTOMATIC GA CLOSE IPOYIDHI 

### DEPENDENCIES ITHE SPEECH_RECOGNITION,PYTTSX3,PANDAS KAVALI ANTE PLAYSOUND PACKAGES INSTALL CHESKO









import speech_recognition as sr
import pyttsx3
import pandas as pd
import re
import tkinter as tk
from tkinter import Frame, Label, Scrollbar, Canvas
import threading

# Initialize text-to-speech engine
engine = pyttsx3.init()
engine.setProperty('rate', 180)

# Load CSV files into DataFrames
try:
    hotels_df = pd.read_csv('hotels.csv')
    hospitals_df = pd.read_csv('hospitals.csv')
    tourist_spots_df = pd.read_csv('tourist_spots.csv')
    churches_df = pd.read_csv('churches.csv')
except Exception as e:
    print(f"Error loading CSV files: {e}")

# Function to get data based on category and city
def get_data(category_df, city_name):
    city_data = category_df[category_df['City'].str.lower() == city_name.lower()]
    return city_data.iloc[:, 1].tolist() if not city_data.empty else []

# Function to speak the output
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to capture voice input
def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        query = recognizer.recognize_google(audio)
        print(f"You said: {query}")
        return query.lower()
    except sr.UnknownValueError:
        print("Sorry, I did not understand that.")
        speak("Sorry, I did not understand that.")
        return None
    except sr.RequestError:
        print("Sorry, I'm unable to connect to the speech recognition service.")
        speak("Sorry, I'm unable to connect to the speech recognition service.")
        return None

# Function to detect city and intent from user's query
def process_query(query):
    categories = {
        'hotel': ['hotel', 'hotels', 'accommodation'],
        'hospital': ['hospital', 'hospitals', 'medical'],
        'tourist_spot': ['tourist spot', 'tourist spots', 'places to visit', 'attraction', 'attractions'],
        'church': ['church', 'churches']
    }

    intent = None
    city = None

    for key, keywords in categories.items():
        for word in keywords:
            if word in query:
                intent = key
                break
        if intent:
            break

    if not intent:
        return None, None

    match = re.search(r'in\s+([A-Za-z\s]+)|at\s+([A-Za-z\s]+)', query)
    if match:
        city = match.group(1) if match.group(1) else match.group(2)
        city = city.strip()
    else:
        return intent, None

    return intent, city

# Function to add messages in the chat window
def add_message(frame, text, sender):
    msg_frame = Frame(frame, bg="white", pady=5)
    
    if sender == "user":
        lbl = Label(msg_frame, text=text, bg="#DCF8C6", anchor="e", justify="left", padx=10, pady=5, font=("Arial", 12), wraplength=250)
        lbl.pack(anchor="e", fill="x")
    else:
        lbl = Label(msg_frame, text=text, bg="#FFFFFF", anchor="w", justify="left", padx=10, pady=5, font=("Arial", 12), wraplength=250)
        lbl.pack(anchor="w", fill="x")

    msg_frame.pack(fill="x", padx=10, pady=5, anchor="e" if sender == "user" else "w")

# Function to make the chat scrollable and auto-scroll
def update_scroll_region(canvas, chat_frame):
    canvas.update_idletasks()
    canvas.config(scrollregion=canvas.bbox("all"))
    canvas.yview_moveto(1)  # This will auto-scroll to the bottom

# Function to run the assistant
def start_assistant(chat_frame, canvas, root):
    while True:
        user_input = listen()
        if user_input:
            # Check for exit commands
            if any(exit_word in user_input for exit_word in ["exit", "bye", "ok bye", "quit", "goodbye"]):
                add_message(chat_frame, "Thank you for using TravelGuru. Have a nice day!", "assistant")
                speak("Thank you for using TravelGuru. Have a nice day!")
                root.after(2000, root.destroy)  # Close the window after 2 seconds to allow speaking
                break

            # Display user's input in the chat
            add_message(chat_frame, user_input, "user")

            # Process the query
            intent, city = process_query(user_input)

            if intent and city:
                if intent == 'hotel':
                    data = get_data(hotels_df, city)
                    category_name = "hotels"
                elif intent == 'hospital':
                    data = get_data(hospitals_df, city)
                    category_name = "hospitals"
                elif intent == 'tourist_spot':
                    data = get_data(tourist_spots_df, city)
                    category_name = "tourist spots"
                elif intent == 'church':
                    data = get_data(churches_df, city)
                    category_name = "churches"
                else:
                    data = []
                    category_name = "unknown category"

                if data:
                    limited_data = data[:10]
                    response = f"Here are some {category_name} in {city}: " + ", ".join(limited_data)
                else:
                    response = f"Sorry, I couldn't find any {category_name} in {city}."
            else:
                response = "Sorry, I didn't understand your request."

            # Display assistant's response in the chat
            add_message(chat_frame, response, "assistant")
            speak(response)
            
            # Ensure chat scrolls as new messages come in
            update_scroll_region(canvas, chat_frame)

# Function to handle the button click and start the assistant in the same window
def on_button_click():
    # Remove the start button
    start_button.pack_forget()

    # Create a scrollable canvas for the chat area
    canvas = Canvas(root)
    scrollbar = Scrollbar(root, command=canvas.yview)
    canvas.config(yscrollcommand=scrollbar.set)
    canvas.pack(side=tk.LEFT, fill="both", expand=True)
    scrollbar.pack(side=tk.RIGHT, fill="y")

    chat_frame = Frame(canvas)
    canvas.create_window((0, 0), window=chat_frame, anchor="nw", width=root.winfo_width())

    # Start the assistant in a new thread
    thread = threading.Thread(target=start_assistant, args=(chat_frame, canvas, root))
    thread.start()

    # Ensure scroll region is updated
    update_scroll_region(canvas, chat_frame)

# Set up main GUI
root = tk.Tk()
root.title("Voice Assistant")
root.geometry("400x600")
root.grid_columnconfigure(0, weight=1)  # Make sure the window is resizable

# Create a button to activate the assistant
start_button = tk.Button(root, text="Start Voice Assistant", command=on_button_click, font=("Arial", 14), bg="#25D366", fg="white")
start_button.pack(pady=20)

# Run the Tkinter main loop
root.mainloop()
