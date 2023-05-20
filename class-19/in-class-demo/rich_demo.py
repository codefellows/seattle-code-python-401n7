from rich.console import Console
from rich.prompt import Prompt
from rich.table import Table


# Instantiate a console object
console = Console()

# Greet the user
console.print("Hello! [bold green]Hello again![/bold green]")

# Ask for user's name
name = Prompt.ask("What is your [bold]name?[/bold]")

# Display a message to the user
console.print(f"Nice to meet you, [bold blue]{name}[/bold blue]!")

# Create a table!
table = Table()
table.add_column("Name")
table.add_column("Age")

# use rich print
console.print(table)
