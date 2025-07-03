# Windows Installation Guide

## Quick Start for Windows Users

### Option 1: Batch File (Recommended - No Python Required)

1. **Download the batch file**:
   - Right-click and save `desktop_organizer.bat` to your computer
   - Place it anywhere on your computer (Downloads folder is fine)

2. **Run the organizer**:
   - Double-click `desktop_organizer.bat`
   - Choose option 1 for dry run (safe preview)
   - Choose option 2 to actually organize files
   - Choose option 3 to exit

### Option 2: Python Version (More Features)

1. **Check if Python is installed**:
   - Open Command Prompt (Windows Key + R, type `cmd`, press Enter)
   - Type `python --version` and press Enter
   - If you see a version number, Python is installed
   - If you get an error, download Python from [python.org](https://www.python.org/downloads/)

2. **Download and run**:
   - Save `desktop_organizer.py` to your computer
   - Double-click the file, or
   - Open Command Prompt, navigate to the file location, and run: `python desktop_organizer.py`

## Testing the Organizer

1. **Generate test files**:
   - Run `generate_test_files.bat` to create 25 sample files on your desktop
   - This is safe - it only creates small text files for testing

2. **Test with dry run**:
   - Run the organizer and choose option 1 (Dry Run)
   - This shows you what would happen without moving any files

3. **Organize files**:
   - Choose option 2 to actually move the files
   - Watch as files get organized into folders

4. **Clean up**:
   - Run `cleanup_test_files.bat` to remove all test files and folders

## Troubleshooting

### "Desktop folder not found"

- Make sure you have a Desktop folder in `C:\Users\YourName\Desktop`
- Check if your user profile path is correct

### "Permission denied" errors

- Right-click the batch file and select "Run as administrator"
- Make sure no files are currently open or in use

### Python not found

- Download Python from [python.org](https://www.python.org/downloads/)
- During installation, check "Add Python to PATH"
- Restart Command Prompt after installation

## Windows Versions Supported

- ✅ Windows 11
- ✅ Windows 10  
- ✅ Windows 8.1
- ✅ Windows 8
- ✅ Windows 7

## File Types Organized

The organizer handles these file types on Windows:

- **Images**: .jpg, .png, .gif, .bmp, .svg, .webp, .tiff, etc.
- **Videos**: .mp4, .avi, .mkv, .mov, .wmv, .flv, .webm, etc.
- **Audio**: .mp3, .wav, .flac, .aac, .ogg, .wma, .m4a, etc.
- **Documents**: .pdf, .doc, .docx, .txt, .rtf, .odt, etc.
- **Spreadsheets**: .xls, .xlsx, .csv, .ods, etc.
- **Presentations**: .ppt, .pptx, .odp, etc.
- **Code**: .py, .js, .html, .css, .java, .cpp, .php, etc.
- **Applications**: .exe, .msi, .app, .apk, etc.
- **Archives**: .zip, .rar, .7z, .tar, .gz, etc.
- **Other**: Unknown file types go to "other" folder

## Safety Features

- **Dry run mode**: Preview changes before applying them
- **Conflict resolution**: Never overwrites existing files
- **Error handling**: Graceful handling of permission errors
- **Confirmation prompts**: Asks before making actual changes
- **Detailed logging**: Shows exactly what happens to each file
