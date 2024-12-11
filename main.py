from neuralintents import BasicAssistant
import speech_recognition as sr
import pyttsx3 as tts
import sys

# Initialize speech recognition and TTS
recognizer = sr.Recognizer()
speaker = tts.init()
speaker.setProperty('rate', 150)

# To-do list
todo_list = ["Wake", "Eat", "Code", "Sleep"]

# Microphone initialization
mic = sr.Microphone()

# Define intent methods
def speak_text(text):
    """Speaks the provided text using TTS."""
    speaker.say(text)
    speaker.runAndWait()

def create_note():
    speak_text("What do you want to write on your note?")

    done = False
    while not done:
        try:
            with mic as source:
                recognizer.adjust_for_ambient_noise(source, duration=2)
                audio = recognizer.listen(source)
                note = recognizer.recognize_google(audio).lower()

                speak_text("Choose a filename!")
                recognizer.adjust_for_ambient_noise(source, duration=2)
                audio = recognizer.listen(source)
                filename = recognizer.recognize_google(audio).lower()

            with open(f"{filename}.txt", 'w') as f:
                f.write(note)
                done = True
                speak_text(f"I successfully created the note {filename}.")

        except sr.UnknownValueError:
            speak_text("I did not understand you! Please try again.")

def add_todo():
    speak_text("What do you want to add?")

    done = False
    while not done:
        try:
            with mic as source:
                recognizer.adjust_for_ambient_noise(source, duration=2)
                audio = recognizer.listen(source)
                item = recognizer.recognize_google(audio).lower()

                todo_list.append(item)
                done = True
                speak_text(f"I added {item} to the to-do list!")

        except sr.UnknownValueError:
            speak_text("I did not understand you! Please try again.")

def show_todos():
    if todo_list:
        speak_text("The items on your to-do list are the following.")
        for item in todo_list:
            speak_text(item)
    else:
        speak_text("Your to-do list is empty.")

def hi():
    speak_text("Hello. What can I do for you?")

def quit_assistant():
    speak_text("Goodbye!")
    sys.exit(0)

# Initialize assistant with intents loaded from JSON
assistant = BasicAssistant('intents.json')

# Map intents to methods manually
assistant.intent_methods = {
    "greeting": hi,
    "create_note": create_note,
    "add_todo": add_todo,
    "show_todos": show_todos,
    "exit": quit_assistant
}

# Main loop to handle user input via microphone
while True:
    try:
        with mic as source:
            recognizer.adjust_for_ambient_noise(source, duration=1.5)
            audio = recognizer.listen(source)

            message = recognizer.recognize_google(audio).lower()
            print(f"Recognized: {message}")

        # Check for trigger word "Roxy"
        if "roxy" in message:
            hi()  # Call the greeting method
        elif "add" in message and "to do" in message:
            add_todo()
        elif "show" in message and "to do" in message:
            show_todos()
        elif "create" in message and "note" in message:
            create_note()
        elif "exit" in message:
            quit_assistant()
        else:
            speak_text("Sorry, I didn't understand that. Can you rephrase?")

    except sr.UnknownValueError:
        speak_text("I didn't catch that. Could you repeat it more clearly?")
