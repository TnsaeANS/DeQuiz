import customtkinter as ctk
import _sqlite3
from tkinter import messagebox

class LoginApp(ctk.CTkFrame):
    def __init__(self, master, db_conn):
        super().__init__(master)
        self.master = master
    
        self.conn = db_conn
        self.cur = self.conn.cursor()
        self.configure(fg_color = "#242424")
        self.create_table()
     
        self.display_login()

    def create_table(self):
        self.cur.execute("""
            CREATE TABLE IF NOT EXISTS users(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            fullname VARCHAR(255) NOT NULL, 
            password VARCHAR(255) NOT NULL,
            is_teacher BIT)
        """)
    
        self.cur.execute("""
        CREATE TABLE IF NOT EXISTS quizzes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            teacher_id INTEGER,
            title TEXT,
            FOREIGN KEY (teacher_id) REFERENCES teachers (id)
        )
    """)
        
        self.cur.execute("""
        CREATE TABLE IF NOT EXISTS scores (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_id INTEGER,
            quiz_id INTEGER,
            score INTEGER,
            FOREIGN KEY (student_id) REFERENCES students (id),
            FOREIGN KEY (quiz_id) REFERENCES quizzes (id)
    )
""")

    def register(self):
        fullname = self.fullname_entry.get()
        password = self.password_entry.get()
        is_teacher = self.is_teacher_state.get()

        if fullname and password:
            self.cur.execute("SELECT fullname FROM users WHERE fullname=?", [fullname])
            if self.cur.fetchone() is not None:
                messagebox.showerror("Error", "Name already exists.")
            else:
                self.cur.execute("INSERT INTO users (fullname, password, is_teacher) VALUES (?, ?, ?)",
                                 (fullname, password, is_teacher))
                self.conn.commit()
                messagebox.showinfo("Success", "Your account is created.")
        else:
            messagebox.showerror("Error", "Information missing!")

    def login(self):
        fullname = self.fullname_entry.get()
        password = self.password_entry.get()

        if fullname and password:
            self.cur.execute("SELECT password, is_teacher FROM users WHERE fullname=?", [fullname])
            result = self.cur.fetchone()
            if result:
                stored_password = result[0]
                is_teacher = result[1]
                if stored_password == password:
                    messagebox.showinfo("Success", "Logged in.")
                    if is_teacher:
                        self.master.switch_to_teacher_dashboard()
                    else:
                        self.master.switch_to_student_dashboard()
                else:
                    messagebox.showerror("Error", "Invalid password.")
            else:
                messagebox.showerror("Error", "Invalid user.")
        else:
            messagebox.showerror("Error", "Information missing!")

    def display_login(self):
        self.pack(fill="both", expand=True)
        # self.configure(fg_color = "red")
        login_frame = ctk.CTkFrame(self, width=600, height=400)
        login_frame.pack(side="top", pady=100)

        label = ctk.CTkLabel(login_frame, text="Sign In")
        label.pack(padx=130, pady=10)

        self.fullname_entry = ctk.CTkEntry(login_frame, width=200, height=30, placeholder_text="Full_name")
        self.fullname_entry.pack(padx=10, pady=10)

        self.password_entry = ctk.CTkEntry(login_frame, width=200, height=30, placeholder_text="Password", show="*")
        self.password_entry.pack(padx=10, pady=10)

        login_button = ctk.CTkButton(login_frame, text='Sign in', width=200, cursor="hand2", command=self.login)
        login_button.pack(padx=10, pady=10)

        go_register_button = ctk.CTkButton(login_frame, text="Register", cursor="hand2", command=self.master.switch_to_register, fg_color="transparent")
        go_register_button.pack(padx=10, pady=50)

