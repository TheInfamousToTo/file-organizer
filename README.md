# Desktop Organizer - Windows Edition

A powerful file organization tool **specifically optimized for Windows systems**. Available in both Python and Windows Batch versions. Automatically organizes files on your desktop into categorized folders based on file types.

## 🪟 Windows-First Design

This project is **designed specifically for Windows** and includes:

- **Native Windows batch scripts** - No Python installation required
- **Windows environment variables** - Uses `%USERPROFILE%\Desktop` for reliability
- **Windows file system optimization** - Handles Windows paths, permissions, and file operations
- **Windows-specific error handling** - Clear error messages for Windows users
- **Windows console commands** - Uses `cls`, `pause`, `mkdir`, and other Windows commands
- **Windows versions supported** - Compatible with Windows 7, 8, 10, and 11

## Features

### Python Version (Complete)

- **Interactive Menu**: Choose between dry run, organize, show statistics, or exit
- **Enhanced file type support**: Over 80+ file extensions across 12 categories  
- **Dry-run mode**: Preview organization without moving files
- **Advanced logging**: Detailed logs with timestamps and file operations
- **Command-line options**: Full argparse support for advanced users
- **Statistics view**: See file distribution and supported categories
- **Error handling**: Comprehensive error handling and user feedback
- **Cross-platform compatibility**: Works on Windows, macOS, and Linux (Windows-optimized)
- **Safe operation**: Skips existing files to prevent overwrites
- **Screen clearing**: Automatic console clearing for better user experience

### Batch Version (Windows Native)

- **Interactive Menu**: Same menu system as Python version
- **Native Windows support**: No Python installation required
- **Dry-run capability**: Preview mode just like Python version
- **Real-time feedback**: Shows progress as files are organized
- **Comprehensive file support**: Handles the same file types as Python version
- **Confirmation prompts**: Safety confirmations before actual file moves
- **Error handling**: Graceful handling of file conflicts and errors

## File Categories

Both versions organize files into these categories:

- **Images**: jpg, png, gif, bmp, svg, webp, tiff, etc.
- **Videos**: mp4, avi, mkv, mov, wmv, flv, webm, etc.
- **Audio**: mp3, wav, flac, aac, ogg, m4a, etc.
- **Documents**: pdf, doc, docx, txt, rtf, odt, etc.
- **Spreadsheets**: xls, xlsx, csv, ods, numbers
- **Presentations**: ppt, pptx, odp, key
- **Code**: py, js, html, css, java, cpp, php, json, etc.
- **Applications**: exe, msi, dmg, pkg, apk, etc.
- **Archives**: zip, rar, 7z, tar, gz, etc.
- **Fonts**: ttf, otf, woff, woff2, etc.
- **E-books**: epub, mobi, azw, fb2, etc.
- **Shortcuts**: lnk, url, desktop
- **Other**: Unknown file types

## Installation & Usage

### Python Version

#### Requirements

- Python 3.6 or higher
- No external dependencies (uses only standard library)

#### Basic Usage

**Interactive Menu Mode (Recommended):**

```bash
# Run the script
python desktop_organizer.py

# Then choose from the menu:
# 1. Dry Run (Preview without moving files)
# 2. Organize (Actually move files)  
# 3. Show Statistics (View file distribution)
# 4. Exit
```

**Command Line Mode (Advanced):**

```bash
# Organize desktop with default settings
python desktop_organizer.py --no-interactive

# Organize a specific directory
python desktop_organizer.py --target-dir "C:\MyFolder" --no-interactive

# Dry run (test without moving files)
python desktop_organizer.py --dry-run

# Disable logging to file
python desktop_organizer.py --no-logging
```

#### Testing

**Generate Test Files:**

```bash
# Python version (cross-platform)
python generate_test_files.py

# Windows batch version
generate_test_files.bat
```

**Test the Organizer:**

```bash
# Run the advanced test script
python test_organizer.py
```

**Clean Up After Testing:**

```batch
# Windows cleanup script
cleanup_test_files.bat
```

### Windows Batch Version

#### System Requirements

- Windows operating system
- No additional software needed

#### How to Use

**Method 1: Double-click (Easiest)**

1. Download `desktop_organizer.bat`
2. Double-click the file
3. Choose from the interactive menu:
   - Option 1: Dry Run (Preview only)
   - Option 2: Organize (Move files)
   - Option 3: Exit

**Method 2: Command Prompt**

1. Open Command Prompt
2. Navigate to the folder containing the .bat file
3. Run: `desktop_organizer.bat`
4. Follow the menu prompts

## Windows System Requirements

Both versions are fully optimized for Windows:

- **File paths**: Uses Windows environment variables (`%USERPROFILE%\Desktop`)
- **File names**: Supports spaces and special characters in Windows file names
- **Case sensitivity**: Handles mixed-case file extensions (e.g., .JPG, .jpg)
- **Error handling**: Windows-specific error messages and troubleshooting
- **User interface**: Windows console commands (cls, pause, mkdir)
- **Permissions**: Handles Windows file permission issues gracefully

## How it works

1. **Scans** the target directory for files
2. **Categorizes** files based on their extensions
3. **Creates** necessary folders if they don't exist
4. **Moves** files to appropriate category folders
5. **Logs** all operations (Python version)
6. **Reports** statistics and any issues encountered

## Safety Features

- **Conflict resolution**: Files with same names are skipped, not overwritten
- **Logging**: Python version creates detailed logs of all operations
- **Dry-run mode**: Test organization without moving files (Python version)
- **Error handling**: Graceful handling of permission errors and file locks

## Examples

### Before Organization

```text
Desktop/
├── vacation_photo.jpg
├── presentation.pptx
├── music_file.mp3
├── document.pdf
├── script.py
├── archive.zip
└── unknown_file.xyz
```

### After Organization

```text
Desktop/
├── images/
│   └── vacation_photo.jpg
├── presentations/
│   └── presentation.pptx
├── audio/
│   └── music_file.mp3
├── documents/
│   └── document.pdf
├── code/
│   └── script.py
├── archives/
│   └── archive.zip
└── other/
    └── unknown_file.xyz
```

## Testing Workflow

To safely test the desktop organizer:

1. **Generate test files**: Run `generate_test_files.bat` (Windows) or `python generate_test_files.py` (any OS)
2. **Run dry run**: Choose option 1 in the organizer to preview changes
3. **Organize files**: Choose option 2 to actually move files
4. **Verify results**: Check that files are in correct folders
5. **Clean up**: Run `cleanup_test_files.bat` to remove test files and folders

The test file generator creates 25 files across all supported categories, giving you a comprehensive test of the organizer's functionality.

## Contributing

We welcome contributions! If you have ideas for improvements or new features:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

Some ideas for contributions:

- Adding GUI interface
- Supporting more file types
- Adding configuration file support
- Creating macOS shell script version
- Adding file size-based organization
- Implementing undo functionality

## License

MIT License - see LICENSE file for details.

## Disclaimer

This software is provided as is, without any warranty or liability. Use it at your own risk. Make sure you have a backup of your files before running the script. The authors are not responsible for any loss or damage caused by this software.

We appreciate feedback on this project and welcome suggestions for improvements. If you can contribute by adding features (such as GUI interface, icons, etc.), that would be greatly appreciated.
