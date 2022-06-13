import pyttsx3
import datetime
import speech_recognition as sr
import playsound
import wikipedia
import smtplib
import webbrowser as wb
import os
import pyautogui
import psutil 
import json
from urllib.request import urlopen
import requests

assist = pyttsx3.init()


def customize(i,voice_rate):
    voice = assist.getProperty('voices')
    assist.setProperty('voice', voice[i].id)
    assist.setProperty('rate', voice_rate)
def speak(audio):
    assist.say(audio)
    assist.runAndWait()
def get_time():
    time = datetime.datetime.now().strftime("%H:%M:%S")
    speak("The current time is: ")
    speak(time)
def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    day = int(datetime.datetime.now().day)
    speak("Today's date is ")
    speak(day)
    speak(month)
    speak(year)
def wish():
    speak("Welcome back!")
    hour = datetime.datetime.now().hour
    if hour>= 6 and hour < 12:
        speak("Good Morning")
    elif hour>=12 and hour< 18:
        speak("Good afternoon")
    elif hour >= 18 and hour < 24:
        speak("Good evening")
    else:
        speak("GoodNight, Time to sleep")

def cpu():
    usage = str(psutil.cpu_percent())
    speak("CPU is at " + usage)

    battery = psutil.sensors_battery()
    plugged = battery.power_plugged
    speak("Your battery is at ")
    speak(str(battery.percent))
    plugged = speak("Plugged In") if plugged else speak("Not Plugged In")
    # print(percent+'% | '+plugged)

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold =1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language= 'en-in')
        # print(query)
    except Exception as e:
        print(e)
        speak("Please repeat")

        return "None"
    return query

def screenshot():
    img = pyautogui.screenshot()

    img.save("C:/Users/Dell/OneDrive/Pictures/Screenshots/ss.png")

def sendmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login("rachel18.rc11@gmail.com", "************" )
    server.sendmail("rc5409@srmist", to, content)
    server.close()

customize(2,220)

if __name__ == "__main__":
    wish()
    speak("How may I help you Today?")
    while True:
        query = takeCommand().lower()
        print (query)

        if "time" in query:
            get_time()
        elif "date" in query:
            date()
        elif "offline" in query:
            speak("Going offline, bye")
            quit()

        elif 'how are you' in query:
            speak("I am fine, Thank you")
            speak("How are you, Sir")
 
        elif 'fine' in query or "good" in query:
            speak("It's good to know that your fine")

        elif "wikipedia" in query:
            speak("Searching...")
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences = 3)
            speak(result)

        elif "where is" in query:
            query = query.replace("where is", "")
            location = query
            speak("User asked to Locate")
            speak(location)
            wb.open("https://www.google.nl / maps / place/" + location + "")

        elif 'news' in query:
             
            try:
                jsonObj = urlopen('''https://newsapi.org / v1 / articles?source = the-times-of-india&sortBy = top&apiKey =\\times of India Api key\\''')
                data = json.load(jsonObj)
                i = 1
                 
                speak('here are some top news from the times of india')
                print('''=============== TIMES OF INDIA ============'''+ '\n')
                 
                for item in data['articles']:
                     
                    print(str(i) + '. ' + item['title'] + '\n')
                    print(item['description'] + '\n')
                    speak(str(i) + '. ' + item['title'] + '\n')
                    i += 1
            except Exception as e:
                 
                print(str(e))

        elif "weather" in query:
             
            # Google Open weather website
            # to get API of Open weather
            # api_key = "275ca1ca8a9264a066713c24bf809cff"
            # base_url = "http://api.openweathermap.org / data / 2.5 / forecast?"
            speak(" City name ")
            print("City name : ")
            city_name = takeCommand()
            # complete_url = base_url + "appid =" + api_key + "&q =" + city_name
            complete_url = "http://api.openweathermap.org/data/2.5/forecast?id=524901&appid=275ca1ca8a9264a066713c24bf809cff"+"&q =" + city_name
            response = requests.get(complete_url)
            x = response.json()
             
            if x["cod"] != "404":
                y = x["main"]
                current_temperature = y["temp"]
                current_pressure = y["pressure"]
                current_humidiy = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                print(" Temperature (in kelvin unit) = " +str(current_temperature)+"\n atmospheric pressure (in hPa unit) ="+str(current_pressure) +"\n humidity (in percentage) = " +str(current_humidiy) +"\n description = " +str(weather_description))
             
            else:
                speak(" City Not Found ")

        elif "send email" in query:
            try:
                speak("Please provide the content for the mail")
                content = takeCommand()
                to = "rc5409@srmist.edu.in"
                sendmail(to, content)
                speak("Mail sent successfully..")
            except Exception as e:
                # speak(e)
                print(e)
                speak("unable to send the message")

        elif "search in google" in query:
            speak("What should I search?")
            chrome_path = "C:\Program Files\Google\Chrome\Application\chrome.exe %s"
            search = takeCommand().lower()
            print(search)
            wb.get(chrome_path).open_new_tab(search + ".com")
        
        elif "play songs" in query:
            songs_dir = "D:\Rashmi\My music\Music"
            songs = os.listdir(songs_dir)
            print(list(songs))
            os.startfile(os.path.join(songs_dir, songs[0]))
        
        elif "remember that" in query:
            speak("what should I remember?")
            data = takeCommand()
            speak("You asked me to remember, " + data)
            remember = open("data.txt" , "w")
            remember.write(data)
            remember.close()

        elif "do you remember" in query:
            remember = open("data.txt", "r")
            speak("You asked me to remember that" + remember.read())

        elif "take screenshot"  in query:
            screenshot()
            speak("Done")

        elif "cpu" in query:
            cpu()
 


        elif "settings" in query:
            # speak("you can customize my voice rate and voice by: ")
            # sr.Recognizer.pause_threshold = 2
            speak("I have 3 voice options")
            customize(0,220)
            speak("This is my first voice option")
            customize(1,220)
            speak("This is my second voice option")
            customize(2,220)
            speak("This is my third voice option")
            speak("Please choose your preferred voice")
            change = takeCommand().lower()
            print (change)
            if "first" in change:
               customize(0,220)
            elif "second"  in change:
                customize(1,220)
            elif "third"  in change:
                customize(2,220)
            sr.Recognizer.pause_threshold = 5
            speak("This is the final changed voice, you can change it again by using settings")

            
            

# customize(2,220)
# speak("xyz")
# wish()
# date()
# get_time()
# takeCommand()


       