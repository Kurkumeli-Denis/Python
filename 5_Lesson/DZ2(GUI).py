# TKinter

from tkinter import*


window = Tk()  
window.title("Крестики - Нолики")  
window.geometry('800x450')  
window.config(bg = '#FFA500')
  
btn = Button(window, text="Начать!", activeforeground='white')  
btn.grid(column = 0, row = 0)  
btn.place(height = 100, width = 300, anchor="c", relx = .5, rely = .5)
btn.config(fg = 'black')
window.mainloop()
