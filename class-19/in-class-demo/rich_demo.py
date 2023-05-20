from rich.console import Console
from rich.prompt import Prompt


# Instantiate a console object
console = Console()

# Greet the user
console.print("Hello! [bold green]Hello again![/bold green]")

# Ask for user's name
name = Prompt.ask("What is your [bold]name?[/bold]")

# Display a message to the user
console.print(f"Nice to meet you, [bold blue]{name}[/bold blue]!")
