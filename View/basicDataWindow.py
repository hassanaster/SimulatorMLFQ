#----------------------------------------------------------------------------------
# Basic Data Window: After get how many jobs and periods is needed other basic information for each quantum
# This window take the basic data: priority of each quantum, quantum time, and period time
#----------------------------------------------------------------------------------

#----------------------------------------------------------------------------------
# @Authors: Miriam Arango, Luisa Arboleda, Yeison Quinto
# @Version: Version 1.0
# @Date: 02 - 01 - 2021
#----------------------------------------------------------------------------------

import tkinter as tk
import tkinter.messagebox as mb
import tkinter.ttk as cb

#Window or root: First we should create the root or window
basicDataWindow=tk.Tk()
basicDataWindow.title("MLFQ Simulation - Basic Data Window")
basicDataWindow.resizable(False,False)
basicDataWindow.iconbitmap("/icon.ico")

#Frame, container or first widget: After this we create the frame where we are going to put the widgets needed for this window
frameBasicDataWindow=tk.Frame()
frameBasicDataWindow.pack()
frameBasicDataWindow.config(width="800", height="800")
frameBasicDataWindow['bg']='#EAF6F5'

#----------------------------------------------------------------------------------
# Variables
#----------------------------------------------------------------------------------

#variables from fields I need to recover
quantumTime=tk.StringVar()
periodTime=tk.StringVar()
"""priorityJobA=tk.StringVar()
priorityJobB=tk.StringVar()
priorityJobC=tk.StringVar()
aditionalWindow=tk.StringVar()"""


#Global variables
quantum=""
period=""
priorityA=""
priorityB=""
priorityC=""
aditionalW=""

#----------------------------------------------------------------------------------
# Functions to create the events for each button
#----------------------------------------------------------------------------------

#Event for OK button on click
def eventOkBWButton():
    global quantum
    global period
    quantum=quantumTime.get()
    period=periodTime.get()
    priorityA=jobAComboBox.current()
    priorityB=jobBComboBox.current()
    priorityC=jobCComboBox.current()
    aditionalW=jobTwoOptionsComboBox.current()
    if (quantum==""):
        quantum="0"
    if (period==""):
        period="0"
    if((int(quantum)==0) and (int(period)==0)):
        period=""
        quantum=""
        mb.showerror(title="Error", message="Data typed for quantum and period field are invalid, please verify.")
        #call the windows aditionalDataWindows.py
    else:
        print("Priority Job A:", priorityA)
        print("Priority Job B:", priorityB)
        print("Priority Job C:", priorityC)
        print("Quantum:", quantum)
        print("Period Time:", period)
        print("Aditional data:", aditionalW)

#Event for CANCEL button on click
def eventCancelBWButton():
    quantumTime.set("")
    periodTime.set("")
    jobAComboBox.current(newindex=3)
    jobBComboBox.current(newindex=3)
    jobCComboBox.current(newindex=3)
    jobTwoOptionsComboBox.current(newindex=1)

#Validation for just acept numbers
#This code was taken from: https://riptutorial.com/es/tkinter/example/27780/anadiendo-validacion-a-un-widget-de-entrada
def onlyNumbers(char):
    return char.isdigit()

#---We need a function to disabled comboBox B, C when is chosen 2 or 1 job in the last window

#Create the widgets and add them in a grid to add all the widgets needed in the right places
#Labels
tk.Label(frameBasicDataWindow,text="Jobs, period & Basic data", font=("Arial", 18), bg='#EAF6F5').grid(row=0, column=0, sticky="W", columnspan=2, padx=10, pady=20)
tk.Label(frameBasicDataWindow,text="Priority", font=("Arial", 10), bg='#EAF6F5').grid(row=1, column=1, sticky="W", padx=20, pady=1)
tk.Label(frameBasicDataWindow,text="Job A:*", font=("Arial", 14), bg='#EAF6F5').grid(row=2, column=0, sticky="E", padx=10, pady=10)
jobBLabel=tk.Label(frameBasicDataWindow,text="Job B:*", font=("Arial", 14), bg='#EAF6F5')
jobBLabel.grid(row=3, column=0, sticky="E", padx=10, pady=10)
jobCLabel=tk.Label(frameBasicDataWindow,text="Job C:*", font=("Arial", 14), bg='#EAF6F5')
jobCLabel.grid(row=4, column=0, sticky="E", padx=10, pady=10)
tk.Label(frameBasicDataWindow,text="----------------------------------------------------------------------------------------", font=("Arial", 12), bg='#EAF6F5').grid(row=5, column=0, sticky="W",columnspan=2, padx=40)
tk.Label(frameBasicDataWindow,text="Quantum time:*", font=("Arial", 14), bg='#EAF6F5').grid(row=6, column=0, sticky="E", padx=10, pady=10)
tk.Label(frameBasicDataWindow,text="Period time 'S':*", font=("Arial", 14), bg='#EAF6F5').grid(row=7, column=0, sticky="E", padx=10, pady=10)
tk.Label(frameBasicDataWindow,text="Do you want to add more", font=("Arial", 12), bg='#EAF6F5').grid(row=8, column=0, sticky="E", padx=10)
tk.Label(frameBasicDataWindow,text="information for the simulation?", font=("Arial", 12), bg='#EAF6F5').grid(row=9, column=0, sticky="E", padx=10)

#Inputs or fields
validation = frameBasicDataWindow.register(onlyNumbers)

quantumField=tk.Entry(frameBasicDataWindow, font=("Arial"), fg="gray", width=17, textvariable=quantumTime, validate="key", validatecommand=(validation, '%S'))
quantumField.grid(row=6, column=1, sticky="W", padx=20, pady=10)

periodField=tk.Entry(frameBasicDataWindow, font=("Arial"), fg="gray", width=17, textvariable=periodTime, validate="key", validatecommand=(validation, '%S'))
periodField.grid(row=7, column=1, sticky="W", padx=20, pady=10)

#ComboBox
options=["High", "Medium", "Low", "N/A"]
twoOptions=["Yes", "No"]
jobAComboBox=cb.Combobox(frameBasicDataWindow, width=14, state="readonly")
jobAComboBox.grid(row=2, column=1, sticky="W", padx=20, pady=10)
jobAComboBox['values']=options
jobAComboBox.current(newindex=3)

jobBComboBox=cb.Combobox(frameBasicDataWindow, width=14, state="readonly")
jobBComboBox.grid(row=3, column=1, sticky="W", padx=20, pady=10)
jobBComboBox['values']=options
jobBComboBox.current(newindex=3)

jobCComboBox=cb.Combobox(frameBasicDataWindow, width=14, state="readonly")
jobCComboBox.grid(row=4, column=1, sticky="W", padx=20, pady=10)
jobCComboBox['values']=options
jobCComboBox.current(newindex=3)

jobTwoOptionsComboBox=cb.Combobox(frameBasicDataWindow, width=14, state="readonly")
jobTwoOptionsComboBox.grid(row=8, column=1, sticky="W", padx=20, pady=10, rowspan=2)
jobTwoOptionsComboBox['values']=twoOptions
jobTwoOptionsComboBox.current(newindex=1)

#Buttons
okButtonBW=tk.Button(frameBasicDataWindow, text="OK", width=10, height=2, font=("Arial"), command=eventOkBWButton)
okButtonBW.grid(row=10, column=0, sticky="E", padx=10, pady=20)

cancelButtonBW=tk.Button(frameBasicDataWindow, text="CANCEL", width=10, height=2, font=("Arial"), command=eventCancelBWButton)
cancelButtonBW.grid(row=10, column=1, sticky="W", padx=10, pady=20)

#Should be always in the end of the file
basicDataWindow.mainloop()

