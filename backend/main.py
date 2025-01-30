from flask import Flask, request, jsonify
from flask_cors import CORS
import speech_recognition as sr
import os
import webbrowser
import datetime
import pyttsx3
import pywhatkit
import wikipedia
import logging

 
app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})  # Enable CORS for your Flask app
 
# Configure logging
logging.basicConfig(level=logging.INFO)
 
listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
 
# Flag to track whether the welcome message has been spoken
welcome_spoken = False
 
def say(text):
    escaped_text = text.replace("'", "''")
    os.system(f'PowerShell -Command "Add-Type –AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak(\'{escaped_text}\')"')
 
def takeCommand():
    query = ""
    try:
        with sr.Microphone() as source:
            logging.info('Listening...')
            voice = listener.listen(source)
            query = listener.recognize_google(voice)
            query = query.lower()
            if 'xabiar' in query:
                query = query.replace('xabiar', '')
                logging.info(f"Recognized command: {query}")
            else:
                logging.info("Keyword 'xabiar' not found in query.")
    except sr.RequestError as e:
        logging.error(f"Could not request results from Google Speech Recognition service; {e}")
    except sr.UnknownValueError:
        logging.error("Google Speech Recognition could not understand audio")
    except Exception as e:
        logging.error(f"Error: {e}")
    return query
 
def openSite(url):
    webbrowser.open(url)
 
def process_query(query):
    logging.info(f"Processing query: {query}")
    response = ""
    if 'play' in query:
        song = query.replace('play', '')
        response = f"Playing {song}"
        pywhatkit.playonyt(song)
    elif "open youtube" in query.lower():
        openSite("https://www.youtube.com/")
        response = "Opening YouTube"
    elif "open wikipedia" in query.lower():
        openSite("https://www.wikipedia.org/")
        response = "Opening Wikipedia"
    elif 'who is' in query:
        person = query.replace('who is', '')
        info = wikipedia.summary(person, 1)
        response = info
    elif "open google" in query.lower():
        openSite("https://www.google.com/")
        response = "Opening Google"
    elif "open music" in query.lower():
        musicPath = r"C:\Users\janna\Music\Playlists"
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
    elif "What's the time" in query.lower():
        strfTime = datetime.datetime.now().strftime("%H:%M")
        response = f"The time is {strfTime}"
    else:
        response = "I can't reply, I am not ChatGPT."
 
    return response
 
@app.route('/welcome', methods=['GET'])
def handle_welcome():
    global welcome_spoken
    welcomeMsg = 'Welcome to Xabiar AI. How can I help you?'
    if not welcome_spoken:
        say(welcomeMsg)
        welcome_spoken = True
    return jsonify({'message': welcomeMsg})
 
@app.route('/chat', methods=['POST'])
def handle_chat():
    data = request.get_json()
    query = data['query']
    logging.info(f"/chat endpoint called with query: {query}")
    response = process_query(query)
    say(response)  # Say the response only once
    return jsonify({'query': query, 'response': response})
 
@app.route('/take-command', methods=['GET'])
def handle_take_command():
    logging.info("/take-command endpoint called")
    query = takeCommand()
    response = process_query(query)
    say(response)  # Say the response only once
    return jsonify({'query': query, 'response': response})
 
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port)