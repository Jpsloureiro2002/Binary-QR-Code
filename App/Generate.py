import tkinter as tk
import Qr_Code_Gen as Qgen
import Read_Qr_Code as Rcode

# Top level window
frame = tk.Tk()
frame.title("Binary Image Creator")
frame.geometry('500x300')
# Function for getting Input
# from textbox and printing it
# at label widget

def printInput():
	filename = inputtxt.get(1.0, "end-1c")
	content = ritch.get(1.0, "end-1c")
	content = content.replace("\n", "&")
	content = content.replace("\t", "$")
	print(content)
	gen = Qgen.main(content,filename)
	if gen:
		label_confirm.config(text="Done")
	pass

# TextBox Creation
label_file = tk.Label(frame, text = "Nome do Ficheiro")
label_file.pack()

inputtxt = tk.Text(frame,
				height = 1,
				width = 40)

inputtxt.pack()

label_Content = tk.Label(frame, text = "Conteudo")
label_Content.pack()

ritch = tk.Text(frame,
				height = 10,
				width = 50)
ritch.pack()
# Button Creation
printButton = tk.Button(frame,
						text = "Gerar",
						command = printInput)
printButton.pack()

label_confirm = tk.Label(frame, text="")
label_confirm.pack()
frame.mainloop()
