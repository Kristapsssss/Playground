import tkinter
from tkinter import *
from tkinter import ttk


# Function to update the countdown timer as well as delete all text and reset counter if time runs out
def print_machine():
    global remaining_seconds
    global text
    global word_count
    text = text_widget.get('1.0', tkinter.END)
    word_count = len(text.split())
    word_label.config(text=f"Word Count: {word_count}")
    if remaining_seconds > 0:
        print(remaining_seconds)
        remaining_seconds -= 1
        root.after(1000, print_machine)
    else:
        text_widget.delete('1.0', tkinter.END)
        remaining_seconds = INITIAL_SECONDS
        root.after(1000, print_machine)


# Function to reset the countdown timer
def reset_seconds(event):
    global remaining_seconds
    remaining_seconds = 5


# Constants
INITIAL_SECONDS = 5
word_count = 0

# Global Variables
remaining_seconds = INITIAL_SECONDS

# Create TK Window
root = Tk()
root.title("Text Writing App")
root.geometry("800x600")
root.config(bg='silver')

# Crete Frame within the Window
frame = ttk.Frame(root, padding=10)
frame.grid()

# Add a label with instructions
(ttk.Label(frame, text='Start typing, if you stop for 5 seconds, the text will be destroyed.')
 .pack(side='top', padx=220, expand=True))

# Add a label which shows word count
word_label = ttk.Label(frame, text=f'Word Count: {word_count}')
word_label.pack(side='top', padx=200, expand=True)

# Add a text widget
text_widget = Text(frame, height=32, width=88)
text_widget.pack(side='top', expand=True)

# Add a Quit button
ttk.Button(frame, text='Quit', command=root.destroy).pack(side='top')

# Schedule the timer update
root.after(1000, print_machine)

# Bind the reset function to key release event
root.bind("<KeyRelease>", reset_seconds)

# TK mainloop
root.mainloop()
