class TextEditWindow(tk.Toplevel):
    def __init__(self, parent):
        self.note = note
        super().__init__(parent)
        self.geometry("800x600")
        self.text_area = scrolledtext.ScrolledText(self, width=96, height=35)
        self.text_area.pack()
        self.button = tk.Button(self, text="Сохранить", command=self.save_note)
        self.button.pack()
    def save_note(self):
        new_text = self.text_area.get(1.0, tk.END)
        print(new_text)
        self.dectroy()
