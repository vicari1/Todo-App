import customtkinter

def newTask():
    global newtask
    task = taskEntry.get()
    newtask = customtkinter.CTkTextbox(taskList, width=275, height=35, fg_color="#b47775", font=('Helvetica Bold', 17), corner_radius=8)
    newtask.insert("end", task)
    newtask.pack(pady=5)
    taskEntry.delete(0,"end")

def clearTask():
    newtask.destroy()

def closeApp():
    root.destroy()

def MainCode():
    global root
    root = customtkinter.CTk()
    root.geometry("350x500")
    root.title('Todo App')
    root.resizable(False, False)
    root.iconbitmap('todo.ico')

    todoApp = customtkinter.CTkLabel(master=root, text="Todo App", font=('Helvetica bold', 25), text_color="#a24f5e")
    todoApp.pack()

    global taskEntry
    taskEntry = customtkinter.CTkEntry(master=root, placeholder_text="New Task", width=178, height=25, corner_radius=11, font=('Helvetica bold', 13))
    taskEntry.pack(pady=12)

    addTask = customtkinter.CTkButton(master=root, width=155, height=15, corner_radius=9, text="Add task", font=('Helvetica bold', 13), fg_color="#a24f5e", command=newTask, hover_color="#6b323d")
    addTask.pack(pady=15)

    global taskList
    taskList = customtkinter.CTkScrollableFrame(master=root, width=275, height=310, corner_radius=9)
    taskList.pack(pady=5)

    clearTaskButton = customtkinter.CTkButton(master=root, width=155, height=15, corner_radius=9, text="Clear Task", font=('Helvetica bold', 13), fg_color="#a24f5e", hover_color="#6b323d", command=clearTask)
    clearTaskButton.pack(pady=5)

    closeAppButton = customtkinter.CTkButton(master=root, width=155, height=15, corner_radius=9, text="Close", font=('Helvetica bold', 13), fg_color="#a24f5e", hover_color="#6b323d", command=closeApp)
    closeAppButton.pack(pady=5)

    root.mainloop()

MainCode()
