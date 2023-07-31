import customtkinter as ctk
import _sqlite3
from RG_login import LoginApp
from RG_register import RegisterApp
from student_dashboard import StudentDashboard
from teacher_dashboard import TeacherDashboard
from interface_quiz_display import QuizDisplay
from interface_add_quiz import QuizEditor

class MainWindow(ctk.CTk):
    def __init__(self):
        super().__init__()
        print(self)
        self.title("DeQuiz")
        self.geometry("1000x600")
        width = self.winfo_screenwidth()
        height = self.winfo_screenwidth()
        # self.quiz_title = 
        # self.geometry('{}x{}+0+0'.format(width, height))
        # self.configure(fg_color = "red")
        self.db_conn = _sqlite3.connect('data.db')
       
        self.login_frame = LoginApp(self, self.db_conn)
        self.register_frame = RegisterApp(self, self.db_conn)
       
        print("hi")
        self.add_quiz = QuizEditor(self)
        self.student_dashboard_frame = StudentDashboard(self)
        self.teacher_dashboard_frame = TeacherDashboard(self)

        self.switch_to_login()

    def switch_to_quiz_display(self,quiz_title):
        self.quiz_display = QuizDisplay(self, quiz_title)
        trust = QuizDisplay(self, quiz_title)
        print(trust)
        # .pack()
        self.hide_all_frames()
        self.quiz_display.pack()
        print("switched to quzi")

    def switch_to_quiz_editor(self):
        self.hide_all_frames()
        self.add_quiz.pack()
    
    def switch_to_login(self):
        self.hide_all_frames()
        self.login_frame.place(relx=.5, rely=.5,anchor= "center")   

    def switch_to_register(self):
        self.hide_all_frames()
        self.register_frame.pack()

    def switch_to_student_dashboard(self):
        self.hide_all_frames()
        self.student_dashboard_frame.pack()

    def switch_to_teacher_dashboard(self):
        self.hide_all_frames()
        self.teacher_dashboard_frame.pack()

    def hide_all_frames(self):
        self.login_frame.place_forget()
        self.register_frame.pack_forget()
        self.student_dashboard_frame.pack_forget()
        self.teacher_dashboard_frame.pack_forget()

if __name__ == "__main__":
    main_window = MainWindow()
    main_window.mainloop()
