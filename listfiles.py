import os

def list_files_with_extension(directory, extension):
    files = [file for file in os.listdir(directory) if file.endswith(extension)]
    return files

# Example usage:
directory_path = "/path/to/directory"
file_extension = ".txt"
result = list_files_with_extension(directory_path, file_extension)
print(result)
