# get_file_content.py

import os
from functions.config import MAX_CHARACTERS

def get_file_content(working_directory, file_path):
    # returns the contents of the specified file as a string
    full_path = os.path.join(working_directory, file_path)
    absolute_path = os.path.abspath(full_path)
    
    if not os.path.isfile(absolute_path):
        return f'Error: File not found or is not a regular file: "{file_path}"'
    if not absolute_path.startswith(os.path.abspath(working_directory)):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

    
    try:
        with open(absolute_path, "r") as file:
            file_content_string = file.read(MAX_CHARACTERS)
            if len(file_content_string) >= 10000:
                return (file_content_string + f'[...File "{file_path}" truncated at 10000 characters]')
            else:
                return file_content_string
    except:
        return 'Error: Could not perform file operation'