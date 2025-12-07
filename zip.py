from zipfile import ZipFile, ZIP_DEFLATED
from os import listdir, path

class fileZipper():
    def __init__(self) -> None:
        pass
    def zip_file(self,zip_name:str,zip_loc:str="none") -> None:
        try:
            if zip_loc == "none":
                dir_list = listdir()
            else:
                dir_list = listdir(zip_loc)
                #add directory name in front of each file in the list
                dir_list = list(map(lambda file_name: path.join(zip_loc, file_name), dir_list))
                zip_name = path.join(zip_loc, zip_name)
        except Exception as e:
            print(f"fileZipper |\t ERROR {e} \t| unable to find {zip_loc} directory")
            return None

        if zip_name[-4:-1] != ".zip":
            zip_name += ".zip"
        try:
            with ZipFile(zip_name, 'w', ZIP_DEFLATED) as myzip:
                print(f"fileZipper |\t {zip_name} \t| zipping")
                for file in dir_list:
                    try:
                        print(f"fileZipper |\t {file} \t| zipped")
                        myzip.write(file)
                    except Exception as e:
                        print(f"fileZipper | ERROR {e} | unable to zip {file}")
            print(f"fileZipper |\t {zip_name} \t| done")
        except Exception as e:
            print(f"fileZipper |\t ERROR {e} \t| unable to zip into {zip_name}")
    
    def unzip_file(self,zip_name:str,compress_loc:str="none") -> None:
        if zip_name[-4:-1] != ".zip":
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
    zip.zip_file("zipped","src_testfj")
    zip.unzip_file("zippeder")