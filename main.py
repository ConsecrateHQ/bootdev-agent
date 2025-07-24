import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types
from functions.config import SYSTEM_PROMPT
from functions.get_files_info import schema_get_files_info
from functions.get_files_content import schema_get_file_content
from functions.run_python import schema_run_python_file
from functions.write_files import schema_write_file
from functions.call_function import call_function

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

arguments = sys.argv

def main():

    if len(arguments) < 2:
        print("No prompt provided :<!")
        sys.exit(1)

    messages = [
        types.Content(role="user", parts=[types.Part(text=arguments[1])])
    ]

    available_functions = types.Tool(
        function_declarations=[
            schema_get_files_info,
            schema_get_file_content,
            schema_run_python_file,
            schema_write_file
        ]
    )

    response = client.models.generate_content(model='gemini-2.0-flash-001', contents=messages, config=types.GenerateContentConfig(system_instruction=SYSTEM_PROMPT, tools=[available_functions]))

    print(response.text)

    if response.function_calls:
        for function_call_part in response.function_calls:
            # print(f"Calling function: {function_call_part.name}({function_call_part.args})")
            # Sample Response: Calling function: run_python_file({'file_path': 'main.py'})

            function_call_result = call_function(function_call_part, verbose=("--verbose" in arguments))

            if function_call_result.parts[0].function_response.response:
                if "--verbose" in arguments:
                    print(f"-> {function_call_result.parts[0].function_response.response}")
                else:
                    print(f"-> {function_call_result.parts[0].function_response.response}")
            else:
                raise Exception("SOMETHING WENT WRONG :<<<!")

    if ("--verbose" in arguments):
        print(f"User prompt: {arguments[1]}")
        print("Prompt tokens:", response.usage_metadata.prompt_token_count)
        print("Response tokens:", response.usage_metadata.candidates_token_count)

if __name__ == "__main__":
    main()
