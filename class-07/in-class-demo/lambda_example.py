add = lambda x, y: x + y


print(add(5, 10))


numbers = [1, 2, 3, 4, 5]

# Using a lambda function to square each number in the list
squares = list(map(lambda x: x ** 2, numbers))

print(squares)  # Output: [1, 4, 9, 16, 25]


