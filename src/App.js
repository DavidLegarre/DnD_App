import logo from "./logo.svg";
import "./App.css";

import React, { useEffect, useState } from "react";

function App() {
  const [char, setChar] = useState([]);
  // Fetch Character Data
  const fetchCharacterData = () => {
    const char_uuid = "aa6d8217-60e7-441b-b589-269c27cade62";
    const url = `http://localhost:5000/character/${char_uuid}`;
    console.log(url);
    try {
      fetch(url)
        .then((response) => {
          return response.json();
        })
        .then((data) => {
          setChar(data);
        });
    } catch (error) {
      console.error("Error fetching data: ", error);
    }
  };

  useEffect(() => {
    fetchCharacterData();
  }, []);

  const armorArray = JSON.parse(char._proficiencies.Armor);

  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <div>
          <ul>
            <li>Character Name: {char.name}</li>
            <li>Character Class: {char._class}</li>
            <li>Character Class: {char._class}</li>
            <li>Character Armor proficiencies: </li>
            <ul>
              {armorArray.map((item, index) => (
                <li>{item}</li>
              ))}
            </ul>
          </ul>
        </div>
      </header>
    </div>
  );
}

export default App;
