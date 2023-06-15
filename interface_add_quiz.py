import tkinter as tk
import customtkinter as ctk
from class_quiz_parser import MultipleChoiceParser

import json
import os


ctk.set_appearance_mode("system")
ctk.set_default_color_theme("blue")
myfont = ("Segoe UI Variable", 15, "bold")

root = ctk.CTk()

width = root.winfo_screenwidth()
height = root.winfo_screenwidth()

root.geometry('{}x{}+0+0'.format(width,height))
root.title("DeQuiz")

frame =ctk.CTkFrame(root)
frame.pack(pady = 10, padx = 10, fill = "both", expand = True)

quiz_title = ctk.CTkLabel(frame,  text = "Enter quiz title")
quiz_title.pack(padx = 10, pady=10)

quiz_title = ctk.CTkEntry(frame, width=400, height=30,)
quiz_title.pack()

label_content = ctk.CTkLabel(frame,  text = "Enter your questions. Separate each question and multiple choice on a new line. Example:")
label_content.pack(padx = 10, pady= 10)

quiz_textbox = ctk.CTkTextbox(frame, width=600, height=400)
quiz_textbox.pack(padx = 10, pady= 10)






quiz_textbox.insert("0.0",
"1. What is the capital of France?\n" + 
"A. London\n" + 
"B. Paris\n" +
"C. Madrid\n"
"D. Rome\n"
"B \n\n" +

"2. Which planet is known as the Red Planet?\n" +
"A. Jupiter\n"
"B. Mars\n"
"C. Saturn\n"
"D. Venus\n"
"B")


def save_quiz():
    quiz_title_value = quiz_title.get()
    quiz_text_value = quiz_textbox.get("1.0","end")

    current_question_data = MultipleChoiceParser(quiz_text_value,quiz_title_value).question_data

    if not os.path.exists('quizzes'):
        os.makedirs('quizzes')
    
    file_path = os.path.join('quizzes', f'{quiz_title_value}.json')

    with open(file_path, 'w') as f:
        json.dump(current_question_data, f)

    
save_quiz_button = ctk.CTkButton(frame, text='Save', command=save_quiz)

save_quiz_button.pack(padx = 10, pady = 10)


root.mainloop()  