import tkinter as tk
from tkinter import ttk, messagebox, filedialog


def main():
    root = tk.Tk()
    root.title("Дёмин Дмитрий Сергеевич")
    root.geometry("600x400")

    # Создаем вкладки
    notebook = ttk.Notebook(root)
    notebook.pack(fill='both', expand=True, padx=10, pady=10)

    # Вкладка 1: Калькулятор
    tab1 = ttk.Frame(notebook)
    notebook.add(tab1, text="Калькулятор")

    tk.Label(tab1, text="Первое число:").pack(pady=5)
    entry1 = tk.Entry(tab1, width=20)
    entry1.pack(pady=5)

    tk.Label(tab1, text="Операция:").pack(pady=5)
    op_var = tk.StringVar()
    op_combo = ttk.Combobox(tab1, textvariable=op_var, values=['+', '-', '*', '/'], width=10)
    op_combo.current(0)
    op_combo.pack(pady=5)

    tk.Label(tab1, text="Второе число:").pack(pady=5)
    entry2 = tk.Entry(tab1, width=20)
    entry2.pack(pady=5)

    def calculate():
        try:
            a = float(entry1.get())
            b = float(entry2.get())
            op = op_var.get()

            if op == '+':
                result = a + b
            elif op == '-':
                result = a - b
            elif op == '*':
                result = a * b
            elif op == '/':
                if b == 0:
                    messagebox.showerror("Ошибка", "Деление на ноль!")
                    return
                result = a / b

            messagebox.showinfo("Результат", f"{a} {op} {b} = {result}")
        except ValueError:
            messagebox.showerror("Ошибка", "Введите числа!")

    tk.Button(tab1, text="Вычислить", command=calculate).pack(pady=20)

    # Вкладка 2: Чекбоксы
    tab2 = ttk.Frame(notebook)
    notebook.add(tab2, text="Чекбоксы")

    tk.Label(tab2, text="Выберите варианты:").pack(pady=20)

    var1 = tk.BooleanVar()
    var2 = tk.BooleanVar()
    var3 = tk.BooleanVar()

    tk.Checkbutton(tab2, text="Первый", variable=var1).pack(pady=5)
    tk.Checkbutton(tab2, text="Второй", variable=var2).pack(pady=5)
    tk.Checkbutton(tab2, text="Третий", variable=var3).pack(pady=5)

    def show_selection():
        selected = []
        if var1.get():
            selected.append("первый")
        if var2.get():
            selected.append("второй")
        if var3.get():
            selected.append("третий")

        if selected:
            messagebox.showinfo("Выбор", f"Вы выбрали: {', '.join(selected)}")
        else:
            messagebox.showinfo("Выбор", "Вы ничего не выбрали")

    tk.Button(tab2, text="Показать выбор", command=show_selection).pack(pady=20)

    # Вкладка 3: Работа с текстом
    tab3 = ttk.Frame(notebook)
    notebook.add(tab3, text="Текст")

    # Меню
    menubar = tk.Menu(root)
    file_menu = tk.Menu(menubar, tearoff=0)
    file_menu.add_command(label="Загрузить файл", command=lambda: load_file())
    menubar.add_cascade(label="Файл", menu=file_menu)
    root.config(menu=menubar)

    # Текстовое поле
    text_area = tk.Text(tab3, height=15, width=50)
    text_area.pack(padx=10, pady=10)

    # Функция загрузки файла
    def load_file():
        filename = filedialog.askopenfilename(
            title="Выберите файл",
            filetypes=[("Текстовые файлы", "*.txt"), ("Все файлы", "*.*")]
        )
        if filename:
            try:
                with open(filename, 'r', encoding='utf-8') as f:
                    content = f.read()
                text_area.delete(1.0, tk.END)
                text_area.insert(1.0, content)
            except Exception as e:
                messagebox.showerror("Ошибка", f"Не удалось загрузить файл: {e}")

    # Кнопки
    frame_buttons = tk.Frame(tab3)
    frame_buttons.pack(pady=5)

    tk.Button(frame_buttons, text="Очистить", command=lambda: text_area.delete(1.0, tk.END)).pack(side='left', padx=5)
    tk.Button(frame_buttons, text="Сохранить", command=lambda: save_file()).pack(side='left', padx=5)

    # Функция сохранения файла
    def save_file():
        filename = filedialog.asksaveasfilename(
            title="Сохранить файл",
            defaultextension=".txt",
            filetypes=[("Текстовые файлы", "*.txt"), ("Все файлы", "*.*")]
        )
        if filename:
            try:
                with open(filename, 'w', encoding='utf-8') as f:
                    f.write(text_area.get(1.0, tk.END))
                messagebox.showinfo("Успех", "Файл сохранен")
            except Exception as e:
                messagebox.showerror("Ошибка", f"Не удалось сохранить файл: {e}")

    root.mainloop()


if __name__ == "__main__":
    main()