#!/usr/bin/env python3
"""
Desktop Organizer - Complete Windows-Optimized Version
Organizes files on desktop into categorized folders based on file extensions.

Features:
- Interactive menu system
- Windows-optimized path handling
- Comprehensive file type support (80+ extensions)
- Dry-run mode for safe testing
- Detailed logging and statistics
- Command-line options for advanced users
- Error handling and validation
- Cross-platform compatibility with Windows-first design
"""

import os
import glob
import shutil
import logging
import argparse
import sys
import platform
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Set


class DesktopOrganizer:
    """Desktop file organizer with comprehensive functionality."""
    
    def __init__(self, target_dir: str = None, dry_run: bool = False, enable_logging: bool = True):
        """
        Initialize the organizer.
        
        Args:
            target_dir: Directory to organize (default: Desktop)
            dry_run: If True, only simulate actions without moving files
            enable_logging: If True, create detailed logs
        """
        # Windows-optimized path handling
        if target_dir:
            self.target_dir = target_dir
        else:
            if platform.system() == "Windows":
                # Use Windows-specific path for maximum compatibility
                self.target_dir = os.path.join(os.environ.get('USERPROFILE', os.path.expanduser("~")), "Desktop")
            else:
                # Use standard path for other systems
                self.target_dir = os.path.join(os.path.expanduser("~"), "Desktop")
                
        self.dry_run = dry_run
        self.enable_logging = enable_logging
        self.stats = {
            'files_moved': 0,
            'files_skipped': 0,
            'folders_created': 0,
            'errors': 0
        }
        
        # Setup logging
        if self.enable_logging:
            self._setup_logging()
        else:
            # Create a simple logger that doesn't write to file
            self.logger = logging.getLogger('desktop_organizer')
            self.logger.setLevel(logging.INFO)
            if not self.logger.handlers:
                handler = logging.StreamHandler()
                formatter = logging.Formatter('%(message)s')
                handler.setFormatter(formatter)
                self.logger.addHandler(handler)
        
        # Comprehensive file type mapping - Windows-optimized
        self.file_types = {
            # Images
            "jpg": "images", "jpeg": "images", "png": "images", "gif": "images",
            "bmp": "images", "tiff": "images", "tif": "images", "svg": "images",
            "webp": "images", "ico": "images", "raw": "images", "psd": "images",
            
            # Videos
            "mp4": "videos", "avi": "videos", "mkv": "videos", "mov": "videos",
            "wmv": "videos", "flv": "videos", "webm": "videos", "m4v": "videos",
            "3gp": "videos", "mpg": "videos", "mpeg": "videos", "ogv": "videos",
            
            # Audio
            "mp3": "audio", "wav": "audio", "flac": "audio", "aac": "audio",
            "ogg": "audio", "wma": "audio", "m4a": "audio", "opus": "audio",
            "aiff": "audio", "amr": "audio",
            
            # Documents
            "doc": "documents", "docx": "documents", "pdf": "documents",
            "txt": "documents", "rtf": "documents", "odt": "documents",
            "pages": "documents", "tex": "documents",
            
            # Spreadsheets
            "xls": "spreadsheets", "xlsx": "spreadsheets", "csv": "spreadsheets",
            "ods": "spreadsheets", "numbers": "spreadsheets",
            
            # Presentations
            "ppt": "presentations", "pptx": "presentations", "odp": "presentations",
            "key": "presentations",
            
            # Code files
            "py": "code", "js": "code", "html": "code", "css": "code",
            "java": "code", "cpp": "code", "c": "code", "h": "code",
            "php": "code", "rb": "code", "go": "code", "rs": "code",
            "swift": "code", "kt": "code", "scala": "code", "pl": "code",
            "sh": "code", "bat": "code", "cmd": "code", "ps1": "code",
            "json": "code", "xml": "code", "yaml": "code", "yml": "code",
            "sql": "code", "md": "code", "ini": "code", "cfg": "code",
            
            # Applications
            "exe": "applications", "msi": "applications", "deb": "applications",
            "rpm": "applications", "dmg": "applications", "pkg": "applications",
            "app": "applications", "apk": "applications",
            
            # Archives
            "zip": "archives", "rar": "archives", "7z": "archives",
            "tar": "archives", "gz": "archives", "xz": "archives",
            "bz2": "archives", "tgz": "archives", "tbz2": "archives",
            "z": "archives", "lz": "archives", "lzma": "archives",
            
            # Fonts
            "ttf": "fonts", "otf": "fonts", "woff": "fonts", "woff2": "fonts",
            "eot": "fonts", "fon": "fonts",
            
            # E-books
            "epub": "ebooks", "mobi": "ebooks", "azw": "ebooks", "azw3": "ebooks",
            "fb2": "ebooks", "lit": "ebooks",
            
            # Shortcuts
            "lnk": "shortcuts", "url": "shortcuts", "desktop": "shortcuts",
        }
    
    def _setup_logging(self):
        """Setup logging to file and console."""
        # Create logs directory if it doesn't exist
        log_dir = os.path.join(self.target_dir, "organizer_logs")
        os.makedirs(log_dir, exist_ok=True)
        
        # Setup logger
        self.logger = logging.getLogger('desktop_organizer')
        self.logger.setLevel(logging.INFO)
        
        # Clear existing handlers
        self.logger.handlers.clear()
        
        # File handler
        log_file = os.path.join(log_dir, f"organizer_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log")
        file_handler = logging.FileHandler(log_file, encoding='utf-8')
        file_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(file_formatter)
        self.logger.addHandler(file_handler)
        
        # Console handler
        console_handler = logging.StreamHandler()
        console_formatter = logging.Formatter('%(message)s')
        console_handler.setFormatter(console_formatter)
        self.logger.addHandler(console_handler)
    
    def clear_screen(self):
        """Clear the console screen (Windows-optimized)"""
        if platform.system() == "Windows":
            os.system('cls')
        else:
            os.system('clear')
    
    def show_menu(self):
        """Display the interactive menu"""
        self.clear_screen()
        print("\n" + "="*60)
        print("         DESKTOP ORGANIZER - WINDOWS EDITION")
        print("="*60)
        print("1. Dry Run (Preview organization without moving files)")
        print("2. Organize (Actually move files)")
        print("3. Show Statistics")
        print("4. Exit")
        print("="*60)
        print(f"Target Directory: {self.target_dir}")
        print("="*60)
    
    def get_user_choice(self):
        """Get and validate user choice"""
        while True:
            try:
                choice = input("Please select an option (1-4): ").strip()
                if choice in ['1', '2', '3', '4']:
                    return int(choice)
                else:
                    print("Invalid choice. Please enter 1, 2, 3, or 4.")
            except KeyboardInterrupt:
                print("\nOperation cancelled by user.")
                return 4
    
    def _create_folder_if_not_exists(self, folder_path: str) -> bool:
        """Create folder if it doesn't exist."""
        if not os.path.exists(folder_path):
            if not self.dry_run:
                try:
                    os.makedirs(folder_path)
                    self.logger.info(f"Created folder: {os.path.basename(folder_path)}")
                    self.stats['folders_created'] += 1
                    return True
                except OSError as e:
                    self.logger.error(f"Failed to create folder {folder_path}: {e}")
                    self.stats['errors'] += 1
                    return False
            else:
                self.logger.info(f"[DRY RUN] Would create folder: {os.path.basename(folder_path)}")
                self.stats['folders_created'] += 1
                return True
        return False
    
    def _move_file(self, source: str, destination: str) -> bool:
        """Move file from source to destination."""
        if os.path.exists(destination):
            self.logger.warning(f"Skipped: {os.path.basename(source)} (already exists in {os.path.basename(os.path.dirname(destination))})")
            self.stats['files_skipped'] += 1
            return False
        
        if not self.dry_run:
            try:
                shutil.move(source, destination)
                self.logger.info(f"Moved: {os.path.basename(source)} -> {os.path.basename(os.path.dirname(destination))}")
                self.stats['files_moved'] += 1
                return True
            except (OSError, shutil.Error) as e:
                self.logger.error(f"Failed to move {os.path.basename(source)}: {e}")
                self.stats['errors'] += 1
                return False
        else:
            self.logger.info(f"[DRY RUN] Would move: {os.path.basename(source)} -> {os.path.basename(os.path.dirname(destination))}")
            self.stats['files_moved'] += 1
            return True
    
    def _get_file_extension(self, file_path: str) -> str:
        """Get file extension in lowercase (Windows case-insensitive)."""
        return os.path.splitext(file_path)[1][1:].lower()
    
    def _get_files_to_organize(self) -> List[str]:
        """Get list of files to organize, excluding directories and system files."""
        try:
            all_files = glob.glob(os.path.join(self.target_dir, "*"))
            # Filter out directories, hidden files, and log folder
            files_to_organize = [
                f for f in all_files 
                if os.path.isfile(f) 
                and not os.path.basename(f).startswith('.') 
                and 'organizer_logs' not in f
            ]
            return files_to_organize
        except OSError as e:
            self.logger.error(f"Failed to get files from {self.target_dir}: {e}")
            return []
    
    def organize_files(self) -> Dict[str, int]:
        """Organize files in the target directory."""
        self.logger.info(f"Starting file organization in: {self.target_dir}")
        self.logger.info(f"Mode: {'DRY RUN' if self.dry_run else 'EXECUTE'}")
        self.logger.info("-" * 50)
        
        # Validate target directory
        if not os.path.exists(self.target_dir):
            error_msg = f"Target directory does not exist: {self.target_dir}"
            if platform.system() == "Windows":
                error_msg += f"\nMake sure you have a Desktop folder in your user profile."
                error_msg += f"\nExpected location: {os.environ.get('USERPROFILE', 'C:\\Users\\YourName')}\\Desktop"
            self.logger.error(error_msg)
            return self.stats
        
        # Reset stats
        self.stats = {
            'files_moved': 0,
            'files_skipped': 0,
            'folders_created': 0,
            'errors': 0
        }
        
        files_to_organize = self._get_files_to_organize()
        self.logger.info(f"Found {len(files_to_organize)} files to organize")
        
        if not files_to_organize:
            self.logger.info("No files found to organize.")
            return self.stats
        
        # Group files by extension
        files_by_extension = {}
        unknown_files = []
        
        for file_path in files_to_organize:
            extension = self._get_file_extension(file_path)
            
            if extension in self.file_types:
                category = self.file_types[extension]
                if category not in files_by_extension:
                    files_by_extension[category] = []
                files_by_extension[category].append(file_path)
            else:
                unknown_files.append(file_path)
        
        # Organize known file types
        for category, files in files_by_extension.items():
            self.logger.info(f"Organizing {category} files...")
            category_folder = os.path.join(self.target_dir, category)
            self._create_folder_if_not_exists(category_folder)
            
            for file_path in files:
                file_name = os.path.basename(file_path)
                destination = os.path.join(category_folder, file_name)
                self._move_file(file_path, destination)
        
        # Handle unknown file types
        if unknown_files:
            self.logger.info("Organizing unknown file types...")
            other_folder = os.path.join(self.target_dir, "other")
            self._create_folder_if_not_exists(other_folder)
            
            for file_path in unknown_files:
                file_name = os.path.basename(file_path)
                destination = os.path.join(other_folder, file_name)
                self._move_file(file_path, destination)
        
        self._print_summary()
        return self.stats
    
    def _print_summary(self):
        """Print operation summary."""
        self.logger.info("\n" + "="*50)
        self.logger.info("ORGANIZATION SUMMARY")
        self.logger.info("="*50)
        if self.dry_run:
            self.logger.info("This was a DRY RUN - no files were actually moved")
        self.logger.info(f"Files moved: {self.stats['files_moved']}")
        self.logger.info(f"Files skipped: {self.stats['files_skipped']}")
        self.logger.info(f"Folders created: {self.stats['folders_created']}")
        self.logger.info(f"Errors: {self.stats['errors']}")
        self.logger.info("="*50)
    
    def show_statistics(self):
        """Show current statistics and file type information."""
        self.clear_screen()
        print("\n" + "="*60)
        print("         DESKTOP ORGANIZER STATISTICS")
        print("="*60)
        print(f"Target Directory: {self.target_dir}")
        print(f"Directory Exists: {os.path.exists(self.target_dir)}")
        
        if os.path.exists(self.target_dir):
            files = self._get_files_to_organize()
            print(f"Files Found: {len(files)}")
            
            # Analyze file types
            type_counts = {}
            unknown_count = 0
            
            for file_path in files:
                extension = self._get_file_extension(file_path)
                if extension in self.file_types:
                    category = self.file_types[extension]
                    type_counts[category] = type_counts.get(category, 0) + 1
                else:
                    unknown_count += 1
            
            print("\nFile Type Distribution:")
            print("-" * 30)
            for category, count in sorted(type_counts.items()):
                print(f"{category.capitalize()}: {count}")
            if unknown_count > 0:
                print(f"Unknown types: {unknown_count}")
        
        print("\nSupported Categories:")
        print("-" * 30)
        categories = sorted(set(self.file_types.values()))
        for i, category in enumerate(categories, 1):
            print(f"{i:2d}. {category.capitalize()}")
        
        print("="*60)
        input("Press Enter to continue...")
    
    def run_interactive(self):
        """Run the interactive menu system."""
        while True:
            self.show_menu()
            choice = self.get_user_choice()
            
            if choice == 1:
                # Dry run
                print("\nStarting DRY RUN - No files will be moved...")
                self.dry_run = True
                self.organize_files()
                input("\nPress Enter to continue...")
                
            elif choice == 2:
                # Actual organization
                print("\nWARNING: This will actually move your files!")
                confirm = input("Are you sure you want to continue? (y/N): ").strip().lower()
                if confirm in ['y', 'yes']:
                    self.dry_run = False
                    self.organize_files()
                else:
                    print("Operation cancelled.")
                input("\nPress Enter to continue...")
                
            elif choice == 3:
                # Show statistics
                self.show_statistics()
                
            elif choice == 4:
                # Exit
                print("Thank you for using Desktop Organizer!")
                break


def main():
    """Main function with both interactive and command-line modes."""
    parser = argparse.ArgumentParser(
        description="Desktop Organizer - Windows Edition",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python desktop_organizer.py                    # Interactive mode
  python desktop_organizer.py --dry-run          # Command-line dry run
  python desktop_organizer.py --target-dir "C:\\MyFolder"  # Custom directory
        """
    )
    parser.add_argument(
        "--target-dir", 
        type=str, 
        help="Target directory to organize (default: Desktop)"
    )
    parser.add_argument(
        "--dry-run", 
        action="store_true", 
        help="Simulate actions without actually moving files"
    )
    parser.add_argument(
        "--no-interactive",
        action="store_true",
        help="Run in command-line mode (no interactive menu)"
    )
    parser.add_argument(
        "--no-logging",
        action="store_true",
        help="Disable file logging"
    )
    
    args = parser.parse_args()
    
    try:
        organizer = DesktopOrganizer(
            target_dir=args.target_dir, 
            dry_run=args.dry_run,
            enable_logging=not args.no_logging
        )
        
        if args.no_interactive or args.dry_run:
            # Command-line mode
            organizer.organize_files()
        else:
            # Interactive mode
            organizer.run_interactive()
            
    except KeyboardInterrupt:
        print("\nOperation cancelled by user.")
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()