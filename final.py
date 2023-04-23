# Modified version of code basic.py with more added features like proper 
# error handling, a "Paste" button to paste text from clipboard, 
# "Copy" button to copy encrypted text to clipboard, 
# and a "Reset" button to clear input fields.
# Also added Comments to make the code more readable.


from tkinter import *
from tkinter import messagebox
import base64   # For encoding/decoding data to printable ASCII characters
import os     # Sometimes needed on lower versions of Python for copying/pasting and clearing screen.

def decrypt():
    password = code.get()

    # Check if password is correct
    if password == "1234": 
        # Create new window
        screen2 = Toplevel(screen) 
        screen2.title("Decryption") 
        screen2.geometry("400x200") 
        screen2.configure(bg="#00bd56")

        # Get message from input field
        message = text1.get(1.0, END) 
        
        # Decode message using base64
        decode_message = message.encode("ascii") 
        base64_bytes = base64.b64decode(decode_message) 
        decrypt = base64_bytes.decode("ascii")

        # Show decrypted message to new window
        Label(screen2, text="DECRYPT", font="arial", fg="white", bg="#00bd56").place(x=10, y=0) 
        text2 = Text(screen2, font="Roboto 10", bg="white", relief=GROOVE, wrap=WORD, bd=0) 
        text2.place(x=10, y=40, width=380, height=150)

        text2.insert(END, decrypt)
        
    # If password is empty, show error message
    elif password == "":
        messagebox.showerror("Decryption", "Input Password")

    # If password is incorrect, show error message
    elif password != "1234":
        messagebox.showerror("Decryption", "Invalid Password")

def encrypt():
    password = code.get()

    # Check if password is correct
    if password == "1234": 
        # Create new window
        screen1 = Toplevel(screen) 
        screen1.title("Encryption") 
        screen1.geometry("400x200") 
        screen1.configure(bg="#ed3833")

        # Get message from input field
        message = text1.get(1.0, END) 
        
        # Encode message using base64
        encode_message = message.encode("ascii") 
        base64_bytes = base64.b64encode(encode_message) 
        encrypt = base64_bytes.decode("ascii")

        # Show encrypted message to new window
        Label(screen1, text="ENCRYPT", font="arial", fg="white", bg="#ed3833").place(x=10, y=0) 
        text2 = Text(screen1, font="Roboto 10", bg="white", relief=GROOVE, wrap=WORD, bd=0) 
        text2.place(x=10, y=40, width=380, height=150)

        text2.insert(END, encrypt)

        # Function to copy encrypted message to clipboard
        def copy_text():
            screen1.clipboard_clear()
            screen1.clipboard_append(encrypt)
            messagebox.showinfo("Copy", "Text has been copied to clipboard.")

        Button(screen1, text="Copy", command=copy_text).place(x=180, y=10)

    # If password is empty, show error message
    elif password == "":
        messagebox.showerror("Encryption", "Input Password")

    # If password is incorrect, show error message
    elif password != "1234":
        messagebox.showerror("Encryption", "Invalid Password")

#Main Screen
def main_screen():
    # Declare global variables
    global screen 
    global code 
    global text1

# Create main window
screen=Tk()
# screen.geometry("375x398")
screen.geometry("388x398")

# Set window icon
image_icon=PhotoImage(file="keys.png") 
screen.iconphoto(False,image_icon) 
screen.title("MsgLock")

# Function to clear input fields
def reset():
    code.set("")
    text1.delete(1.0,END)

# Function to paste text from clipboard
def paste_text():
  text1.delete(1.0, END)
  text1.insert(INSERT, screen.clipboard_get())

# Added a "Paste" button to paste text from clipboard
Button(text="Paste", height="1", width="10", bg="#1089ff", fg="white", bd=0, command=paste_text).place(x=305, y=10)

# Added a label for text input
Label(text="Enter text for Encryption or Decryption", fg="black", font=("calbri",13)).place(x=10,y=10) 

# Added a text box for text input
text1=Text(font="Robote 20", bg="white", relief=GROOVE, wrap=WORD, bd=0) 
text1.place(x=10,y=50,width=355, height=100)

# Added a label for password input
Label(text="Enter secret key for encryption and decryption", fg="black", font=("calibri",13)).place(x=10,y=170)

# Added a password entry field for password input
code=StringVar()
Entry(textvariable=code,width=19, bd=0, font=("arial", 25), show="*").place(x=10,y=200)
      
# Add "ENCRYPT" button to encrypt text
Button(text="ENCRYPT", height="2",width=23, bg="#ed3833", fg="white", bd=0,command=encrypt).place(x=10, y=250)

# Add "DECRYPT" button to decrypt text
Button(text="DECRYPT", height="2",width=23, bg="#00bd56", fg="white", bd= 0,command=decrypt).place(x=200, y=250)

# Add "RESET" button to clear input fields
Button(text="RESET", height="2", width=50, bg="#1089ff", fg="white", bd=0,command=reset).place(x=10, y=300)

# Start the main event loop
screen.mainloop()

main_screen()