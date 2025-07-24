import os
from uu import Error
from pathlib import Path
from google import genai
from google.genai import types

def write_file(working_directory, file_path, content):
  try:
    abs_boundary_path = os.path.abspath(working_directory)
    joined_directory = os.path.join(abs_boundary_path, file_path)
    joined_directory_abs_path = os.path.abspath(joined_directory) + "/"

    if joined_directory_abs_path.startswith(abs_boundary_path + "/"):
      if os.path.exists(joined_directory) == False:
        output_path = Path(joined_directory)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(content)
      else:
        output_path = Path(joined_directory)
        output_path.write_text(content)
      print(f'Successfully wrote to "{file_path}" ({len(content)} characters written)')
    else:
      print(f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory')
  except:
    raise Error("Error: something went wrong :<!")

schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Creates or overwrites a file with the specified content, constrained to the working directory. Creates parent directories if they don't exist.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path where the file should be written, relative to the working directory.",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="The content to write to the file.",
            ),
        },
        required=["file_path", "content"],
    ),
)