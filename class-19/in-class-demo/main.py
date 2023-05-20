from rich.console import Console
from rich.prompt import Prompt
from rich.table import Table


def list_files():
    pass


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
