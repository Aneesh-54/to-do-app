# With the below line of code, there is no need to
# prefix anything while calling the function

# from functions import get_todos, write_todos

# The below method is mostly preferred.

import time
import functions_todo_app


print(f"It is {time.strftime("%b %d, %Y %I:%M:%S %p")}")
while True:
    user_input = input("Type \"add\", \"show\", \"edit\", \"complete\" or \"exit\": ").strip()


    if user_input.startswith("add"):
        # file = open("todos.txt", "r")
        # todos = file.readlines()
        # file.close()

        # The above code (commented) can be written using with context manager as follows and
        # the method has been repeated throughout the code

        # with open("todos.txt", "r") as file:
        #     todos = file.readlines()

        # Since we have created a function for reading from "todos.txt" at the top, the above code
        # (commented) is no longer necessary. We can simply write the following code and use it
        # at all repetitions

        todos = functions_todo_app.get_todos()

        todo = user_input[3:].strip().capitalize() + "\n"
        todos.append(todo)

        functions_todo_app.write_todos(todos)

    elif user_input.startswith("show"):
        todos = functions_todo_app.get_todos()

        for i, item in enumerate(todos, start=1):
            print(f"{i}. {item.strip("\n")}")

    elif user_input.startswith("edit"):
        try:
            todos = functions_todo_app.get_todos()

            number = int(user_input[4:].strip())
            todo_to_edit = todos[number - 1].strip("\n")
            new_todo = input("Please enter the new todo: ").capitalize()
            todos[number - 1] = new_todo + "\n"

            functions_todo_app.write_todos(todos)

            print(f"Task number {number}, \"{todo_to_edit}\" was changed! Please check.")
        except ValueError:
            print("Your command is invalid! Please enter the number of task you want to edit.")
        except IndexError:
            print("The task you are trying to edit does not exist! Please enter a valid task number.")

    elif user_input.startswith("complete"):
        try:
            todos = functions_todo_app.get_todos()

            number = int(user_input[8:].strip())
            todo_to_remove = todos[number - 1].strip("\n")
            todos.pop(number - 1)

            functions_todo_app.write_todos(todos)

            print(f"Task number {number}, \"{todo_to_remove}\" has been removed! Please check.")
        except ValueError:
            print("Your command is invalid! Please enter the number of task you want to remove.")
        except IndexError:
            print("The task you are trying to remove does not exist! Please enter a valid task number.")

    elif user_input.startswith("exit"):
        break

    else:
        print("Please enter the correct command!")



