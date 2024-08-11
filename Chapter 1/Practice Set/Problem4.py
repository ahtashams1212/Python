import os

# List all files and directories in a specified directory
directory_path = '/'
entries = os.listdir(directory_path)
for entry in entries:
    # print the file
    print(entry)

