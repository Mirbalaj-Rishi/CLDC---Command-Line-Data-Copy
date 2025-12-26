CLDC
==========================
Command Line Data Copy
--------------------------
This project has a single command desinged to help with backing up files to a different location. This project uses only packages from the python standard library so no package installs are needed. 

- To run the command simply run python3 path_to_main.py with a destination_path.
- OR edit the values in example_command.py to see how the command works

For example here is a simple command:
-------------------------------------
```console
path_to_main.py destination_path
```
Where
- path_to_main.py is the path to the main.py file in this repository 
- destination_path is the destination you want to copy files to 
    - omitting -s means the program will copy the current working directory


Here is an example of a command with all the arguments
------------------------------------------------------ 
```console
path_to_main.py destination_path -s source_path -z -r new_name
```
- path_to_main.py is the path to the main.py file in this repository
- destination_path is the destination you want to copy files to 
- -s is the source flag for when you want to specify the location of the files you want to copy
    - source_path is the location of the files you want to copy
    - omitting -s means the program will copy the current working directory
- -z is the zip flag if you want to zip the files in the directory before copying them
    - by default the zip file will be named after the date it was created in dd-mm-yy format
    - .zip at the end of the file name is optional 
- -r is the rename flag which renames the zip file
    - -r only works when -z is in the command
    - .zip at the end of the file name is optional 

Design 
-------------------------------------
Below is a list of files and there purpose
- main.py - holds the argument parser for the main command of this program
- file.py - holds the fileMover class for moveing, copying files
- zip.py - holds the fileZipper class for zipping and unzipping (not supported yet) files
- example_command.py - has an example command that can be excuted in the file if some constants are changed.

Future Updates
-----------------
- add file unzipping to the command

Known Issues
--------------
- sometimes file zipping can causethe ERROR ZIP does not support timestamps before 1980 even when none of the documents are older than 1980