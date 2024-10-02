import speech_recognition as sr
import pyttsx3
import pandas as pd
import spacy
import tkinter as tk
from tkinter import Frame, Label, Scrollbar, Canvas
import threading
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline

# Initialize text-to-speech engine
engine = pyttsx3.init()
engine.setProperty('rate', 180)

# Load the CSV files for hotels, hospitals, tourist spots, and churches
try:
    hotels_df = pd.read_csv('hotels.csv')
    hospitals_df = pd.read_csv('hospitals.csv')
    tourist_spots_df = pd.read_csv('tourist_spots.csv')
    churches_df = pd.read_csv('churches.csv')

    # Load intent CSVs for each category
    hotels_intent_df = pd.read_csv('hotels_intents.csv')
    hospitals_intent_df = pd.read_csv('hospitals_intents.csv')
    tourist_spots_intent_df = pd.read_csv('tourist_spots_intents.csv')
    churches_intent_df = pd.read_csv('churches_intents.csv')

except Exception as e:
    print(f"Error loading CSV files: {e}")

# Load spaCy model for NER (Named Entity Recognition)
nlp = spacy.load('en_core_web_sm')

# Function to train an intent model for a given dataset
def train_intent_model(intent_df):
    X = intent_df['query']
    y = intent_df['intent']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    intent_pipeline = Pipeline([
        ('tfidf', TfidfVectorizer()),
        ('classifier', LogisticRegression(max_iter=1000))  # Increased max_iter for better convergence
    ])
    intent_pipeline.fit(X_train, y_train)

    return intent_pipeline

# Train models for each category
hotels_intent_model = train_intent_model(hotels_intent_df)
hospitals_intent_model = train_intent_model(hospitals_intent_df)
tourist_spots_intent_model = train_intent_model(tourist_spots_intent_df)
churches_intent_model = train_intent_model(churches_intent_df)

# Train a city classifier using the combined data
def train_city_model():
    combined_df = pd.concat([hotels_intent_df, hospitals_intent_df, tourist_spots_intent_df, churches_intent_df])
    X_city = combined_df['query']
    y_city = combined_df['city']

    X_train_city, X_test_city, y_train_city, y_test_city = train_test_split(X_city, y_city, test_size=0.2, random_state=42)
    
    city_pipeline = Pipeline([
        ('tfidf', TfidfVectorizer()),
        ('classifier', LogisticRegression(max_iter=1000))
    ])
    city_pipeline.fit(X_train_city, y_train_city)

    return city_pipeline

# Train the city model
city_pipeline = train_city_model()

# Extract city name using spaCy NER
def extract_city_with_spacy(query):
    doc = nlp(query)
    for ent in doc.ents:
        if ent.label_ == 'GPE':  # GPE stands for Geopolitical Entity
            return ent.text
    return None

# Get data based on category and city
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

# Function to classify intent based on query
def classify_intent(query):
    intent_predictions = {
        'hotel': hotels_intent_model,
        'hospital': hospitals_intent_model,
        'tourist spot': tourist_spots_intent_model,
        'church': churches_intent_model
    }
    
    # Generalize intent classification for any query
    for keyword, model in intent_predictions.items():
        if keyword in query:
            return model.predict([query])[0]

    # Fallback intent
    return "unknown"

# Function to add messages in the chat window
def add_message(frame, text, sender):
    msg_frame = Frame(frame, bg="white", pady=5)
    
    if sender == "user":
        lbl = Label(msg_frame, text=text, bg="#DCF8C6", anchor="e", justify="left", padx=10, pady=5, font=("Arial", 12), wraplength=250)
        lbl.pack(anchor="e")
    else:
        lbl = Label(msg_frame, text=text, bg="#FFFFFF", anchor="w", justify="left", padx=10, pady=5, font=("Arial", 12), wraplength=250)
        lbl.pack(anchor="w")

    msg_frame.pack(fill="both", padx=10, pady=5, anchor="e" if sender == "user" else "w")

# Function to make the chat scrollable
def update_scroll_region(canvas):
    canvas.update_idletasks()
    canvas.config(scrollregion=canvas.bbox("all"))

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

            # Process the query to get intent and city
            intent = classify_intent(user_input)
            city = extract_city_with_spacy(user_input)
            if not city:
                city = city_pipeline.predict([user_input])[0]

            print(f"Predicted intent: {intent}, Predicted city: {city}")

            # Get data based on the intent and city
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

            # Display assistant's response in the chat
            add_message(chat_frame, response, "assistant")
            
            # Speak the response after adding it to the chat
            speak(response)
            
            # Ensure chat scrolls as new messages come in
            update_scroll_region(canvas)

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
    update_scroll_region(canvas)

# Create the main window
root = tk.Tk()
root.title("Voice Assistant for Travel Info")
root.geometry("400x600")

# Add a welcome message and start button
welcome_label = Label(root, text="Welcome to TravelGuru! Speak to get travel information.", font=("Arial", 14), pady=20)
welcome_label.pack()

start_button = tk.Button(root, text="Start", command=on_button_click, bg="#25D366", fg="white")
start_button.pack(pady=20)

# Run the Tkinter main loop
root.mainloop()
