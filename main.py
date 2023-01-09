import tkinter as tk
from ui import createVerticalFrame
from actions import createFoldersHandler
from globals import titles, frames, files, root, createFoldersButton, folderName

# Input for Name of Main Folder
textfieldTitle=tk.Label(root, text="Enter Name of Folder")
textfieldTitle.grid(column=0, row=0, sticky="ew")
root.grid_columnconfigure(0, weight=1)
createFoldersButton["command"]=createFoldersHandler

# Create Base Frame
baseFrame=tk.Frame(root, bg="black")
baseFrame.grid(column=0, row=1, columnspan=3, sticky="nsew")
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)

# Create Document Frames
for column, title in enumerate(titles):
    frames.append(createVerticalFrame(parent=baseFrame, bg="black", column=column, row=0, title=title))

root.mainloop()