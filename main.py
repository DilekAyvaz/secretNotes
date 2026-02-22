from tkinter import *
from tkinter import messagebox
from cryptography.fernet import Fernet

def load_key():
    """
    Load the previously generated key
    """
    return open("secret.key", "rb").read()

def decrypt_message(encrypted_message):
    """
    Decrypts an encrypted message
    """
    key = load_key()
    f = Fernet(key)
    decrypted_message = f.decrypt(encrypted_message)

    print(decrypted_message.decode())

if __name__ == "__main__":
    decrypt_message(b'gAAAAABgLX7Zj-kn-We2BI_c9NQhEtfJEnHUVhVqtiqjkDi5dgJafj-_8QUDyeNS2zsJTdBWg6SntRJOjOM1U5mIxxsGny7IEGqpVVdHwheTnwzSBlgpb80=')



def save_and_encrypt_notes():
    title= title_entry.get()
    message= input_text.get("1.0","end")
    master_secret = master_secret_input.get()

    if len(title)==0 or len(message)==0 or len(master_secret)==0:
        messagebox.showwarning(title="Error!",message="Please enter your all info.")
    else:
        # TODO: Encrypt message with master_secret before saving
        with open("mysecret.txt", "a") as data_file:
            data_file.write(f"\n{title}\n{message}")
        title_entry.delete(0, "end")
        input_text.delete("1.0", "end")
        master_secret_input.delete(0, "end")


FONT = ("Zapfino",20,"italic")
window = Tk()
window.title("Secret Notes")
window.config(padx=10 ,pady=10)

#UI

photo= PhotoImage(file="topsecret.png")
photo= photo.subsample(4,4)
photo_label = Label(image=photo)
photo_label.pack()


title_info_label = Label(text="Enter your title",font=FONT)
title_info_label.pack()

title_entry=Entry(width=30)
title_entry.pack()

input_info_label = Label(text="Enter your secret",font=FONT)
input_info_label.pack()

input_text = Text()
input_text.pack()

master_secret_label = Label(text="Enter master key",font=FONT)
master_secret_label.pack()

master_secret_input= Entry(width=20)
master_secret_input.pack()

save_button = Button(text="Save & Encrypt" , command=save_and_encrypt_notes)
save_button.pack()

decrypt_button =Button(text="Decrypt")
decrypt_button.pack()


window.mainloop()