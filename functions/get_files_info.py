import os
from uu import Error
from google import genai
from google.genai import types

def get_files_info(working_directory, directory="."):
  try:
    abs_boundary_path = os.path.abspath(working_directory)
    joined_directory = os.path.join(abs_boundary_path, directory)
    joined_directory_abs_path = os.path.abspath(joined_directory) + "/"

    # print("abs_boundary_path", abs_boundary_path)
    # print("joined_directory:", joined_directory)
    # print("joined_directory_abs_path:", joined_directory_abs_path)
    print(f"Result for '{directory}' directory:")
    if joined_directory_abs_path.startswith(abs_boundary_path + "/"):
      if os.path.isdir(joined_directory) == False:
        print(f'Error: "{directory}" is not a directory')
      else:
        for file_name in os.listdir(joined_directory):
          file_path = os.path.join(joined_directory, file_name)
          print(f' - {file_name}: file_size={os.path.getsize(file_path)} bytes, is_dir={not os.path.isfile(file_path)}')
    else:
      print(f'\tError: Cannot list "{directory}" as it is outside the permitted working directory')
  except:
    raise Error("Error: something went wrong :<!")
  
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