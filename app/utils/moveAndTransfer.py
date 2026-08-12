from utils.file import fileMover
from utils.zip import fileZipper
from concurrent.futures import ThreadPoolExecutor
from os import path
from shutil import rmtree
from tempfile import mkdtemp


def zipFolder(source_path: str, folder_name: str, staging_dir: str) -> str:
    folder_path = path.join(source_path, folder_name)
    return fileZipper().zip_file(path.join(staging_dir, folder_name), folder_path)


def zipAndMoveThread(source_path: str, destination_path: str, zip_name: str) -> None:
    fileMover().verifyDirectory(destination_path)
    files, folders = fileMover().listFilesAndFoldersInDir(source_path)

    if not folders:
        # nothing to thread, just zip the directory directly
        fileZipper().zip_file(path.join(destination_path, zip_name), source_path)
        return

    staging_dir = mkdtemp()
    try:
        for file in files:
            fileMover().copyFile(path.join(source_path, file), staging_dir)

        print(f"Total Processes {len(folders)}")
        with ThreadPoolExecutor(max_workers=len(folders)) as executor:
            futures = [executor.submit(zipFolder, source_path, folder, staging_dir) for folder in folders]
            for future in futures:
                future.result()
        print("all processes finished")

        # zip everything staged (per-folder zips + loose files) into one combined archive
        fileZipper().zip_file(path.join(destination_path, zip_name), staging_dir)
    finally:
        rmtree(staging_dir, ignore_errors=True)
