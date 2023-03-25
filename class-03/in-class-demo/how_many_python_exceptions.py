import builtins
exception_count = 0
for name, obj in vars(builtins).items():
    if isinstance(obj, type) and issubclass(obj, BaseException):
        exception_count += 1
print(f"There are {exception_count} built-in exceptions in Python 3.11.2")
