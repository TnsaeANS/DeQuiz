import tkinter as tk
import customtkinter as ctk

quizzes = ["Quiz1","Quiz2", "Quiz3"]



# class MainWindow(ctk.CTk):
#     def __init__(self):
#         super().__init__()
        
        
#         self.title("DeQuiz")
#         self.geometry("1000x600")
        
#         self.teacher_dashboard_frame = TeacherDashboard(self)
#         self.teacher_dashboard_frame.pack()
        

class TeacherDashboard(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        
        self.teacher_frame = ctk.CTkFrame(self, width=200, height=200)
        self.teacher_frame.pack()
        
        self.teacher_text = ctk.CTkLabel(self.teacher_frame, text="Welecome Teacher")
        self.teacher_text.pack(padx = 10, pady= 10)
        self.save_quiz_button = ctk.CTkButton(self, text='Add Quiz', command=self.master.switch_to_quiz_editor)

        # , command = self.master.switch_to_teacher_dashboard

        self.save_quiz_button.pack(padx = 10, pady = 10)
        self.quiz_list_frame = ctk.CTkFrame(self, width=800, height=200)
        self.quiz_list_frame.pack(padx = 100, pady= 100)
        self.display_quizes()

    def display_quizes(self):
        
        self.question_buttons = []
        for quiz_btn in self.quiz_list_frame.winfo_children():
            quiz_btn.destroy()

        self.question_buttons.clear()

        
        for index, car in enumerate(quizzes):
            print(index)
            self.question_btn = ctk.CTkButton(self.quiz_list_frame, text=f"{quizzes[index]}" , fg_color= "transparent" , command=lambda i=index: self.remove_quiz(i))
            self.question_btn.grid(row=index + 2, column=0, padx = 100, pady= 10)
            self.remove_button = ctk.CTkButton(self.quiz_list_frame, text="Remove ", command=lambda i=index: self.remove_quiz(i),  width=20, height=20)
            self.remove_button.grid(row=index + 2, column=2, padx = 10, pady= 10)
            self.result_button = ctk.CTkButton(self.quiz_list_frame, text="Results ", command=lambda i=index: self.remove_quiz(i),  width=20, height=20)
            self.result_button.grid(row=index + 2, column=1, padx = 10, pady= 10)
            
            self.question_buttons.append([self.question_btn, self.remove_button,self.result_button])

    def remove_quiz(self,index):
        quizzes.pop(index)
        self.question_buttons.pop(index)
        self.display_quizes()
    

# main_window = MainWindow()
# main_window.mainloop()