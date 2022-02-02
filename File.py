from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
import os

root = Tk()
root.title("Notepad Editor")
root.minsize(650,650)
root.maxsize(650,650)

openImg = ImageTk.PhotoImage(Image.open("open.png"))
saveImg = ImageTk.PhotoImage(Image.open("save.png"))
exitImg = ImageTk.PhotoImage(Image.open("exit.jpg"))

label_file_name = Label(root,text="File name:")
label_file_name.place(relx=0.28,rely=0.03,anchor=CENTER)

input_file_name = Entry(root)
input_file_name.place(relx=0.46,rely=0.03,anchor=CENTER)

textInput = Text(root, height=35,width=80)
textInput.place(relx=0.5,rely=0.55,anchor=CENTER)



name = ""
def openfile():
    global name
    textInput.delete(1.0,END)
    input_file_name.delete(0,END)
    text_file = filedialog.askopenfilename(title=" Open Text File", filetypes=(("Text Files", "*.txt"),))
    print(text_file)
    name = os.path.basename(text_file)
    
    formatted_name = name.split(".")[0]
    input_file_name.insert(END, formatted_name)
    root.title(formatted_name)
    text_file = open(name, 'r')
    paragraph = text_file.read()
    textInput.insert(END, paragraph)
    text_file.close()

openBtn = Button(root, image = openImg, text="Open File", command=openfile)
openBtn.place(relx=0.05,rely=0.03,anchor=CENTER)

"""saveBtn = Button(root, image = saveImg, text="Save File")
saveBtn.place(relx=0.11, rely=0.03,anchor=CENTER)

exitBtn = Button(root, image = exitImg, text="Exit File")
exitBtn.place(relx=0.17, rely=0.03,anchor=CENTER)"""

root.mainloop()