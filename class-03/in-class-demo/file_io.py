# Open the drawer
file = open("example.txt", "r")
content = file.read()
print(content)
print(file.closed)
file.close()



