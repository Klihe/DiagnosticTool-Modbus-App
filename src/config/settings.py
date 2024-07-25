import json
import os

def load_settings() -> dict:
    """Load the settings from the settings.json file

    Raises:
        FileNotFoundError: If the settings.json file is not found

    Returns:
        dict: The settings from the settings.json file
    """
    
    # Check if the settings.json file exists
    if not os.path.isfile("src/config/settings.json"):
        # Raise an error if the file does not exist
        raise FileNotFoundError("src/config/settings.json not found")
    
    # Open the settings.json file
    with open("src/config/settings.json", "r") as file:
        # Load the settings from the file
        return json.load(file)