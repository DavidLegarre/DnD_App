import logo from "./logo.svg";
import "./App.css";

import React, { useEffect, useState } from "react";
import { fetchCharacterData } from "./api/fetchCharacterData";

function App() {
  // Set states and char
  const [char, setChar] = useState([]);
  // Fetch Character Data
  useEffect(() => {
    fetchCharacterData().then((data) => {
      setChar(data);
    }).catch((error) => {
      console.error("Error fetching data: ", error);
    });
  }, []);

  //console.log(JSON.parse(char._proficiencies));
  //console.log(char._proficiencies)
  //console.log(char._proficiencies.Armor);

  return (
    <div>
      {char.map(item => (
        <p key={item.id}>{item.name}</p>
      ))}
    </div>
  );
}

export default App;
