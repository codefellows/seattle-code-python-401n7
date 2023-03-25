# Open the drawer
file = open("example.txt", "r")
content = file.read()
print(content)
print(file.closed)
file.close()


# Use a 'with' statement!
# example of a context manager. here it automatically closes the file
with open("example.txt", "r") as file:
    content = file.read()
    print(content)


with open("example_write.txt", "w") as file:
    file.write("Hello world!!")


with open("example.txt", "r") as reader, open("example_write.txt", "a") as file:
    file.write("Hello again")
    file.write(reader.read())


# File doesn't exist!
try:
    with open("does_not_exist.txt", "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    # possibly do other logic here
    print("The file does not exist")
else:
    # Code to execute if no exception occurred
    print("The file MUST exist")
finally:
    # Code to execute regardless of whether an exception occurred or not
    print("This will always print, the try except block is done")


