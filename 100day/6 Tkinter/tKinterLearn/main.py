import tkinter


app = tkinter.Tk()
app.title("Hello World")
app.config(width=400, height=400)

main_frame = tkinter.Frame(app, padx=10, pady=10, bg="red")
main_frame.grid(row=0, column=0)


label = tkinter.Label(main_frame, text="Add todo:").grid(
    row=0, column=0, sticky="w")
add_todo_btn = tkinter.Button(
    main_frame, text="Add", command=lambda: add_todo())
add_todo_btn.grid(row=0, column=0, sticky="e")

add_todo_ent = tkinter.Entry(main_frame, width=50)
add_todo_ent.grid(row=1, column=0)





priorities = ["low", "medium", "high"]

todos = [
    {
        "name": "Learn Python",
        "is_completed": 0,
        "priority": "medium",
    },
    {
        "name": "Learn javascript",
        "is_completed": 0,
        "priority": "low",
    },
    {
        "name": "Learn Java",
        "is_completed": 1,
        "priority": "high",
    },
]

def render_todos():

    for i, todo in enumerate(todos):
        todo_label = tkinter.Label(
            main_frame, text=todo["name"], width=50, anchor="w")
        todo_label.grid(row=i+2, column=0, sticky="w")
        
        todo_priority = tkinter.StringVar()
        todo_priority.set(todo["priority"])
        todo_priority_menu = tkinter.OptionMenu(
            main_frame, todo_priority, *priorities)
        todo_priority_menu.grid(row=i+2, column=1, sticky="e")
        
        todo_completed = tkinter.IntVar(value=1)
        todo_completed_cb = tkinter.Checkbutton(
            main_frame, variable=todo_completed)
        todo_completed_cb.grid(row=i+2, column=2, sticky="e")
        
        delete_btn = tkinter.Button(
            main_frame, text="Delete", command=lambda: delete_todo(i))
        delete_btn.grid(row=i+2, column=3, sticky="e")

def add_todo():
    todo = add_todo_ent.get()
    print(todo)
    todos.append({
        "name": todo,
        "is_completed": False,
        "priority": "low",
    })
    render_todos()
    
def delete_todo(index):
    print(index)
    print(todos[index])
    todos.pop(index)
    render_todos()
    
render_todos()
app.mainloop()
