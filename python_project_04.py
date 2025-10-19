#create a new phone website

import io
import webbrowser
import requests
from tkinter import *
from urllib.request import urlopen
from PIL import ImageTk,Image


class NewsApp:

    def __init__(self):

        self.data = requests.get('https://newsdata.io/api/1/latest?apikey=pub_503ff8f4dd794227911e98624c2c3876&q=pizza').json()
                            

        self.load_gui()
 
        self.load_news_item(0)



    def load_gui(self):
        self.root = Tk()
        self.root.geometry('350x600')
        self.root.resizable(0, 0)
        self.root.configure(background = 'black')

    def clear(self):
        for i in self.root.pack_slaves():
            i.destroy()

    def load_news_item(self, index):
        self.clear()

        try:
            url_image = self.data['results'][index]['image_url']
            row_data = urlopen(url_image).read()
            im = Image.open(io. BytesIO(row_data)).resize((350,250))
            photo = ImageTk.PhotoImage(im)
        except:
            url_image = 'https://wurth.ua/themes/demo/assets/img/default-product-image.jpg'
            row_data = urlopen(url_image).read()
            im = Image.open(io. BytesIO(row_data)).resize((350,250))
            photo = ImageTk.PhotoImage(im)

        label = Label(self.root, image= photo) 
        label.pack()

    


        heading = Label(self.root, text= self.data['results'][index]['title'], bg= 'black', fg= 'white', wraplength= 350, justify= 'center')
        heading.pack(pady= (10, 20))
        heading.config(font= ('verdana', 15))

        details = Label(self.root, text= self.data['results'][index]['description'], bg= 'black', fg= 'white', wraplength= 350, justify= 'center')
        details.pack(pady= (2, 20))
        details.config(font= ('verdana', 12))

        frame = Frame(self.root, bg= 'black')
        frame.pack(expand= True, fill= BOTH)

        if index != 0:
            prev = Button(frame, text='Prev', width= 16, height= 3, command= lambda :self.load_news_item(index -1))
            prev.pack(side= LEFT)

        read_btn = Button(frame, text='Read more', width= 16, height= 3, command= lambda :self.open_link(self.data['results'][index]['url']))
        read_btn.pack(side= LEFT)

        if index != len(self.data['results'])-1:
            next_btn = Button(frame, text='Next', width= 16, height= 3, command= lambda :self.load_news_item(index + 1))  
            next_btn.pack(side= LEFT)
         
        self.root.mainloop()   
    
    def open_link(self, url):
        webbrowser.open(url) 



ovj = NewsApp()   
