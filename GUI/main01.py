import tkinter as tk



root=tk.Tk()
root.title("prakashman Singh")
root.geometry("600x400")

def on_button_click():
    label.config(text="buttom clicked")
    
label = tk.Label(root, text ="welcome")
label.pack(pady=20)

buttom = tk.Button(root, text ="click me" , command= on_button_click) 
buttom.pack(pady=10)   

root.mainloop()
