from functions.get_files_info import get_files_info
from functions.get_files_content import get_file_content
from functions.run_python import run_python_file
from functions.write_files import write_file

# get_files_info("calculator", ".")
# get_files_info("calculator", "pkg")
# get_files_info("calculator", "/bin")
# get_files_info("calculator", "../")

# get_file_content("calculator", "lorem.txt")

# get_file_content("calculator", "main.py")
# get_file_content("calculator", "pkg/calculator.py")
# get_file_content("calculator", "/bin/cat")
# get_file_content("calculator", "pkg/does_not_exist.py")


# write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
# write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
# write_file("calculator", "/tmp/temp.txt", "this should not be allowed")

run_python_file("calculator", "main.py")
print("----------")
run_python_file("calculator", "main.py", ["3 + 5"])
print("----------")
run_python_file("calculator", "tests.py")
print("----------")
run_python_file("calculator", "../main.py")
print("----------")
run_python_file("calculator", "nonexistent.py")