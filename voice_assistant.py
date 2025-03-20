from commands import parse_command
from command_executor import execute_command
import speech_recognition as sr

def main():
    while True:
        command = listen()  # Assuming `listen()` is defined in voice_assistant.py
        if command:
            action = parse_command(command)
            if action:
                execute_command(action)
                print(f"Executing: {action}")
            else:
                print("Sorry, I don't understand that command.")




def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio)
            print("Recognized Text:", text)
            return text
        except sr.UnknownValueError:
            print("Sorry, I didn't catch that.")
            return None
        
if __name__ == "__main__":
    main()