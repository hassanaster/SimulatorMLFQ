#----------------------------------------------------------------------------------
# Aditional Data Window: After get basic date from user, user is avalaible to add aditional data for the simulation
# This window take the additional data: arrival time, run time, I/O Time, How often start I/O process*
#----------------------------------------------------------------------------------

#----------------------------------------------------------------------------------
# @Authors: Miriam Arango, Luisa Arboleda, Yeison Quinto
# @Version: Version 1.0
# @Date: 03 - 01 - 2021
#----------------------------------------------------------------------------------

import tkinter as tk
import tkinter.messagebox as mb
import View.shareGraphicFunctions as sgf
from View.simulationWindows import *

#----------------------------------------------------------------------------------
# Variables
#----------------------------------------------------------------------------------
#basicDataWindow=tk.Toplevel()

#Global variables
jobA=[0,0,0,0]
jobB=[0,0,0,0]
jobC=[0,0,0,0]

#----------------------------------------------------------------------------------
# Functions to create the events for each button
#----------------------------------------------------------------------------------

#Event for OK button on click
def validateField (data, array, position):
    if data=="":
        array[position]=0
    else:
        array[position]=int(data)

def eventstartButton(jobQuantity, arrivalJobAField, arrivalJobBField, arrivalJobCField, runTimeJobAField, runTimeJobBField, runTimeJobCField, ioJobCField, ioJobBField, ioJobAField, startIoJobCField, startIoJobBField, startIoJobAField, aditionalDataWindow, mainWindow):
    global JobA
    global JobB
    global JobC
    if jobQuantity=="1":
        jobA[0]=validateField(arrivalJobAField.get(), jobA, 0)
        jobA[1]=validateField(runTimeJobAField.get(), jobA, 1)
        jobA[2]=validateField(ioJobAField.get(), jobA, 2)
        jobA[3]=validateField(startIoJobAField.get(), jobA, 3)
    if jobQuantity=="2" :
        jobB[0]=validateField(arrivalJobBField.get(), jobB, 0)
        jobB[1]=validateField(runTimeJobBField.get(), jobB, 1)
        jobB[2]=validateField(ioJobBField.get(), jobB, 2)
        jobB[3]=validateField(startIoJobBField.get(), jobB, 3)
    if jobQuantity=="3" :
        jobC[0]=validateField(arrivalJobCField.get(), jobC, 0)
        jobC[1]=validateField(runTimeJobCField.get(), jobC, 1)
        jobC[2]=validateField(ioJobCField.get(), jobC, 2)
        jobC[3]=validateField(startIoJobCField.get(), jobC, 3)
    print(jobA[0], jobA[1], jobA[2], jobA[3], jobB[0], jobB[1], jobB[2], jobB[3], jobC[0], jobC[1], jobC[2], jobC[3], sep=",")
    #Before to call the other window persist data in the object Job and queue
    drawSimulationWindow(aditionalDataWindow, mainWindow)
        
#Disable combox JobB when user just chose 1 job to run
def disbledEnabledFieldsB(quantity):
    if quantity == 1:
        return "disabled"
    return "normal"

#Disable combox JobC when user just chose max 2 jobs to run
def disbledEnabledFieldsC(quantity):
    if quantity == 1 or quantity == 2:
        return "disabled"
    return "normal"

def setInitBW():
    JobA=[0,0,0,0]
    JobB=[0,0,0,0]
    JobC=[0,0,0,0]

#Function wich draw the window for the basic data
def drawAditionalDataWindow(quantity, arrivalJobA, arrivalJobB, arrivalJobC, runTimeJobA, runTimeJobB, runTimeJobC, ioJobC, ioJobB, ioJobA, startIoJobC, startIoJobB, startIoJobA, basicDataWindow, mainWindow):
    basicDataWindow.withdraw()
    #Window or root: First we should create the root or window
    aditionalDataWindow=tk.Toplevel()
    aditionalDataWindow.title("MLFQ Simulation - Aditional Data Window")
    aditionalDataWindow.resizable(False,False)
    aditionalDataWindow.iconbitmap("/icon.ico")
    aditionalDataWindow.config(bg='#EAF6F5')
    aditionalDataWindow.geometry('800x400+500+150')

    #Create the widgets and add them in a grid to add all the widgets needed in the right places
    #Labels
    tk.Label(aditionalDataWindow,text="Additional Data", font=("Arial", 18), bg='#EAF6F5').grid(row=0, column=0, sticky="W", columnspan=5, padx=10, pady=20)
    tk.Label(aditionalDataWindow,text="Arrival Time", font=("Arial", 14), bg='#EAF6F5').grid(row=1, column=1, sticky="W", padx=10, pady=10)
    tk.Label(aditionalDataWindow,text="Run Time", font=("Arial", 14), bg='#EAF6F5').grid(row=1, column=2, sticky="W", padx=10, pady=10)
    tk.Label(aditionalDataWindow,text="I/O Time", font=("Arial", 14), bg='#EAF6F5').grid(row=1, column=3, sticky="W", padx=10, pady=10)
    tk.Label(aditionalDataWindow,text="How often start I/O process*", font=("Arial", 10), bg='#EAF6F5').grid(row=1, column=4, sticky="W", padx=10, pady=10)
    tk.Label(aditionalDataWindow,text="Job A:", font=("Arial", 14), bg='#EAF6F5').grid(row=2, column=0, sticky="E", padx=10, pady=10)
    tk.Label(aditionalDataWindow,text="Job B:", font=("Arial", 14), bg='#EAF6F5').grid(row=3, column=0, sticky="E", padx=10, pady=10)
    tk.Label(aditionalDataWindow,text="Job C:", font=("Arial", 14), bg='#EAF6F5').grid(row=4, column=0, sticky="E", padx=10, pady=10)

    tk.Label(aditionalDataWindow,text="This field are additional less the last field, if user fill out the 'I/O time' in a process*", font=("Arial", 12), bg='#EAF6F5', fg="gray").grid(row=6, column=0, sticky="W", padx=200, columnspan=5)

    #Inputs or fields
    validation = basicDataWindow.register(sgf.onlyNumbers)

    #JOB A
    arrivalJobAField=tk.Entry(aditionalDataWindow, font=("Arial"), fg="gray", width=12, validate="key", validatecommand=(validation, '%S'))
    arrivalJobAField.grid(row=2, column=1, sticky="W", padx=10, pady=10)

    runTimeJobAField=tk.Entry(aditionalDataWindow, font=("Arial"), fg="gray", width=12, validate="key", validatecommand=(validation, '%S'))
    runTimeJobAField.grid(row=2, column=2, sticky="W", padx=10, pady=10)

    ioJobAField=tk.Entry(aditionalDataWindow, font=("Arial"), fg="gray", width=12, validate="key", validatecommand=(validation, '%S'))
    ioJobAField.grid(row=2, column=3, sticky="W", padx=10, pady=10)

    startIoJobAField=tk.Entry(aditionalDataWindow, font=("Arial"), fg="gray", width=12, validate="key", validatecommand=(validation, '%S'))
    startIoJobAField.grid(row=2, column=4, sticky="W", padx=10, pady=10)

    #JOB B
    arrivalJobBField=tk.Entry(aditionalDataWindow, font=("Arial"), fg="gray", width=12, validate="key", validatecommand=(validation, '%S'), state=disbledEnabledFieldsB(int(quantity)))
    arrivalJobBField.grid(row=3, column=1, sticky="W", padx=10, pady=10)

    runTimeJobBField=tk.Entry(aditionalDataWindow, font=("Arial"), fg="gray", width=12, validate="key", validatecommand=(validation, '%S'), state=disbledEnabledFieldsB(int(quantity)))
    runTimeJobBField.grid(row=3, column=2, sticky="W", padx=10, pady=10)

    ioJobBField=tk.Entry(aditionalDataWindow, font=("Arial"), fg="gray", width=12, validate="key", validatecommand=(validation, '%S'), state=disbledEnabledFieldsB(int(quantity)))
    ioJobBField.grid(row=3, column=3, sticky="W", padx=10, pady=10)

    startIoJobBField=tk.Entry(aditionalDataWindow, font=("Arial"), fg="gray", width=12, validate="key", validatecommand=(validation, '%S'), state=disbledEnabledFieldsB(int(quantity)))
    startIoJobBField.grid(row=3, column=4, sticky="W", padx=10, pady=10)

    #JOB C
    arrivalJobCField=tk.Entry(aditionalDataWindow, font=("Arial"), fg="gray", width=12, validate="key", validatecommand=(validation, '%S'), state=disbledEnabledFieldsC(int(quantity)))
    arrivalJobCField.grid(row=4, column=1, sticky="W", padx=10, pady=10)

    runTimeJobCField=tk.Entry(aditionalDataWindow, font=("Arial"), fg="gray", width=12, validate="key", validatecommand=(validation, '%S'), state=disbledEnabledFieldsC(int(quantity)))
    runTimeJobCField.grid(row=4, column=2, sticky="W", padx=10, pady=10)

    ioJobCField=tk.Entry(aditionalDataWindow, font=("Arial"), fg="gray", width=12, validate="key", validatecommand=(validation, '%S'), state=disbledEnabledFieldsC(int(quantity)))
    ioJobCField.grid(row=4, column=3, sticky="W", padx=10, pady=10)

    startIoJobCField=tk.Entry(aditionalDataWindow, font=("Arial"), fg="gray", width=12, validate="key", validatecommand=(validation, '%S'), state=disbledEnabledFieldsC(int(quantity)))
    startIoJobCField.grid(row=4, column=4, sticky="W", padx=10, pady=10)


    #Buttons
    startButton=tk.Button(aditionalDataWindow, text="START", width=10, height=2, font=("Arial"), command=lambda:eventstartButton(quantity, arrivalJobA, arrivalJobB, arrivalJobC, runTimeJobA, runTimeJobB, runTimeJobC, ioJobC, ioJobB, ioJobA, startIoJobC, startIoJobB, startIoJobA, aditionalDataWindow, mainWindow))
    startButton.grid(row=5, column=0, sticky="E", padx=10, pady=20, columnspan=3)

    closeButtonAW=tk.Button(aditionalDataWindow, text="CLOSE", width=10, height=2, font=("Arial"), command=lambda:sgf.eventCloseButton(mainWindow))
    closeButtonAW.grid(row=5, column=3, sticky="W", padx=10, pady=20, columnspan=2)