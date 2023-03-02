import tkinter as tk
import Qr_Code_Gen as Qgen
import Read_Qr_Code as Rcode
from tkinter import filedialog
import os


frame = tk.Tk()
frame.title("Decoder")
frame.geometry('250x150')

title = tk.Label(frame, text = "Binary Deconpiler", font=("Roboto", 20))
title.pack()
label_file = tk.Label(frame, text = "Path File")
label_file.pack(pady = 10)
def browseFile():
    label_done.config(text="Working...")
    file_path_variable = search_for_file_path()
    if not Rcode.main(file_path_variable):
        label_done.config(text="Fail..")
    else:
    	label_done.config(text="Done")
def search_for_file_path ():
    currdir = os.getcwd()
    tempdir = filedialog.askopenfilename(parent=frame, initialdir=currdir,filetypes =(('gif files','*.gif'),('jpeg files','*.jpg')), title='Please select a directory')
    if len(tempdir) > 0:
        print ("You chose: %s" % tempdir)
    return tempdir

printButton = tk.Button(frame,
						text = "Search",
						command = browseFile)
printButton.pack(pady = 5)

label_done = tk.Label(frame, text="")
label_done.pack(pady=5)

frame.mainloop()
