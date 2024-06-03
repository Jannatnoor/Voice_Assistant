import React, { useState, useEffect } from "react";
import axios from "axios";

import microphoneImage from "./microphone.gif";
import "./App.css";

function App() {
  const [response, setResponse] = useState("");
  const [userQuery, setUserQuery] = useState("");
  const [welcomeMsg, setWelcomeMsg] = useState("");
  const [isListening, setIsListening] = useState(false);

  const fetchWelcomeMessage = async () => {
    try {
      const response = await axios.get("http://127.0.0.1:5000/welcome");
      setWelcomeMsg(response.data.message);
    } catch (error) {
      console.error("Error fetching welcome message:", error);
    }
  };

  useEffect(() => {
    fetchWelcomeMessage();
  }, []); // Empty dependency array ensures this effect runs only once when the component mounts

  const handleSpeechRecognition = async () => {
    if (isListening) return;

    setIsListening(true);
    try {
      console.log("Requesting speech recognition...");
      const res = await axios.get("http://127.0.0.1:5000/take-command");
      const query = res.data.query;
      setUserQuery(query);
      setResponse(res.data.response);
      console.log("Fetching chat response...");
      //fetchChatResponse(query);  //// this was the culprit 😤😤😤
    } catch (error) {
      console.error("Error fetching speech recognition:", error);
    } finally {
      setIsListening(false);
    }
  };

  return (
    <div className="app">
      <h1>{welcomeMsg}</h1>
      <div className="microphone-container">
        <img
          src={microphoneImage}
          alt="Microphone"
          onClick={handleSpeechRecognition}
          className={`mic-button ${isListening ? "disabled" : ""}`}
        />
      </div>
      <div>
        <h2>User Said:</h2>
        <p>{userQuery}</p>
        <h2>Response:</h2>
        <p>{response}</p>
      </div>
    </div>
  );
}

export default App;
