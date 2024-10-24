import tkinter as tk
from tkinter import messagebox

# Initialize the main window
root = tk.Tk()
root.title("Python Quiz Game")
root.geometry("900x500")

# Global variables
score = 0
attempt = 0
current_question = 0
questions = [
        ("What is the term for a collection of instructions that a computer can execute?", "program"),
        ("What do we call a variable that can hold multiple values, often of the same type?", "list"),
        ("What is the structure called that allows you to control the flow of your program based on conditions?", "if statement"),
        ("What is the term for reusing code by creating a named block of code that can be called?", "function"),
        ("What is the name of the error that occurs when you try to access an index that is out of bounds?", "IndexError"),
        ("What do we call a sequence of characters in Python?", "string"),
        ("What is the term for a programming style that focuses on using objects to represent data?", "object-oriented programming"),
        ("What do we call a block of code that runs when an error occurs?", "exception handler"),
        ("What is the term for a data type that can hold true or false values?", "boolean"),
        ("What is the keyword used to create a new class in Python?", "class"),
        ("What do we call a function that calls itself?", "recursive function"),
        ("What is the term for a collection of key-value pairs in Python?", "dictionary"),
        ("What is the name of the built-in function that can be used to output text to the console?", "print"),
        ("What is the term for code that is written to solve a specific problem?", "algorithm"),
        ("What do we call a file containing a collection of Python code that can be imported?", "module"),

]

# Function to check the guess
def check_guess():
    global score, attempt, current_question

    guess = entry_guess.get().lower()
    answer = questions[current_question][1].lower()

    if guess == answer:
        messagebox.showinfo("Result", "Correct Answer!")
        score += 1
        lbl_score.config(text="Score: " + str(score))
        next_question()
    else:
        if attempt < 2:
            attempt += 1
            messagebox.showinfo("Result", "Wrong! Try again.")
        else:
            messagebox.showinfo("Result", f"Wrong! The correct answer is {answer}")
            next_question()

# Function to move to the next question
def next_question():
    global attempt, current_question

    attempt = 0
    current_question += 1

    if current_question < len(questions):
        lbl_question.config(text=questions[current_question][0])
        entry_guess.delete(0, tk.END)
    else:
        lbl_question.config(text="Game Over!")
        entry_guess.config(state='disabled')
        btn_submit.config(state='disabled')
        messagebox.showinfo("Final Score", f"Your final score is {score}")

# Create and place widgets
lbl_question = tk.Label(root, text=questions[current_question][0], font=("Arial", 14))
lbl_question.pack(pady=20)

entry_guess = tk.Entry(root, font=("Arial", 14))
entry_guess.pack(pady=40)

btn_submit = tk.Button(root, text="Submit Guess", command=check_guess)
btn_submit.pack(pady=70)

lbl_score = tk.Label(root, text="Score: 0", font=("Arial", 12))
lbl_score.pack(pady=10)
root.mainloop()
