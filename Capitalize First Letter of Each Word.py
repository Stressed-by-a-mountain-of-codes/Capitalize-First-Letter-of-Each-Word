import tkinter as tk
from tkinter import messagebox
import pyttsx3

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def capitalize_words(event=None):
    text = entry.get()
    if not text.strip():
        messagebox.showerror("Input Error", "Please enter a sentence.")
        return

    capitalized = ' '.join(word.capitalize() for word in text.strip().split())
    result_label.config(text=f"Capitalized: {capitalized}", fg="darkblue")
    speak(capitalized)
    root.after(3000, reset)

def reset():
    entry.delete(0, tk.END)
    result_label.config(text="")

root = tk.Tk()
root.title("Capitalize Each Word")
root.geometry("480x240")
root.resizable(False, False)

tk.Label(root, text="Enter your sentence:", font=("Arial", 12)).pack(pady=10)

entry = tk.Entry(root, font=("Arial", 14), justify="center", width=45)
entry.pack(pady=5)
entry.bind("<Return>", capitalize_words)

tk.Button(root, text="Capitalize", font=("Arial", 12), command=capitalize_words).pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 12), wraplength=440)
result_label.pack(pady=10)

entry.focus()
root.mainloop()
