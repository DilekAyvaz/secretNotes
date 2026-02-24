from email import message
from tkinter import *
from tkinter import messagebox
from cryptography.fernet import Fernet
import base64
import hashlib


def get_fernet_key(master_secret: str) -> bytes:
    # Şifreyi 32 bayta sabitle (Fernet için uygun anahtar üretir)
    digest = hashlib.sha256(master_secret.encode()).digest()
    return base64.urlsafe_b64encode(digest)

def decrypt_pasted_message():
    master_secret = master_secret_input.get().strip()
    token = encrypted_text.get("1.0", "end").strip()  # gAAAAA... gibi

    if not master_secret or not token:
        messagebox.showwarning("Error!", "Enter master key and paste encrypted message.")
        return

    try:
        f = Fernet(get_fernet_key(master_secret))
        plaintext = f.decrypt(token.encode()).decode()
#       
#        title ve secret'ı ayır
        title, message = plaintext.split("\n", 1) if "\n" in plaintext else (plaintext, "")

        # title alanını doldur
        title_entry.delete(0, "end")
        title_entry.insert(0, title)

        # secret alanını doldur
        input_text.delete("1.0", "end")
        input_text.insert("1.0", message)


    except Exception:
        messagebox.showerror("Decrypt Error", "Wrong key or invalid encrypted message.")

def save_and_encrypt_notes():
    title= title_entry.get()
    message= input_text.get("1.0","end").strip()
    master_secret = master_secret_input.get().strip()

    if len(title)==0 or len(message)==0 or len(master_secret)==0:
        messagebox.showwarning(title="Error!",message="Please enter your all info.")
        return
    else:
        key = get_fernet_key(master_secret)
        f = Fernet(key)
        combined = f"{title}\n{message}"
        encrypted = f.encrypt(combined.encode())

    with open("mysecret.txt", "ab") as data_file:
        data_file.write(encrypted + b"\n")

    title_entry.delete(0, "end")
    input_text.delete("1.0", "end")
    master_secret_input.delete(0, "end")
    messagebox.showinfo("Saved", "Note encrypted and saved.")

def decrypt_notes():
    master_secret = master_secret_input.get().strip()
    if not master_secret:
        messagebox.showwarning(title="Error!", message="Enter master key to decrypt.")
        return

    try:
        key = get_fernet_key(master_secret)
        f = Fernet(key)
        with open("mysecret.txt", "rb") as data_file:
            content = data_file.read()
        if not content.strip():
            messagebox.showinfo("Decrypt", "No saved notes.")
            return

        lines = content.split(b"\n")
        decrypted_list = []
        for line in lines:
            if not line:
                continue
            try:
                decrypted = f.decrypt(line)
                decrypted_list.append(decrypted.decode())
            except Exception:
                pass
        if not decrypted_list:
            messagebox.showerror("Decrypt Error", "Wrong key or no notes with this key.")
        else:
            messagebox.showinfo("Decrypted Notes", "\n\n---\n\n".join(decrypted_list))

    except FileNotFoundError:
       messagebox.showinfo("Decrypt", "No saved notes.")
    except Exception:
       messagebox.showerror("Decrypt Error", "Wrong key or invalid data.")

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

input_text = Text(width=40,height=10)
input_text.pack()

master_secret_label = Label(text="Enter master key",font=FONT)
master_secret_label.pack()

master_secret_input= Entry(width=20,show="*")
master_secret_input.pack()

encrypted_label = Label(text="Paste encrypted message", font=FONT)
encrypted_label.pack()

encrypted_text = Text(width=40, height=4)
encrypted_text.pack()

save_button = Button(text="Save & Encrypt" , command=save_and_encrypt_notes)
save_button.pack()

decrypt_button =Button(text="Decrypt",command=decrypt_pasted_message)
decrypt_button.pack()

window.mainloop()