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




