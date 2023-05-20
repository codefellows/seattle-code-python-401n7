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
table = Table(show_header=True, header_style="bold magenta")
table.add_column("Name", style="dim", width=20)
table.add_column("Age")
table.add_column("Country")

# Add rows to the table
table.add_row("John Doe", "30", "USA")
table.add_row("Jane Doe", "25", "Canada")
table.add_row(name, Prompt.ask("What is your age?"), Prompt.ask("What is your country?"))

# use rich print
console.print(table)
