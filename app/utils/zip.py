from shutil import make_archive,unpack_archive
from os import path, getcwd
from file import fileMover
from zipfile import is_zipfile
class fileZipper():
    def __init__(self) -> None:
        pass
    def zip_file(self,zip_name:str,zip_loc:str="none") -> str:
        try:
            if zip_loc == "none":
                zip_loc = getcwd()
        except Exception as e:
            print(f"fileZipper |\t ERROR {e} \t| unable to find {zip_loc} directory")
            return ""
        if zip_name[-4:] == ".zip": #remove .zip
            zip_name = zip_name[:-4]
        try:
            make_archive(zip_name, 'zip', zip_loc)
            return zip_name + ".zip"
        except Exception as e:
            print(f"fileZipper |\t ERROR {e} \t| unable to zip into {zip_name}")
            return ""
    
    def unzip_file(self,zip_name:str,zip_loc:str="none",unzip_to:str="none",create_folder_at_dest:bool = False) -> None:
        # unzips files to unzip_to - if create_folder_at_dest is true it puts the files in a new folder
        if zip_name[-4:] != ".zip":
            zip_name += ".zip"

        if zip_loc != "none":
            zip_loc = path.join(zip_loc, zip_name)

        
        try:
            if not is_zipfile(zip_loc):
                raise ValueError(f"{zip_loc} is not a valid zip file")
            
            unpack_now = True
            if create_folder_at_dest == True:
                new_folder_name = zip_name[:-4]
                new_folder_full_location = path.join(unzip_to, new_folder_name)
                unpack_now = fileMover().createFolder(new_folder_full_location) 
                unzip_to = new_folder_full_location

            
            if unpack_now == True:
                unpack_archive(zip_loc, unzip_to, "zip")
            
        except Exception as e:
            print(f"fileZipper |\t ERROR {e} \t| unable to unzip {zip_name}")
            
        

if __name__ == "__main__":
    zip = fileZipper()
    #zip.zip_file("zipped.zip","src_test")
    zip.unzip_file("zipped.zip","src_test","dest_test")