# functions/write_file.py

import os
from google.genai import types

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
    

schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path to the file that is being written, relative to the working directory. If a file does not exist in the location specified, it will be created",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="The content to be written to the file. will overwrite all data in the file being written if the file already exists. This is always the last argument.",
            ),
        },
    ),
)