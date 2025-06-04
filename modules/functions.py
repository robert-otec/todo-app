FILEPATH = "todo_app/todos.txt"


def get_todos(filepath=FILEPATH):
    """Read a text file and return the list of todos."""
    with open(filepath, "r") as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    """Write the list of todos to a text file."""
    with open(filepath, "w") as file_local:
        file_local.writelines(todos_arg)

print(__name__)
if __name__ == "__main__":
    # This block is executed when the module is run directly.
    # It can be used for testing or demonstration purposes.
    print("Hello from functions")
    print(get_todos())