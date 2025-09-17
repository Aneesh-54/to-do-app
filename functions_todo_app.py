# The below line is how we declare constants.
FILEPATH = "todos.txt"

# Since we know that filepath will always be "todos.txt", we can use default arguments
def get_todos(filepath=FILEPATH):
    """ Read a text file and return the contents
    as a list
    """
    with open(filepath, "r") as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    """ Write the contents of a list to a text file"""
    with open(filepath, "w") as file_local:
        file_local.writelines(todos_arg)


if __name__ == "__main__":
    print(get_todos())
