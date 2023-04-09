import React, { useState, useEffect } from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import './App.css';

function App() {
  const [commands, setCommands] = useState([]);

  useEffect(() => {
    fetchCommands();
  }, []);

  const fetchCommands = async () => {
    // Replace this URL with the URL of your backend API
    const response = await fetch('http://192.168.122.187:5000/commands');
    const data = await response.json();
    setCommands(data);
  };
  return (
    <div className="App">
      <header className="bg-primary text-white text-center py-5">
        <h1>Unix Commands</h1>
      </header>
      <div className="container mt-5">
        <ul className="list-group">
          {commands.map((command) => (
            <li key={command.id} className="list-group-item">
              <h2 className="h4">{command.name}</h2>
              <p>{command.description}</p>
            </li>
          ))}
        </ul>
      </div>
    </div>
  );
}

export default App;

