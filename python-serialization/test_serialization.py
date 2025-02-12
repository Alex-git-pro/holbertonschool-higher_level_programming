#!/usr/bin/env python3
from task_00_basic_serialization import load_and_deserialize, serialize_and_save_to_file

# Données à sérialiser
data_to_serialize = {
    "name": "John Doe",
    "age": 30,
    "city": "New York"
}

# Sérialiser les données et les sauvegarder dans un fichier JSON
serialize_and_save_to_file(data_to_serialize, 'data.json')

# Charger et désérialiser les données depuis le fichier 'data.json'
deserialized_data = load_and_deserialize('data.json')

# Afficher les données désérialisées
print("Données désérialisées :")
print(deserialized_data)
