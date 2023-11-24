import logo from "./logo.svg";
import "./App.css";

import React, { useEffect, useState } from "react";
import { fetchCharacterData } from "./api/fetchCharacterData";

function App() {
  // Set states and char
  const [char, setChar] = useState([]);
  // Fetch Character Data
  useEffect(() => {
    fetchCharacterData(setChar);
  }, []);

  //console.log(JSON.parse(char._proficiencies));
  console.log(char._proficiencies)
  //console.log(char._proficiencies.Armor);

  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p></p>
        <div>
          <ul>
            <li>Character Name: {char.name}</li>
            <li>Character Class: {char._class}</li>
            <li>Character Class: {char._class}</li>
            <li>Character Armor proficiencies: </li>
          </ul>
        </div>
      </header>
    </div>
  );
}

export default App;
