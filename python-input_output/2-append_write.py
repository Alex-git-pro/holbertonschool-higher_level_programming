#!/usr/bin/python3
def append_write(filename="", text=""):
    """
    Appends a string at the end of a text file (UTF8) and returns the number of characters added.

    Args:
        filename (str): The name of the file to append to. If the file does not exist, it will be created.
        text (str): The string to append to the file.

    Returns:
        int: The number of characters added to the file.
    """
    # Ouvrir le fichier en mode ajout ('a') et spécifier l'encodage UTF-8
    with open(filename, 'a', encoding='utf-8') as f:
        return f.write(text)
