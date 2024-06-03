# Xabiar AI Voice Assistant

This is a voice assistant application developed for my thesis work. It uses a Python backend with Flask and a React frontend. The assistant can perform various tasks like playing music, opening websites, and providing information using voice commands.

## Features
- Voice recognition using Python's `speech_recognition` library.
- Text-to-speech responses using the `pyttsx3` library.
- tegration with external services like YouTube and Wikipedia for additional functionality.
- Web-based frontend for easy user interaction.

## Prerequisites
- Python 3.x

- Node.js and npm

## Getting Started

### Backend Setup

1. **Clone the repository:**
-- https://github.com/Jannatnoor/Voice_Assistant.git

   ```bash
   git clone <repository-url>
   cd <repository-directory>/backend

Create a virtual environment and activate it:

```bash enviroment (run following code):

-- python -m venv venv
-- source venv/bin/activate   # On Windows, use `venv\Scripts\activate`

Install the required packages for backend (run following code)):

-- pip install -r requirements.txt

1. First Generate `requirements.txt`

Generate the `requirements.txt` file with the installed packages (run following code):

-- pip freeze > requirements.txt

2. This should create a requirements.txt file that includes all the necessary dependencies. Here is an example of how the file should look:

Flask==2.0.1
Flask-CORS==3.0.10
SpeechRecognition==3.8.1
pyttsx3==2.90
pywhatkit==5.2
wikipedia-api==0.5.4


Ensure you have all these packages installed in your virtual environment before running `pip freeze` to generate your `requirements.txt`. You can install any missing packages using `pip install <package-name>``. Here's how you can generate the requirements.txt file (run following code):

-- pip install Flask Flask-CORS SpeechRecognition pyttsx3 pywhatkit wikipedia-api

3. Run the backend server:

-- python main.py

### Frontend Setup

1. Navigate to the frontend directory((run following code)):

-- cd ../frontend

2. Install the required packages (run following code):

-- npm install

3. Run the frontend server (run following code):

-- npm start



## Usage

-- Open your web browser and navigate to http://localhost:3000.
-- Click the microphone image to start giving voice commands.
-- The application will listen to your command, process it, and provide a response.

## Project Structure
backend/

main.py: The main Flask application.
requirements.txt: Python dependencies.
venv/: Python virtual environment directory (not included in the zip file).

frontend/

src/: React source files.
public/: Public assets.
.env: Environment variables.
package.json: Node.js dependencies.
package-lock.json: Lockfile for Node.js dependencies.
node_modules/: Node.js dependencies directory (not included in the zip file).


## Troubleshooting

#Backend Issues

--Ensure your virtual environment is activated before running the backend server.
--Check if all dependencies are installed using pip install -r requirements.txt.

#Frontend Issues

-- Ensure all Node.js dependencies are installed using npm install.
-- If something is already running on port 3000, you can change the port by running npm start and specifying a different port when prompted.



