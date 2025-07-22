import os
import sys
from pathlib import Path
from event.event import Event


# Add the root directory to the sys.path to allow imports from there
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


class File:
    """Class with static methods that read from a file and write to a file"""   

    @staticmethod
    def read_from_file(file_name):
        """Static method that reads from a given file and returns a list of Event dictionaries"""
        try:
            result = []
            with open(f"{file_name}", mode="r", encoding="UTF-8") as file:
                result.extend([Event(line.rstrip('\n')).__dict__ for line in file])
            return result
        except FileNotFoundError:
            print(f"The file {file_name} does not exist\n")
        return result


    @staticmethod
    def write_to_file(file_name, content):
        """
            Static method that writes content to a file
            Checks if file exists
            Creates file if it doesn't exist
        """
        file_path = Path(file_name)
        if not file_path.exists():
            print(f"File {file_name} not found. Creation in progress...\n")
            with open(file_path, mode="w", encoding="UTF-8") as file:
                for row in content:
                    # Write the values in a row.
                    file.write(','.join(str(x) for x in row.values()))
                    file.write('\n') # Add a new line
            print(f"File {file_name} created!\n")
        else:
            print(f"The file {file_name} already exists\n")