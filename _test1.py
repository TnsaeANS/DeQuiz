import tkinter as tk
from tkinter import messagebox
import os
window = tk.Tk()

def delete_file(file_path):
    # Delete the file
    os.remove(file_path)
    messagebox.showinfo("Success", "File deleted successfully.")

def delete_selected_file():
    # Get the selected file from the listbox
    selected_file = file_listbox.get(file_listbox.curselection())
    # Construct the full file path
    file_path = os.path.join(directory_path, selected_file)
    # Call the delete_file function
    delete_file(file_path)


# Create a listbox to display the files
file_listbox = tk.Listbox(window)
file_listbox.pack()

# Function to populate the listbox with files in a directory
def load_files(directory):
    file_listbox.delete(0, tk.END)  # Clear the listbox
    files = os.listdir(directory)
    for file in files:
        file_listbox.insert(tk.END, file)

# Set the directory path
directory_path = '/path/to/directory'
load_files(directory_path)  # Load the initial files

# Create a button to delete the selected file
delete_button = tk.Button(window, text="Delete", command=delete_selected_file)
delete_button.pack()

window.mainloop()
