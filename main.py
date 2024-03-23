import tkinter as tk

def add_task():
    task = task_entry.get()
    if task:
        task_list_box.insert(tk.END,task)
        task_entry.delete(0,tk.END)

def delete_task():
    selected_task = task_list_box.curselection()
    if selected_task:
        task_list_box.delete(selected_task)

def mark_task():
    selected_task = task_list_box.curselection()
    if selected_task:
        task_list_box.itemconfig(selected_task, bg = "green yellow")

root = tk.Tk()

root.title("Task List")
root.configure(background = "black")

text1 = tk.Label(root, text = "Введите вашу задачу", bg = "black", fg = "white" )
text1.pack(pady = 5)

task_entry = tk.Entry(root, width = 30, bg = "lawn green", fg = "blue")
task_entry.pack(pady = 10)

add_task_button = tk.Button(root, text = "Добавить задачу", command = add_task)
add_task_button.pack(pady = 5)

delete_button = tk.Button(root, text = "Удалить задачу", command = delete_task)
delete_button.pack(pady = 5)

mark_button = tk.Button(root, text = "Отметить выполненную задачу", command = mark_task)
mark_button.pack(pady = 5)

text2 = tk.Label(root, text = "Список задач", bg = "black", fg = "white")
text2.pack(pady = 5)

task_list_box = tk.Listbox(root, height = 10, width = 50, bg = "magenta2", fg = "black")
task_list_box.pack(pady = 10)


root.mainloop()


