from doctest import master
from tkinter import *


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

save_button = Button(text="Save & Encrypt")
save_button.pack()

decrypt_button =Button(text="Decrypt")
decrypt_button.pack()


window.mainloop()