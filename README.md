# Desktop Organizer

This is a Python script that organizes the files on your desktop into different folders based on their file types.

## How it works

The script defines a dictionary that maps each file type to a folder name. For example, `jpg` files go to the `images` folder, `mp3` files go to the `audio` folder, and so on. You can customize this dictionary to suit your needs.

The script then loops through each file type and folder name in the dictionary and moves all the files matching that file type from the desktop to the corresponding folder. If the folder does not exist, it creates it. If the file already exists in the destination folder, it skips it.

The script also handles files that have extensions that are not in the dictionary. It moves them to a folder called `other`. You can change this behavior if you want.

## How to use it

To use this script, you need to have Python installed on your computer. You can download it from [https://www.python.org/downloads/](https://www.python.org/downloads/).

You also need to save the script as `desktop_organizer.py` on your desktop.

To run the script, open a terminal or command prompt and navigate to your desktop. Then type:

```bash
python desktop_organizer.py
```

The script will start organizing your files and print any messages if there are any errors or skipped files.

You can check the results by looking at your desktop and the folders that were created or modified.

## Disclaimer

This script is provided as is, without any warranty or liability. Use it at your own risk. Make sure you have a backup of your files before running the script. The author is not responsible for any loss or damage caused by this script.

## NOTE

i would really appreciate if you could give me some feedback on this project, anything that you think would make it better.
also if you can make branch and add some features to it(adding icons, etc.), that would be great.
```