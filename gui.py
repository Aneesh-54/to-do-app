# We use FreeSimpleGUI module (3rd party) for this app
import functions_todo_app as fta
import FreeSimpleGUI as sg
import time

sg.theme("DarkPurple3")
# The below section is completely designing the layout of the GUI
label = sg.Text("Type in a to-do")
label_time = sg.Text("", key="clock")
input_box = sg.InputText(tooltip="Enter a todo", key="todo")
add_button = sg.Button("Add")
output_box = [[sg.Listbox(values=fta.get_todos(), key="todos",
                        enable_events=True, size=(45, 15))]]
edit_button = [sg.Button("Edit")]
complete_button = [sg.Button("Complete")]
exit_button = sg.Button("Exit")
left_col_content = sg.Column(output_box)
right_col_content = sg.Column([edit_button, complete_button])

window = sg.Window("My to-do app",
                   [[label_time], [label], [input_box, add_button],
                    [[left_col_content, right_col_content]], [exit_button]],
                   font=["Helvetica", 19])

# Check for "events" and alter "values"
while True:
    event, values = window.read(timeout=10)
    window["clock"].update(value=time.strftime("%b %d, %Y %I:%M:%S %p"))
    print(event)
    print(values)
    match event:
        case "Add":
            if values["todo"] == "":
                sg.popup("Please enter a task.", font=["Helvetica", 19])
            else:
                todos = fta.get_todos()

                new_todo = values["todo"].capitalize() + "\n"
                todos.append(new_todo)

                fta.write_todos(todos)
                window["todos"].update(values=todos)
                window["todo"].update(value="")

        case "Edit":
            try:
                if values["todo"] == "":
                    sg.popup("Please enter the new task.", font=["Helvetica", 19])
                else:
                    todos = fta.get_todos()

                    todo_to_edit = values["todos"][0]
                    new_todo = values["todo"].capitalize() + "\n"
                    index = todos.index(todo_to_edit)
                    todos[index] = new_todo

                    fta.write_todos(todos)
                    window["todos"].update(values=todos)
                    window["todo"].update(value="")
            except IndexError:
                sg.popup("Please select a task to edit.", font=["Helvetica", 19])

        case "Complete":
            try:
                todos = fta.get_todos()

                todo_to_complete = values["todos"][0]
                index = todos.index(todo_to_complete)
                todos.pop(index)

                fta.write_todos(todos)
                window["todos"].update(values=todos)
                window["todo"].update(value="")
            except IndexError:
                sg.popup("Please select a task to complete.", font=["Helvetica", 19])

        case "Exit":
            break

        case sg.WIN_CLOSED:
            break

window.close()

