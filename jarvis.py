import pyttsx3
import speech_recognition as sr
import datetime
import os
import cv2
import random
from requests import get
import wikipedia
import webbrowser
import pywhatkit
import smtplib
import sys
import time
import pyjokes
import pyautogui
import requests
from bs4 import BeautifulSoup
from temperature import temp
from pywikihow import search_wikihow
import psutil
import speedtest

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate',200)

def speak(audio):

    engine.say(audio)
    print(audio)
    engine.runAndWait()

def takecommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1
        audio = r.listen(source,timeout=8,phrase_time_limit=5)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language='en-in')
        print(f"user said: {query}")
    except Exception as e:
        speak("Say that again please...")
        return "none"
    query = query.lower()
    return query

def wish():

    hour = int(datetime.datetime.now().hour)
    tt = time.strftime("%H:%M:%S")
    if hour>=0 and hour<=12:
        speak(f"good morning,its {tt}")
    elif hour>12 and hour<18:
        speak(f"good afternoon,its {tt}")
    else:
        speak(f"good evening,its {tt}")
    speak("i am jarvis ma'am please tell me how can i help you")

def semdEmail(to,content):

    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login("garvitatyagi2@gmail.com","Garvita!@#123")
    server.sendmail('garvitatyagi2@gmail.com',to,content)
    server.close()

def news():

    main_url = 'http://newsapi.org/v2/top-headlines?sources=techcrunch&apikey=310089a010c24ce0abaffe58086d2c0c'
    main_page = requests.get(main_url).json()
    articles = main_page["articles"]
    head = []
    day=["first","seconds","third","fouth","five","sixth","seventh","eighth","ninth","tenth"]
    for ar in articles:
        head.append(ar["title"])
    for i in range (len(day)):
        speak(f"today's { day[i]} news is:{head[i]}")

if _name_ == "_main_":

    wish()

    while True:

        query = takecommand().lower()

        if "switch the window" in query:

            pyautogui.keyDown("alt")
            pyautogui.press("tab")
            time.sleep(1)
            pyautogui.keyUp("alt")

        elif "open notepad" in query:

           npath = "C:\\Windows\\WinSxS\\amd64_microsoft-windows-notepad_31bf3856ad364e35_10.0.22000.653_none_6a6258f1f542ccd6"
           os.startfile(npath)

        elif "open command prompt" in query:

            os.system("start cmd")
        
        elif "what is your name" in query:

            speak('my name is JARVIS')
 
        elif "stands for" in query:

            speak('JARVIS stands for JUST A RATHER VERY INTELLIGENT SYSTEM')

        elif "open camera" in query:

            cap = cv2.VideoCapture(0)
            while True:
                ret, img = cap.read()
                cv2.imshow('wedcam', img) 
                k = cv2.waitKey(50)
                if k==27:
                    break;
                cap.release()
                cv2.destroyAllWindows()

        elif 'open music' in query:

            music_dir = "Music"
            songs = os.listdir(music_dir)
            rd = random.choice(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'ip address' in query:

            ip = get("https://api.ipify.org").text
            speak(f"your ip address is {ip}")

        elif 'time' in query:

            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'open wikipedia' in query:

            speak('Searching wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:

            webbrowser.open('www.youtube.com')

        elif 'open google' in query:

            speak("mam,what should i search on google")
            cm = takecommand().lower()
            webbrowser.open(f"{cm}")

        elif 'open facebook' in query:

            webbrowser.open("www.facebook.com")

        elif 'open instagram' in query:

            webbrowser.open("www.instagram.com")

        elif 'open twitter' in query:

            webbrowser.open("www.twitter.com")

        elif 'open stackoverflow' in query:

            os.system("stackoverflow.com")

        elif 'battery' in query:

            battery = psutil.sensors_battery()
            percentage = battery.percent
            speak(f"mam our system have {percentage} percent battery")

        elif 'internet speed' in query:

            st = speedtest.Speedtest()
            dl = st.download()
            up = st.upload()
            speak(f"mam we have {dl} bit per second downloading speed and {up} bit per second uploading speed.")

        elif 'send message' in query:

            speak("message has been sent")
            speak("what message you want to send")
            message=takecommand().lower()
            hour=int(datetime.datetime.now().hour)
            min=int(datetime.datetime.now().minute)
            speak("phone number:")
            contact=takecommand().lower()   
            contact="+91"+ str(contact)      
            pywhatkit.sendwhatmsg(f"{contact}",message,time_hour=hour,time_min=min) 

        elif 'play song on youtube' in query:

            pywhatkit.playonyt("see you again")

        elif 'email to garvita' in query:

            try:
                speak("what should i say")
                content = takecommand().lower()
                to = "garvitatyagi2809@gmail.com"
                semdEmail(to,content)
                speak("Email has been send to garvita")

            except Exception as e:
                print(e)
                speak("sorry ma'am,i am not able to sent this mail to end")

        elif 'weather' in query:
            
            search = "temperature in moradabad"
            url = (f"https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwjlq5fmorz7AhXGSGwGHf5oBn0QFnoECAoQAQ&url=https%3A%2F%2Fwww.timeanddate.com%2Fweather%2Findia%2Fmoradabad%2Fext&usg=AOvVaw1GPTqfTGvlOSvQFVuaZHpQ")
            r = requests.get(url)
            data = BeautifulSoup(r.text,"html.parser")
            temp = data.find("div",class_="BNeawe").text
            speak(f"current {search} is {temp}")
            print(results)
            speak(results)

        elif 'how to do mode' in query:

            speak("how to do mode is activated please tell me what you want to know")
            how = takecommand()
            max_results = 1
            how_to = search_wikihow(how, max_results)
            assert len(how_to) == 1
            how_to[0].print()
            speak(how_to[0].summary)

        elif 'no thanks' in query:

            speak('thanks for using me mam,have a good day')
            sys.exit()

        elif 'close notepad' in query:

            speak('okay mam,closing notepad')
            os.system('taskkill /f /im notepad.exe')

        elif 'close command prompt' in query:

            speak('okay mam,closing command prompt')
            os.system('taskkill /f /im cmd.exe')

        elif 'close music' in query:

            speak('okay mam,closing music')
            os.system('taskkill /f /im music.exe')

        elif 'close google' in query:

             speak("okay mam,closing google")
             os.system("taskkill /im google.exe /f")

        elif 'close facebook' in query:

            speak('okay mam,closing facebook')
            os.system('taskkill /im facebook.com.exe')

        elif 'close instagram' in query:

            speak('okay mam,closing instagram')
            os.system('taskkill /f /im instagram.com.exe')

        elif 'close sendmessage' in query:

            speak("okay mam,closing sendmessage")
            os.system("taskkill /f /im sendmessage.exe")

        elif 'close Email' in query:

            speak('okay mam,closing Email')
            os.system('taskkill /f /im Email.exe')

        elif 'close youtube' in query:

            speak('okay mam,closing youtube')
            os.system('taskkill /f /im youtube.exe')

        elif 'close twitter' in query:

            speak('okay mam,closing twitter')
            os.system('taskkill /f /im twitter.com.exe')

        elif 'set alarm' in query:

            nn = int(datetime.datetime.now().hour)
            if nn==22:
                music_dir = 'music'
                songs = os.listdir(music_dir)
                os.startfile(os.path.join(music_dir,songs[0]))            

        elif 'joke' in query:

            joke = pyjokes.get_joke()
            speak(joke)

        elif 'tell me the news' in query:

            speak("please wait mam,feteching the latest news")
            news()

        elif 'take rest' in query:

            speak("take care")
            speak("bye")
            sys.exit()    

        elif 'shut down the system' in query:

            os.system('shutdown /s /t S')

        elif 'restart the system' in query:

            os.system('shutdown /r /t S')

        elif 'sleep the system' in query:

            os.system('rundll32.exe powrprof.dil,SetSuspendState 0,1,0')

        elif 'hello' in query or 'hey' in query:

            speak("hello mam, may i help you with something.")

        elif 'how are you' in query:

            speak("i am fine mam, what about you.")

        elif 'also good' in query or 'fine' in query:

            speak("that's great to hear from you.")

        elif 'thank you' in query or 'thanks' in query:

            speak("it's my pleasure mam.")

        elif 'you can sleep' in query or 'sleep now' in query:

            speak("ok mam,i am going to sleep you can call me anytime.")
            sys.exit()

if _name_ == "_main_":

    while True:

        permission = takecommand()

        if 'goodbye' in permission:
            speak("thanks for using me, have a god day.")
            sys.exit()
