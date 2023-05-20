from rich.console import Console
from rich.prompt import Prompt
from rich.table import Table


# Main entrypoint
def main():
    """
    Main function to run the CLI app. Going to act like my menu.
    :return: None
    """
    while True:
        console.print("\n1. List files\n2. Exit")
        choice = Prompt.ask("Choose a task or exit")


if __name__ == "__main__":
    console = Console()
    main()
