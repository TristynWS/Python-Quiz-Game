import unittest
import tkinter as tk
from tkinter import Button

from self_quiz_game import QuizApp  


class TestQuizApp(unittest.TestCase):
    def setUp(self):
        self.root = tk.Tk()
        self.app = QuizApp(self.root)

    def tearDown(self):
        self.root.destroy()

    def test_question_label(self):
        expected_question_text = "Test question"
        self.app.questions = [(expected_question_text, True)]
        self.app.display_question()
        actual_question_text = self.app.question_label.cget("text")
        self.assertEqual(actual_question_text, expected_question_text)

    def test_evaluate_answer_correct(self):
        self.app.score = 0
        self.app.current_question_index = 0
        self.app.evaluate_answer(True)
        self.assertEqual(self.app.score, 1)

    def test_evaluate_answer_incorrect(self):
        self.app.score = 0
        self.app.current_question_index = 0
        self.app.evaluate_answer(False)
        self.assertEqual(self.app.score, 0)

    def test_next_question(self):
        self.app.current_question_index = 0
        self.app.next_question()
        self.assertEqual(self.app.current_question_index, 1)

    def test_show_results(self):
        self.app.score = 3
        self.app.show_results()
        expected_message = "You scored 3/5. Better luck next time!"
        actual_message = self.app.question_label.cget("text")
        self.assertEqual(actual_message, expected_message)

    def test_show_results_0_correct(self):
        self.app.score = 0
        self.app.show_results()
        expected_message = "You scored 0/5. Maybe try again?"
        actual_message = self.app.question_label.cget("text")
        self.assertEqual(actual_message, expected_message)

    def test_show_results_0_correct(self):
        self.app.score = 1
        self.app.show_results()
        expected_message = "You scored 1/5. Maybe try again?"
        actual_message = self.app.question_label.cget("text")
        self.assertEqual(actual_message, expected_message)

    def test_show_results_0_correct(self):
        self.app.score = 2
        self.app.show_results()
        expected_message = "You scored 2/5. Maybe try again?"
        actual_message = self.app.question_label.cget("text")
        self.assertEqual(actual_message, expected_message)

    def test_show_results_0_correct(self):
        self.app.score = 4
        self.app.show_results()
        expected_message = "You scored 4/5. Great job!"
        actual_message = self.app.question_label.cget("text")
        self.assertEqual(actual_message, expected_message)

    def test_show_results_0_correct(self):
        self.app.score = 5
        self.app.show_results()
        expected_message = "You scored 5/5. Great job!"
        actual_message = self.app.question_label.cget("text")
        self.assertEqual(actual_message, expected_message)


if __name__ == "__main__":
    unittest.main()