import tkinter as tk

# Функция для добавления плейсхолдера
def set_placeholder(entry, placeholder):
    entry.insert(0, placeholder)
    entry.config(fg='grey')

    def on_focus_in(event):
        if entry.get() == placeholder:
            entry.delete(0, tk.END)
            entry.config(fg='black')

    def on_focus_out(event):
        if entry.get() == '':
            entry.insert(0, placeholder)
            entry.config(fg='grey')

    entry.bind("<FocusIn>", on_focus_in)
    entry.bind("<FocusOut>", on_focus_out)

# Функция валидации для проверки, что ввод только числовой и не более 12 символов
def validate_card_number(char, entry_value):
    if char.isdigit() and len(entry_value) < 12:
        return True
    elif char == "" and len(entry_value) <= 12:  # Допускаем удаление символов
        return True
    return False

# Функция валидации для месяца (максимум 2 цифры)
def validate_month(char, entry_value):
    if char.isdigit() and len(entry_value) < 3:
        return True
    elif char == "" and len(entry_value) <= 2:  # Допускаем удаление символов
        return True
    return False
# Функция валидации для года (максимум 2 цифры)
def validate_year(char, entry_value):
    if char.isdigit() and len(entry_value) < 3:
        return True
    elif char == "" and len(entry_value) <= 2:  # Допускаем удаление символов
        return True
    return False
# Функция валидации для CVC (максимум 3 цифры)
def validate_cvc(char, entry_value):
    if char.isdigit() and len(entry_value) < 4:
        return True
    elif char == "" and len(entry_value) <= 3:  # Допускаем удаление символов
        return True
    return False
# Создание окна
window = tk.Tk()
window.title('Страница оплаты')
window.geometry("450x300")

# Валидация ввода для номера карты
validate_card_command = window.register(validate_card_number)
# Валидация ввода для месяца
validate_month_command = window.register(validate_month)
# Валидация ввода для года
validate_year_command = window.register(validate_year)
# Валидация ввода для CVC
validate_cvc_command = window.register(validate_cvc)
# Поля ввода
card_number_entry = tk.Entry(window, width=28, validate="key", validatecommand=(validate_card_command, "%S", "%P"))
card_number_entry.place(x=100, y=75)

month_entry = tk.Entry(window, width=3, validate="key", validatecommand=(validate_month_command, "%S", "%P"))
month_entry.place(x=100, y=170)

year_entry = tk.Entry(window, width=3, validate="key",validatecommand=(validate_year_command, "%S", "%P"))
year_entry.place(x=140, y=170)

cvc_entry = tk.Entry(window, width=6, validate="key",validatecommand=(validate_cvc_command, "%S", "%P"))
cvc_entry.place(x=230, y=170)

# Метки
card_number = tk.Label(window, text="Введите номер карты")
card_number.place(x=100, y=50)

at = tk.Label(window, text="/")
at.place(x=125, y=170)

# Установка плейсхолдера
set_placeholder(card_number_entry, "0000 0000 0000 0000")
set_placeholder(month_entry, "MM")
set_placeholder(year_entry, "YY")
set_placeholder(cvc_entry, "CVC")

window.mainloop()
