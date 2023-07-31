import tkinter as tk
import customtkinter as ctk
from tkinter.messagebox import askyesno
from tkinter import messagebox
from question_model import Question
from data import question_data
import json

file_path = f'quizzes/file.txt'
class QuizDisplay(ctk.CTkFrame):
    def __init__(self, master, file_name):
        self.file_name = file_name
        super().__init__(master)
        self.qst_num = 0
        self.score = 0
        self.qst_obj_list = []
        self.options = []
        self.user_choices = [0 for _ in range(len(question_data))]
        self.item_number_objects = []

        self.initialize_question_bank(self.file_name)

        self.create_question_frame()
        self.create_button_frame()
        self.create_item_number_buttons()

    def initialize_question_bank(self,file_name):
        with open(f'quizzes\{file_name}.json', 'r') as f:
            json_str = f.read()

        self.qst_data_list = json.loads(json_str)
        print('SUCC',file_name)
        print(self.qst_data_list)
        print("typpp",type(self.qst_data_list))
        print('bUCC',file_name)
     
        # self.qst_list = [Question(qst_data["stem"], qst_data["answer"], qst_data["options"]) 
        #                  for qst_data in self.qst_data_list if list(qst_data.keys())[0] == "stem"]
      
        for qst_data in self.qst_data_list:
            if list(qst_data.keys())[0] == "stem":
                print("processing",qst_data.keys())
                question = Question(qst_data["stem"], qst_data["answer"], qst_data["options"])
                self.qst_obj_list.append(question)

        print('bdsdUCC',self.qst_obj_list)
    def create_question_frame(self):
        
        self.question_frame = ctk.CTkFrame(self, width=500, height=220)
        self.question_label = ctk.CTkLabel(self.question_frame)
        self.question_frame.pack(padx=50, pady=50)
        self.question_frame.pack_propagate(0)
        self.question_label.pack(padx=10, pady=10)
        print("creating a btn fram")
    def create_button_frame(self):
        
        button_frame = ctk.CTkFrame(self, width=200)

        self.check_option_state = ctk.IntVar()

        for item_num, choice in enumerate(self.qst_obj_list[self.qst_num].options):
            option_btn = ctk.CTkRadioButton(self.question_frame, value=item_num + 1, text=choice, variable=self.check_option_state)
            option_btn.pack(padx=10, pady=10)
            self.options.append(option_btn)
        print("creating a number buttons")
        self.btn_next = ctk.CTkButton(button_frame, text="Next", command=self.next_question)
        self.btn_next.pack(side=ctk.RIGHT, padx=10, pady=10)

        self.btn_previous = ctk.CTkButton(button_frame, text="Previous", command=self.previous_question)
        self.btn_previous.pack(side=ctk.LEFT, padx=10, pady=10)

        button_frame.pack(pady=10)

        self.btn_finish = ctk.CTkButton(self, text="Finish", command=self.check_answer)
        self.btn_finish.pack(padx=10, pady=10)
       
    def create_item_number_buttons(self):
        self.item_button_frame = ctk.CTkFrame(self)

        for item_num in range(len(self.qst_obj_list)):
            item_number_btn = ctk.CTkButton(self.item_button_frame, text=item_num + 1, width=20, height=20,
                                            command=lambda jn=item_num: self.jump_to_question(jn))
            item_number_btn.grid(row=item_num // 10, column=item_num % 10, padx=10, pady=10)
            self.item_number_objects.append(item_number_btn)

        self.item_button_frame.pack(padx=10, pady=10)

    def jump_to_question(self, jump_num):
        self.set_answer()
        self.qst_num = jump_num
        self.set_button()

        current_question = self.qst_obj_list[self.qst_num]
        self.question_label.configure(text=current_question.text)

        for i, option in enumerate(self.options):
            option.configure(text=self.qst_obj_list[self.qst_num].options[i])

    def next_question(self):
        self.set_answer()

        if self.qst_num + 1 < len(self.qst_obj_list):
            self.qst_num += 1
            current_question = self.qst_obj_list[self.qst_num]
            self.question_label.configure(text=current_question.text)

            for i, option in enumerate(self.options):
                option.configure(text=self.qst_obj_list[self.qst_num].options[i])
        else:
            print("Your Score is:", self.score)

        self.set_button()

    def previous_question(self):
        self.set_answer()

        if self.qst_num + 1 > 1:
            self.qst_num -= 1
            current_question = self.qst_obj_list[self.qst_num]
            self.question_label.configure(text=current_question.text)

            for i, option in enumerate(self.options):
                option.configure(text=self.qst_obj_list[self.qst_num].options[i])
        else:
            print("Your Score is:", self.score)

        self.set_button()

    def check_answer(self):
        for i, choice in enumerate(self.user_choices):
            if choice == 0:
                messagebox.showinfo("Error", f"Answer for question number {i + 1} is missing!")
                break
        else:
            self.btn_finish.configure(state="disabled")

            for i in range(len(self.qst_data_list)):
                if self.qst_data_list[i]["answer"] == self.user_choices[i]:
                    self.score += 1

            messagebox.showinfo("Score", f"Your Score is: {self.score}")

    def set_answer(self):
        self.choice_letter = [0, "A", "B", "C", "D"]
        self.user_choices[self.qst_num] = self.choice_letter[self.check_option_state.get()]

        if self.user_choices[self.qst_num] != 0:
            self.item_number_objects[self.qst_num].configure(fg_color="LightSkyBlue4")

    def set_button(self):
        if self.user_choices[self.qst_num] == 0:
            self.check_option_state.set(0)
        elif self.user_choices[self.qst_num] == "A":
            self.check_option_state.set(1)
        elif self.user_choices[self.qst_num] == "B":
            self.check_option_state.set(2)
        elif self.user_choices[self.qst_num] == "C":
            self.check_option_state.set(3)
        elif self.user_choices[self.qst_num] == "D":
            self.check_option_state.set(4)
