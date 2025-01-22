import json
import os

class JSONManager:
    def __init__(self, directory="maps"):
        self.directory = directory
        os.makedirs(self.directory, exist_ok=True)  # Ensure the directory exists

    def save(self, metadata, filename="new_map.json"):
        """
        Save the entire metadata to a JSON file.
        """
        filepath = os.path.join(self.directory, filename)
        try:
            with open(filepath, "w") as file:
                json.dump(metadata, file, indent=4)
            print(f"Map saved to {filepath}")
        except IOError as e:
            print(f"Failed to save map: {e}")

    def save_section(self, metadata, section, filename="new_map.json"):
        """
        Save a specific section of metadata to the JSON file.
        """
        filepath = os.path.join(self.directory, filename)
        try:
            # Load existing data or create a new structure
            data = self.load(filename) if os.path.exists(filepath) else {}
            data[section] = metadata.get(section, {})
            with open(filepath, "w") as file:
                json.dump(data, file, indent=4)
            print(f"Section '{section}' saved to {filepath}")
        except IOError as e:
            print(f"Failed to save section: {e}")

    def load(self, filename, metadata=None):
        """
        Load the entire JSON file into the provided metadata variable.
        """
        filepath = os.path.join(self.directory, filename)
        if not os.path.exists(filepath):
            raise FileNotFoundError(f"File not found: {filepath}")
        try:
            with open(filepath, "r") as file:
                data = json.load(file)
            if metadata is not None:
                metadata.update(data)  # Merge loaded data into the existing metadata
            return data
        except (IOError, json.JSONDecodeError) as e:
            print(f"Failed to load map: {e}")
            raise

    def load_section(self, filename, section, metadata=None):
        """
        Load a specific section of the JSON file.
        """
        filepath = os.path.join(self.directory, filename)
        if not os.path.exists(filepath):
            raise FileNotFoundError(f"File not found: {filepath}")
        try:
            with open(filepath, "r") as file:
                data = json.load(file)
            section_data = data.get(section, {})
            if metadata is not None:
                metadata[section] = section_data
            return section_data
        except (IOError, json.JSONDecodeError) as e:
            print(f"Failed to load section: {e}")
            raise

    def sync(self, metadata, filename, section):
        """
        Sync the metadata's section with the JSON file's section.
        """
        filepath = os.path.join(self.directory, filename)
        try:
            # Load existing data or create a new structure
            data = self.load(filename) if os.path.exists(filepath) else {}
            # Update the specific section
            data[section] = metadata.get(section, {})
            with open(filepath, "w") as file:
                json.dump(data, file, indent=4)
            print(f"Section '{section}' synced successfully in {filepath}")
        except IOError as e:
            print(f"Failed to sync section: {e}")

    def generate_unique_filename(self, base_name="new_map"):
        """
        Generate a unique filename by appending an incrementing index.
        """
        index = 1
        while True:
            filename = f"{base_name}_{index}.json"
            filepath = os.path.join(self.directory, filename)
            if not os.path.exists(filepath):
                return filename
            index += 1
