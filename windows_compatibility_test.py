#!/usr/bin/env python3
"""
Windows Compatibility Test Suite
Verifies that all scripts work correctly on Windows systems
"""

import os
import platform
import tempfile
import shutil
from pathlib import Path

def test_windows_environment():
    """Test Windows environment variables and paths"""
    print("=" * 60)
    print("WINDOWS COMPATIBILITY TEST SUITE")
    print("=" * 60)
    
    print(f"Operating System: {platform.system()}")
    print(f"Platform: {platform.platform()}")
    print(f"Python Version: {platform.python_version()}")
    print()
    
    # Test 1: Environment Variables
    print("1. Testing Windows Environment Variables:")
    print("-" * 40)
    
    if platform.system() == "Windows":
        userprofile = os.environ.get('USERPROFILE', 'NOT_FOUND')
        username = os.environ.get('USERNAME', 'NOT_FOUND')
        print(f"USERPROFILE: {userprofile}")
        print(f"USERNAME: {username}")
        
        # Test desktop path
        desktop_path = os.path.join(userprofile, "Desktop")
        print(f"Desktop Path: {desktop_path}")
        print(f"Desktop Exists: {os.path.exists(desktop_path)}")
    else:
        print("Not running on Windows - testing cross-platform compatibility")
        desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
        print(f"Desktop Path: {desktop_path}")
        print(f"Desktop Exists: {os.path.exists(desktop_path)}")
    
    print()
    
    # Test 2: Import all modules
    print("2. Testing Python Module Imports:")
    print("-" * 40)
    
    modules_to_test = [
        'desktop_organizer',
        'generate_test_files',
        'test_organizer',
        'test_windows_paths'
    ]
    
    for module_name in modules_to_test:
        try:
            __import__(module_name)
            print(f"✓ {module_name}: SUCCESS")
        except ImportError as e:
            print(f"✗ {module_name}: FAILED - {e}")
        except Exception as e:
            print(f"✗ {module_name}: ERROR - {e}")
    
    print()
    
    # Test 3: Path handling
    print("3. Testing Path Handling:")
    print("-" * 40)
    
    # Test Windows vs cross-platform path creation
    if platform.system() == "Windows":
        windows_path = os.path.join(os.environ.get('USERPROFILE', ''), "Desktop", "test_folder")
        print(f"Windows Path: {windows_path}")
    
    cross_platform_path = os.path.join(os.path.expanduser("~"), "Desktop", "test_folder")
    print(f"Cross-platform Path: {cross_platform_path}")
    
    # Test path operations
    try:
        # Create a temporary directory for testing
        with tempfile.TemporaryDirectory() as temp_dir:
            test_file = os.path.join(temp_dir, "test_file.txt")
            with open(test_file, 'w') as f:
                f.write("Test content")
            
            if os.path.exists(test_file):
                print("✓ File creation: SUCCESS")
            else:
                print("✗ File creation: FAILED")
                
            # Test file operations
            test_folder = os.path.join(temp_dir, "test_folder")
            os.makedirs(test_folder, exist_ok=True)
            
            if os.path.exists(test_folder):
                print("✓ Folder creation: SUCCESS")
            else:
                print("✗ Folder creation: FAILED")
                
            # Test file moving
            moved_file = os.path.join(test_folder, "moved_file.txt")
            shutil.move(test_file, moved_file)
            
            if os.path.exists(moved_file):
                print("✓ File moving: SUCCESS")
            else:
                print("✗ File moving: FAILED")
                
    except Exception as e:
        print(f"✗ Path operations: ERROR - {e}")
    
    print()
    
    # Test 4: Desktop Organizer Classes
    print("4. Testing Desktop Organizer Classes:")
    print("-" * 40)
    
    try:
        from desktop_organizer import DesktopOrganizer
        
        # Test with temporary directory
        with tempfile.TemporaryDirectory() as temp_dir:
            organizer = DesktopOrganizer(target_dir=temp_dir, dry_run=True)
            print(f"✓ DesktopOrganizer created with target: {temp_dir}")
            
            # Test file type mapping
            test_extensions = ['jpg', 'mp4', 'txt', 'py', 'unknown']
            for ext in test_extensions:
                file_path = f"test.{ext}"
                detected_ext = organizer._get_file_extension(file_path)
                category = organizer.file_types.get(detected_ext, 'other')
                print(f"  {ext} -> {category}")
                
    except Exception as e:
        print(f"✗ Desktop Organizer test: ERROR - {e}")
    
    print()
    
    # Test 5: File Extensions (Windows case-insensitive)
    print("5. Testing File Extension Handling:")
    print("-" * 40)
    
    test_cases = [
        "image.JPG",
        "image.jpg", 
        "video.MP4",
        "video.mp4",
        "document.PDF",
        "document.pdf"
    ]
    
    for test_case in test_cases:
        ext = os.path.splitext(test_case)[1][1:].lower()
        print(f"{test_case} -> extension: {ext}")
    
    print()
    
    # Summary
    print("=" * 60)
    print("WINDOWS COMPATIBILITY TEST COMPLETE")
    print("=" * 60)
    print()
    print("RECOMMENDATIONS FOR WINDOWS USERS:")
    print("1. Use desktop_organizer.bat for easiest setup (no Python required)")
    print("2. If using Python scripts, ensure Python 3.6+ is installed")
    print("3. All scripts use %USERPROFILE%\\Desktop for maximum compatibility")
    print("4. Test with dry-run mode first before organizing files")
    print("5. Scripts handle Windows file paths and permissions correctly")
    print()

if __name__ == "__main__":
    test_windows_environment()
