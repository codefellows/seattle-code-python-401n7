from rich.console import Console
from rich.prompt import Prompt
from rich.table import Table
import os


def list_files(directory):
    """List all files in a given directory"""
    try:
        files = os.listdir(directory)
        # build up a rich table iteratively
        table = Table(title=f"Files in [bold green]{directory}[/bold green]:")
        table.add_column("File Name")
        for file in files:
            table.add_row(file)
        console.print(table)
    except FileNotFoundError:
        console.print(f"[bold red]Directory [underline]{directory}[/underline] not found!!!!![/bold red]")


# Main entrypoint
def main():
    """
    Main function to run the CLI app. Going to act like my menu.
    :return: None
    """
    while True:
        # 1. Print options
        console.print("\n1. List files\n2. Exit")
        choice = Prompt.ask("Choose a task or exit")

        # 2. Build if/elif/else block
        if choice == "1":
            # invoke list_files function
            # 3. Get user input
            directory = Prompt.ask("Enter the [red]directory[/red] to list [underline]files[/underline]")
            list_files(directory)
        elif choice == "2":
            break


if __name__ == "__main__":
    console = Console()
    main()
