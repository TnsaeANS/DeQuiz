import tkinter as tk
import customtkinter as ctk
from class_quiz_parser import MultipleChoiceParser
from tkinter.messagebox import askyesno
from tkinter import messagebox
import json
import os

class QuizEditor(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.create_widgets()

    def create_widgets(self):
        self.quiz_title = ctk.CTkLabel(self, text="Enter quiz title")
        self.quiz_title.pack(padx=10, pady=10)

        self.quiz_title_entry = ctk.CTkEntry(self, width=400, height=30)
        self.quiz_title_entry.pack()

        self.label_content = ctk.CTkLabel(self, text="Enter your questions. Separate each question and multiple choice on a new line. Example:")
        self.label_content.pack(padx=10, pady=10)

        self.quiz_textbox = ctk.CTkTextbox(self, width=600, height=400)
        self.quiz_textbox.pack(padx=10, pady=10)

        self.save_quiz_button = ctk.CTkButton(self, text="Save", command=self.save_quiz)
        self.save_quiz_button.pack(padx=10, pady=10)

    def save_quiz(self):
        quiz_title_value = self.quiz_title_entry.get()
        quiz_text_value = self.quiz_textbox.get("1.0", "end")

        current_question_data = MultipleChoiceParser(quiz_text_value, quiz_title_value).question_data

        if not os.path.exists('quizzes'):
            os.makedirs('quizzes')

        file_path = os.path.join('quizzes', f'{quiz_title_value}.json')

        with open(file_path, 'w') as f:
            json.dump(current_question_data, f)
        
        # quiz_data = {
        #     'teacher_id': 1,  # Replace with the actual teacher ID
        #     'quiz_file': json.dumps(current_question_data),
        #     'title': quiz_title_value }

        # self.cur.execute("""
        #     INSERT INTO quizzes (teacher_id, quiz_file, title)
        #     VALUES (:teacher_id, :quiz_file, :title)
        # """, quiz_data)

        # self.conn.commit()

        messagebox.showinfo("Success", "Quiz saved successfully.")


