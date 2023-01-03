# import library
from tkinter.ttk import *
from tkinter import *
from PIL import ImageTk, Image

# window
window = Tk()
window.title('')
window.geometry('350x200')
window.configure(bg='grey')

# up frames
frame_line = Frame(window, width=400, height=5)
frame_line.grid(row=0, column=0)

frame_body = Frame(window, width=400, height=290, bg='blue')
frame_body.grid(row=1, column=0)

# body frame
img = Image.open('bell.png')
img.resize((100, 100))
img = ImageTk.PhotoImage(img)

app_image = Label(frame_body, height=100, image=img)
app_image.place(x=10, y=10)

name = Label(frame_body, text='Alarm', height=1,
             font=('Modern 20 bold'), bg='white')
name.place(x=150, y=10)


window.mainloop()
