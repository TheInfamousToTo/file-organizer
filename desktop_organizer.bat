@echo off
REM Desktop Organizer Batch Script with Interactive Menu
REM Organizes files on desktop into categorized folders
REM Author: Windows-optimized version with dry run functionality
REM Compatible with Windows 7, 8, 10, 11

setlocal enabledelayedexpansion

REM Set the desktop path using Windows environment variable
set "DESKTOP_PATH=%USERPROFILE%\Desktop"

REM Verify desktop path exists
if not exist "%DESKTOP_PATH%" (
    echo ERROR: Desktop folder not found at %DESKTOP_PATH%
    echo Please make sure your Desktop folder exists.
    echo.
    pause
    exit /b 1
)

REM Initialize counters
set /a FILES_MOVED=0
set /a FILES_SKIPPED=0
set /a FOLDERS_CREATED=0
set "DRY_RUN=false"

:MAIN_MENU
cls
echo.
echo ==================================================
echo           DESKTOP ORGANIZER
echo ==================================================
echo 1. Dry Run (Preview organization without moving files)
echo 2. Organize (Actually move files)
echo 3. Exit
echo ==================================================
echo.
set /p CHOICE="Please select an option (1-3): "

if "%CHOICE%"=="1" (
    set "DRY_RUN=true"
    goto START_ORGANIZATION
)
if "%CHOICE%"=="2" (
    set "DRY_RUN=false"
    echo.
    echo WARNING: This will actually move your files!
    set /p CONFIRM="Are you sure you want to continue? (Y/N): "
    if /i "!CONFIRM!"=="Y" goto START_ORGANIZATION
    if /i "!CONFIRM!"=="YES" goto START_ORGANIZATION
    echo Operation cancelled.
    echo.
    pause
    goto MAIN_MENU
)
if "%CHOICE%"=="3" (
    echo Thank you for using Desktop Organizer!
    goto END
)

echo Invalid choice. Please enter 1, 2, or 3.
echo.
pause
goto MAIN_MENU

:START_ORGANIZATION
cls
echo.
echo ========================================
echo Desktop File Organizer
echo ========================================
echo Target directory: %DESKTOP_PATH%
if "%DRY_RUN%"=="true" (
    echo Mode: DRY RUN ^(Preview only^)
) else (
    echo Mode: ORGANIZE ^(Moving files^)
)
echo ----------------------------------------
echo.

REM Reset counters
set /a FILES_MOVED=0
set /a FILES_SKIPPED=0
set /a FOLDERS_CREATED=0

REM Create necessary folders
call :CreateFolder "images"
call :CreateFolder "videos"
call :CreateFolder "audio"
call :CreateFolder "documents"
call :CreateFolder "spreadsheets"
call :CreateFolder "presentations"
call :CreateFolder "code"
call :CreateFolder "applications"
call :CreateFolder "archives"
call :CreateFolder "fonts"
call :CreateFolder "ebooks"
call :CreateFolder "shortcuts"
call :CreateFolder "other"

REM Organize image files
echo Organizing image files...
call :MoveFiles "images" "*.jpg *.jpeg *.png *.gif *.bmp *.tiff *.tif *.svg *.webp *.ico *.raw"

REM Organize video files
echo Organizing video files...
call :MoveFiles "videos" "*.mp4 *.avi *.mkv *.mov *.wmv *.flv *.webm *.m4v *.3gp *.mpg *.mpeg"

REM Organize audio files
echo Organizing audio files...
call :MoveFiles "audio" "*.mp3 *.wav *.flac *.aac *.ogg *.wma *.m4a *.opus *.aiff"

REM Organize document files
echo Organizing document files...
call :MoveFiles "documents" "*.doc *.docx *.pdf *.txt *.rtf *.odt *.pages *.tex"

REM Organize spreadsheet files
echo Organizing spreadsheet files...
call :MoveFiles "spreadsheets" "*.xls *.xlsx *.csv *.ods *.numbers"

REM Organize presentation files
echo Organizing presentation files...
call :MoveFiles "presentations" "*.ppt *.pptx *.odp *.key"

REM Organize code files
echo Organizing code files...
call :MoveFiles "code" "*.py *.js *.html *.css *.java *.cpp *.c *.h *.php *.rb *.go *.rs *.swift *.kt *.json *.xml *.yaml *.yml *.sql *.md *.bat *.cmd *.ps1 *.sh"

REM Organize application files
echo Organizing application files...
call :MoveFiles "applications" "*.exe *.msi *.deb *.rpm *.dmg *.pkg *.app *.apk"

REM Organize archive files
echo Organizing archive files...
call :MoveFiles "archives" "*.zip *.rar *.7z *.tar *.gz *.xz *.bz2 *.tgz *.tbz2"

REM Organize font files
echo Organizing font files...
call :MoveFiles "fonts" "*.ttf *.otf *.woff *.woff2 *.eot *.fon"

REM Organize ebook files
echo Organizing ebook files...
call :MoveFiles "ebooks" "*.epub *.mobi *.azw *.azw3 *.fb2 *.lit"

REM Organize shortcut files
echo Organizing shortcut files...
call :MoveFiles "shortcuts" "*.lnk *.url *.desktop"

REM Move remaining files to "other" folder
echo Organizing remaining files...
for %%f in ("%DESKTOP_PATH%\*.*") do (
    if exist "%%f" (
        if not exist "%DESKTOP_PATH%\other\%%~nxf" (
            if "%DRY_RUN%"=="true" (
                echo [DRY RUN] Would move: %%~nxf ^-^> other
                set /a FILES_MOVED+=1
            ) else (
                move "%%f" "%DESKTOP_PATH%\other\" >nul 2>&1
                if !errorlevel! equ 0 (
                    echo Moved: %%~nxf ^-^> other
                    set /a FILES_MOVED+=1
                )
            )
        ) else (
            if "%DRY_RUN%"=="true" (
                echo [DRY RUN] Would skip: %%~nxf (already exists in other)
            ) else (
                echo Skipped: %%~nxf (already exists in other)
            )
            set /a FILES_SKIPPED+=1
        )
    )
)

REM Display summary
echo.
echo ========================================
echo ORGANIZATION SUMMARY
echo ========================================
if "%DRY_RUN%"=="true" (
    echo This was a DRY RUN - no files were actually moved
    echo Files that would be moved: %FILES_MOVED%
    echo Files that would be skipped: %FILES_SKIPPED%
    echo Folders that would be created: %FOLDERS_CREATED%
) else (
    echo Files moved: %FILES_MOVED%
    echo Files skipped: %FILES_SKIPPED%
    echo Folders created: %FOLDERS_CREATED%
)
echo ========================================
echo.
if "%DRY_RUN%"=="true" (
    echo Preview complete!
) else (
    echo Organization complete!
)
echo.
pause
goto MAIN_MENU

:END
echo Goodbye!
pause >nul
exit /b 0

REM Function to create folders
:CreateFolder
set "FOLDER_NAME=%~1"
if not exist "%DESKTOP_PATH%\%FOLDER_NAME%" (
    if "%DRY_RUN%"=="true" (
        echo [DRY RUN] Would create folder: %FOLDER_NAME%
        set /a FOLDERS_CREATED+=1
    ) else (
        mkdir "%DESKTOP_PATH%\%FOLDER_NAME%" 2>nul
        if !errorlevel! equ 0 (
            echo Created folder: %FOLDER_NAME%
            set /a FOLDERS_CREATED+=1
        )
    )
)
goto :eof

REM Function to move files by pattern
:MoveFiles
set "FOLDER_NAME=%~1"
set "PATTERNS=%~2"

for %%p in (%PATTERNS%) do (
    for %%f in ("%DESKTOP_PATH%\%%p") do (
        if exist "%%f" (
            if not exist "%DESKTOP_PATH%\%FOLDER_NAME%\%%~nxf" (
                if "%DRY_RUN%"=="true" (
                    echo [DRY RUN] Would move: %%~nxf ^-^> %FOLDER_NAME%
                    set /a FILES_MOVED+=1
                ) else (
                    move "%%f" "%DESKTOP_PATH%\%FOLDER_NAME%\" >nul 2>&1
                    if !errorlevel! equ 0 (
                        echo Moved: %%~nxf ^-^> %FOLDER_NAME%
                        set /a FILES_MOVED+=1
                    ) else (
                        echo Error moving: %%~nxf
                    )
                )
            ) else (
                if "%DRY_RUN%"=="true" (
                    echo [DRY RUN] Would skip: %%~nxf (already exists in %FOLDER_NAME%)
                ) else (
                    echo Skipped: %%~nxf (already exists in %FOLDER_NAME%)
                )
                set /a FILES_SKIPPED+=1
            )
        )
    )
)
goto :eof
