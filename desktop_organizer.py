# import modules
import os
import glob
import shutil

# define the path of the desktop
path = os.path.join(os.path.expanduser("~"), "Desktop")

# define a dictionary mapping each file type to a folder name
file_types = {
    "jpg": "images",
    "png": "images",
    "gif": "images",
    "bmp": "images",
    "mp4": "videos",
    "avi": "videos",
    "mkv": "videos",
    "mov": "videos",
    "mp3": "audio",
    "wav": "audio",
    "flac": "audio",
    "docx": "documents",
    "pdf": "documents",
    "txt": "documents",
    "xlsx": "excel", 
    "pptx": "documents",
    "exe": "apps",
    "py": "codes", 
    "c": "codes", 
    "cpp": "codes", 
    "java": "codes",
    "json": "codes",
    "html": "codes",
    "css": "codes",
    "js": "codes",
    "php": "codes",
    "sql": "codes",
    "xml": "codes",
    "md": "codes",
    "csv": "codes",
    "db": "codes",
    "dll": "codes",
    "apk": "codes",
    "bat": "codes",
    "bin": "codes",
    "class": "codes",
    "cmd": "codes",
    "com": "codes",
    "dat": "codes",
    "dmg": "codes",
    "elf": "codes",
    "h": "codes",
    "jar": "codes",
    "msi": "codes",
    "out": "codes",
    "ahk": "codes", 
    "zip": "compressed", 
    "rar": "compressed", 
    "7z": "compressed",
    "tar": "compressed",
    "gz": "compressed",
    "xz": "compressed",
    "bz2": "compressed",
    "iso": "compressed",
    "pkg": "compressed",
    "tgz": "compressed",
    "z": "compressed",
    "lnk": "shortcuts", 
}

# loop through each file type and folder name
for file_type, folder_name in file_types.items():
    # get all the files matching the file type
    files = glob.glob(os.path.join(path, f"*.{file_type}"))
    
    # if there are any files of that type
    if files:
        # create the folder if it does not exist
        folder_path = os.path.join(path, folder_name)
        if not os.path.isdir(folder_path):
            os.mkdir(folder_path)
        
        # move each file to the corresponding folder
        for file in files:
            # get the file name without the path
            file_name = os.path.basename(file)
            # get the destination path for the file
            dst = os.path.join(folder_path, file_name)
            # check if the file already exists in the destination folder
            if not os.path.exists(dst):
                # if not, move the file
                shutil.move(file, dst)
            else:
                # if yes, skip the file
                print(f"File {file} already exists in {dst}, skipping.")

# get all the files in the desktop with any extension
all_files = glob.glob(os.path.join(path, "*.*"))

# create a set of all the extensions in the dictionary
known_extensions = set(file_types.keys())

# loop through each file in the desktop
for file in all_files:
    # get the file extension without the dot
    file_extension = os.path.splitext(file)[1][1:]
    # check if the file extension is not in the dictionary
    if file_extension not in known_extensions:
        # create a folder called "other" if it does not exist
        other_folder = os.path.join(path, "other")
        if not os.path.isdir(other_folder):
            os.mkdir(other_folder)
        # get the file name without the path
        file_name = os.path.basename(file)
        # get the destination path for the file
        dst = os.path.join(other_folder, file_name)
        # check if the file already exists in the destination folder
        if not os.path.exists(dst):
            # if not, move the file
            shutil.move(file, dst)
        else:
            # if yes, skip the file
            print(f"File {file} already exists in {dst}, skipping.")