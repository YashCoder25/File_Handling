
from pathlib import Path

BASE_DIR = Path(".")

def readfileandfolder():
    """Display files and folders in the project directory."""
    items = sorted(BASE_DIR.iterdir())

    if not items:
        print("The folder is empty.")
        return

    for i, item in enumerate(items, start=1):
        kind = "Folder" if item.is_dir() else "File"
        print(f"{i}. {item.name} ({kind})")


def createfile():
    try:
        name = input("Enter the file name: ").strip()
        if not name:
            print("File name cannot be empty.")
            return

        p = BASE_DIR / name

        if p.exists():
            print("File or folder already exists.")
            return

        data = input("What do you want to write? ")
        p.write_text(data, encoding="utf-8")
        print("File created successfully!")

    except (OSError, ValueError) as err:
        print(f"An error occurred: {err}")


def readfile():
    try:
        readfileandfolder()
        name = input("Which file do you want to read? ").strip()
        p = BASE_DIR / name

        if p.is_file():
            print("\n--- File Content ---")
            print(p.read_text(encoding="utf-8"))
            print("--------------------")
        else:
            print("This file does not exist.")

    except (OSError, ValueError) as err:
        print(f"File reading error: {err}")


def updatefile():
    try:
        readfileandfolder()
        name = input("Which file do you want to update? ").strip()
        p = BASE_DIR / name

        if not p.is_file():
            print("This file does not exist.")
            return

        print("1. Rename file")
        print("2. Overwrite file content")
        print("3. Append content")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            new_name = input("Enter the new file name: ").strip()
            new_path = BASE_DIR / new_name

            if not new_name or new_path.exists():
                print("Invalid name or destination already exists.")
                return

            p.rename(new_path)
            print("File renamed successfully!")

        elif choice == "2":
            data = input("Enter the new content: ")
            p.write_text(data, encoding="utf-8")
            print("File content overwritten successfully!")

        elif choice == "3":
            data = input("Enter the content to append: ")
            with p.open("a", encoding="utf-8") as fs:
                fs.write(data)
            print("Content appended successfully!")

        else:
            print("Invalid choice.")

    except (OSError, ValueError) as err:
        print(f"File update error: {err}")


def deletefile():
    try:
        readfileandfolder()
        name = input("Which file do you want to delete? ").strip()
        p = BASE_DIR / name

        if not p.is_file():
            print("This file does not exist.")
            return

        confirm = input(f"Delete '{p.name}'? (y/n): ").strip().lower()

        if confirm == "y":
            p.unlink()
            print("File deleted successfully!")
        else:
            print("Deletion cancelled.")

    except OSError as err:
        print(f"File deletion error: {err}")


def main():
    while True:
        print("\n===== Python File Handling System =====")
        print("1. Create a file")
        print("2. Read a file")
        print("3. Update a file")
        print("4. Delete a file")
        print("5. List files and folders")
        print("0. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            createfile()
        elif choice == "2":
            readfile()
        elif choice == "3":
            updatefile()
        elif choice == "4":
            deletefile()
        elif choice == "5":
            readfileandfolder()
        elif choice == "0":
            print("Thank you for using the program!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
