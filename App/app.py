'''
Author: Devin Himmelheber
Date: 6/17/2022
Description: This app is meant to queue up different user selected applications 
    and then run them when a specific button is selected. 
'''



import tkinter as tk
# I cannot figure out why it is recommended to pull these two functions from tkinter when we already have imported tkinter.
from tkinter import filedialog, Text
import os

# Global list for list of apps. Need to find better way to initialize this.
apps = []

# Function to add apps to apps list.
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

# Function to run apps in apps list.
def runApps():
    for app in apps:
        os.startfile(app)

# Clears the apps list, clears the save.txt file, and clears all current widgets in frame.
def clearApps():
    apps.clear()
    with open('save.txt', 'w') as f:
        f.write('')
    for widget in frame.winfo_children():
        widget.destroy()

if __name__ == '__main__':
    # If save file present, loads data into apps list.
    if os.path.isfile('save.txt'):
        with open('save.txt', 'r') as f:
            tempApps = f.read()
            tempApps = tempApps.split(',')
            apps = [x for x in tempApps if x.strip()]

    # Creates a toplevel widget.
    root = tk.Tk()

    # Creates canvas onto root widget. Color is a dark greyish blue.
    canvas =tk.Canvas(root, height = 700, width = 700, bg = "#263D42")
    canvas.pack()

    # Creates a white fram onto the root widget.
    frame = tk.Frame(root, bg = "white")
    frame.place(relwidth = 0.8, relheight = 0.8, relx = 0.1, rely= 0.1)

    # The following create buttons for opening an application, running selected apps, and clearing the apps.
    openFile = tk.Button(root, text="Open File", padx = 10, pady = 5, fg = "white", bg = "#263D42", command = addApps)
    openFile.pack()

    runApps = tk.Button(root, text="Run Apps", padx = 10, pady = 5, fg = "white", bg = "#263D42", command= runApps)
    runApps.pack()

    clearApps = tk.Button(root, text="Clear Apps", padx=9, pady=5, fg = "white", bg = "#263D42", command= clearApps)
    clearApps.pack()

    # Prints the app locations to the frame.
    for app in apps:
        label = tk.Label(frame, text=app)
        label.pack()

    # Runs the root widget.
    root.mainloop()

    # Once the widget is closed, creates/updates the save file. Format is: <filepath>,... 
    with open('save.txt', 'w') as f:
        for app in apps:
            f.write(f'{app},')