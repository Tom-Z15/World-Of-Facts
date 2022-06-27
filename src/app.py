from tkinter import *
import tkinter.colorchooser
import main


root = Tk(className="Świat ciekawostek")
root.config(bg='black')


fore_ground = "white"
back_ground = "grey"


# Pasek inputu
bar = Label(root, width=40, height= 10, borderwidth=5, bg="grey", fg="black", wraplength=100)
bar.grid(row=1, column=60, columnspan=3, padx=10, pady=10)


def set_text(text):
    bar.config(text=text)


# Buttony
button_dogs = Button(root, text="dogs", pady=50, padx=70,
                     fg=fore_ground, bg=back_ground, command=lambda: set_text(main.get_api('dogs').get_json()['facts'][0]))
button_cats = Button(root, text="cats", pady=50, padx=70,
                     fg=fore_ground, bg=back_ground, command=lambda: set_text(main.get_api('cats').get_json()['fact']))


"""
button_ = Button(root, text="", pady=50, padx=70,fg=fore_ground, bg=back_ground)
button_ = Button(root, text="", pady=50, padx=70,fg=fore_ground, bg=back_ground)
button_ = Button(root, text="", pady=50, padx=70,fg=fore_ground, bg=back_ground)
button_ = Button(root, text="", pady=50, padx=70,fg=fore_ground, bg=back_ground)
"""


button_dogs.grid(row=0, column=30)
button_cats.grid(row=1, column=30)


root.mainloop()
