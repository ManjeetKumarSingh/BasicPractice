"""File I/O Operations Module
This module contains functions to perform various I/O operations on files in Python.
Functions:
- read_file: Read the contents of a file.
- write_file: Write content to a file.
- append_file: Append content to a file.
- delete_file: Delete a file.
"""


def file_operations():
    """File I/O Operations
    This function performs various I/O operations on files in Python.
    """

    # Read the contents of a file
    def read_file(file_path):
        """Read the contents of a file
        This function reads the contents of a file and returns it as a string.
        Args: file_path (str): The path to the file to be read.
        Returns: str: The contents of the file.
        """
        with open(file_path, "r") as file:
            content = file.read()
            return content

    # Write content to a file
    def write_file(file_path, content):
        """Write content to a file
        This function writes the specified content to a file.
        Args: file_path (str): The path to the file to be written.
              content (str): The content to be written to the file.
        """
        with open(file_path, "w") as file:
            file.write(content)

    return read_file, write_file


read_file, write_file = file_operations()
# Example usage
file_path = "/Users/manjeetkumar/Devlopment/DD-Academy/BasicPractice/data/file.txt"
content = read_file(file_path)
print("*=*" * 40)
print(content)
print("*=*" * 40)

write_file(file_path, "This is a sample content written to the file.")

content = read_file(file_path)
print("*=*" * 40)
print(content)
print("*=*" * 40)
