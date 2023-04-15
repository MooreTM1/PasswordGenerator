# Generate unique password

from tkinter import *
from random import randint

root = Tk()
root.title('Custom Password Generator')
root.geometry("500x300")

my_password = chr(randint(10, 126))

# Generate random password
def new_rand():
    # Clear Entry Box
    pw_entry.delete(0, END)

    # Get Password length and convert to integer
    pw_length = int(my_entry.get())

    # Create variable to hold password
    my_password = ''

    # Loop password length
    for x in range(pw_length):
        my_password += chr(randint(33, 126))

    # Output password
    pw_entry.insert(0, my_password)

# Copy to clipboard
def clipper():
    # Clear clipboard
    root.clipboard_clear()
    # Copy to clipboard
    root.clipboard_append(pw_entry.get())

# Frame Label
lf = LabelFrame(root, text="How many characters?")
lf.pack(pady=20)

# Entry Box for characters
my_entry = Entry(lf, font=("Times New Roman", 24))
my_entry.pack(pady=20, padx=20)


# Entry Box for returned password
pw_entry = Entry(root, text='', font=("Times New Roman", 24), bd=0, bg="white")
pw_entry.pack(pady=20)

# Create frame for buttons
my_frame = Frame(root)
my_frame.pack(pady=20)

# Create buttons
my_button = Button(my_frame, text="Generate Password", command=new_rand)
my_button.grid(row=0, column=0, padx=10)

clip_button = Button(my_frame, text="Copy to Clipboard", command=clipper)
clip_button.grid(row=0, column=1, padx=10)

root.mainloop()
