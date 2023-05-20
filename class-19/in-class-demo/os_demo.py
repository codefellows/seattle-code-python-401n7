import os
import shutil


# Create a new directory
os.mkdir('test_dir')
print('Directory created.')

# List files and directories in the current directory
# List of files and directories
print(os.listdir("."))

# Delete the directory with shutil
# Use shutil.rmtree() to remove a directory and all its contents
shutil.rmtree('test_dir')
print('test_dir deleted')

