# functions/run_python_file.py

import os
import subprocess
from google.genai import types

def run_python_file(working_directory, file_path, args=[]):
    full_path = os.path.join(working_directory, file_path)
    absolute_path = os.path.abspath(full_path)

    if not absolute_path.startswith(os.path.abspath(working_directory)):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    
    if not os.path.exists(absolute_path):
        return f'Error: File "{file_path}" not found.'
    
    if not absolute_path.endswith('.py'):
        return f'Error: "{file_path}" is not a Python file.'
    
    run_args = ['uv', 'run', f'{full_path}']
    if args:
        run_args.extend(args)

    try:
        completed_process = subprocess.run(run_args, capture_output=True, timeout=30, text=True)
        return_strings = []
        if completed_process.stdout is not None:
            return_strings.append(f'STDOUT: {completed_process.stdout}')
        if completed_process.stderr is not None:
            return_strings.append(f'STDERR: {completed_process.stderr}')
        if not return_strings:
            return_strings.append(f'No output produced.')
        if completed_process.returncode != 0:
            return_strings.append(f'Process exited with code {completed_process.returncode}')
        return " ".join(return_strings)

    except Exception as e:
        return f"Error: executing Python file: {e}"
    



schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Runs .py type files, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path to the .py file to be executed, relative to the working directory.",
            ),
            "args": types.Schema(
                type=types.Type.STRING,
                description="Arguments for the python file being executed, formated as a list of strings. If no arguments are providwed it defaults to an empty list",
            ),
        },
    ),
)