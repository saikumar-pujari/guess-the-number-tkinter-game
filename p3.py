import tkinter 
from random import randint
from tkinter import messagebox

low = 0
high = 100
rand = randint(low, high)
print(f"Secret number: {rand}")  # for testing/debugging

def check(guess):
    try:
        guess = int(guess)
        if guess < rand:
            result_label.config(text=f"{guess} is too low ❄️")
        elif guess > rand:
            result_label.config(text=f"{guess} is too high 🔥")
        else:
            messagebox.showinfo("You win! 🎉", f"{guess} is correct!")
            result_label.config(text="Game Over! You guessed it right.")
    except ValueError:
        result_label.config(text="Please enter a valid number.")

# GUI Setup
tk = tkinter.Tk()
tk.title("🎯 Number Guessing Game")

tkinter.Label(tk, text=f"Guess a number between {low} and {high}").pack()

entry = tkinter.Entry(tk)
entry.pack()

button = tkinter.Button(tk, text="Take a guess", command=lambda: check(entry.get()))
button.pack()

result_label = tkinter.Label(tk, text="")
result_label.pack()

tk.mainloop()
