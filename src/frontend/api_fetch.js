function fetchCharacterData() {
  const char_uuid = "aa6d8217-60e7-441b-b589-269c27cade62";
  fetch(
    "http://localhost:5000/character/aa6d8217-60e7-441b-b589-269c27cade62"
  )
    .then((response) => response.json())
    .then((data) => {
      document.getElementById("characterData").innerHTML = JSON.stringify(
        data,
        null,
        2
      );
    })
    .catch((error) => console.error("Error fetching data:", error));
}
