import customtkinter as ctk
import random
import time

# Create a list of 1000 most used english words
with open("words.txt", 'r') as file:
    words_list = file.read().splitlines()

words_list = [' ' + item for item in words_list]


class App:
    def __init__(self):
        self.button = 0
        self.list_of_buttons = []
        self.words_list = words_list
        self.text = None
        self.seconds = 30
        self.counter_started = False
        self.score = 0
        self.characters = 0
        self.wrong_words = []
        self.start_game = True

    def handle_space(self, event):
        self.text = entry_words.get()
        characters = len(self.text)
        if event.keysym == 'space' and self.start_game:
            if not self.counter_started:
                self.counter_started = True
                self.update_counter()
            entry_words.delete(0, len(self.text))
            if self.text == self.list_of_buttons[self.button].cget('text'):
                self.list_of_buttons[self.button].configure(fg_color='green')
                self.score += 1
                self.characters += characters
            else:
                self.wrong_words.append(self.text)
                self.list_of_buttons[self.button].configure(fg_color='crimson')
            self.button += 1
            if self.button == 16:
                for button in self.list_of_buttons:
                    button.destroy()
                self.button = 0
                self.list_of_buttons = []
                self.initial_words()

    def initial_words(self):
        for y in range(4):
            for n in range(4):
                button_word_n = ctk.CTkButton(frame_words, text=random.choice(words_list), font=('Trebuchet MS', 60))
                button_word_n.grid(row=y, column=n, padx=5, pady=5)
                self.list_of_buttons.append(button_word_n)

    def update_counter(self):
        if self.seconds > 0:
            self.seconds -= 1
            label_counter.configure(text=f"Seconds Remaining: {app.seconds}")
            root.after(1000, self.update_counter)
        else:
            self.start_game = False
            with open('highscore.txt', 'r') as highscore_file:
                scores = highscore_file.read().splitlines()
                all_time_wpm = int(scores[0])
                all_time_cpm = int(scores[1])
                if all_time_wpm < (self.score * 2) or all_time_cpm < (self.characters * 2):
                    all_time_wpm = self.score * 2
                    all_time_cpm = self.characters * 2
                    with open('highscore.txt', 'w') as highscore:
                        lines = [f'{self.score * 2}\n', f'{self.characters * 2}\n']
                        highscore.writelines(lines)
            label_counter.configure(text=f"Done! \n\n"
                                         f"Your words per minute is: {self.score * 2}\n"
                                         f"Character Per Minute: {self.characters * 2}\n"
                                         f"Words you got wrong: {len(self.wrong_words)}\n\n"
                                         f"All-time highscores\n"
                                         f"Words per minute: {all_time_wpm}\n"
                                         f"Characters per minutes: {all_time_cpm}\n\n"
                                         f"If you would like to restart press ENTER\n"
                                         f"If you would like to exit press ESC")
            frame_words.grid_forget()
            time.sleep(1)
            self.start_game = True

    def restart(self, event):
        if event.keysym == 'Return':
            frame_words.grid(row=1, column=0, pady=100)
            for button in self.list_of_buttons:
                button.destroy()
            label_counter.configure(text=f"Seconds Remaining: 30\n\n"
                                         f"Press SPACE to start")
            self.button = 0
            self.list_of_buttons = []
            self.words_list = words_list
            self.text = None
            self.seconds = 30
            self.counter_started = False
            self.score = 0
            self.characters = 0
            self.wrong_words = []
            self.initial_words()

    def exit(self, event):
        if event.keysym == 'Escape':
            return root.destroy()


root = ctk.CTk()
app = App()

root.title('Type Speed Application')
root.geometry("1600x1200")
root.config(bg='silver')
root.attributes('-fullscreen', True)

frame_top = ctk.CTkFrame(root, bg_color='silver')
frame_words = ctk.CTkFrame(root, bg_color='silver')
frame_entry = ctk.CTkFrame(root)

app.initial_words()

frame_top.grid(row=0, column=0)
frame_words.grid(row=1, column=0, pady=100)
frame_entry.grid(row=2, column=0, pady=50)

label_counter = ctk.CTkLabel(frame_top,
                             text=f"Seconds Remaining: 30\n\nPress SPACE to start",
                             font=('Trebuchet MS', 50))
label_counter.grid(row=0, column=0)

entry_words = ctk.CTkEntry(frame_entry, font=('Terminal', 50), width=600, height=100)
entry_words.grid(row=1, column=2, pady=0)

entry_words.bind('<KeyPress>', app.handle_space)
entry_words.bind('<KeyPress>', app.restart)
entry_words.bind('<KeyPress>', app.exit)

root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

root.mainloop()
