import json
from pathlib import Path

from flask import Flask, jsonify

from src.backend.api_utils import is_character_created

app = Flask("DnD_App")
data_path = Path.cwd() / 'data'
characters_path = data_path / 'characters'
database_path = characters_path / 'database.txt'


@app.route('/')
def index():
    return "Welcome to the DnD Character Management App!"


@app.route("/character/<uuid>", methods=["GET"])
def get_character(uuid):
    """Checks if the character requested has been created"""
    uuid = str(uuid)

    if not is_character_created(database_path, uuid):
        return jsonify({'error': 'character not found'}), 404

    chr_path = characters_path / (uuid + '.json')
    with open(chr_path, "w") as chr_json:
        chr_data = json.load(chr_json)
    return jsonify(chr_data)
