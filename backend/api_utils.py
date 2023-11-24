def is_character_created(database_path, chr_uuid):
    with open(database_path, 'r') as f:
        characters = f.read().splitlines()

    return chr_uuid in characters
