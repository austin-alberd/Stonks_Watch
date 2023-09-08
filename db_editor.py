#Library imports
import sqlite3, db_init
import tkinter,customtkinter

#make the database if it is not made yet
db_init.init_db()

#setup connection and cursor
con =sqlite3.connect("portfolio.db")
cur = con.cursor()

#Window Setup
window = customtkinter.CTk()
window.geometry("400x500")
window.title("Portfolio Builder")

#functions
def add_to_db():
    try:
        exchange=exchange_input_box.get("0.0","end")
        ticker=ticker_input_box.get("0.0","end")
        shares = shares_input_box.get("0.0","end")
        cur.execute(f""" 
        INSERT INTO portfolio VALUES
            ("{ticker}","{exchange}","{shares}")
        """)
        con.commit()
        print(f"successfuly added the current values: Ticker:{ticker}  Exchange:{exchange}   Shares:{shares}")
    except:
        print("Aw Shucks an error occoured")
#whacky widgets
#ticker input 
ticker_input_box = customtkinter.CTkTextbox(window,height=25)
ticker_input_box.grid(column=1,row=0)
ticker_prompt_label= customtkinter.CTkLabel(window,text="Input the ticker!   ")
ticker_prompt_label.grid(column=0,row=0)

#exchange input
exchange_input_box = customtkinter.CTkTextbox(window,height=25)
exchange_input_box.grid(column=1,row=1)
exchange_prompt_label= customtkinter.CTkLabel(window,text="Input the exchange!   ")
exchange_prompt_label.grid(column=0,row=1)

#shares input
shares_input_box = customtkinter.CTkTextbox(window,height=25)
shares_input_box.grid(column=1,row=2)
shares_prompt_label= customtkinter.CTkLabel(window,text="Input the number of shares!   ")
shares_prompt_label.grid(column=0,row=2)

#submit changes button
submit_button = customtkinter.CTkButton(window,text="Submit Changes",command=add_to_db)
submit_button.grid(column=0,row=3)

#main looop
window.mainloop()