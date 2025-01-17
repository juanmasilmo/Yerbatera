from tkinter import *

root = Tk()

root.title("Distribuidora")
root.geometry("500x400")

lbl = Label(root,text="Este es el Label")
btn = Button(root,text="alta clientes")
btn.config(bg="white",fg="red")


lbl.pack()
btn.pack()







root.mainloop()