import tkinter as tk
from actions import addFileHandler, removeFilesHandler, addWidget, manageMonitor
from globals import buttons, removalTexts, monitorTexts

def createVerticalFrame(parent, bg, column, row, title):
    frame=tk.Frame(parent, bg=bg)
    frame.grid(column=column, row=row, sticky="nsew")
    parent.grid_columnconfigure(column, weight=1)
    parent.grid_rowconfigure(row, weight=1)

    # Adding Column Title
    title=tk.Label(frame, text=title)
    title.grid(column=0, row=0, columnspan=2, sticky="ew")
    frame.grid_columnconfigure(0, weight=1)
    frame.grid_rowconfigure(1, weight=1)

    # Add Action Buttons
    timerButton=tk.Button(frame, textvariable=monitorTexts[column], command=lambda: manageMonitor(column))
    removeFilesButton=tk.Button(frame, textvariable=removalTexts[column], command=lambda: removeFilesHandler(column))
    addFileButton=tk.Button(frame, text="Add Files", command=lambda: addFileHandler(column))
    timerButton.grid(column=0, row=2, columnspan=2, sticky="ew")
    removeFilesButton.grid(column=0, row=3, columnspan=2, sticky="ew")
    addFileButton.grid(column=0, row=4, columnspan=2, sticky="ew")

    buttonList=list([timerButton, removeFilesButton, addFileButton])
    buttons[column]=buttonList

    # Adding Scrollable Canvas
    listbox = tk.Listbox(frame, borderwidth=0, bg="#000", selectmode='multiple')

    def setRemovalTexts(_):
        selectedItems=listbox.curselection()
        if len(selectedItems)==0:
            removalTexts[column].set("Remove All Files")
        else:
            removalTexts[column].set("Remove Selected Files")
        
    listbox.bind('<<ListboxSelect>>', setRemovalTexts)
    scrollbar = tk.Scrollbar(frame, orient="vertical", command=listbox.yview)
    listbox.configure(yscrollcommand=scrollbar.set)

    scrollbar.grid(column=1, row=1, sticky="ns")
    frame.grid_rowconfigure(1, weight=1)
    listbox.grid(column=0, row=1, sticky="nsew")
    frame.grid_rowconfigure(1, weight=1)

    return listbox