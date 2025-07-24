import os
from tkinter.tix import MAX
from uu import Error
from google import genai
from google.genai import types

from functions.config import MAX_CHARS

def get_file_content(working_directory, file_path):
  try:
    abs_boundary_path = os.path.abspath(working_directory)
    joined_directory = os.path.join(abs_boundary_path, file_path)
    joined_directory_abs_path = os.path.abspath(joined_directory) + "/"

    if joined_directory_abs_path.startswith(abs_boundary_path + "/"):
      if os.path.isfile(joined_directory) == False:
        print(f'Error: File not found or is not a regular file: "{file_path}"')
      else:
        with open(joined_directory, "r") as f:
          file_content_string = f.read(MAX_CHARS)
          if len(file_content_string) == MAX_CHARS:
            file_content_string += " " + file_path
            file_content_string += " truncated at 10000 characters"
          print(file_content_string)
    else:
      print(f'Error: Cannot read "{file_path}" as it is outside the permitted working directory')
  except:
    raise Error("Error: something went wrong :<!")

schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Reads and displays the content of a specified file, constrained to the working directory. Content is truncated at 10000 characters if the file is too large.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path to the file to read, relative to the working directory.",
            ),
        },
        required=["file_path"],
    ),
)