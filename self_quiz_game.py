import tkinter as tk
from tkinter import messagebox

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("True or False Quiz")
        self.root.geometry("400x300")  # Fixed size window
        self.root.configure(bg="white")

        self.questions = [
            ("Tristyn has been bitten by a baby rattlesnake.", True),
            ("Tristyn wrestled a bear once.", False),
            ("Tristyn loves to problem solve.", True),
            ("Tristyn is fascinated by AI.", True),
            ("Tristyn is a dedicated and creative team player.", True)
        ]
        self.current_question_index = 0
        self.score = 0

        self.question_label = tk.Label(self.root, text="", wraplength=380, bg="white")
        self.question_label.pack(pady=20)

        self.true_button = tk.Button(self.root, text="True", command=self.check_true)
        self.true_button.pack(side="left", padx=20)

        self.false_button = tk.Button(self.root, text="False", command=self.check_false)
        self.false_button.pack(side="right", padx=20)

        self.next_button = tk.Button(self.root, text="Next", command=self.next_question)
        self.next_button.pack(pady=20)
        self.next_button.pack_forget()  # Hide the Next button initially

        self.display_question()  # Display the first question

    def display_question(self):
        question_text = self.questions[self.current_question_index][0]
        self.question_label.config(text=question_text)

    def check_true(self):
        self.evaluate_answer(True)

    def check_false(self):
        self.evaluate_answer(False)

    def evaluate_answer(self, selected_answer):
        correct_answer = self.questions[self.current_question_index][1]
        if selected_answer == correct_answer:
            self.score += 1
            messagebox.showinfo("Correct", "Correct! Good job!")
        else:
            messagebox.showerror("Incorrect", "Nope, nice try!")

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
        elif self.score >= 3:
            message += " Better luck next time!"
        else:
            message += " Maybe try again?"
        messagebox.showinfo("Quiz Complete", message)
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()
