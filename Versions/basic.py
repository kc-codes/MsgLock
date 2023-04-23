# Importing modules
from tkinter import *
import base64

# Creating window
window = Tk()
window.title("Message Encryption Decryption")
window.geometry("700x350")

# Creating input and output components
text = StringVar()
key = StringVar()
result = StringVar()

text_label = Label(window, text="Enter the message:", font=("Calibri", 12))
text_label.pack()
text_entry = Entry(window, textvariable=text)
text_entry.pack()

key_label = Label(window, text="Enter the key:", font=("Calibri", 12))
key_label.pack()
key_entry = Entry(window, textvariable=key)
key_entry.pack()

result_label = Label(window, text="Result:", font=("Calibri", 12))
result_label.pack()
result_entry = Entry(window, textvariable=result)
result_entry.pack()

# Defining encryption function
def encrypt():
    # Getting input values
    message = text.get()
    secret_key = key.get()

    # Encoding message using base64 and key
    encoded_message = []
    for i in range(len(message)):
        key_char = secret_key[i % len(secret_key)]
        encoded_char = chr((ord(message[i]) + ord(key_char)) % 256)
        encoded_message.append(encoded_char)

    # Converting list to string and displaying result
    encrypted_message = base64.urlsafe_b64encode("".join(encoded_message).encode()).decode()
    result.set(encrypted_message)

# Defining decryption function
def decrypt():
    # Getting input values
    encrypted_message = text.get()
    secret_key = key.get()

    # Decoding message using base64 and key
    decoded_message = base64.urlsafe_b64decode(encrypted_message).decode()
    decrypted_message = []
    for i in range(len(decoded_message)):
        key_char = secret_key[i % len(secret_key)]
        decrypted_char= chr((256 + ord(decoded_message[i]) - ord(key_char)) % 256)
        decrypted_message.append(decrypted_char)

     # Converting list to string and displaying result   
    original_message= "".join(decrypted_message)
    result.set(original_message)

# Creating buttons for encryption and decryption
encrypt_button= Button(window,text="Encrypt",command=encrypt,bg="pink")
encrypt_button.pack()

decrypt_button= Button(window,text="Decrypt",command=decrypt,bg="pink")
decrypt_button.pack()

# Running main loop
window.mainloop() 