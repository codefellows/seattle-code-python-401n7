from rich.console import Console
from rich.prompt import Prompt
from rich.table import Table
import shutil
import re
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


def search_files(directory, pattern):
    """Search files in the given directory that match the given regex pattern."""
    try:
        files = os.listdir(directory)
        matches = [file for file in files if re.search(pattern, file)]
        table = Table(title=f"Files in [bold green]{directory}[/bold green] matching [bold blue]{pattern}[/bold blue]")
        table.add_column("Matching File Name", style="dim")
        for match in matches:
            table.add_row(match)
        console.print(table)
    except FileNotFoundError:
        console.print("[bold red]Directory not found.[/bold red]")


def move_file(directory, file, target_directory):
    """Move the given file from the current directory to the target directory."""
    try:
        shutil.move(os.path.join(directory, file), os.path.join(target_directory, file))
        console.print(f"[bold green]{file}[/bold green] has been moved from [bold blue]{directory}[/bold blue] to [bold yellow]{target_directory}[/bold yellow]")
    except FileNotFoundError:
        console.print("[bold red]Directory or file not found.[/bold red]")


# Main entrypoint
def main():
    """
    Main function to run the CLI app. Going to act like my menu.
    :return: None
    """
    while True:
        # 1. Print options
        console.print("\n1. List files\n2. Search files\n3. Move file\n4. Exit")
        choice = Prompt.ask("Choose a task (Enter the number)", choices=['1', '2', '3', '4'], default='4')

        # 2. Build if/elif/else block
        if choice == "1":
            # invoke list_files function
            # 3. Get user input
            directory = Prompt.ask("Enter the [red]directory[/red] to list [underline]files[/underline]")
            list_files(directory)
        elif choice == '2':
            directory = Prompt.ask("Enter the directory to search files")
            pattern = Prompt.ask("Enter the regex pattern to search for")
            search_files(directory, pattern)
        elif choice == '3':
            directory = Prompt.ask("Enter the current directory of the file")
            file = Prompt.ask("Enter the file to move")
            target_directory = Prompt.ask("Enter the target directory to move the file to")
            move_file(directory, file, target_directory)
        else:
            break


if __name__ == "__main__":
    console = Console()
    main()
