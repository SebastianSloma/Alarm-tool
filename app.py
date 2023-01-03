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

hour = Label(frame_body, text='hour', height=1,
             font=('Modern 10 bold'), bg='white')
hour.place(x=150, y=50)

c_hour = Combobox(frame_body, width=2, font=('modern 15'))
c_hour['values'] = ('00', '01', '02', '03', '04', '05',
                    '06', '07', '08', '09', '10', '11', '12')
c_hour.current(0)
c_hour.place(x=150, y=80)


min = Label(frame_body, text='minutes', height=1,
            font=('Modern 10 bold'), bg='white')
min.place(x=200, y=50)

c_min = Combobox(frame_body, width=2, font=('modern 15'))
c_min['values'] = ('00', '01', '02', '03', '04', '05',
                   '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51', '52', '52', '53', '54', '55', '56', '57', '58', '59')
c_min.current(0)
c_min.place(x=200, y=80)


sec = Label(frame_body, text='seconds', height=1,
            font=('Modern 10 bold'), bg='white')
sec.place(x=250, y=50)

c_sec = Combobox(frame_body, width=2, font=('modern 15'))
c_sec['values'] = ('00', '01', '02', '03', '04', '05',
                   '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51', '52', '52', '53', '54', '55', '56', '57', '58', '59')
c_sec.current(0)
c_sec.place(x=250, y=80)

window.mainloop()
