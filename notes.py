import tkinter as tk
from tkinter import scrolledtext

class NotesApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Notes App")

        # Text area for taking notes
        self.note_area = scrolledtext.ScrolledText(self.root, wrap=tk.WORD, width=40, height=10)
        self.note_area.pack(padx=10, pady=10)

        # Save button
        self.save_button = tk.Button(self.root, text="Save", command=self.save_notes)
        self.save_button.pack(pady=5)

        # Load button
        self.load_button = tk.Button(self.root, text="Load", command=self.load_notes)
        self.load_button.pack(pady=5)

    def save_notes(self):
        notes = self.note_area.get("1.0", tk.END)
        with open("notes.txt", "w") as file:
            file.write(notes)

    def load_notes(self):
        try:
            with open("notes.txt", "r") as file:
                notes = file.read()
                self.note_area.delete("1.0", tk.END)
                self.note_area.insert(tk.END, notes)
        except FileNotFoundError:
            self.note_area.delete("1.0", tk.END)
            self.note_area.insert(tk.END, "No saved notes found.")

if __name__ == "__main__":
    root = tk.Tk()
    app = NotesApp(root)
    root.mainloop()
