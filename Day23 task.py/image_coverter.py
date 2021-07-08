import tkinter as imageConverter
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image

root= imageConverter.Tk()

canvas1 = imageConverter.Canvas(root, width = 300, height = 250, bg = 'white', relief = 'raised')
canvas1.pack()

label1 = imageConverter.Label(root, text='Basic Image converter\n App', bg = 'white')
label1.config(font=('avenir', 20))
canvas1.create_window(150, 60, window=label1)

def getJPEG ():
    global im1
    
    import_file_path = filedialog.askopenfilename()
    im1 = Image.open(import_file_path)
    
browse = imageConverter.Button(text="      Browse    ", command=getJPEG, bg='royalblue', fg='white', font=('avenir', 12, 'bold'))
canvas1.create_window(150, 130, window=browse)

def convertToPNG ():
    global im1
    
    export_file_path = filedialog.asksaveasfilename(defaultextension='.png')
    im1.save(export_file_path)

png= imageConverter.Button(text='Convert JPEG to PNG', command=convertToPNG, bg='royalblue', fg='white', font=('avenir', 12, 'bold'))
canvas1.create_window(150, 180, window=png)

root.mainloop()