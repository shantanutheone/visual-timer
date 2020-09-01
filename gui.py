from tkinter import *
from PIL import ImageTk,Image
root = Tk()

root.title("Simple Calculator")
root.iconbitmap("blue.ico")

my_img = ImageTk.PhotoImage(Image.open("bluetooth.png"))
my_Label = Label(image = my_img)
my_Label.pack()

root.mainloop()