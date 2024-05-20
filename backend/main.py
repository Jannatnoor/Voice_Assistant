from flask import Flask, request, jsonify
from flask_cors import CORS
import speech_recognition as sr
import os
import webbrowser
import datetime
import pyttsx3
import pywhatkit
import wikipedia

app = Flask(__name__)
CORS(app)  # Add this line to enable CORS for your Flask app

chatStr = ""

def chat(query):
    global chatStr
    chatStr += f"Jannat: {query}\n Xabiar: "
    return "I'm sorry, but I can't chat without OpenAI."

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)    

def say(text):
    # Windows-specific command to speak text
   os.system(f'PowerShell -Command "Add-Type –AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak(\'{text}\')"')

def takeCommand():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            query = listener.recognize_google(voice)
            query = query.lower()
            if 'Xabiar' in query:
                query = query.replace('Xabiar', '')
                print(query)
    except:
        pass
    return query

def openSite(url):
    webbrowser.open(url)

@app.route('/welcome', methods=['GET'])
def handle_welcome():
    welcomeMsg = 'Welcome to Xabiar AI. How can I help you?'
    say(welcomeMsg)
    return jsonify({'message': welcomeMsg})

@app.route('/chat', methods=['POST'])
def handle_chat():
    data = request.get_json()
    query = data['query']
    response = chat(query)
    return jsonify({'query': query, 'response': response})

@app.route('/take-command', methods=['GET'])
def handle_take_command():
    query = takeCommand()
    response = "How can I help you?"
    
    if 'play' in query:
        song = query.replace('play', '')
        response = f"playing {song}"
        pywhatkit.playonyt(song)
    
    if "open youtube" in query.lower():
        openSite("https://www.youtube.com/")
        response = "Opening YouTube"
    elif "open wikipedia" in query.lower():
        openSite("https://www.wikipedia.org/")
        response = "Opening Wikipedia"
    
    elif 'who is this' in query:
        person = query.replace('who is this', '')
        info = wikipedia.summary(person, 1)
        print(info)
        say(info)
            
    elif "open google" in query.lower():
        openSite("https://www.google.com/")
        response = "Opening Google"
    
            
    elif "open music" in query.lower():
        musicPath = r"C:\Users\janna\Music\Playlists"  # Adjust this path to your music directory
        os.system(f"start {musicPath}")
        response = "Opening Music"
    elif "open gmail" in query.lower():
        openSite("https://mail.google.com/")
        response = "Opening Gmail"
    elif "open notepad" in query.lower():
        os.system("notepad.exe")
        response = "Opening Notepad"
    elif "open vs code" in query.lower():
        os.system("code")
        response = "Opening Visual Studio Code"
    elif "the time" in query.lower():
        strfTime = datetime.datetime.now().strftime("%H:%M")
        response = f"The time is {strfTime}"
    else:
        response = query  # Return the original query if no specific command is recognized
        
    say(response)

    return jsonify({'query': query, 'response': response})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
    
