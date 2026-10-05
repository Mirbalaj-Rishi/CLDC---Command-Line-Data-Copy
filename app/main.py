import argparse
from utils.file import fileMover
from utils.zip import fileZipper
from datetime import datetime
from os import getcwd, path
from utils.mutithreaded_job_executor import zipThreaded, retoreThreaded

def main(): 
    # Initialize the parser
    parser = argparse.ArgumentParser(
                    prog='CDLM',
                    description='COMMAND LINE DATA COPY - tool for backups and moveing files',
                    epilog='Made by Mirbalaj Rishi')

    # Add arguments
    
    parser.add_argument("destination_path", help="Where the file will be moved too.")
    parser.add_argument("-s","--source_path", help="File or directory you want to move. Uses current directory if not included")
    parser.add_argument("-z", "--zip", action="store_true", help="If -z is included Zip the files at the path before sending the file to the destination.")
    parser.add_argument("-r", "--rename", help="Rename the file when saved in destination.")
    parser.add_argument("-res","--restore", help="restore files zipped by CDLC (or other programs). This argument takes the name of the zipped file inside the given destination_path and restores it back to the current working directory. If -s path is given then it restores it at that path instead. By default, restore unzips files, but if -z is given then it returns the zipped file")
    # Parse the arguments
    args = parser.parse_args()

    # Access the arguments
    destination_path = args.destination_path
    source_path = args.source_path
    zip_bool = args.zip
    rename = args.rename
    restore_name = args.restore
    if not source_path:
        source_path = getcwd()

    if restore_name and zip_bool == False:
        # moving from destination to source
        retoreThreaded().restoreAndMoveThread(destination_path, source_path, restore_name)
    elif restore_name and zip_bool == True:
        # moving from destination to source
        full_restore_path = path.join(destination_path, restore_name)
        fileMover().moveFile(full_restore_path, source_path)
    elif zip_bool == True and not restore_name:
        #from source to destination
        if rename:
            name = rename
        else:
            date = datetime.now()
            date = date.strftime("%d-%m-%y")
            name = str(date) + ".zip"
        zipThreaded().zipAndMoveThread(source_path, destination_path, name)
    else:
        fileMover().copyAll(destination_path, source_path)

if __name__ == "__main__":
    main()