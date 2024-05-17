# Subtle Bugs Python Code

import os
import shutil
from datetime import datetime

def backup_files(source_dir, dest_dir):
    # This function is intended to backup files from source directory to destination directory
    try:
        files = os.listdir(source_dir)
        for file in files:
            source_path = os.path.join(source_dir, file)
            dest_path = os.path.join(dest_dir, file)
            shutil.copy(source_path, dest_path)
        print("Files backed up successfully!")
    except Exception as e:
        print(f"Error occurred during backup: {e}")

def log_activity(activity):
    # This function is intended to log activity to a file
    try:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open("activity_log.txt", "a") as f:
            f.write(f"{timestamp}: {activity}\n")
        print("Activity logged successfully!")
    except:
        print("Failed to log activity!")

def validate_input(number):
    # This function is intended to validate if the input is a positive integer
    try:
        if int(number) > 0:
            return True
        else:
            return False
    except ValueError:
        return False

def create_directory(dir_name):
    # This function is intended to create a new directory
    try:
        os.makedirs(dir_name)
        print("Directory created successfully!")
    except FileExistsError:
        print("Directory already exists!")
    except PermissionError:
        print("Permission denied!")
    except:
        print("Failed to create directory!")

if __name__ == "__main__":
    # Main entry point of the script
    print("Welcome to the Subtle Bugs Python Code")

    while True:
        print("\nMenu:")
        print("1. Backup Files")
        print("2. Log Activity")
        print("3. Create Directory")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            source_dir = input("Enter source directory: ")
            dest_dir = input("Enter destination directory: ")
            backup_files(source_dir, dest_dir)
        elif choice == "2":
            activity = input("Enter activity to log: ")
            log_activity(activity)
        elif choice == "3":
            dir_name = input("Enter directory name: ")
            create_directory(dir_name)
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")
