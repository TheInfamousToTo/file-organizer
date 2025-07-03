@echo off
REM Cleanup Script for Test Files
REM Removes all test files created by generate_test_files.bat
REM Windows-optimized version

setlocal enabledelayedexpansion

REM Set the desktop path using Windows environment variable
set "DESKTOP_PATH=%USERPROFILE%\Desktop"

REM Verify desktop path exists
if not exist "%DESKTOP_PATH%" (
    echo ERROR: Desktop folder not found at %DESKTOP_PATH%
    echo Nothing to clean up.
    echo.
    pause
    exit /b 1
)

echo ========================================
echo   TEST FILE CLEANUP FOR WINDOWS
echo ========================================
echo Target directory: %DESKTOP_PATH%
echo Removing test files...
echo ========================================
echo.

REM Initialize counter
set /a FILES_REMOVED=0

REM List of test files to remove
set FILES_TO_REMOVE=test-photo.jpg screenshot.png animated.gif logo.bmp icon.svg movie.mp4 clip.avi presentation.mkv song.mp3 soundtrack.wav music.flac resume.pdf report.docx notes.txt manual.rtf budget.xlsx data.csv slides.pptx demo.odp script.py webpage.html installer.exe backup.zip compressed.rar mystery.xyz

REM Remove each test file
for %%f in (%FILES_TO_REMOVE%) do (
    if exist "%DESKTOP_PATH%\%%f" (
        del "%DESKTOP_PATH%\%%f" >nul 2>&1
        if !errorlevel! equ 0 (
            echo   Removed: %%f
            set /a FILES_REMOVED+=1
        ) else (
            echo   ERROR: Failed to remove %%f
        )
    )
)

REM Also remove any created folders if they're empty
echo.
echo Checking for empty test folders...
set FOLDERS_TO_CHECK=images videos audio documents spreadsheets presentations code applications archives fonts ebooks shortcuts other

for %%d in (%FOLDERS_TO_CHECK%) do (
    if exist "%DESKTOP_PATH%\%%d" (
        rmdir "%DESKTOP_PATH%\%%d" >nul 2>&1
        if !errorlevel! equ 0 (
            echo   Removed empty folder: %%d
        )
    )
)

echo.
echo ========================================
echo CLEANUP COMPLETE
echo ========================================
echo Files removed: %FILES_REMOVED%
echo Desktop should now be clean and ready for new tests
echo.
pause
