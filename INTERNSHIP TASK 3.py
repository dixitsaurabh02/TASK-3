import tkinter as tk
from tkinter import messagebox
import random

def computer_selection():
    choices = ["rock", "paper", "scissor"]
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissor") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissor" and computer_choice == "paper"):
        return "You Win!"
    else:
        return "You Lose!"

def play_game(user_choice):
    computer_choice = computer_selection()
    result = determine_winner(user_choice, computer_choice)
    result_label.config(text=f"Computer chose: {computer_choice}\n{result}")

    if "Win" in result:
        global user_score
        user_score += 1
    elif "Lose" in result:
        global computer_score
        computer_score += 1

    score_label.config(text=f"Score: You {user_score} - Computer {computer_score}")

def reset_game():
    global user_score, computer_score
    user_score = 0
    computer_score = 0
    score_label.config(text="Score: You 0 - Computer 0")
    result_label.config(text="")

user_score = 0
computer_score = 0

root = tk.Tk()
root.title("Rock-Paper-Scissors Game")

instruction_label = tk.Label(root, text="Choose rock, paper, or scissor:")
instruction_label.pack()

rock_button = tk.Button(root, text="Rock", command=lambda: play_game("rock"))
rock_button.pack()

paper_button = tk.Button(root, text="Paper", command=lambda: play_game("paper"))
paper_button.pack()

scissor_button = tk.Button(root, text="Scissor", command=lambda: play_game("scissor"))
scissor_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

score_label = tk.Label(root, text="Score: You 0 - Computer 0")
score_label.pack()

reset_button = tk.Button(root, text="Reset Game", command=reset_game)
reset_button.pack()

root.mainloop()
