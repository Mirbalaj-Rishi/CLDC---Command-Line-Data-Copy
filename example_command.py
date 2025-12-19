import subprocess
from os import getcwd, path
# Define the paths as variables for clarity and easier maintenance
dir = getcwd()
SCRIPT_PATH = f"{dir}/main.py"

#edit these values
DEST_PATH = ""
SOURCE_PATH = ""
RENAME = ""

result = subprocess.run([
    "python",
    SCRIPT_PATH,
    # Positional Argument 1: destination_path
    DEST_PATH, 
    # Optional Argument Flag: -s
    "-s", 
    # Optional Argument Value: source_path
    SOURCE_PATH,
    # zip the files
    "-z",
    #rename the files
    "-r",
    RENAME
])

print(result)
