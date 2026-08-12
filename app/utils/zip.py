from zipfile import ZipFile
from shutil import make_archive
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
            print(f"fileZipper |\t {zip_name + ".zip"} \t| done")
            return zip_name + ".zip"
        except Exception as e:
            print(f"fileZipper |\t ERROR {e} \t| unable to zip into {zip_name}")
            return ""
    
    def unzip_file(self,zip_name:str,compress_loc:str="none") -> None:
        if zip_name[-4:] != ".zip":
            zip_name += ".zip"

        if compress_loc != "none":
            zip_name = path.join(compress_loc, zip_name)
        try:
            with ZipFile(zip_name, 'r') as myzip:
                print(f"fileZipper |\t {zip_name} \t| unzipping")
                myzip.printdir()
                # extracting all the files
                if compress_loc != "none":
                    myzip.extractall(compress_loc)
                else:
                    myzip.extractall()
                print(f"fileZipper |\t {zip_name} \t| done")
        except Exception as e:
            print(f"fileZipper |\t ERROR {e} \t| unable to unzip {zip_name}")

if __name__ == "__main__":
    zip = fileZipper()
    zip.zip_file("zipped.zip","src_test")
    #zip.unzip_file("zippeder")