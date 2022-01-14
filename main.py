from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import speech_recognition as sr

def speech_recognition():
    global command
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        command = r.recognize_google(audio, language="en-US")

        print(f"What I heard: {command}")
        print("Searching on Google...")
    except Exception as e:
        print("An error occurred:")
        print(e)

speech_recognition()

PATH = "/Library/chromedriver" #path for your chromedriver
driver = webdriver.Chrome(PATH)
driver.get("https://google.com")

textbox = driver.find_element_by_name("q")
textbox.send_keys(command)
textbox.send_keys(Keys.RETURN)

#we are now done!
#run it yourself and see the output!
