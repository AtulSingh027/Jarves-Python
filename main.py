import pyttsx3
import pyautogui
import os
import time
import webbrowser
import subprocess as s
import requests
import speech_recognition as sr
import datetime

# Initialize the recognizer and text-to-speech engine
r = sr.Recognizer()
engine = pyttsx3.init()

# Function to listen to user's voice
def Listen():
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            print("You said:", text)
        except sr.UnknownValueError:
            print("Sorry, I didn't catch that.")
            text = ""
        return text.lower()

# Function to speak
def Say(text):
    engine.say(text)
    engine.runAndWait()

# Function to get current time
def get_time():
    now = datetime.datetime.now().strftime("%I:%M %p")
    Say(f"The current time is {now}")

# Function to get weather (uses OpenWeatherMap API, replace 'YOUR_API_KEY' with an actual key)
def get_weather(city="Delhi"):
    api_key = "_"  # Replace with your API key
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    try:
        response = requests.get(url).json()
        temp = response["main"]["temp"]
        weather_desc = response["weather"][0]["description"]
        Say(f"The temperature in {city} is {temp} degrees Celsius with {weather_desc}.")
    except:
        Say("Unable to fetch weather details at the moment.")

def control_volume(action):
    """Control system volume."""
    if "up" in action:
         pyautogui.press("volumeup")
         time.sleep(0.2)
         pyautogui.press("volumeup")
         time.sleep(0.2)
         pyautogui.press("volumeup")
         time.sleep(0.2)
         pyautogui.press("volumeup")
         Say("Volume increased.")

    elif "down" in action:
        pyautogui.press("volumedown")
        time.sleep(0.2)
        pyautogui.press("volumedown")
        time.sleep(0.2)
        pyautogui.press("volumedown")
        time.sleep(0.2)
        pyautogui.press("volumedown")
        Say("Volume decreased.")

    elif "mute" in action:
        pyautogui.press("volumemute")
        Say("Volume muted.")        

# Main loop for listening to commands
while True:
    command = Listen()

    if "hi" in command:
        Say("Hello Boss, How can I help you?")

    elif "time" in command:
        get_time()

    elif "weather" in command:
        Say("Which city's weather do you want?")
        city = Listen()
        if city:
            get_weather(city)

    elif "open chrome" in command:
        Say("Opening Chrome")
        os.startfile("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")

    elif "volume" in command:
        control_volume(command)    

    elif "search" in command:
        Say("What should I search for?")
        query = Listen()
        if query:
            webbrowser.open(f"https://www.google.com/search?q={query}")
            Say(f"Searching for {query} on Google")

        elif "open documents" in command:
            Say("Opening Documents Boss")
            os.startfile("C:\\Users\\HP\\Documents")

     
    elif "search" in command:
        SearchQuery = command[7:]
        Say("Searching On GoogleBoss")
        webbrowser.open("https://www.google.com/search?q="+SearchQuery)
        

    
        
    elif "video" in command:
        SearchQuery = command[7:]
        Say("Searching On Youtube Boss")
        webbrowser.open("https://www.youtube.com/results?search_query="+SearchQuery)
        time.sleep(6)
        pyautogui.moveTo(400,330)
        time.sleep(0.5)
        pyautogui.click()

    elif "open camera" in command:
        Say("Ok Boss")
        s.Popen("Start microsoft.windows.camera:",shell=True)

    elif "close camera" in command:
        Say("Closing Camera, Boss")
        time.sleep(0.7)
        os.system("taskkill /IM WindowsCamera.exe /F")
        time.sleep(0.6)  
        
          
        
    elif "click my picture" in command:
        Say("Yes Boss")
        s.Popen("Start microsoft.windows.camera:",shell=True)
        time.sleep(1)
        pyautogui.moveTo(1875,550)
        time.sleep(1)
        pyautogui.click()        

    elif "stop" in command:
        Say("Goodbye Boss, see you soon!")
        break

    else:
        Say("Sorry, I didn't understand that.")
