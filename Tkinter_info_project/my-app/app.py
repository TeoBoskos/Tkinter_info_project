import tkinter as tk
import ttkbootstrap as ttk

from ttkbootstrap.constants import CENTER
from main_function import next_question

# Create the main window.
style = ttk.Style("darkly")
root = style.master
root.geometry("800x600")
root.title("YourInfo")

# Title label.
title_label = ttk.Label(root, text="YourInfo", font = "Ariel 22 bold")
title_label.pack(pady=20)

# Label for user input.
input_label = ttk.Label(root, text="What is your name?", font = "Ariel 18")
input_label.pack(pady=20)

# Entry for user input.
input_entry_str = ttk.StringVar()
input_entry = ttk.Entry(root, width=50, font = "Ariel 16", textvariable=input_entry_str)
input_entry.pack()

# Bind the enter key.
input_entry.bind("<Return>", lambda event: next_question(input_entry_str, user_info, questions, input_label, output_label, input_entry, next_button))

# Variables to store user info.
user_info = {"name": "", "age": "", "gender": "", "hobby": ""}
questions = [
  "What is your name?",
  "What is your age?",
  "What is your gender?",
  "What is your hobby?"
]

output_label = 1
next_button = 1

# Button to move to the next question.
next_button = tk.Button(root, text="Next", font=("Ariel", 18), command=lambda: next_question(input_entry_str, user_info, questions, input_label, output_label, input_entry, next_button))
next_button.pack(pady=20)

# Output label.
output_label = ttk.Label(root, text="", font = "Ariel 18", wraplength=750)
output_label.pack()

# Run the main loop.
root.mainloop()
print("Goodbye")