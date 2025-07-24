from wsgiref import types
from functions.get_files_content import get_file_content
from functions.run_python import run_python_file
from functions.write_files import write_file
from functions.get_files_info import get_files_info

from google import genai
from google.genai import types

def call_function(function_call_part, verbose=False):
  if verbose:
    print(f"Calling function: {function_call_part.name}({function_call_part.args})")
  else:
    print(f" - Calling function: {function_call_part.name}")
  
  available_functions = {
    "get_files_info": get_files_info,
    "get_file_content": get_file_content,
    "run_python_file": run_python_file,
    "write_file": write_file
  }

  if function_call_part.name in available_functions:
    function_result = available_functions[function_call_part.name]("./calculator",**function_call_part.args)
    return types.Content(
      role="tool",
      parts=[
          types.Part.from_function_response(
              name=function_call_part.name,
              response={"result": function_result},
          )
      ],
    )
  else:
    return types.Content(
      role="tool",
      parts=[
          types.Part.from_function_response(
              name=function_call_part.name,
              response={"error": f"Unknown function: {function_call_part.name}"},
          )
      ],
    )