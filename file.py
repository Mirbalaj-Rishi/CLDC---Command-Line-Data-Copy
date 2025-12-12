from shutil import move, copy2
from os import path, makedirs, listdir, getcwd
from typing import Callable
class fileMover():
    def __init__(self):
        pass

    def verifyDirectory(self,loc) -> bool:
        #verify destination directory exists
        exists = path.isdir(loc)
        if exists == False:
            try:
                makedirs(loc)
                print(f"fileMover |\t created directory {loc}")
                return True
            except Exception as e:
                print(f"fileMover |\t ERROR {e} \t| unable to create nonexistent directory {loc}")
                return False
        else:
            return True

    def moveFile(self, file_name:str,destination:str) -> None:
        can_move = self.verifyDirectory(destination)
        if can_move == False:
            print(f"fileMover |\t ERROR \t| destination does not exist and cant be created {destination}")
            return None
        try:
            move(file_name, destination)
            print(f"fileMover |\t file moved successfully {file_name}")
        except Exception as e:
            print(f"fileMover |\t ERROR {e} \t| unable to move {file_name}")

    def copyFile(self, file_name:str, destination:str) -> None:
        can_copy = self.verifyDirectory(destination)
        if can_copy == False:
            print(f"fileMover |\t ERROR \t| destination does not exist and cant be created {destination}")
            return None
        try: 
            copy2(file_name,destination)
            print(f"fileMover |\t file copyied successfully {file_name}")
        except Exception as e:
            print(f"fileMover |\t ERROR {e} \t| unable to copy {file_name}")
    
    def copyAll(self,destination:str, directory_path:str="none") -> None:
        if directory_path == "none":
            directory_path = getcwd()

        try:
            directory_list = listdir(directory_path)
        except Exception as e:
            print(f"fileMover |\t ERROR {e} \t| can find files in {directory_path}")
            return None 
        
        for discovery_name in directory_list:  # Iterate over all files and directories
            try:
                discovered_path = path.join(directory_path, discovery_name) # Construct full path
                
                if path.isdir(discovered_path) == True: # if its a directory
                    print(f"fileMover |\t found directory {discovery_name}")
                    recursive_destination = path.join(destination, discovery_name)
                    self.copyAll(recursive_destination, discovered_path) # copy everything there
                else:
                    print(f"fileMover |\t found file {discovery_name}")
                    self.copyFile(discovered_path, destination)
            except Exception as e:
                print(f"fileMover |\t ERROR {e} \t| file not valid {discovery_name}")
    
    def recursiveDirectoryCrawl(self,func:Callable, directory_path:str = "none") -> None:
        pass

if __name__ == "__main__":
    fileMover().copyAll("dest_test", "src_test")

