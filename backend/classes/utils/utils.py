import json
from pathlib import Path


def get_class_features(Class: str, level: int = 0):
    features_path = Path('C:\Projects\DnD_App\src\\backend\data\classes\Barbarian\Barbarian.json')
    print(features_path.resolve())
    if features_path.exists():
        # Read JSON data from the file
        with features_path.open() as json_file:
            features = json.load(json_file)
    return features[f"lvl_{level}"]


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
