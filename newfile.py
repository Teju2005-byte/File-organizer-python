import os
import shutil
from pathlib import Path

# File type categories
FILE_TYPES = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif'],
    'Videos': ['.mp4', '.mkv', '.avi'],
    'Documents': ['.doc', '.docx', '.txt'],
    'PDFs': ['.pdf'],
    'Others': []
}

def organize_files(folder_path):
    folder = Path(folder_path)

    for file in folder.iterdir():
        if file.is_file():
            moved = False
            for category, extensions in FILE_TYPES.items():
                if file.suffix.lower() in extensions:
                    target_dir = folder / category
                    target_dir.mkdir(exist_ok=True)
                    shutil.move(str(file), str(target_dir / file.name))
                    moved = True
                    break
            if not moved:
                other_dir = folder / 'Others'
                other_dir.mkdir(exist_ok=True)
                shutil.move(str(file), str(other_dir / file.name))

# User input
user_folder = input("Enter the full folder path you want to organize:\n")
organize_files(user_folder)
print("✅ Folder organized successfully!")