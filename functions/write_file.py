# functions/write_file.py

import os

def write_file(working_directory, file_path, content):
    full_path = os.path.join(working_directory, file_path)
    absolute_path = os.path.abspath(full_path)

    if not absolute_path.startswith(os.path.abspath(working_directory)):
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    
    if not os.path.exists(absolute_path):
        folder_path = os.path.dirname(full_path)
        os.makedirs(folder_path, exist_ok=True)

    try:
        with open(absolute_path, "w") as file:
            written_chars = file.write(content)
            return f'Successfully wrote to "{file_path}" ({written_chars} characters written)'
    except:
        return f'Unable to write to file, due to permissions'