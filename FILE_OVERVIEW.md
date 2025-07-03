# File-Organizer Project Files - Windows Edition

## Core Organizer Files (Windows Optimized)

- **`desktop_organizer.py`** - Complete Python script with interactive menu and advanced features (Windows optimized)
- **`desktop_organizer.bat`** - Windows batch version with interactive menu (recommended for Windows users)

## Testing Files (Windows Compatible)

- **`generate_test_files.py`** - Python script to create 25 test files (Windows paths)
- **`generate_test_files.bat`** - Windows batch script to create 25 test files (recommended)
- **`cleanup_test_files.bat`** - Windows script to remove test files and folders
- **`test_organizer.py`** - Advanced test script for the Python version
- **`test_windows_paths.py`** - Windows path compatibility test
- **`windows_compatibility_test.py`** - Comprehensive Windows compatibility test suite

## Documentation (Windows Focused)

- **`README.md`** - Complete documentation optimized for Windows
- **`WINDOWS_GUIDE.md`** - Detailed Windows installation and usage guide
- **`FILE_OVERVIEW.md`** - This file - project overview
- **`LICENSE`** - MIT license file

## Configuration Files

- **`config.ini`** - Configuration template for customizing file mappings
- **`requirements.txt`** - Python dependencies (none needed for core functionality)

## Git Files

- **`.gitignore`** - Git ignore patterns
- **`.gitattributes`** - Git line ending settings
- **`.github/workflows/`** - CI/CD workflows for testing

## Usage Summary for Windows

### For Windows Users (Easiest Method)

1. Download `desktop_organizer.bat`
2. Double-click to run
3. Choose option 1 for dry run, option 2 to organize
4. Files will be organized in `C:\Users\YourName\Desktop\`

### For Python Users on Windows

1. Download `desktop_organizer.py`
2. Run: `python desktop_organizer.py`
3. Uses Windows environment variables for paths
4. Optimized for Windows file system

### For Testing on Windows

1. Run `generate_test_files.bat` to create 25 test files
2. Test the organizer with dry run first
3. Run `cleanup_test_files.bat` to clean up when done
4. Run `test_windows_paths.py` to verify path compatibility

## Windows-Specific Features

- **Path Handling**: Uses `%USERPROFILE%\Desktop` environment variable
- **Error Messages**: Windows-specific troubleshooting information
- **File Operations**: Optimized for Windows file system
- **Console Commands**: Uses Windows batch commands (cls, pause, mkdir)
- **Compatibility**: Tested on Windows 7, 8, 10, and 11
