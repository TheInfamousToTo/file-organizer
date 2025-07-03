#!/usr/bin/env python3
"""
Test script for the Desktop Organizer
Creates sample files and tests the organizer functionality
"""

import os
import tempfile
import shutil
from pathlib import Path
from desktop_organizer import DesktopOrganizer


def create_test_files(test_dir: str) -> None:
    """Create sample files for testing."""
    test_files = [
        "test_image.jpg",
        "test_video.mp4", 
        "test_audio.mp3",
        "test_document.pdf",
        "test_spreadsheet.xlsx",
        "test_presentation.pptx",
        "test_code.py",
        "test_archive.zip",
        "test_app.exe",
        "test_font.ttf",
        "test_ebook.epub",
        "test_shortcut.lnk",
        "unknown_file.xyz"
    ]
    
    for filename in test_files:
        file_path = os.path.join(test_dir, filename)
        with open(file_path, 'w') as f:
            f.write(f"Test content for {filename}")
        print(f"Created test file: {filename}")


def test_organizer():
    """Test the desktop organizer functionality."""
    # Create temporary directory for testing
    with tempfile.TemporaryDirectory() as temp_dir:
        print(f"Testing in directory: {temp_dir}")
        
        # Create test files
        print("\nCreating test files...")
        create_test_files(temp_dir)
        
        # List files before organization
        print(f"\nFiles before organization:")
        for item in os.listdir(temp_dir):
            if os.path.isfile(os.path.join(temp_dir, item)):
                print(f"  {item}")
        
        # Test dry run first
        print(f"\n--- DRY RUN TEST ---")
        organizer = DesktopOrganizer(target_dir=temp_dir, dry_run=True)
        stats = organizer.organize_files()
        
        # Test actual organization
        print(f"\n--- ACTUAL ORGANIZATION TEST ---")
        organizer = DesktopOrganizer(target_dir=temp_dir, dry_run=False)
        stats = organizer.organize_files()
        
        # Check results
        print(f"\nDirectory structure after organization:")
        for root, dirs, files in os.walk(temp_dir):
            level = root.replace(temp_dir, '').count(os.sep)
            indent = ' ' * 2 * level
            print(f"{indent}{os.path.basename(root)}/")
            subindent = ' ' * 2 * (level + 1)
            for file in files:
                if not file.endswith('.log'):  # Skip log files
                    print(f"{subindent}{file}")
        
        print(f"\nTest completed successfully!")
        return stats


if __name__ == "__main__":
    test_organizer()
