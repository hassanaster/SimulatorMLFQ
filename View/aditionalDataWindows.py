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

#Window or root: First we should create the root or window
aditionalDataWindow=tk.Tk()
aditionalDataWindow.title("MLFQ Simulation - Aditional Data Window")
aditionalDataWindow.resizable(False,False)
aditionalDataWindow.iconbitmap("/icon.ico")

#Frame, container or first widget: After this we create the frame where we are going to put the widgets needed for this window
frameAditionalDataWindow=tk.Frame()
frameAditionalDataWindow.pack()
frameAditionalDataWindow.config(width="800", height="800")
frameAditionalDataWindow['bg']='#EAF6F5'

#Create the widgets and add them in a grid to add all the widgets needed in the right places
#Labels
tk.Label(frameAditionalDataWindow,text="Additional Data", font=("Arial", 18), bg='#EAF6F5').grid(row=0, column=0, sticky="W", columnspan=5, padx=10, pady=20)
tk.Label(frameAditionalDataWindow,text="Arrival Time", font=("Arial", 14), bg='#EAF6F5').grid(row=1, column=1, sticky="W", padx=10, pady=10)
tk.Label(frameAditionalDataWindow,text="Run Time", font=("Arial", 14), bg='#EAF6F5').grid(row=1, column=2, sticky="W", padx=10, pady=10)
tk.Label(frameAditionalDataWindow,text="I/O Time", font=("Arial", 14), bg='#EAF6F5').grid(row=1, column=3, sticky="W", padx=10, pady=10)
tk.Label(frameAditionalDataWindow,text="How often start I/O process*", font=("Arial", 10), bg='#EAF6F5').grid(row=1, column=4, sticky="W", padx=10, pady=10)
tk.Label(frameAditionalDataWindow,text="Job A:", font=("Arial", 14), bg='#EAF6F5').grid(row=2, column=0, sticky="E", padx=10, pady=10)
tk.Label(frameAditionalDataWindow,text="Job B:", font=("Arial", 14), bg='#EAF6F5').grid(row=3, column=0, sticky="E", padx=10, pady=10)
tk.Label(frameAditionalDataWindow,text="Job C:", font=("Arial", 14), bg='#EAF6F5').grid(row=4, column=0, sticky="E", padx=10, pady=10)

tk.Label(frameAditionalDataWindow,text="This field are additional less the last field, if user fill out the 'I/O time' in a process*", font=("Arial", 12), bg='#EAF6F5', fg="gray").grid(row=6, column=0, sticky="W", padx=200, columnspan=5)

#Inputs or fields
#JOB A
arrivalJobAField=tk.Entry(frameAditionalDataWindow, font=("Arial"), fg="gray", width=12)
arrivalJobAField.grid(row=2, column=1, sticky="W", padx=10, pady=10)

runTimeJobAField=tk.Entry(frameAditionalDataWindow, font=("Arial"), fg="gray", width=12)
runTimeJobAField.grid(row=2, column=2, sticky="W", padx=10, pady=10)

ioJobAField=tk.Entry(frameAditionalDataWindow, font=("Arial"), fg="gray", width=12)
ioJobAField.grid(row=2, column=3, sticky="W", padx=10, pady=10)

startIoJobAField=tk.Entry(frameAditionalDataWindow, font=("Arial"), fg="gray", width=12)
startIoJobAField.grid(row=2, column=4, sticky="W", padx=10, pady=10)

#JOB B
arrivalJobBField=tk.Entry(frameAditionalDataWindow, font=("Arial"), fg="gray", width=12)
arrivalJobBField.grid(row=3, column=1, sticky="W", padx=10, pady=10)

runTimeJobBField=tk.Entry(frameAditionalDataWindow, font=("Arial"), fg="gray", width=12)
runTimeJobBField.grid(row=3, column=2, sticky="W", padx=10, pady=10)

ioJobBField=tk.Entry(frameAditionalDataWindow, font=("Arial"), fg="gray", width=12)
ioJobBField.grid(row=3, column=3, sticky="W", padx=10, pady=10)

startIoJobBField=tk.Entry(frameAditionalDataWindow, font=("Arial"), fg="gray", width=12)
startIoJobBField.grid(row=3, column=4, sticky="W", padx=10, pady=10)

#JOB C
arrivalJobCField=tk.Entry(frameAditionalDataWindow, font=("Arial"), fg="gray", width=12)
arrivalJobCField.grid(row=4, column=1, sticky="W", padx=10, pady=10)

runTimeJobCField=tk.Entry(frameAditionalDataWindow, font=("Arial"), fg="gray", width=12)
runTimeJobCField.grid(row=4, column=2, sticky="W", padx=10, pady=10)

ioJobCField=tk.Entry(frameAditionalDataWindow, font=("Arial"), fg="gray", width=12)
ioJobCField.grid(row=4, column=3, sticky="W", padx=10, pady=10)

startIoJobCField=tk.Entry(frameAditionalDataWindow, font=("Arial"), fg="gray", width=12)
startIoJobCField.grid(row=4, column=4, sticky="W", padx=10, pady=10)


#Buttons
startButton=tk.Button(frameAditionalDataWindow, text="START", width=10, height=2, font=("Arial"))
startButton.grid(row=5, column=0, sticky="E", padx=10, pady=20, columnspan=3)

cancelButtonAW=tk.Button(frameAditionalDataWindow, text="CANCEL", width=10, height=2, font=("Arial"))
cancelButtonAW.grid(row=5, column=3, sticky="W", padx=10, pady=20, columnspan=2)

#Should be always in the end of the file
aditionalDataWindow.mainloop()