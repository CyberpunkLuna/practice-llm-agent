# main.py

import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types
from functions.get_files_info import schema_get_files_info
from functions.get_file_content import schema_get_file_content
from functions.write_file import schema_write_file
from functions.run_python_file import schema_run_python_file
from functions.call_function import call_function

def main():
    # loads env variables and inits genemi client instance, and system prompt
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)
    system_prompt = """
        You are a helpful AI coding agent.

        When a user asks a question or makes a request, make a function call plan. You can perform the following operations:

        - List files and directories
        - Read file contents
        - Execute Python files with optional arguments
        - Write or overwrite files

        All paths you provide should be relative to the working directory. You do not need to specify the working directory in your function calls as it is automatically injected for security reasons.
    """

    # list of available tools for the LLM
    available_functions = types.Tool(
        function_declarations=[
        schema_get_files_info,
        schema_get_file_content,
        schema_write_file,
        schema_run_python_file,
        ]
    )

    # captures sys.argv as user prompt
    if len(sys.argv) <= 1:
        sys.exit(1)
    user_prompt = sys.argv[1]

    # historical list of messages and function calls
    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]
    function_responses = []


    for i in range(20):
        try:
            # calling the llm
            response = client.models.generate_content(
                model='gemini-2.0-flash-001', 
                contents=messages,
                config=types.GenerateContentConfig(tools=[available_functions], system_instruction=system_prompt)
            )

            #determining if agent is finished with task
            if not response.function_calls and response.text:
                print(f"Final response:\n\n{response.text}")
                break

            # adding context to llm messages list
            for candidate in response.candidates:
                messages.append(candidate.content)

            # calling functions or printing text result
            if response.function_calls:
                for function_call_part in response.function_calls:
                    function_call_result = call_function(function_call_part, verbose=False)
                    if not function_call_result.parts[0].function_response.response:
                        raise Exception("error: function call had a null response")
                    else:
                        function_responses.append(function_call_result.parts[0])
                        if sys.argv[-1] == '--verbose':
                            print(f"-> {function_call_result.parts[0].function_response.response}")

            # adding function responses context
            messages.append(types.Content(role="user", parts=function_responses))

        except:
            print(Exception)

    if sys.argv[-1] == '--verbose':
        print(f"User prompt: {user_prompt}")
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

if __name__ == "__main__":
    main()
