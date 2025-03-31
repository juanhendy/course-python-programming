# Case Study: Virtual Assistant using Python (Assistant.py)

# CLUE: import necessary libraries here
from turtle import listen
import speech_recognition as sr
import pyttsx3
import os
import webbrowser

class Assistant():
    def __init__(self, nama):
        self.nama = nama

    def speak(text):
        engine = pyttsx3.init()
        engine.say(text)
        engine.runAndWait()
    
    def listen():
        recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)

        try:
            command = recognizer.recognize_google(audio)
            print("You said:", command)
            return command.lower()
        except sr.UnknownValueError:
            return "Sorry, I didn't catch that."
        except sr.RequestError:
            return "Speech recognition service is unavailable."

    if __name__ == "__main__":
        speak("Hello! How can I assist you?")
        command = listen()
        speak(f"You said: {command}")

    def handle_command(command):
        if "open youtube" in command:
            pyttsx3.speak("Opening YouTube")
            webbrowser.open("https://www.youtube.com")
        elif "open google" in command:
            pyttsx3.speak("Opening Google")
            webbrowser.open("https://www.google.com")
        elif "open notepad" in command:
            pyttsx3.speak("Opening Notepad")
            os.system("notepad")
        else:
            pyttsx3.speak("Sorry, I don't understand that command.")

    if __name__ == "__main__":
        pyttsx3.speak("I'm ready! Say something.")
        command = listen()
        handle_command(command)
    
    # CLUE: create multiple functions here