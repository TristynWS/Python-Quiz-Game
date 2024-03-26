import tkinter as tk
from tkinter import messagebox

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("True or False Quiz")
        self.root.geometry("400x300")  # Fixed size window
        self.root.configure(bg="#f0f0f0")  # Set background color

        self.questions = [
            ("Tristyn has been bitten by a baby rattlesnake.", True),
            ("Tristyn wrestled a bear once.", False),
            ("Tristyn loves to problem solve.", True),
            ("Tristyn is fascinated by AI.", True),
            ("Tristyn is a dedicated and creative team player.", True)
        ]
        self.current_question_index = 0
        self.score = 0

        self.question_label = tk.Label(self.root, text="", wraplength=380, bg="#f0f0f0", fg="#333333", font=("Arial", 12))
        self.question_label.pack(pady=20)

        self.true_button = tk.Button(self.root, text="True", command=lambda: self.evaluate_answer(True), bg="#b8d8d8", fg="#333333", font=("Arial", 10))
        self.true_button.pack(side="left", padx=20)

        self.false_button = tk.Button(self.root, text="False", command=lambda: self.evaluate_answer(False), bg="#b8d8d8", fg="#333333", font=("Arial", 10))
        self.false_button.pack(side="right", padx=20)

        self.next_button = tk.Button(self.root, text="Next", command=self.next_question, bg="#b8d8d8", fg="#333333", font=("Arial", 10))
        self.next_button.pack(pady=20)
        self.next_button.pack_forget()  # Hide the Next button at first

        self.display_question()  # Display the first question

    def display_question(self):
        question_text = self.questions[self.current_question_index][0]
        self.question_label.config(text=question_text)

    def evaluate_answer(self, selected_answer):
        correct_answer = self.questions[self.current_question_index][1]
        if selected_answer == correct_answer:
            self.score += 1
            self.question_label.config(text="Correct! Good job!")
        else:
            self.question_label.config(text="Nope, nice try!")

        # Show the Next button after an answer is selected
        self.next_button.pack(pady=20)
        self.true_button.config(state="disabled")
        self.false_button.config(state="disabled")

    def next_question(self):
        self.current_question_index += 1
        if self.current_question_index < len(self.questions):
            self.display_question()
            # Hide the Next button again for the next question
            self.next_button.pack_forget()
            self.true_button.config(state="normal")
            self.false_button.config(state="normal")
        else:
            self.show_results()

    def show_results(self):
        message = f"You scored {self.score}/5."
        if self.score >= 4:
            message += " Great job!"
        elif self.score == 3:
            message += " Better luck next time!"
        else:
            message += " Maybe try again?"
        self.question_label.config(text=message)
        self.true_button.pack_forget()
        self.false_button.pack_forget()
        self.next_button.config(text="Quit", command=self.root.destroy)
        self.next_button.pack(pady=20)

if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()
