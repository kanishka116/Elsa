import pyttsx3
import datetime
import speech_recognition as sr  # sr is used for speech recognition 
import wikipedia

 

engine = pyttsx3.init('sapi5')   # sapi5 is the technology  for voice recoginition and synthesis provided by microsoft .
voices = engine.getProperty('voices')   # Gets the current value of a property .Valid names and values
engine.setProperty('voice',voices[0].id)  # voice[1]= female voice     voice[0]= male voice
     # Adds a property value to set to the event queue. Valid names and values



def speak(audio):  # this function is used for giving the voice for our program 
    engine.say(audio)  #Adds an utterance to speak to the event queue.
    engine.runAndWait()   
    """ Runs an event loop until all commands queued up until this method call
        complete. Blocks during the event loop and returns when the queue is
        cleared."""

def WishMe():
    hour = int(datetime.datetime.now().hour)   # this function wish us after running the program and also the timing according to the time 
    if hour>=0 and hour<12:
        speak("good morning himani")

    elif hour>=12 and hour<16:
        speak('Good Afternoon himani')
    
    else:
        speak('Good Evening himani')
    
    speak('My Name is Elsa . Tell Me How may i help you ')

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1   #seconds of non-speaking audio before a phrase is considered complete
        audio = r.listen(source)    # Records a single phrase

        try:
            print("Recognizing...")    
            query = r.recognize_google(audio, language='en-in') #Using google for voice recognition.
            print(f"User said: {query}\n")  #User query will be printed.

        except Exception as e:
            # print(e)    
            print("Say that again please...")   #Say that again will be printed in case of improper voice 
            return "None" #None string will be returned
        return query

if __name__ == "__main__":
    WishMe()
    while True:
    # if 1:
        query = takeCommand().lower() #Converting user query into lower case

        # Logic for executing tasks based on query
        if 'wikipedia' in query:  #if wikipedia found in the query then this block will be executed
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=3) 
            speak("According to Wikipedia")
            print(results)
            speak(results)