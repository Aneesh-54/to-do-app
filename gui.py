import functions_todo_app
import FreeSimpleGUI as sg

label = sg.Text("Type in a to-do")
input_box = sg.InputText()
add_button = sg.Button("Add")

window = sg.Window("My to-do app", [[label, add_button], [input_box]])
window.read()
window.close()


