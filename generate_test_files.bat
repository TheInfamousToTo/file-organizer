@echo off
REM Test File Generator for Desktop Organizer
REM Creates 25 sample files of different types on the desktop for testing
REM Windows-optimized version compatible with Windows 7, 8, 10, 11

setlocal enabledelayedexpansion

REM Set the desktop path using Windows environment variable
set "DESKTOP_PATH=%USERPROFILE%\Desktop"

REM Verify desktop path exists
if not exist "%DESKTOP_PATH%" (
    echo ERROR: Desktop folder not found at %DESKTOP_PATH%
    echo Please make sure your Desktop folder exists.
    echo Expected location: %USERPROFILE%\Desktop
    echo.
    pause
    exit /b 1
)

echo ========================================
echo   TEST FILE GENERATOR FOR WINDOWS
echo ========================================
echo Target directory: %DESKTOP_PATH%
echo Creating 25 test files...
echo ========================================
echo.

REM Initialize counter
set /a FILE_COUNT=0

REM Create image files (5 files)
echo Creating image files...
call :CreateFile "test-photo.jpg" "JPEG image file for testing"
call :CreateFile "screenshot.png" "PNG image file for testing"
call :CreateFile "animated.gif" "GIF image file for testing"
call :CreateFile "logo.bmp" "BMP image file for testing"
call :CreateFile "icon.svg" "SVG image file for testing"

REM Create video files (3 files)
echo Creating video files...
call :CreateFile "movie.mp4" "MP4 video file for testing"
call :CreateFile "clip.avi" "AVI video file for testing"
call :CreateFile "presentation.mkv" "MKV video file for testing"

REM Create audio files (3 files)
echo Creating audio files...
call :CreateFile "song.mp3" "MP3 audio file for testing"
call :CreateFile "soundtrack.wav" "WAV audio file for testing"
call :CreateFile "music.flac" "FLAC audio file for testing"

REM Create document files (4 files)
echo Creating document files...
call :CreateFile "resume.pdf" "PDF document file for testing"
call :CreateFile "report.docx" "Word document file for testing"
call :CreateFile "notes.txt" "Text document file for testing"
call :CreateFile "manual.rtf" "RTF document file for testing"

REM Create spreadsheet files (2 files)
echo Creating spreadsheet files...
call :CreateFile "budget.xlsx" "Excel spreadsheet file for testing"
call :CreateFile "data.csv" "CSV spreadsheet file for testing"

REM Create presentation files (2 files)
echo Creating presentation files...
call :CreateFile "slides.pptx" "PowerPoint presentation file for testing"
call :CreateFile "demo.odp" "OpenDocument presentation file for testing"

REM Create code files (2 files)
echo Creating code files...
call :CreateFile "script.py" "# Python script file for testing\nprint('Hello World')"
call :CreateFile "webpage.html" "<!DOCTYPE html><html><head><title>Test</title></head><body><h1>Test Page</h1></body></html>"

REM Create application files (1 file)
echo Creating application files...
call :CreateFile "installer.exe" "Executable application file for testing"

REM Create archive files (2 files)
echo Creating archive files...
call :CreateFile "backup.zip" "ZIP archive file for testing"
call :CreateFile "compressed.rar" "RAR archive file for testing"

REM Create unknown/other files (1 file)
echo Creating unknown file types...
call :CreateFile "mystery.xyz" "Unknown file type for testing"

echo.
echo ========================================
echo GENERATION COMPLETE
echo ========================================
echo Total files created: %FILE_COUNT%
echo Location: %DESKTOP_PATH%
echo.
echo These files are ready for testing with:
echo - desktop_organizer.py (Python version)
echo - desktop_organizer.bat (Batch version)
echo.
echo TESTING RECOMMENDATIONS:
echo 1. First run a DRY RUN to see what would happen
echo 2. Then run the actual organization
echo 3. Check that files are moved to correct folders
echo.
pause
goto :eof

REM Function to create test files
:CreateFile
set "FILENAME=%~1"
set "CONTENT=%~2"

REM Create the file with content
echo %CONTENT% > "%DESKTOP_PATH%\%FILENAME%"

if exist "%DESKTOP_PATH%\%FILENAME%" (
    echo   Created: %FILENAME%
    set /a FILE_COUNT+=1
) else (
    echo   ERROR: Failed to create %FILENAME%
)

goto :eof
