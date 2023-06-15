import customtkinter as ctk
import _sqlite3
from tkinter import *
from tkinter import messagebox

#subprocess for opening other files
import os
import subprocess

current_dir = os.path.dirname(os.path.abspath(__file__))

quiz_display_path = os.path.join(current_dir, "..", "interface_quiz_display.py")
add_display_path = os.path.join(current_dir, "..", "interface_add_quiz.py") 

# the screen
login_page = ctk.CTk()
login_page.title("Login")
login_page.geometry("800x800")

conn = _sqlite3.connect('data.db')
cur = conn.cursor()

cur.execute("""
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        fullname VARCHAR(255) NOT NULL, 
        password VARCHAR(255) NOT NULL,
        is_teacher BIT
    )
""")

def register():
    # Get the values entered by the user in the GUI entry fields
    fullname = fullname_entry.get()
    password = password_entry.get()
    is_teacher = is_teacher_state.get()

    # Check if both fullname and password are provided
    if fullname !="" and password !="":
        print(is_teacher)
        # Execute a SQL SELECT statement to check if the fullname already exists in the database
        cur.execute("SELECT fullname FROM users WHERE fullname=?", [fullname])
        # If the fullname already exists, display an error message
        if cur.fetchone() is not None:
            messagebox.showerror("Error", "Name already Exists.")
        # If the fullname does not exist, execute a SQL INSERT statement to add the user to the database
        else:
            cur.execute("INSERT INTO users (fullname, password, is_teacher) VALUES (?, ?, ?)", (fullname,password,is_teacher))
            conn.commit()
            # Display a success message
            messagebox.showinfo("Success", "Your Account is Created")
    # If either fullname or password is missing, display an error message
    else:
        messagebox.showerror("Error", "Information Missing!")
        
def login():
    fullname = fullname_entry2.get()
    password = password_entry2.get()
    is_teacher = is_teacher_state.get()

    if fullname !="" and password !="":
        cur.execute("SELECT password FROM users WHERE fullname=?", [fullname])
        result = cur.fetchone()
        if result :
            print(result[0], password)
            if result[0] == password:
                messagebox.showinfo("Success", "Logged IN")

                #checking if teacher
                cur.execute("SELECT is_teacher FROM users WHERE fullname=?", [fullname])
                is_result = cur.fetchone()
                print(is_result[0])

                if is_result[0] == 1:
                    #teacher things
                        #close this interface
                    login_page.withdraw()
                    #open the quiz display
                    quiz_process = subprocess.Popen(["python", add_display_path]) 
                     # wait for the quiz process to finish
                    stdout, stderr = quiz_process.communicate()           
                    login_page.deiconify()   
                if is_result[0] == 0:                   
                    #close this interface
                    login_page.withdraw()
                    #open the quiz display
                    quiz_process = subprocess.Popen(["python", quiz_display_path]) 
                     # wait for the quiz process to finish
                    stdout, stderr = quiz_process.communicate()           
                    login_page.deiconify()    
                else:
                    print("something's wrong")
         

                     
            else:
                messagebox.showerror("Error", "Invalid pd")
        else:
             messagebox.showerror("Error", "Invalid user")
    else:
        messagebox.showerror("Error", "Information Missing!")


login_frame = None
register_frame = None 

is_teacher_state = None
        
def display_login():
    global register_frame
    if register_frame:
        register_frame.destroy()


    global login_frame
    login_frame = ctk.CTkFrame(login_page) 
    login_frame.pack() 

    login_label = ctk.CTkLabel(login_frame,  text = "Sign In")
    login_label.pack( padx = 10, pady=10)

    global fullname_entry2
    global password_entry2

    fullname_entry2 = ctk.CTkEntry(login_frame, width=200, height=30, placeholder_text="Full_name")
    fullname_entry2.pack(padx = 10, pady=10)

    password_entry2 = ctk.CTkEntry(login_frame, width=200, height=30, placeholder_text="Password", show = "*")
    password_entry2.pack(padx = 10, pady=10)  
    
    login_button = ctk.CTkButton(login_frame, text='Sign in', width=200, cursor = "hand2", hover_color = "blue", command=login)
    login_button.pack(padx = 10, pady = 10)

    go_signin_label = ctk.CTkButton(login_frame,  text = "Register", cursor = "hand2", hover_color = "blue", command=display_register)
    go_signin_label.pack(padx = 10, pady=50)

def display_register():

    global login_frame  # use the global keyword to access the global login_frame variable
    if login_frame:
        login_frame.destroy()

    global register_frame  # use the global keyword to access the global register_frame variable
    register_frame = ctk.CTkFrame(login_page) 
    register_frame.pack() 


    signup_label = ctk.CTkLabel(register_frame,  text = "Create An Account")
    signup_label.pack( padx = 10, pady=10)

    fullname_entry = ctk.CTkEntry(register_frame, width=200, height=30, placeholder_text="Full_name")
    fullname_entry.pack(padx = 10, pady=5)

    password_entry = ctk.CTkEntry(register_frame, width=200, height=30, placeholder_text="Password", show = "*")
    password_entry.pack(padx = 10, pady=5)

    global is_teacher_state
    is_teacher_state = ctk.IntVar()
    teacher_btn = ctk.CTkCheckBox(register_frame, text="Teacher", variable=is_teacher_state)
    teacher_btn.pack(padx = 10, pady = 5)

    register_button = ctk.CTkButton(register_frame, text='Register', width=200, cursor = "hand2", hover_color = "blue", command=register)
    register_button.pack(padx = 10, pady = 10)

    go_signin_label = ctk.CTkButton(register_frame,  text = "Already have an account?", cursor = "hand2", hover_color = "blue", command=display_login)
    go_signin_label.pack(padx = 10, pady=80)


display_register()
login_page.mainloop()

def mo():
    print("moooo")

