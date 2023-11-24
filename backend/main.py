import json
from pathlib import Path
from fastapi.responses import JSONResponse


from api_utils import is_character_created
from fastapi import FastAPI, HTTPException, status

from classes import CharacterRequest


app = FastAPI()

data_path = Path.cwd() / 'data'
characters_path = data_path / 'characters'
database_path = characters_path / 'database.txt'


@app.get('/')
def index():
    return "Welcome to the DnD Character Management App!"


@app.post("/character")
def get_character(character: CharacterRequest):
    """Checks if the character requested has been created"""
    character_id = character.character_id
    if not character_id:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Character ID is missing")

    if not is_character_created(database_path, character_id):
        raise HTTPException(status_code=404, detail="Character not found")

    chr_path = characters_path / (character_id + '.json')
    with open(chr_path, "r") as chr_json:
        chr_data = json.load(chr_json)

    response = JSONResponse(chr_data, status_code=status.HTTP_200_OK)

    return response
