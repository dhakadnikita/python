import os

def list_directory_contents(path):
    try:
        # List all files and directories in the specified path
        contents = os.listdir(path)
        print(f"Contents of the directory '{path}':")
        for item in contents:
            print(item)
    except FileNotFoundError:
        print(f"The directory '{path}' does not exist.")
    except PermissionError:
        print(f"Permission denied to access the directory '{path}'.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
directory_path = "/path/to/your/directory"
list_directory_contents(directory_path)

