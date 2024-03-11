import tkinter as tk

window = tk.Tk()
window.title("Мой блокнот")
window.geometry("400x400")

content_text = tk.Text(window, wrap="word")
content_text.place(x=0, y=0, relwidth=1, relheight=1)

main_menu = tk.Menu(window)
window.configure(menu=main_menu)

buttom=tk.Button(window, text="+")
buttom.place(x=10, y=12)

buttom1=tk.Button(window, text="-")
buttom1.place(x=19 , y=12)

file_menu = tk.Menu(main_menu)
main_menu.add_cascade(label="Файл", menu=file_menu)
new_file_icon = tk.PhotoImage(file="new_file.gif")
open_file_icon = tk.PhotoImage(file="open_file.gif")
save_file_icon = tk.PhotoImage(file="save_file.gif")

file_menu.add_command(label="Новый", image=new_file_icon, compound="left")
file_menu.add_command(label="Открыть", image=open_file_icon, compound="left")
file_menu.add_command(label="Сохранить", image=save_file_icon, compound="left")

window.mainloop()
