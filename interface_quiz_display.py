import tkinter as tk
import customtkinter as ctk
from tkinter. messagebox import askyesno
from question_model import Question
from data import question_data
from tkinter import messagebox

# Print the options of the first question from the question_data list
print(question_data[0]["options"])

# Create a question_bank list using list comprehension(this is a list of question objects with there own stem, opiton and answers)
question_bank = [Question(question["stem"], question["answer"], question["options"]) for question in question_data]

# Create a class called MyQz
class MyQz:
    def __init__(self, qst_list):
        # Initialize some variables
        self.qst_num = 0
        self.score = 0
        self.qst_list = qst_list
        self.options = []
        self.user_choices = [0 for i in range(len(question_bank))]
        self.item_number_objects = []
        
        current_question = self.qst_list[self.qst_num]

        # Customizing the window
        ctk.set_appearance_mode("system")
        ctk.set_default_color_theme("blue")
        self.root = ctk.CTk()
        self.root.geometry('1000x600')
        self.root.title("DeQuiz")

        # Creating a question frame and displaying the question
        self.quesion_frame = ctk.CTkFrame(self.root ,width=500, height=220)
        self.question_label = ctk.CTkLabel(self.quesion_frame, text=current_question.text)
        self.quesion_frame.pack(padx=50, pady=50)
        self.quesion_frame.pack_propagate(0)
        self.question_label.pack(padx=10, pady=10)
       
        button_frame = ctk.CTkFrame(self.root, width=200)

        # Displaying each choice
        self.check_option_state = ctk.IntVar()

        for item_num, choice in enumerate(question_data[self.qst_num]["options"]):
            self.option_btn = ctk.CTkRadioButton(self.quesion_frame, value=item_num + 1, text=choice, variable=self.check_option_state)
            self.option_btn.pack(padx=10, pady=10)
            self.options.append(self.option_btn)

        self.btn_next = ctk.CTkButton(button_frame, text="Next", command=self.next_question)
        self.btn_next.pack(side=ctk.RIGHT, padx=10, pady=10)

        self.btn_previous = ctk.CTkButton(button_frame, text="Previous", command=self.previous_question)
        self.btn_previous.pack(side=ctk.LEFT, padx=10, pady=10)
        
        button_frame.pack(pady=10)

        
    


        # Displaying item number buttons


        self.item_button_frame = ctk.CTkFrame(self.root)

        for item_num in range(len(question_bank)):
            self. item_number_btn = ctk.CTkButton(self.item_button_frame, text=item_num+1 , width=20, height=20, 
                             command =  lambda jn=item_num : self.jumpto_question(jn)
            )
            self.item_number_btn.grid( row = item_num//10 , column = item_num%10, padx = 10, pady = 10)
            self.item_number_objects.append(self. item_number_btn)
        self.item_button_frame.pack(padx=10, pady=10)

        self.btn_finish = ctk.CTkButton(self.root, text="Finish", command=self.check_answer)
        self.btn_finish.pack(padx=10, pady=10)



        def confirm():
            answer = askyesno(title='confirmation',
                            message='Are you sure that you want to quit?')
            if answer:
                self.root.destroy()

        self.root.protocol("WM_DELETE_WINDOW", confirm)
        
        self.root.mainloop()

                
        
    def jumpto_question(self, jump_num):
    
        self.set_answer()
        self.j_item_num = jump_num
        self.qst_num = jump_num
        print("jumped to", self.qst_num+1)
        self.set_button()
    
        current_question = self.qst_list[self.j_item_num]
        self.question_label.configure(text=current_question.text)

        for i, option in enumerate(self.options):
            option.configure(text=question_data[self.j_item_num]["options"][i])
        

    def next_question(self):
        self.set_answer()
        print(self.user_choices)
        if self.qst_num + 1 < len(self.qst_list):
            self.qst_num += 1
            current_question = self.qst_list[self.qst_num]
            self.question_label.configure(text=current_question.text)

            for i, option in enumerate(self.options):
                option.configure(text=question_data[self.qst_num]["options"][i])
        else:
            print("Your Score is : ", self.score)
        self.set_button()

    def previous_question(self):
        self.set_answer()
        print(self.user_choices)
        if self.qst_num + 1 > 1:
            self.qst_num -= 1
            current_question = self.qst_list[self.qst_num]
            self.question_label.configure(text=current_question.text)

            for i, option in enumerate(self.options):
                option.configure(text=question_data[self.qst_num]["options"][i])
        else:
            print("Your Score is : ", self.score)
        self.set_button()
        

    def check_answer(self):
        #check if every question is answered
        for i, choice in enumerate(self.user_choices):
            if choice == 0:
                messagebox.showinfo("Error", f"Answer for question number {i+1} missing!")
                break
            else:
                self.btn_finish.configure(state="disabled")
                self.correct_answer = [question_data[self.qst_num]["answer"] for i in range(len(question_bank))]
                for i in range(len(question_data)):
                    self.choice_letter = [0, "A", "B", "C", "D"]
                    if question_data[i]["answer"] ==  self.user_choices[i]:
                        self.score += 1
                messagebox.showinfo("Error", f"Your Score is {self.score}")
                break
        

    def set_answer(self):
        
        self.choice_letter = [0, "A", "B", "C", "D"]
        self.user_choices[self.qst_num] = self.choice_letter[self.check_option_state.get()]
        if self.user_choices[self.qst_num] != 0:
                print("setto")
                self.item_number_objects[self.qst_num].configure(fg_color= "LightSkyBlue4")
        print(self.qst_num+1, "dd" ,self.user_choices)
        
        #Setting Button color
  
            


    def set_button(self):
        print("setted to",self.user_choices[self.qst_num])
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

    
        

# Create an instance of MyQz and pass the question_bank list
quiz = MyQz(question_bank)
