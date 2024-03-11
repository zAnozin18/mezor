import tkinter
a=tkinter.Tk()
a.title('bloknot')
a.geometry('500x500')
text=tkinter.Text(a, wrap='word', width=800 , height=500)
text.place(x=200 , y=200)

menu=tkinter.Menu(a)
a.configure(menu=menu)
filemenu=tkinter.Menu(menu)
menu.add_cascade(label='file', menu=filemenu)









a.mainloop()