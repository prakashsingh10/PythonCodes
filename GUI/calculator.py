import tkinter as tk
from tkinter import messagebox

def get_sum():
    value1 = float(entry1.get())
    value2 = float(entry2.get())
    
    reasult = value1+ value2
    messagebox.showinfo("reasult", f"the sum is {reasult}")

root = tk.Tk()
root.title("PM claculator")
root.geometry("700x200")

label1 = tk.Label(root, text="enter the first number :")
label1.pack(pady=5)
entry1 = tk.Entry(root)
entry1.pack(pady=5)


label2 = tk.Label(root, text="enter the second  number :")
label2.pack(pady=5)
entry2 = tk.Entry(root)
entry2.pack(pady=5)

buttom = tk.Button(root, text ="sum" , command= get_sum) 
buttom.pack(pady=10)




root.mainloop()
