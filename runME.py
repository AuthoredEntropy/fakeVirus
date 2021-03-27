#Author: @AuthoredEntropy 
import tkinter as tk
import random as random
author = "@AuthoredEntropy"
window = tk.Tk()
window.geometry("400x50")
window.title("virus Installer")
virusFrame = tk.Frame(master=window, width=50,height=50)
virusFrame.pack()

def game():
    for i in range(0,10):
        x = tk.Toplevel(window)
        x.title("VIRUS!")
        x.geometry("150x75+" + str(random.randint(100,1500)) + "+"+str(random.randint(100,1000)))
        x.resizable(False, False)
        tk.Label(x, text = "virus").pack()
        tk.Button(x, text = " install ", command = game).pack(side=tk.BOTTOM)
        x.attributes('-topmost', False)
    
button = tk.Button(master=virusFrame, height=3,text="activate", command=game)
button.pack(anchor="center", side="top")
window.attributes('-topmost', True)
window.mainloop()