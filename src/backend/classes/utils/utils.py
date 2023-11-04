import json
from pathlib import Path


def get_class_features(Class: str, level: int):
    features_path = Path('C:\mis_archivos\Projects\DnD_App') / 'src' / 'backend' / 'data' / 'classes'
    features_path = features_path / 'Barbarian' / 'Barbarian.json'
    features = json.load(open(features_path, 'r'))
    features = features["lvl_0"]
    features_to_extract = [
        "hit_die", "HP_lvl1", "Proficiencies",
        "Saving_throws", "Starting_equipment"
    ]
    features_out = {}
    for feature in features_to_extract:
        if feature in features:
            features_out[feature] = features[feature]

    return features_out
