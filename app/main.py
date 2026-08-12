import argparse
from utils.file import fileMover
from utils.zip import fileZipper
from datetime import datetime
from os import getcwd
from utils.moveAndTransfer import zipAndMoveThread

def main(): 
    # Initialize the parser
    parser = argparse.ArgumentParser(
                    prog='CDLM',
                    description='COMMAND LINE DATA COPY - tool for backups and moveing files',
                    epilog='')

    # Add arguments
    
    parser.add_argument("destination_path", help="Where the file will be moved too.")
    parser.add_argument("-s","--source_path", help="File or directory you want to move. Uses current directory if not included")
    parser.add_argument("-z", "--zip", action="store_true", help="If -z is included Zip the files at the path before sending the file to the destination.")
    parser.add_argument("-r", "--rename", help="Rename the file when szved in destination.")
    # Parse the arguments
    args = parser.parse_args()

    # Access the arguments
    destination_path = args.destination_path
    source_path = args.source_path
    zip_bool = args.zip
    rename = args.rename

    if not source_path:
        source_path = getcwd()

    
    if zip_bool == True:
        if rename:
            name = rename
        else:
            date = datetime.now()
            date = date.strftime("%d-%m-%y")
            name = str(date) + ".zip"
        zipAndMoveThread(source_path, destination_path, name)
    else:
        fileMover().copyAll(destination_path, source_path)

if __name__ == "__main__":
    main()