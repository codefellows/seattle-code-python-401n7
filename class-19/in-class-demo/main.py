from rich.console import Console
from rich.prompt import Prompt
from rich.table import Table
import os


def list_files(directory):
    """List all files in a given directory"""
    files = os.listdir(directory)
    # build up a rich table iteratively
    table = Table(title=f"Files in [bold green]{directory}[/bold green]:")
    table.add_column("File Name")
    for file in files:
        table.add_row(file)


# Main entrypoint
def main():
    """
    Main function to run the CLI app. Going to act like my menu.
    :return: None
    """
    while True:
        console.print("\n1. List files\n2. Exit")
        choice = Prompt.ask("Choose a task or exit")

        # if elif else block
        if choice == "1":
            # invoke list_files function
            pass
        elif choice == "2":
            break


if __name__ == "__main__":
    console = Console()
    main()
