from tkinter import *

def main():

    #these are the global variables that are used
    global main_window
    global customer_details, entry_name,entry_receipt,entry_item,entry_quantity, total_entries

    #create empty list for camp details and empty variable for entries in the list
    customer_details = []
    total_entries = 0

    #create the GUI and start it up
    main_window = Tk()

    main_window.title("Tracking Program")

    main_window.mainloop()
   
   
main()