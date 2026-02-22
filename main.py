from tkinter import *
from tkinter import messagebox
from turtle import end_fill


def save_and_encrypt_notes():
    title= title_entry.get()
    message= input_text.get("1.0","end")
    master_secret = master_secret_input.get()

    if len(title)==0 or len(message)==0 or len(master_secret)==0:
        messagebox.showwarning(title="Error!",message="Please enter your all info.")
    else:
        #encr
        
            with open("mysecret.txt" ,"a") as data_file:
                data_file.write(f"\n{title}\n{message}")
            title_entry.delete(0, "end")
            input_text.delete("1.0", "end")
            master_secret_input.delete(0,"end")


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