const fetchCharacterData = (setChar) => {
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

export { fetchCharacterData };