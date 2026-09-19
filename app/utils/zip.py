from zipfile import ZipFile
from shutil import make_archive,unpack_archive
from os import path, getcwd

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
    
    def unzip_file(self,zip_name:str,zip_loc:str="none",unzip_to:str="none") -> None:
        if zip_name[-4:] != ".zip":
            zip_name += ".zip"

        if zip_loc != "none":
            zip_name = path.join(zip_loc, zip_name)
        try:
            unpack_archive(zip_name, unzip_to, "zip")
        except Exception as e:
            print(f"fileZipper |\t ERROR {e} \t| unable to unzip {zip_name}")

if __name__ == "__main__":
    zip = fileZipper()
    #zip.zip_file("zipped.zip","src_test")
    zip.unzip_file("zipped.zip","src_test","dest_test")