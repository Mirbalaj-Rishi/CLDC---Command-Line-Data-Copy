from shutil import move, copy2
from os import path, makedirs

class fileMover():
    def __init__(self):
        pass

    def verifyDirectory(self,loc) -> bool:
        #verify directory exists
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

    def moveFile(self,file_name:str,destination:str) -> None:
        can_move = self.verifyDirectory(destination)
        if can_move == False:
            print(f"fileMover |\t ERROR \t| destination does not exist and cant be created {destination}")
            return None
        try:
            move(file_name, destination)
            print(f"fileMover |\t file moved successfully {file_name}")
        except Exception as e:
            print(f"fileMover |\t ERROR {e} \t| unable to move {file_name}")

    def copyFile(self,file_name:str,destination:str) -> None:
        can_copy = self.verifyDirectory(destination)
        if can_copy == False:
            print(f"fileMover |\t ERROR \t| destination does not exist and cant be created {destination}")
            return None
        try: 
            copy2(file_name,destination)
            print(f"fileMover |\t file copyied successfully {file_name}")
        except Exception as e:
            print(f"fileMover |\t ERROR {e} \t| unable to copy {file_name}")

if __name__ == "__main__":
    fileMover().copyFile("src_test/file2.txt","dest_test")
    fileMover().copyFile("src_test/file2.txt","test")
    fileMover().copyFile("zipped.zip","dest_test")
    fileMover().copyFile("zippeder.zip","dest_test")

