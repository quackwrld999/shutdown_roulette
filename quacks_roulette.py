import random
import tkinter as tk
from tkinter import messagebox
import os

def check_guess():
    global attempts
    try:
        guess = int(entry.get())
        if guess == guess_num:
            messagebox.showinfo("Congratulations!", "You guessed the number!")
            reset_game()
        else:
            attempts -= 1
            if attempts > 0:
                messagebox.showwarning("Wrong Guess", f"Wrong guess! You have {attempts} attempts left.")
            else:
                messagebox.showerror("Game Over", f"Game over! The correct number was {guess_num}. Shutting down...")
                shutdown_system()
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number.")

def reset_game():
    global guess_num, attempts
    guess_num = random.randint(1, 5)
    attempts = 2
    entry.delete(0, tk.END)

def shutdown_system():
    os.system("shutdown /s /t 1")

guess_num = random.randint(1, 5)
attempts = 2

root = tk.Tk()
root.title("Quacks roulette")
root.geometry("300x200")

label = tk.Label(root, text="Guess a number between 1 and 5", font=("Arial", 12))
label.pack(pady=10)

entry = tk.Entry(root, font=("Arial", 12))
entry.pack(pady=5)

button = tk.Button(root, text="Submit Guess", command=check_guess, font=("Arial", 12))
button.pack(pady=10)

reset_button = tk.Button(root, text="Reset Game", command=reset_game, font=("Arial", 12))
reset_button.pack(pady=5)

root.mainloop()