downloadsPath="/Users/hittudesai/Desktop/BankDocs"

titles=list(["Dastavej", "Naamkaran", "Mamlatdar"])
frames=list()
files=dict()
buttons=dict()

timer=(0, False)

# Root
import tkinter as tk
root = tk.Tk()
root.state("zoomed")
# root.geometry("640x360")
root.title("Rudra Developers File Manager")

removalTexts=list()
monitorTexts=list()
for i in range(len(titles)):
    removalText=tk.StringVar()
    removalText.set("Remove All Files")
    removalTexts.append(removalText)
    
    monitorText=tk.StringVar()
    monitorText.set("Start Monitoring")
    monitorTexts.append(monitorText)

folderName=tk.StringVar()
textfield=tk.Entry(root, textvariable=folderName)
textfield.grid(column=1, row=0, sticky="ew")
root.grid_columnconfigure(1, weight=1)

createFoldersButton=tk.Button(root, text="Create Folders", )
createFoldersButton.grid(column=2, row=0, sticky="ew")
root.grid_columnconfigure(2, weight=1)

columnBeingMonitored=tk.IntVar()
isMonitoring=tk.BooleanVar()
monitor=list([columnBeingMonitored, isMonitoring])

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

def handleFileCreate(self, event):
    if event.is_directory or event.is_synthetic: return
    
    file=event.src_path
    fileObject=dict()
    fileName=file.split("/")[-1]
    fileObject["path"]=file
    fileObject["name"]=fileName

    column=monitor[0].get()
    if column in files.keys(): files[column]+=list([fileObject])
    else: files[column]=list([fileObject])

    from actions import renderFileWidgets
    renderFileWidgets(column)
    
eventHandler=FileSystemEventHandler()
FileSystemEventHandler.on_created = handleFileCreate

downloadsObserver = Observer()
downloadsObserver.schedule(eventHandler, downloadsPath, recursive=True)