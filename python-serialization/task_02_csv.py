#!/usr/bin/env python3
import csv
import json

def convert_csv_to_json(csv_filename):
    """
    Convert a CSV file to JSON format and write to 'data.json'.
    
    Parameters:
    csv_filename (str): The name of the input CSV file.
    
    Returns:
    bool: True if conversion is successful, False if an error occurs.
    """
    try:
        # Open and read the CSV file using csv.DictReader
        with open(csv_filename, mode='r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            
            # Convert CSV data to a list of dictionaries
            data = [row for row in csv_reader]
        
        # Write the data to a JSON file
        with open('data.json', mode='w') as json_file:
            json.dump(data, json_file, indent=4)
        
        return True
    
    except FileNotFoundError:
        print(f"Error: The file {csv_filename} was not found.")
        return False
    
    except Exception as e:
        print(f"Error: {e}")
        return False
