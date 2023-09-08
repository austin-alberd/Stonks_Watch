#imports 
import tkinter
import customtkinter
import scraper,pull_from_db


#window setup
app =customtkinter.CTk()
app.title("STONKS WATCH")
app.geometry("400x555")

#functions
def pull_data():
    pass

#init frames
options_frame= customtkinter.CTkFrame(app,height=500,bg_color="white")
options_frame.grid(row=1,column=0)

#layout work and MAKE it PRETTY
title_label= customtkinter.CTkLabel(app,text="Stonks Watch")
title_label.grid(row=0, column=0)

pull_data_button = customtkinter.CTkButton(options_frame,text="Pull Data",command=pull_data)
pull_data_button.grid(row=0,column=0)

#app main loop no touch
app.mainloop()