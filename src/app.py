from tkinter import *
import tkinter.colorchooser
import main


root = Tk(className="Świat ciekawostek")
root.config(bg='black')


fore_ground = "white"
back_ground = "grey"


# Pasek inputu
bar = Label(root, width=40, height= 10, borderwidth=5, bg="grey", fg="black", wraplength=100)
bar.grid(row=1, column=60, columnspan=3)


def set_text(text):
    bar.config(text=text)


# Buttony
button_dogs = Button(root, text="dogs", pady=50, padx=70,
                     fg=fore_ground, bg=back_ground, command=lambda: set_text(main.get_api('dogs').get_json()['facts'][0]))

button_cats = Button(root, text="cats", pady=50, padx=70,
                     fg=fore_ground, bg=back_ground, command=lambda: set_text(main.get_api('cats').get_json()
                     ['fact']))


button_chuck_norris = Button(root, text="Chuck Norris", pady=50, padx=70, fg=fore_ground, bg=back_ground, command=lambda: set_text(main.get_api('chuck norris').get_json()
                     ['value']))
"""
button_ = Button(root, text="", pady=50, padx=70,fg=fore_ground, bg=back_ground)
button_ = Button(root, text="", pady=50, padx=70,fg=fore_ground, bg=back_ground)
button_ = Button(root, text="", pady=50, padx=70,fg=fore_ground, bg=back_ground)
button_ = Button(root, text="", pady=50, padx=70,fg=fore_ground, bg=back_ground)
"""


button_dogs.grid(row=0, column=1)
button_cats.grid(row=1, column=1)
button_chuck_norris.grid(row=2, column=1)


root.mainloop()
