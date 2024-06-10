import tkinter as tk

class LetterSelectorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Letter Selector")

        self.letters = [
            'A', 'B', 'C', 'D', 'E',
            'F', 'G', 'H', 'I', 'J',
            'K', 'L', 'M', 'N', 'O',
            'P', 'Q', 'R', 'S', 'T',
            'U', 'V', 'W', 'X', 'Y', 'Z'
        ]

        self.selected_row = 0
        self.selected_col = 0
        self.sentence = ""

        self.create_grid()
        self.create_navigation_buttons()
        self.create_sentence_label()
        self.update_grid_selection()

    def create_grid(self):
        self.letter_labels = []
        for i in range(5):
            row_labels = []
            for j in range(5):
                letter = self.letters[i*5 + j] if i*5 + j < len(self.letters) else ' '
                label = tk.Label(self.root, text=letter, width=7, height=5, font=("Helvetica", 28), borderwidth=2, relief="solid", fg="blue")
                label.grid(row=i, column=j)
                row_labels.append(label)
            self.letter_labels.append(row_labels)

    def create_navigation_buttons(self):
        nav_frame = tk.Frame(self.root)
        nav_frame.grid(row=6, columnspan=5)

        self.up_button = tk.Button(nav_frame, text="Up", command=self.move_up)
        self.up_button.grid(row=0, column=1)

        self.down_button = tk.Button(nav_frame, text="Down", command=self.move_down)
        self.down_button.grid(row=2, column=1)

        self.left_button = tk.Button(nav_frame, text="Left", command=self.move_left)
        self.left_button.grid(row=1, column=0)

        self.right_button = tk.Button(nav_frame, text="Right", command=self.move_right)
        self.right_button.grid(row=1, column=2)

        self.select_button = tk.Button(nav_frame, text="Select", command=self.select_letter)
        self.select_button.grid(row=1, column=1)

    def create_sentence_label(self):
        self.sentence_label = tk.Label(self.root, text=self.sentence, font=("Helvetica", 18))
        self.sentence_label.grid(row=7, columnspan=5)

    def update_grid_selection(self):
        for i in range(5):
            for j in range(5):
                if i == self.selected_row and j == self.selected_col:
                    self.letter_labels[i][j].config(bg="red")
                else:
                    self.letter_labels[i][j].config(bg="white")

    def move_up(self):
        self.selected_row = (self.selected_row - 1) % 5
        self.update_grid_selection()

    def move_down(self):
        self.selected_row = (self.selected_row + 1) % 5
        self.update_grid_selection()

    def move_left(self):
        self.selected_col = (self.selected_col - 1) % 5
        self.update_grid_selection()

    def move_right(self):
        self.selected_col = (self.selected_col + 1) % 5
        self.update_grid_selection()

    def select_letter(self):
        selected_letter = self.letter_labels[self.selected_row][self.selected_col].cget("text")
        if selected_letter != ' ':
            self.sentence += selected_letter
            self.sentence_label.config(text=self.sentence)

if __name__ == "__main__":
    root = tk.Tk()
    app = LetterSelectorApp(root)
    root.mainloop()
