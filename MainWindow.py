class MainWondow(tk.Tk):
    def __init__(self):
        super.__init__()
        self.__name = "Приложение для заметок"
    def start(self):
        self.title(self.__name)
        self.geometry("800x600")
        self.add_button = tk.Button(self, text="+", font=('Arial', 16)),
        self.add_button.pack(side='bottom', pady=5)

        self.mainloop()

    def create_note_card(self):
        edit_note = TextEditWindow(self)
        edit_note.grab_set()
