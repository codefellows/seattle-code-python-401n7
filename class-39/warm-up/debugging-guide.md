# Python Debugging Guide with `pdb`

Additional Links:

- [Geeks for Geeks](https://www.geeksforgeeks.org/python-debugger-python-pdb/)
- [Python Docs](https://docs.python.org/3/library/pdb.html)

`pdb` is a built-in Python module for interactive source code debugging. It supports setting breakpoints, stepping through code, inspecting variables, evaluating expressions, and more. It's a very useful tool when trying to identify and understand errors or unexpected behavior in your Python scripts.

**1. Importing pdb**

To use pdb, you first need to import it into your Python script. You can do this using the following import statement:

```python
import pdb
```

**2. Setting Breakpoints**

The most common use of pdb is to set a "breakpoint" in your code. When the Python interpreter hits this breakpoint, it will pause execution and give control to pdb, allowing you to manually inspect and control the program execution. You can set a breakpoint using the `set_trace` function.

```python
def some_function():
    x = 10
    y = 20
    pdb.set_trace()  # this is where the execution will pause
    z = x + y
    print(z)
```

In the example above, when the `set_trace` line is executed, the program will pause and open a pdb debugging prompt. The prompt allows you to input pdb commands directly.

**3. The pdb prompt and commands**

When pdb is active, you'll see a command prompt that looks something like this: `(Pdb)`. At this prompt, you can type a number of commands to control execution and inspect your program. Here are a few of the most commonly used commands:

- `n(ext)`: Execute the next line and stop.
- `s(tep)`: Execute and step into function.
- `r(eturn)`: Continue execution until the current function returns.
- `c(ont(inue))`: Continue execution and only stop when a breakpoint is encountered.
- `q(uit)`: Quit the debugger and exit.
- `p(rint)`: Print the value of an expression.
- `l(ist)`: List the source code around the current line.
- `h(elp)`: Show a list of all available commands, or get detailed help on a specific command.

For example, you can print the value of a variable by typing `p variable_name` at the pdb prompt. This can be useful if you're not sure what value a variable is taking on at a certain point in your program.

**4. Practical example**

Let's walk through a simple example where we use pdb to debug a function that calculates the factorial of a number.

```python
import pdb

def factorial(n):
    if n == 0:
        return 1
    else:
        pdb.set_trace()
        return n * factorial(n - 1)

print(factorial(5))
```

This program is intended to calculate the factorial of 5, but we have introduced a breakpoint in the recursive part of the factorial function. When you run this program, execution will stop at the `pdb.set_trace()` call, and you'll be dropped into the pdb prompt.

At the pdb prompt, you can use commands like `p n` to print the current value of `n`. You can use `n` to step to the next line (this will take you into the recursive call to `factorial`). As you step through the function calls, you can see how the value of `n` changes with each call, giving you insight into how the recursion is progressing.

Remember, Python also has the `pdb` module's functionality built into the built-in function breakpoint since Python 3.7. You can call this function without arguments to start the debugger at that point.

```python
breakpoint()
```

The behavior of `breakpoint()` can be controlled by two environment variables `PYTHONBREAKPOINT` and `PYTHONDEBUGGER`.

**5. Post-mortem debugging**

Another useful feature of pdb is the ability to do "post-mortem" debugging. This allows you to inspect your program's state at the point of an exception. This is particularly useful for examining the program state in the event of an unexpected error.

```python
import pdb

def divide(x, y):
    return x / y

try:
    divide(1, 0)
except Exception:
    pdb.post_mortem()
```

In the example above, calling `1/0` raises a `ZeroDivisionError`. When the exception is caught, we call `pdb.post_mortem()`. This starts a pdb session at the point of the exception, allowing you to inspect the state of your program at that point.

In a real-world development scenario, pdb can be a powerful tool for understanding and debugging complex behaviors in your Python programs. This is just a basic introduction to pdb, and there are many more advanced features and techniques to explore.
