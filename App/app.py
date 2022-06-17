import tkinter as tk
from tkinter import filedialog, Text
import os

apps = []

def addApps():

    for widget in frame.winfo_children():
        widget.destroy()


    filename = filedialog.askopenfilename(initialdir="/", title= "Select File", 
        filetypes=(("executables", "*.exe"), ("all files", "*.*")))
    apps.append(filename)
    print(filename)
    for app in apps:
        label = tk.Label(frame, text = app, bg = "gray")
        label.pack()

def runApps():
    for app in apps:
        os.startfile(app)

def clearApps():
    apps.clear()
    with open('save.txt', 'w') as f:
        f.write('')
    for widget in frame.winfo_children():
        widget.destroy()

if __name__ == '__main__':
    if os.path.isfile('save.txt'):
        with open('save.txt', 'r') as f:
            tempApps = f.read()
            tempApps = tempApps.split(',')
            apps = [x for x in tempApps if x.strip()]

    root = tk.Tk()

    canvas =tk.Canvas(root, height = 700, width = 700, bg = "#263D42")
    canvas.pack()

    frame = tk.Frame(root, bg = "white")
    frame.place(relwidth = 0.8, relheight = 0.8, relx = 0.1, rely= 0.1)

    openFile = tk.Button(root, text="Open File", padx = 10, pady = 5, fg = "white", bg = "#263D42", command = addApps)
    openFile.pack()

    runApps = tk.Button(root, text="Run Apps", padx = 10, pady = 5, fg = "white", bg = "#263D42", command= runApps)
    runApps.pack()

    clearApps = tk.Button(root, text="Clear Apps", padx=9, pady=5, fg = "white", bg = "#263D42", command= clearApps)
    clearApps.pack()

    for app in apps:
        label = tk.Label(frame, text=app)
        label.pack()
        
    root.mainloop()

    with open('save.txt', 'w') as f:
        for app in apps:
            f.write(app + ',')