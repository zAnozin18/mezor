import tkinter

window = tkinter.Tk()
window.title("calculator")
window.geometry("500x500")
window.configure(bg="black")


def qwert():
    num1=int("введите текст")
    return num1


def qwert1():
    num2 = text2.get()
    num2 = int(num2)
    return num2


def qwert3(resoulte):
    answer.delete(0, "end")
    answer.insert(0, resoulte)


def ad():
    num1 = qwert()
    num2 = qwert1()
    resoulte = num1 + num2
    qwert3(resoulte)


def ad1():
    num1 = qwert()
    num2 = qwert1()
    resoulte = num1 - num2
    qwert3(resoulte)


def ad2():
    num1 = qwert()
    num2 = qwert1()
    resoulte = num1 * num2
    qwert3(resoulte)


def ad3():
    num1 = qwert()
    num2 = qwert1()
    resoulte = num1 / num2
    qwert3(resoulte)


buttom_text = tkinter.Label(window, text="chislo 2")
buttom_text.place(x=1, y=100)


buttom_text1=tkinter.Label(window, text="chislo 1" , bg='blue')
buttom_text1.place(x=1, y=50)


buttom_add = tkinter.Button(window, text="+", command=ad, fg='blue')
buttom_add.place(x=20, y=250)

buttom_sub = tkinter.Button(window, text="-", command=ad1)
buttom_sub.place(x=100, y=250)

buttom_1 = tkinter.Button(window, text="*", command=ad2)
buttom_1.place(x=70, y=250)

buttom_2 = tkinter.Button(window, text='/', command=ad3)
buttom_2.place(x=180, y=250)

text1 = tkinter.Entry(window, width=20)
text1.place(x=120, y=50)

text2 = tkinter.Entry(window, width=20)
text2.place(x=120, y=100)
answer = tkinter.Entry(window, width=40)
answer.place(x=120, y=10)

window.mainloop()
