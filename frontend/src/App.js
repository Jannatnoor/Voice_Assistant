import React, { useState, useEffect } from 'react';
import axios from 'axios';

function App() {
  const [response, setResponse] = useState('');
  const [userQuery, setUserQuery] = useState('');
  const [welcomeMsg, setWelcomeMsg] = useState('');

  const fetchWelcomeMessage = async () => {
    try {
      const response = await axios.get('http://127.0.0.1:5000/welcome');
      setWelcomeMsg(response.data.message);
    } catch (error) {
      console.error('Error fetching welcome message:', error);
    }
  };

  useEffect(() => {
    fetchWelcomeMessage();
  }, []); // Empty dependency array ensures this effect runs only once when the component mounts

  const fetchChatResponse = async (query) => {
    try {
      const response = await axios.post('http://127.0.0.1:5000/chat', {
        query,
      });
      setResponse(response.data.response);
    } catch (error) {
      console.error('Error fetching chat response:', error);
    }
  };

  const handleSpeechRecognition = async () => {
    try {
      const response = await axios.get('http://127.0.0.1:5000/take-command');
      const query = response.data.query;
      setUserQuery(query); 
      setResponse(response.data.response);
      fetchChatResponse(query);
    } catch (error) {
      console.error('Error fetching speech recognition:', error);
    }
  };

  return (
    <div>
      <h1>{welcomeMsg}</h1>
      <button onClick={handleSpeechRecognition} style={{ padding: '20px' }}>
        Speak
      </button>
      <div>
        <h2>User Said:</h2>
        <p>{userQuery}</p> {/* Display user's spoken query */}
        <h2>Response:</h2>
        <p>{response}</p> {/* Display speech response */}
      </div>
    </div>
  );
}

export default App;
