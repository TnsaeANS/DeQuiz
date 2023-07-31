import customtkinter as ctk
import _sqlite3
from tkinter import messagebox

class RegisterApp(ctk.CTkFrame):
    def __init__(self, master, db_conn):
        super().__init__(master)
        self.master = master

        self.conn = db_conn
        self.cur = self.conn.cursor()
        self.configure(fg_color = "#242424")    
        self.create_table()

        self.display_register()

    def create_table(self):
        self.cur.execute("""
            CREATE TABLE IF NOT EXISTS users(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            fullname VARCHAR(255) NOT NULL, 
            password VARCHAR(255) NOT NULL,
            is_teacher BIT)
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

    def display_register(self):
        self.pack(fill="both", expand=True)

        register_frame = ctk.CTkFrame(self, width=500, height=400)
        register_frame.pack(side="top", pady=100)

        label = ctk.CTkLabel(register_frame, text="Sign Up")
        label.pack(padx=130, pady=10)

        self.fullname_entry = ctk.CTkEntry(register_frame, width=200, height=30, placeholder_text="Full_name")
        self.fullname_entry.pack(padx=10, pady=10)

        self.password_entry = ctk.CTkEntry(register_frame, width=200, height=30, placeholder_text="Password", show="*")
        self.password_entry.pack(padx=10, pady=10)

        self.is_teacher_state = ctk.IntVar()
        teacher_checkbox = ctk.CTkCheckBox(register_frame, text="Teacher", variable=self.is_teacher_state)
        teacher_checkbox.pack(padx=10, pady=10)

        register_button = ctk.CTkButton(register_frame, text='Register', width=200, cursor="hand2", command=self.register)
        register_button.pack(padx=10, pady=10)

        go_login_button = ctk.CTkButton(register_frame, text="Sign in", cursor="hand2", command=self.master.switch_to_login, fg_color="transparent")
        go_login_button.pack(padx=10, pady=50)
