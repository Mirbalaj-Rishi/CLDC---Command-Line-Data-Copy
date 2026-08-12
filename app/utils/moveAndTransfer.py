from utils.file import fileMover
from utils.zip import fileZipper
from concurrent.futures import ThreadPoolExecutor, as_completed
from os import path
from shutil import rmtree
from tempfile import mkdtemp
from threading import Lock


class progressBar():
    def __init__(self, total: int, width: int = 30) -> None:
        self.total = total
        self.width = width
        self.done = 0
        self.lock = Lock()

    def advance(self, label: str) -> None:
        with self.lock:
            self.done += 1
            done, total = self.done, self.total
            filled = int(self.width * done / total)
            bar = "#" * filled + "-" * (self.width - filled)
            percent = int(100 * done / total)
            end = "\n" if done == total else ""
            print(f"\r[{bar}] {percent:3d}% ({done}/{total} zipped) {label}" + " " * 20, end=end, flush=True)


def zipFolder(source_path: str, folder_name: str, staging_dir: str, progress: progressBar) -> str:
    folder_path = path.join(source_path, folder_name)
    result = fileZipper().zip_file(path.join(staging_dir, folder_name), folder_path)
    progress.advance(folder_name)
    return result


def zipAndMoveThread(source_path: str, destination_path: str, zip_name: str) -> None:
    fileMover().verifyDirectory(destination_path)
    files, folders = fileMover().listFilesAndFoldersInDir(source_path)

    # total items to zip: one per subfolder, plus one for the final archive
    # of the source directory itself (loose files + subfolder zips combined)
    total_to_zip = len(folders) + 1
    progress = progressBar(total_to_zip)

    if not folders:
        # nothing to thread, just zip the directory directly
        fileZipper().zip_file(path.join(destination_path, zip_name), source_path)
        progress.advance(path.basename(source_path.rstrip("/\\")) or source_path)
        return

    staging_dir = mkdtemp()
    try:
        for file in files:
            fileMover().copyFile(path.join(source_path, file), staging_dir)

        with ThreadPoolExecutor(max_workers=len(folders)) as executor:
            futures = [executor.submit(zipFolder, source_path, folder, staging_dir, progress) for folder in folders]
            for future in as_completed(futures):
                future.result()

        # zip everything staged (per-folder zips + loose files) into one combined archive
        fileZipper().zip_file(path.join(destination_path, zip_name), staging_dir)
        progress.advance(path.basename(source_path.rstrip("/\\")) or source_path)
    finally:
        rmtree(staging_dir, ignore_errors=True)
