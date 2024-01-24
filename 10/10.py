import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog

def calculate():
    num1 = float(entry1.get())
    num2 = float(entry2.get())
    operation = operation_var.get()
    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "/":
        result = num1 / num2
    result_label.config(text="Result: " + str(result))

def show_checkbox_selection():
    selected_options = []
    if var1.get():
        selected_options.append("Первый")
    if var2.get():
        selected_options.append("Второй")
    if var3.get():
        selected_options.append("Третий")
    message = "Вы выбрали: " + ", ".join(selected_options)
    messagebox.showinfo("Выбор", message)

def open_file():
    file_path = filedialog.askopenfilename()
    with open(file_path, 'r') as file:
        content = file.read()
        text_box.delete(1.0, tk.END)
        text_box.insert(tk.END, content)

app = tk.Tk()
app.title("Тимошенко Родион Валерьевич")

tab_control = ttk.Notebook(app)

tab1 = tk.Frame(tab_control)
tab2 = tk.Frame(tab_control)
tab3 = tk.Frame(tab_control)

tab_control.add(tab1, text='Калькулятор')
tab_control.add(tab2, text='Чекбоксы')
tab_control.add(tab3, text='Работа с текстом')

tab_control.pack(expand=1, fill='both')

# Tab 1 - Калькулятор
entry1 = tk.Entry(tab1)
entry1.pack()
entry2 = tk.Entry(tab1)
entry2.pack()

operation_var = tk.StringVar(tab1)
operation_var.set("+")  # default value

operation_menu = tk.OptionMenu(tab1, operation_var, "+", "-", "*", "/")
operation_menu.pack()

calculate_button = tk.Button(tab1, text="Calculate", command=calculate)
calculate_button.pack()

result_label = tk.Label(tab1, text="Result:")
result_label.pack()

# Tab 2 - Чекбоксы
var1 = tk.IntVar()
var2 = tk.IntVar()
var3 = tk.IntVar()

checkbox1 = tk.Checkbutton(tab2, text="Первый", variable=var1)
checkbox2 = tk.Checkbutton(tab2, text="Второй", variable=var2)
checkbox3 = tk.Checkbutton(tab2, text="Третий", variable=var3)

checkbox1.pack()
checkbox2.pack()
checkbox3.pack()

show_selection_button = tk.Button(tab2, text="Show Selection", command=show_checkbox_selection)
show_selection_button.pack()

# Tab 3 - Работа с текстом
menu_bar = tk.Menu(app)
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Открыть", command=open_file)
menu_bar.add_cascade(label="Файл", menu=file_menu)
app.config(menu=menu_bar)

text_box = tk.Text(tab3)
text_box.pack()

app.mainloop()
