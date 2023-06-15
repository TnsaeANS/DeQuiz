import tkinter as tk

def change_color():
    index = int(entry.get()) - 1
    if 0 <= index < len(buttons):
        buttons[index].config(bg="red")

root = tk.Tk()
root.title("Change Button Color")

buttons_frame = tk.Frame(root)
buttons_frame.pack()

buttons = []
for i in range(1, 4):
    button = tk.Button(buttons_frame, text="Button {}".format(i), width=10)
    button.pack(side="left", padx=5)
    buttons.append(button)

entry_frame = tk.Frame(root)
entry_frame.pack(pady=10)

entry_label = tk.Label(entry_frame, text="Enter a number (1-3):")
entry_label.pack(side="left")

entry = tk.Entry(entry_frame, width=5)
entry.pack(side="left")

change_button = tk.Button(root, text="Change Color", command=change_color)
change_button.pack()

root.mainloop()
