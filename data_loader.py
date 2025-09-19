import os
import json

def load_toy_data():
    # Load toy data from raw zone JSON file
    toy_data_path = os.path.join('data', 'raw', 'toy_data.json')
    if os.path.exists(toy_data_path):
        with open(toy_data_path, 'r') as f:
            return json.load(f)
    return {"error": "Toy data file not found."}

def load_data(source_type="toy"):
    if source_type == "toy":
        return load_toy_data()
    # Future: Add logic for loading from local files or remote sources
    return {"error": "No data source configured."}
