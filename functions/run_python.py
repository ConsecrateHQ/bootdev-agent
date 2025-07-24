import os
from uu import Error
import subprocess
from google import genai
from google.genai import types

def run_python_file(working_directory, file_path, args=[]):
  try:
    abs_boundary_path = os.path.abspath(working_directory)
    joined_directory = os.path.join(abs_boundary_path, file_path)
    joined_directory_abs_path = os.path.abspath(joined_directory)

    if joined_directory_abs_path.startswith(abs_boundary_path + "/"):
      if os.path.exists(joined_directory) == False:
        print(f'Error: File "{file_path}" not found.')
      elif joined_directory.endswith(".py") == False:
        print(f'Error: "{file_path}" is not a Python file.')
      else:
        try:
          completed_process = subprocess.run(["python3", joined_directory_abs_path, *args], check=True, capture_output=True, text=True, timeout=30)

          has_output = False

          if completed_process.stdout:
            print("STDOUT", completed_process.stdout)
            has_output = True
          if completed_process.stderr:
            print("STDERR", completed_process.stderr)
            has_output = True
          if not has_output:
            print("No output produced.")
        except subprocess.CalledProcessError as e:
          print(f"Process exited with code {e.returncode}")
          if e.stdout:
            print("STDOUT", e.stdout)
          if e.stderr:
            print("STDERR", e.stderr)
    else:
      print(f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory')
  except Error as e:
    print(f"Error: executing Python file: {e}")

schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Executes a Python file with optional command-line arguments, constrained to the working directory. Has a 30-second timeout.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path to the Python file to execute, relative to the working directory. Must have a .py extension.",
            ),
            "args": types.Schema(
                type=types.Type.ARRAY,
                description="Optional list of command-line arguments to pass to the Python script.",
                items=types.Schema(type=types.Type.STRING),
            ),
        },
        required=["file_path"],
    ),
)