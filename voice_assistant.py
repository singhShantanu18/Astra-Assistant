import speech_recognition as sr
import pyttsx3
import os
import datetime
import requests

# Initialize text-to-speech engine
engine = pyttsx3.init()

def speak(text):
    """Convert text to speech."""
    engine.say(text)
    engine.runAndWait()

def recognize_speech():
    """Capture and recognize voice commands."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio)
        print(f"You said: {command}")
        return command.lower()
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand.")
        return ""
    except sr.RequestError:
        print("Network error.")
        return ""

def tell_date():
    """Tell the current date."""
    today = datetime.date.today()
    date_str = today.strftime("%B %d, %Y")
    speak(f"Today's date is {date_str}.")
    print(f"Today's date is {date_str}.")

def get_news():
    """Fetch and read the latest news using NewsAPI."""
    api_key = "ea089d5c341749d8a88a7c56669b9310"  
    url = f"https://newsapi.org/v2/top-headlines?country=in&apiKey=ea089d5c341749d8a88a7c56669b9310"  

    response = requests.get(url)
    news_data = response.json()

    if news_data["status"] == "ok":
        articles = news_data["articles"][:5]  # Get top 5 news headlines
        speak("Here are the top news headlines.")
        for i, article in enumerate(articles, 1):
            print(f"{i}. {article['title']}")
            speak(article['title'])
    else:
        print("Failed to fetch news.")
        speak("Sorry, I couldn't fetch the news at the moment.")

def process_command(command):
    """Process user commands and execute actions."""
    if "hello" in command:
        speak("Hey there! How can I help you today?")
    
    elif "what's the date" in command or "tell me today's date" in command:
        tell_date()

    elif "open notepad" in command:
        speak("Opening Notepad.")
        os.system("notepad")

    elif "close notepad" in command:
        speak("Closing Notepad.")
        os.system("taskkill /f /im notepad.exe")

    elif "open chrome" in command:
        speak("Opening Google Chrome.")
        os.system("start chrome")

    elif "close chrome" in command:
        speak("Closing Google Chrome.")
        os.system("taskkill /f /im chrome.exe")

    elif "open calculator" in command:
        speak("Opening Calculator.")
        os.system("calc")

    elif "close calculator" in command:
        speak("Closing Calculator.")
        os.system("taskkill /f /im calculator.exe")

    elif "open vs code" in command:
        speak("Opening Visual Studio Code.")
        os.system("code")

    elif "close vs code" in command:
        speak("Closing Visual Studio Code.")
        os.system("taskkill /f /im Code.exe")

    elif "open command prompt" in command:
        speak("Opening Command Prompt.")
        os.system("start cmd")

    elif "close command prompt" in command:
        speak("Closing Command Prompt.")
        os.system("taskkill /f /im cmd.exe")

    elif "tell me the news" in command:
        get_news()

    elif "exit" in command:
        speak("Goodbye! Have a great day!")
        exit()

    else:
        speak("I'm not sure I understand that command.")

# Main Execution
if __name__ == "__main__":
    speak("Ready to assist! Just say a command, and I'll do my best to help.")
    
    while True:
        user_command = recognize_speech()
        if user_command:
            process_command(user_command)
