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


def seconds_to_hms(seconds):
    """
    Convert seconds to hours, minutes, and seconds.

    Args:
    - seconds (float): Time in seconds.

    Returns:
    - str: Time in the format "h:m:s".
    """
    hours, remainder = divmod(seconds, 3600)
    minutes, seconds = divmod(remainder, 60)

    return "{:02}:{:02}:{:02}".format(int(hours), int(minutes), int(seconds))


def clean_upper(string: str):
    return (
        string
        .strip()
        .upper()
    )


def clean_lower(string: str):
    return (
        "_".join(string)
        .strip()
        .lower()
    )
