#!/usr/bin/env python3
"""
Windows Path Test for Desktop Organizer
Verifies that paths work correctly on Windows systems
"""

import os
import platform

def test_windows_paths():
    """Test Windows-specific path handling"""
    print("=" * 50)
    print("WINDOWS PATH COMPATIBILITY TEST")
    print("=" * 50)
    print(f"Operating System: {platform.system()}")
    print(f"Platform: {platform.platform()}")
    print()
    
    # Test environment variables
    print("Windows Environment Variables:")
    userprofile = os.environ.get('USERPROFILE', 'Not found')
    print(f"USERPROFILE: {userprofile}")
    
    username = os.environ.get('USERNAME', 'Not found')
    print(f"USERNAME: {username}")
    
    homepath = os.environ.get('HOMEPATH', 'Not found')
    print(f"HOMEPATH: {homepath}")
    print()
    
    # Test desktop paths
    print("Desktop Path Detection:")
    
    # Method 1: Using USERPROFILE (recommended for Windows)
    if platform.system() == "Windows":
        windows_desktop = os.path.join(os.environ.get('USERPROFILE', ''), "Desktop")
    else:
        windows_desktop = "N/A (not Windows)"
    
    # Method 2: Using expanduser (cross-platform)
    standard_desktop = os.path.join(os.path.expanduser("~"), "Desktop")
    
    print(f"Windows method: {windows_desktop}")
    print(f"Standard method: {standard_desktop}")
    print()
    
    # Check which paths exist
    print("Path Existence Check:")
    if windows_desktop != "N/A (not Windows)":
        exists_windows = os.path.exists(windows_desktop)
        print(f"Windows path exists: {exists_windows}")
    
    exists_standard = os.path.exists(standard_desktop)
    print(f"Standard path exists: {exists_standard}")
    print()
    
    # Recommended path for the organizer
    if platform.system() == "Windows":
        recommended_path = windows_desktop
        method = "Windows USERPROFILE method"
    else:
        recommended_path = standard_desktop
        method = "Standard expanduser method"
    
    print("Recommendation:")
    print(f"Use: {recommended_path}")
    print(f"Method: {method}")
    print(f"Exists: {os.path.exists(recommended_path)}")
    print()
    
    # Test file operations
    if os.path.exists(recommended_path):
        print("Testing file operations...")
        try:
            test_file = os.path.join(recommended_path, "desktop_organizer_test.txt")
            
            # Try to create a test file
            with open(test_file, 'w') as f:
                f.write("Test file for desktop organizer")
            print("✓ File creation: SUCCESS")
            
            # Try to check if file exists
            if os.path.exists(test_file):
                print("✓ File existence check: SUCCESS")
            
            # Try to delete the test file
            os.remove(test_file)
            print("✓ File deletion: SUCCESS")
            
            print("✓ All file operations work correctly!")
            
        except Exception as e:
            print(f"✗ File operations failed: {e}")
    else:
        print("⚠ Cannot test file operations - desktop path doesn't exist")
    
    print()
    print("=" * 50)
    print("TEST COMPLETE")
    print("=" * 50)

if __name__ == "__main__":
    test_windows_paths()
    input("Press Enter to exit...")
