#!/usr/bin/env python3
"""
Test File Generator for Desktop Organizer
Creates 25 sample files of different types on the desktop for testing
Windows-optimized version
"""

import os
import platform

def create_test_files():
    """Create 25 test files of different types on the desktop"""
    
    # Get desktop path - Windows-optimized
    if platform.system() == "Windows":
        # Use Windows-specific path
        desktop_path = os.path.join(os.environ.get('USERPROFILE', os.path.expanduser("~")), "Desktop")
    else:
        # Use standard path for other systems
        desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    
    if not os.path.exists(desktop_path):
        print(f"Error: Desktop directory not found at {desktop_path}")
        if platform.system() == "Windows":
            print("Make sure you have a Desktop folder in your user profile.")
            print(f"Expected location: {os.environ.get('USERPROFILE', 'C:\\Users\\YourName')}\\Desktop")
        return
    
    print("=" * 40)
    print("   TEST FILE GENERATOR")
    print("=" * 40)
    print(f"Target directory: {desktop_path}")
    print("Creating 25 test files...")
    print("=" * 40)
    print()
    
    file_count = 0
    
    # Define test files with their content
    test_files = [
        # Image files (5)
        ("test-photo.jpg", "JPEG image file for testing"),
        ("screenshot.png", "PNG image file for testing"),
        ("animated.gif", "GIF image file for testing"),
        ("logo.bmp", "BMP image file for testing"),
        ("icon.svg", "<svg><circle cx='50' cy='50' r='40'/></svg>"),
        
        # Video files (3)
        ("movie.mp4", "MP4 video file for testing"),
        ("clip.avi", "AVI video file for testing"),
        ("presentation.mkv", "MKV video file for testing"),
        
        # Audio files (3)
        ("song.mp3", "MP3 audio file for testing"),
        ("soundtrack.wav", "WAV audio file for testing"),
        ("music.flac", "FLAC audio file for testing"),
        
        # Document files (4)
        ("resume.pdf", "PDF document file for testing"),
        ("report.docx", "Word document file for testing"),
        ("notes.txt", "This is a test text file.\nIt contains multiple lines.\nUsed for testing the desktop organizer."),
        ("manual.rtf", "RTF document file for testing"),
        
        # Spreadsheet files (2)
        ("budget.xlsx", "Excel spreadsheet file for testing"),
        ("data.csv", "Name,Age,City\nJohn,25,New York\nJane,30,London"),
        
        # Presentation files (2)
        ("slides.pptx", "PowerPoint presentation file for testing"),
        ("demo.odp", "OpenDocument presentation file for testing"),
        
        # Code files (2)
        ("script.py", "#!/usr/bin/env python3\n# Python script file for testing\nprint('Hello World!')"),
        ("webpage.html", "<!DOCTYPE html>\n<html>\n<head><title>Test</title></head>\n<body><h1>Test Page</h1></body>\n</html>"),
        
        # Application files (1)
        ("installer.exe", "Executable application file for testing"),
        
        # Archive files (2)
        ("backup.zip", "ZIP archive file for testing"),
        ("compressed.rar", "RAR archive file for testing"),
        
        # Unknown/other files (1)
        ("mystery.xyz", "Unknown file type for testing the 'other' category"),
    ]
    
    # Group files by category for organized output
    categories = {
        "Image files": test_files[0:5],
        "Video files": test_files[5:8],
        "Audio files": test_files[8:11],
        "Document files": test_files[11:15],
        "Spreadsheet files": test_files[15:17],
        "Presentation files": test_files[17:19],
        "Code files": test_files[19:21],
        "Application files": test_files[21:22],
        "Archive files": test_files[22:24],
        "Unknown file types": test_files[24:25]
    }
    
    # Create files by category
    for category, files in categories.items():
        print(f"Creating {category.lower()}...")
        for filename, content in files:
            file_path = os.path.join(desktop_path, filename)
            try:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"  Created: {filename}")
                file_count += 1
            except Exception as e:
                print(f"  ERROR: Failed to create {filename} - {e}")
    
    print()
    print("=" * 40)
    print("GENERATION COMPLETE")
    print("=" * 40)
    print(f"Total files created: {file_count}")
    print(f"Location: {desktop_path}")
    print()
    print("These files are ready for testing with:")
    print("- desktop_organizer.py (Python version)")
    print("- desktop_organizer.bat (Batch version)")
    print()
    print("TESTING RECOMMENDATIONS:")
    print("1. First run a DRY RUN to see what would happen")
    print("2. Then run the actual organization")
    print("3. Check that files are moved to correct folders")
    print()

if __name__ == "__main__":
    try:
        create_test_files()
        input("Press Enter to exit...")
    except KeyboardInterrupt:
        print("\nOperation cancelled by user.")
    except Exception as e:
        print(f"An error occurred: {e}")
        input("Press Enter to exit...")
