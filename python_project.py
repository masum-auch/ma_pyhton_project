#create login interface

from tkinter import *
# from PIL import ImageTk, Image
from tkinter import messagebox


def log_handle():
    email = email_input.get()
    password = Password_input.get()

    if email == 'masumpl@gmail.com' and password == '1234':
        messagebox.showinfo('Box', 'Login_Successfully')
    else:
        messagebox.showinfo('Login Fild')



root = Tk()

root.title("Login From File") 
 
root.iconbitmap('favicon.ico') 

root.geometry('350x500')

root.configure(background= '#9b59b6')
# Img = ImageTk.PhotoImage(Image.open(file="fipkart_images.png"))
# ima_label = Label(root, Image= img)


text_lable = Label(root, text= 'Fipkart', fg= 'white', bg= '#9b59b6')
text_lable.pack(pady= (10, 10))
text_lable.config(font= ('verdana', 14))

email_label = Label(root, text= 'Enter Email', fg= 'white', bg= '#9b59b6')
email_label.pack(pady= (20, 5))
email_label.config(font= ('verdana', 14))

email_input = Entry(root, width= 50)
email_input.pack(ipadx= 6, pady= (1, 15))

Password_label = Label(root, text= 'Enter Password', fg= 'white', bg= '#9b59b6')
Password_label.pack()
Password_label.config(font= ('verdana', 14))

Password_input = Entry(root, width= 50)
Password_input.pack(ipadx= 6, pady= (1, 15))

log_button = Button(root, text= 'Login', fg= 'white', bg= '#0096DC', width= '14', height= '1', command= log_handle)
log_button.pack(pady= (10, 20))
log_button.config(font= ('verdana', 13))

root.mainloop()    