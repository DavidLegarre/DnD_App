export const fetchCharacterData = () => {
  const char_uuid = "aa6d8217-60e7-441b-b589-269c27cade62";
  const url = ("http://localhost:5000/character/", char_uuid);
  console.log(url);
  return fetch(url).then((response) => {
    if (!response.ok){
      throw new Error('Network response was not ok');
    }
    return response.json();
  });
};
