import tkinter as tk
import customtkinter as ctk
import os 
import json
quizzes = ["Quiz1","Quiz2", "Quiz3"]


quiz_files =  [f for f in os.listdir('quizzes') if f.endswith('.json')]
quiz_drop = []
for file in quiz_files:
    with open('quizzes/'+ file) as f:
        data = json.load(f)
        quiz_drop.append(data[0]['title'])

# class MainWindow(ctk.CTk):
#     def __init__(self):
#         super().__init__()
        
        
#         self.title("DeQuiz")
#         self.geometry("1000x600")
#         self.configure(padx = 10, pady= 10)
#         self.teacher_dashboard_frame = StudentDashboard(self)
#         self.teacher_dashboard_frame.pack()
        

class StudentDashboard(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        
        self.teacher_frame = ctk.CTkFrame(self, width=200, height=200)
        self.teacher_frame.pack(padx = 10, pady= 10)
        
        self.teacher_text = ctk.CTkLabel(self.teacher_frame, text="Welecome Student")
        self.teacher_text.pack(padx = 10, pady= 10)
   

        # , command = self.master.switch_to_teacher_dashboard

        self.quiz_list_frame = ctk.CTkFrame(self, width=800, height=200)
        self.quiz_list_frame.pack(padx = 100, pady= 30)
        self.display_quizes()

    def display_quizes(self):
        
        self.question_buttons = []
       
        for quiz_btn in self.quiz_list_frame.winfo_children():
            quiz_btn.destroy()

        self.question_buttons.clear()

        
        for index, quiz_title in enumerate(quiz_drop):
            print(index)
            self.question_btn = ctk.CTkButton(self.quiz_list_frame, text=f"{quiz_drop[index]}" , fg_color= "transparent" , 
                                              command=lambda q=quiz_title: self.open_quiz(q))
            self.question_btn.grid(row=index + 2, column=0, padx = 100, pady= 10)
            self.result_button = ctk.CTkButton(self.quiz_list_frame, text="Result", command=lambda i=index: self.remove_quiz(i),  width=20, height=20)
            self.result_button.grid(row=index + 2, column=1, padx = 10, pady= 10)
            
            self.question_buttons.append([self.question_btn, self.result_button])


    def open_quiz(self, quiz_title):
        print(quiz_title)
        self.master.switch_to_quiz_display("phy")
        # self.master.switch_to_quiz_display()
        return quiz_title
    # def remove_quiz(self,index):
    #     quiz_drop.pop(index)
    #     self.question_buttons.pop(index)
    #     self.display_quizes()

    def remove_quiz(self, index):
        quiz_title = quiz_drop[index]
        quiz_file = [file for file in quiz_files if quiz_title in file][0]
        quiz_path = os.path.join('quizzes', quiz_file)
        os.remove(quiz_path)

        quiz_drop.pop(index)
        quiz_files.remove(quiz_file)
        self.display_quizes()
    

# main_window = MainWindow()
# main_window.mainloop()