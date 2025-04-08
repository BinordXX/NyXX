import json
import os

class Config:
    """
    Configuration handler for NyXX system-wide settings.
    Loads settings from a JSON file and allows for easy access to them.
    """

    def __init__(self, config_file="config/system_config.json"):
        self.config_file = config_file
        self.config_data = self.load_config()

    def load_config(self):
        """
        Loads the configuration data from the specified JSON file.
        """
        if not os.path.exists(self.config_file):
            raise FileNotFoundError(f"Configuration file {self.config_file} not found.")
        
        with open(self.config_file, "r") as f:
            return json.load(f)

    def get(self, key, default=None):
        """
        Gets the value for a given configuration key.
        If the key does not exist, returns the default value.
        """
        return self.config_data.get(key, default)

    def set(self, key, value):
        """
        Sets the value for a given configuration key and updates the config file.
        """
        self.config_data[key] = value
        self.save_config()

    def save_config(self):
        """
        Saves the current configuration data back to the JSON file.
        """
        with open(self.config_file, "w") as f:
            json.dump(self.config_data, f, indent=4)

# Example of how this might be used:
if __name__ == "__main__":
    config = Config()

    # Get a config value (e.g., a path or an integer setting)
    db_path = config.get("database_path")
    print(f"Database path: {db_path}")

    # Update a config value
    config.set("new_feature_enabled", True)
