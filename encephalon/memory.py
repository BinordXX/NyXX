# NyXX/encephalon/memory.py

import json
from datetime import datetime
from NyXX.utils.logging import log_info, log_error


class Memory:
    """
    A class that stores and manages CoreMind's memory.
    Memory helps CoreMind make decisions based on historical data.
    """

    def __init__(self, memory_file="memory.json"):
        """
        Initialize the memory system.
        :param memory_file: The file where the memory is saved. (Defaults to memory.json)
        """
        self.memory_file = memory_file
        self.memory_data = self.load_memory()

    def load_memory(self):
        """
        Load the memory data from the specified memory file.
        If the file does not exist, create a new empty memory.
        """
        try:
            with open(self.memory_file, "r") as file:
                memory_data = json.load(file)
            log_info("Memory successfully loaded.")
            return memory_data
        except (FileNotFoundError, json.JSONDecodeError) as e:
            log_error(f"Error loading memory: {str(e)}. Creating new memory file.")
            return {}

    def save_memory(self):
        """
        Save the current memory to the memory file.
        """
        try:
            with open(self.memory_file, "w") as file:
                json.dump(self.memory_data, file, indent=4)
            log_info("Memory successfully saved.")
        except Exception as e:
            log_error(f"Error saving memory: {str(e)}")

    def store_event(self, event_data):
        """
        Store an event in CoreMind's memory.
        :param event_data: A dictionary containing information about the event.
        """
        event_timestamp = datetime.now().isoformat()
        event_data["timestamp"] = event_timestamp
        self.memory_data[event_timestamp] = event_data
        self.save_memory()
        log_info(f"Event stored: {event_timestamp}")

    def get_recent_events(self, limit=10):
        """
        Retrieve the most recent events stored in memory.
        :param limit: The number of recent events to retrieve. Defaults to 10.
        :return: A list of recent events (dictionaries).
        """
        recent_events = list(self.memory_data.values())[-limit:]
        return recent_events

    def get_event_by_timestamp(self, timestamp):
        """
        Retrieve a specific event by its timestamp.
        :param timestamp: The timestamp of the event to retrieve.
        :return: The event data, or None if not found.
        """
        return self.memory_data.get(timestamp, None)

