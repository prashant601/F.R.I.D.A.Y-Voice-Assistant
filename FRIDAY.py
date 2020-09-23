import pyttsx3 #"pip install pyttsx3"   type all this quoted commands in terminal to install packages
import speech_recognition as sr #"pip install speechRecognition"
import datetime
import wikipedia  #"pip install wikipedia" 
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[2].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning sir")

    elif hour>=12 and hour<18:
        speak("Good Afternoon sir")   

    else:
        speak("Good Evening sir")  

    speak("hi ,this is friday, your personal desktop assistant" )       

def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening..")
        r.pause_threshold = 0.8
        audio = r.listen(source)

    try:
        print("Recognizing..")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except:
        print("Say that again please :) ")  
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('your mail id ', 'your-password')
    server.sendmail('recipents mail id ', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
    
        query = takeCommand().lower()
        
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            #print(results)   //if you want to print the result 
            speak(results)

        elif 'hello' in query or 'hi' in query:
            speak("hi sir, what can i do for u") 
           
        elif 'full form of friday' in query:
            speak(' sir its Female Replacement Intelligent Digital Assistant Youth')
                                            
        elif 'what can you do ' in query:
            speak("sir , you can command me to open some website stuff, to open some app,or put down pc to sleep Et cetera. ps you program me specially for saving your time")         

        elif 'hi siri'  in query:  #this one is just for fun 
            speak("who the fuck is siri, i respect you sir but please dont do that again")   
        
        elif 'sorry' in query or 'apologize' in query:
            speak("its ok sir ;)")

        elif 'youtube' in query:
            webbrowser.open_new_tab("https://www.youtube.com/")
            speak('opening youtube')

        elif 'open google' in query:
            webbrowser.open_new_tab("https://www.google.com/")
            speak("opening google")

        elif 'open stackoverflow' in query:
            webbrowser.open_new_tab("https://stackoverflow.com/")    

        elif 'whatsapp' in query:
            speak("opening whatsapp") 
            webbrowser.open_new_tab("https://web.whatsapp.com/")   

        elif 'sleep' in query:
            speak("you pc is going to sleep mode sir") 
            os.system('rundll32.exe powrprof.dll,SetSuspendState 0,1,0')   

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif "open notepad" in query:
            speak("opening notepad sir")
            os.system('notepad') 
    
        elif "open camera" in query:
            speak("opening camera sir")
            os.system('camera')

        elif 'mail to' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "enter recipents mail here"    
                sendEmail(to, content)
                speak("mail has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry sir. I am not able to send this mail")    
