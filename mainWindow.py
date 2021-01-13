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
import tkinter.ttk as cb
from View.basicDataWindow import *

#----------------------------------------------------------------------------------
# Variables
#----------------------------------------------------------------------------------
#Global variables
queue=""
job=""

#We create the root window here to be able to call StringVar() function
mainWindow=tk.Tk()

#variables from fields I need to recover
quantityQueue=tk.StringVar()
quantityJob=tk.StringVar()

#variables from fields I need to recover
quantumTime=tk.StringVar()
periodTime=tk.StringVar()


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
        #Define a object Job which will persist the data in this part (set job), (Set queue)
        print(job, queue, sep=",")
        drawBasicDataWindow(job, quantumTime, periodTime, mainWindow)
        setInit()
    else:
        setInit()
        mb.showerror(title="Error", message="Numbers admitted for both fields are 1, 2 or 3, please take a look.")
    

#Event for CANCEL button on click
def eventCloseButton():
    mainWindow.destroy()

def setInit():
    global queue
    global job
    queue=""
    job=""

#---Start the main program
#root window
mainWindow.title("MLFQ Simulation - Main window")
mainWindow.resizable(False,False)
mainWindow.iconbitmap("icon.ico")
mainWindow.config(bg='#EAF6F5')
mainWindow.geometry('350x250+500+350')

#Widgets creation
#Labels
tk.Label(mainWindow,text="Jobs & Queue", font=("Arial", 18), bg='#EAF6F5').grid(row=0, column=0, columnspan=2, sticky="W", padx=20, pady=10)
tk.Label(mainWindow, text="Queue quantity*:", font=("Arial", 14), bg='#EAF6F5').grid(row=1, column=0, sticky="E", padx=10, pady=10)
tk.Label(mainWindow, text="Jobs quantity*:", font=("Arial", 14), bg='#EAF6F5').grid(row=2, column=0, sticky="E", padx=10, pady=10)
tk.Label(mainWindow, text="Maximum quantity for both fields is 3", font=("Arial", 16), bg='#EAF6F5', fg="gray").grid(row=4, column=0, columnspan=2, padx=10, pady=10)

#Inputs
validation = mainWindow.register(sgf.onlyNumbers)

queueField=tk.Entry(mainWindow, font=("Arial"), fg="gray", textvariable=quantityQueue, validate="key", validatecommand=(validation, '%S'))
queueField.grid(row=1, column=1, sticky="W", padx=5, pady=5)

jobField=tk.Entry(mainWindow, font=("Arial"), fg="gray", textvariable=quantityJob, validate="key", validatecommand=(validation, '%S'))
jobField.grid(row=2, column=1, sticky="W", padx=5, pady=5)

#Buttons
okButton=tk.Button(mainWindow, text="OK", width=10, height=2, font=("Arial"), command=eventOkButton)
okButton.grid(row=3, column=0, padx=10, pady=10)

cancelButton=tk.Button(mainWindow, text="CLOSE", width=10, height=2, font=("Arial"), command=eventCloseButton)
cancelButton.grid(row=3, column=1, padx=10, pady=10)

#Should be always in the end of the file
mainWindow.mainloop()