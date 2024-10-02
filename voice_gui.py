import tkinter as tk
from tkinter import PhotoImage
import threading

# Import the voice assistant functions from the previous code
# Assuming the previous code is in a file named "voice_assistant.py"
from voice3 import run_voice_assistant as run_voice_assistant  # You need to replace this with your actual function import

# Function to handle button click and run the voice assistant
def start_voice_assistant():
    threading.Thread(target=run_voice_assistant).start()  # Run in a separate thread to keep the GUI responsive

# Create the main window
root = tk.Tk()
root.title("Cute Voice Assistant")
root.geometry("300x400")  # Set window size
root.configure(bg='#f0f8ff')  # Light blue background for a cute look

# Load an image for the button (optional) or create a round button
# If you want an image, use PhotoImage and update the file path
# cute_button_image = PhotoImage(file="cute_button.png")  # If you have a cute button image

# Create a canvas to make a circular button
canvas = tk.Canvas(root, width=300, height=400, bg='#f0f8ff', highlightthickness=0)
canvas.pack()

# Add a round button to the canvas
round_button = tk.Button(
    root,
    text="Let's Travel!",
    command=start_voice_assistant,
    bg="#ffb6c1",  # Light pink color
    fg="white",
    font=("Helvetica", 16, "bold"),
    relief="flat",
    bd=0,
    highlightthickness=0,
    activebackground="#ff69b4"  # Hot pink when pressed
)

# Create a circular shape around the button using the canvas
button_window = canvas.create_window(150, 200, window=round_button, height=120, width=120)
canvas.create_oval(60, 110, 240, 290, fill="#ffb6c1", outline="#ff69b4", width=3)

# Start the Tkinter event loop
root.mainloop()
