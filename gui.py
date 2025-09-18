import functions_todo_app as fta
import FreeSimpleGUI as sg

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter a todo", key="todo")
add_button = sg.Button("Add")

window = sg.Window("My to-do app",
                   [[label, add_button], [input_box]],
                   font=["Helvetica", 19])

while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case "Add":
            todos = fta.get_todos()
            new_todo = values["todo"].capitalize() + "\n"
            todos.append(new_todo)
            fta.write_todos(todos)

        case WIN_CLOSED:
            break

window.close()


