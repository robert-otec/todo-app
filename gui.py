import modules.functions
import FreeSimpleGUI as sg

label = sg.Text("Type in a todo")
input_box = sg.InputText(tooltip="Enter a todo", key="todo")
# The key parameter is used to identify the input box in the event loop.
add_button = sg.Button("Add")

window = sg.Window("My To-Do App",
                   layout=[[label], [input_box, add_button]],
                   font=("Helvetica", 20))

while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case "Add":
            todos = modules.functions.get_todos()
            new_todo = values["todo"] + "\n"
            todos.append(new_todo)
            modules.functions.write_todos(todos)
        case sg.WIN_CLOSED:
            break

window.close()