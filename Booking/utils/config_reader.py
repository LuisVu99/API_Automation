import json
import os

def get_config(env):
    # Lấy thư mục của file config_reader.py
    current_dir = os.path.dirname(os.path.abspath(__file__))
    # Lên 1 level lên (từ utils/ lên Booking/)
    config_path = os.path.join(current_dir, "..", "config", f"{env}.json")
    with open(config_path) as file:
        return json.load(file)
    
def get_data(data_name):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    data_path = os.path.join(current_dir, "..", "data", f"{data_name}.json")
    with open(data_path) as file:
        return json.load(file)
