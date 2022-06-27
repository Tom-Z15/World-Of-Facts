from tkinter import *
import tkinter.colorchooser


root = Tk(className="Świat ciekawostek")
root.configure(bg='black')


fore_ground = "white"
back_ground = "grey"


button_dogs = Button(root, text="dogs", pady=50, padx=70,
                     fg=fore_ground, bg=back_ground)
button_cats = Button(root, text="cats", pady=50, padx=70,
                     fg=fore_ground, bg=back_ground)


"""
button_ = Button(root, text="", pady=50, padx=70,fg=fore_ground, bg=back_ground)
button_ = Button(root, text="", pady=50, padx=70,fg=fore_ground, bg=back_ground)
button_ = Button(root, text="", pady=50, padx=70,fg=fore_ground, bg=back_ground)
button_ = Button(root, text="", pady=50, padx=70,fg=fore_ground, bg=back_ground)
"""


button_dogs.grid(row=0, column=30)
button_cats.grid(row=1, column=30)
root.mainloop()
