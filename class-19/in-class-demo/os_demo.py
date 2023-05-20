import os
import shutil


# Create a new directory
os.mkdir('test_dir')
print('Directory created.')

# List files and directories in the current directory
# List of files and directories
# print(os.listdir("."))

# Delete the directory with shutil
# Use shutil.rmtree() to remove a directory and all its contents
# shutil.rmtree('test_dir')
# print('test_dir deleted')

# Join path components for the new file in the created directory
file_path = os.path.join('test_dir', 'test_file.txt')  # returns a file path!
print(f'Constructed file path: {file_path}')

# # Create a new file in the created directory
with open(file_path, 'w') as file:
    file.write('Hello, World!')

# # List files and directories in the created directory
print('List of files/directories in test_dir:')
print(os.listdir('test_dir'))

# Split the file path into root and extension
root, ext = os.path.splitext(file_path)
print(f'Root of the file path: {root}')
print(f'Extension of the file path: {ext}')

