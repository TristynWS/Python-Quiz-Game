import tkinter as tk
from tkinter import messagebox

class QuizGame:
    def __init__(self, master):
        self.master = master
        self.master.title("True or False Quiz Game")
        
        self.questions = [
            {"statement": "Tristyn has been bitten by a baby rattlesnake.", "answer": True},
            {"statement": "Tristyn wrestled a bear once.", "answer": False},
            {"statement": "Tristyn loves to problem solve.", "answer": True},
            {"statement": "Tristyn is fascinated by AI.", "answer": True},
            {"statement": "Tristyn is a dedicated and creative team player.", "answer": True}
        ]
        
        self.current_question_index = 0
        self.score = 0
        
        self.label = tk.Label(master, text=self.questions[self.current_question_index]["statement"])
        self.label.pack()
        
        self.true_button = tk.Button(master, text="True", command=lambda: self.check_answer(True))
        self.true_button.pack()
        
        self.false_button = tk.Button(master, text="False", command=lambda: self.check_answer(False))
        self.false_button.pack()
        
        self.next_button = tk.Button(master, text="Next", command=self.next_question)
        self.next_button.pack()
    
    def check_answer(self, user_answer):
        correct_answer = self.questions[self.current_question_index]["answer"]
        if user_answer == correct_answer:
            self.score += 1
            messagebox.showinfo("Correct", "You got it right!")
        else:
            messagebox.showinfo("Incorrect", "Sorry, the correct answer is {}.".format(correct_answer))
    
    def next_question(self):
        self.current_question_index += 1
        if self.current_question_index < len(self.questions):
            self.label.config(text=self.questions[self.current_question_index]["statement"])
        else:
            self.show_result()
    
    def show_result(self):
        result_message = ""
        if self.score == 5:
            result_message = "Great job!"
        elif self.score >= 3:
            result_message = "Better luck next time!"
        else:
            result_message = "Maybe try again?"
        messagebox.showinfo("Quiz Finished", "{} Your score: {}/5".format(result_message, self.score))

def main():
    root = tk.Tk()
    app = QuizGame(root)
    root.mainloop()

if __name__ == "__main__":
    main()
