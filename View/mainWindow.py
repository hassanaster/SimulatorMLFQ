#----------------------------------------------------------------------------------
# Main Window: When the simulator started this is the first GUI interface displayed.
# This window take the initial data: # of Queue and # of Jobs (max 3 of each data)
#----------------------------------------------------------------------------------

#----------------------------------------------------------------------------------
# @Authors: Miriam Arango, Luisa Arboleda, Yeison Quinto
# @Version: Version 1.0
# @Date: 26 - 12 - 2020
#----------------------------------------------------------------------------------


import tkinter as tk
import tkinter.messagebox as mb
import View.shareGraphicFunctions as sgf

#----------------------------------------------------------------------------------
# Variables
#----------------------------------------------------------------------------------
#Global variables
queue=""
job=""
mainWindow=tk.Tk()

#variables from fields I need to recover
quantityQueue=tk.StringVar()
quantityJob=tk.StringVar()

#----------------------------------------------------------------------------------
# Functions to create the events for each button
#----------------------------------------------------------------------------------

#Event for OK button on click
def eventOkButton():
    global queue
    global job
    queue=quantityQueue.get()
    job=quantityJob.get()
    if (quantityJob.get()==""):
        job="0"
    if (quantityQueue.get()==""):
        queue="0"
    if((int(job)>=1 and int(job)<=3) and (int(queue)>=1 and int(queue)<=3)):
        mainWindow.destroy()
    else:
        setInit()
        mb.showerror(title="Error", message="Numbers admitted for both fields are 1, 2 or 3, please take a look.")
    

#Event for CANCEL button on click
def eventCancelButton():
    quantityQueue.set("")
    quantityJob.set("")

def setInit():
    global queue
    global job
    queue=""
    job=""

def getQueue():
    global queue
    return queue

def getJob():
    global job
    return job


#---Variable firstTime has de name of the window to close
def drawMainWindow():
    global mainWindow

    #Window or root: First we should create the root or window
    mainWindow.title("MLFQ Simulation - Main window")
    mainWindow.resizable(False,False)
    mainWindow.iconbitmap("/icon.ico")

    #Frame, container or first widget: After this we create the frame where we are going to put the widgets needed for this window
    frameMainWindow=tk.Frame()
    frameMainWindow.pack()
    frameMainWindow.config(width="450", height="250")
    frameMainWindow['bg']='#EAF6F5'

    #Widgets creation
    #Labels
    titleLabel=tk.Label(frameMainWindow,text="Jobs & Queue", font=("Arial", 18), bg='#EAF6F5')
    titleLabel.place(x=25, y=25)
    tk.Label(frameMainWindow, text="Queue quantity*:", font=("Arial", 14), bg='#EAF6F5').place(x=75, y=75)
    jobLabel= tk.Label(frameMainWindow, text="Jobs quantity*:", font=("Arial", 14), bg='#EAF6F5')
    jobLabel.place(x=75, y=115)
    messageLabel= tk.Label(frameMainWindow, text="Maximum quantity for both fields is 3", font=("Arial", 16), bg='#EAF6F5', fg="gray")
    messageLabel.place(x=100, y=215)

    #Inputs
    validation = frameMainWindow.register(sgf.onlyNumbers)

    queueField=tk.Entry(frameMainWindow, font=("Arial"), fg="gray", textvariable=quantityQueue, validate="key", validatecommand=(validation, '%S'))
    queueField.place(x=195, y=75)

    jobField=tk.Entry(frameMainWindow, font=("Arial"), fg="gray", textvariable=quantityJob, validate="key", validatecommand=(validation, '%S'))
    jobField.place(x=195, y=115)

    #Buttons
    okButton=tk.Button(frameMainWindow, text="OK", width=10, height=2, font=("Arial"), command=eventOkButton)
    okButton.place(x=125, y=165)

    cancelButton=tk.Button(frameMainWindow, text="CANCEL", width=10, height=2, font=("Arial"), command=eventCancelButton)
    cancelButton.place(x=245, y=165)

    #Should be always in the end of the file
    mainWindow.mainloop()