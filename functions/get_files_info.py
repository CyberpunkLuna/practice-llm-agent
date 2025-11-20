# functions/get_files_info.py

import os
from google.genai import types

def get_files_info(working_directory, directory="."):
    full_path = os.path.join(working_directory, directory)
    absolute_path = os.path.abspath(full_path)

    if not os.path.isdir(absolute_path):
        return f'Error: "{directory}" is not a directory'
    if (absolute_path not in [os.path.join(os.path.abspath(working_directory), x) for x in os.listdir(working_directory)]) and (absolute_path != os.path.abspath(working_directory)):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    
    output = []
    for item in os.listdir(full_path):
        temp_path = os.path.join(full_path, item)
        try:
            temp_output = f'- {item}: file_size={os.path.getsize(temp_path)} bytes, is_dir={os.path.isdir(temp_path)}'
        except:
            return f'Error: cannot perform file operations'
        output.append(temp_output)
    
    return '\n'.join(output)


schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)