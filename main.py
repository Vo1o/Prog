from string import ascii_lowercase, ascii_uppercase, digits, punctuation
import tkinter as tk
import customtkinter as custom_tk
import password


class App(custom_tk.CTk):
    def __init__(self):
        super().__init__()

        self.geometry("460x370")
        self.title("Генератор случайных паролей")
        self.resizable(False, False)

        self.Text = custom_tk.CTkLabel(text='Генератор случайных паролей')
        self.Text.grid(row=0, column=0, padx=(120, 150))

        self.entry_password = custom_tk.CTkEntry(width=150)
        self.entry_password.grid(row=1, column=0, padx=(120, 150))

        self.btn_generate = custom_tk.CTkButton(text="Сгенерировать", width=100,
                                                command=self.set_password)
        self.btn_generate.grid(row=8, column=0)

        self.text = custom_tk.CTkLabel(text='Длина пароля:')
        self.text.grid(row=2, padx=(0, 350), )

        self.password_length_slider = custom_tk.CTkSlider(from_=0, to=100, number_of_steps=100,
                                                          command=self.slider_event)
        self.password_length_slider.grid(row=2, column=0, padx=(100, 160))

        self.password_length_entry = custom_tk.CTkEntry(width=50)
        self.password_length_entry.grid(row=2, column=0, padx=(200, 0))

        self.cb_digits_var = tk.StringVar()

        self.cb_digits = custom_tk.CTkCheckBox(text="Цифры",
                                               variable=self.cb_digits_var, onvalue=digits, offvalue="")
        self.cb_digits.grid(row=3, column=0, padx=55, pady=10, sticky='we')
        self.cb_digits.select()
        self.cb_lower_var = tk.StringVar()
        self.cb_lower = custom_tk.CTkCheckBox(text="Строчные", variable=self.cb_lower_var,
                                              onvalue=ascii_lowercase, offvalue="10")
        self.cb_lower.grid(row=4, column=0, padx=55, pady=10, sticky='we')
        self.cb_lower.select()
        self.cb_upper_var = tk.StringVar()
        self.cb_upper = custom_tk.CTkCheckBox(text="Прописные", variable=self.cb_upper_var,
                                              onvalue=ascii_uppercase, offvalue="")
        self.cb_upper.grid(row=5, column=0, padx=55, pady=10, sticky='we')
        self.cb_upper.select()

        self.cb_symbols_var = tk.StringVar()
        self.cb_symbols = custom_tk.CTkCheckBox(text="Спец. символы", variable=self.cb_symbols_var,
                                                onvalue=punctuation, offvalue="")
        self.cb_symbols.grid(row=6, column=0, padx=55, pady=10, sticky='we')

        self.password_length_slider.set(8)

    def slider_event(self, value):
        self.password_length_entry.delete(0, 'end')
        self.password_length_entry.insert(0, int(value))

    def get_characters(self):
        chars = "".join(self.cb_digits_var.get() + self.cb_lower_var.get()
                        + self.cb_upper_var.get() + self.cb_symbols_var.get())
        return chars

    def set_password(self):
        self.entry_password.delete(0, 'end')
        self.entry_password.insert(0, password.create_new(length=int(self.password_length_entry.get()),
                                                          characters=self.get_characters()))


if __name__ == "__main__":
    App().mainloop()
