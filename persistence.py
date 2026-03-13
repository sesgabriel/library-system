# The persistence module of the program

import json
import os 

archive = 'data_bank.json'

def save_data(data):
    try:
        with open(archive, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4)
            print('Data saved succesfully!')
    except Exception as e:
        print(f'Error to save: {e}')

def load_data():
    if not os.path.exists(archive):
        return {}
    try:
        with open(archive, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception:
        return {}
    
