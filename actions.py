import tkinter as tk
from tkinter import filedialog
from globals import files, frames, downloadsPath, removalTexts, monitor, buttons, monitorTexts, downloadsObserver, folderName, createFoldersButton, titles
import os
import shutil

def addFileHandler(column):
    addedFiles = filedialog.askopenfilenames(initialdir=downloadsPath, title="Select File for Column "+str(column))
    
    listOfFileDicts=list()
    for file in addedFiles:
        fileObject=dict()
        fileName=file.split("/")[-1]
        fileObject["path"]=file
        fileObject["name"]=fileName
        listOfFileDicts.append(fileObject)
    
    if column in files.keys(): files[column]+=list(listOfFileDicts)
    else: files[column]=list(listOfFileDicts)
    renderFileWidgets(column)

def removeFilesHandler(column):
    if column in files.keys():
        removalText=removalTexts[column]
        removalType=removalText.get().split(" ")[1]

        if removalType=="All":
            numberOfFiles=len(files[column])
            for row in range(numberOfFiles-1, -1, -1):
                frames[column].delete(row)
            del files[column]

        if removalType=="Selected":
            listbox=frames[column]
            itemsToRemove = listbox.curselection()[::-1]
            for i in itemsToRemove:
                del files[column][i]
                listbox.delete(i)
            removalTexts[column].set("Remove All Files")
    
def addWidget(parent, row, file):
    widget = tk.Frame(parent, width=100, height=100, bg="yellow")
    widget.grid(column=0, row=row, pady=10, sticky="ew")
    parent.grid_columnconfigure(0, weight=1)
    parent.grid_rowconfigure(row, weight=1)

def renderFileWidgets(column):
    numberOfEntries=len(frames[column].get(0, tk.END))
    for row in range(numberOfEntries-1, -1, -1):
        frames[column].delete(row)

    if column in files.keys():
        for index, file in enumerate(files[column]):
            frames[column].insert(index, file["name"])

def createFoldersHandler():
    nameOfFolder = folderName.get().strip()
    if len(nameOfFolder) == 0: return

    mainFilePath=downloadsPath+"/"+nameOfFolder
    os.mkdir(mainFilePath)

    for column in files.keys():
        directory=mainFilePath+"/"+titles[column]
        os.mkdir(directory)
        for file in files[column]:
            filePath=file["path"]
            shutil.copy(filePath, directory)

    files.clear()
    folderName.set("")
    for i in range(len(frames)):
        renderFileWidgets(i)

def manageMonitor(column):
    columnBeingMonitored=monitor[0].get()
    isMonitoring=monitor[1].get()

    if not isMonitoring:
        monitor[1].set(True)
        monitor[0].set(column)

        for col in buttons.keys():
            buttonsList=buttons[col]

            for button in buttonsList:
                button["state"]=tk.DISABLED

        buttons[column][0]["state"]=tk.NORMAL
        monitorTexts[column].set("Stop Monitoring")
        createFoldersButton["state"]=tk.DISABLED

        downloadsObserver.start()
    
    elif columnBeingMonitored == column:
        monitor[1].set(False)
        monitor[0].set(0)

        for col in buttons.keys():
            buttonsList=buttons[col]

            for button in buttonsList:
                button["state"]=tk.NORMAL

        monitorTexts[column].set("Start Monitoring")
        createFoldersButton["state"]=tk.NORMAL

        downloadsObserver.stop()
        downloadsObserver.join()

    else:
        print("Already monitoring column", monitor[0].get())