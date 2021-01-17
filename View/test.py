#----------------------------------------------------------------------------------
# Simulation Window: After get all data needed, user is avalaible to simulate MFLQ 
# This window show graphic the simulation in miliseconds how MFLQ works
#----------------------------------------------------------------------------------

#----------------------------------------------------------------------------------
# @Authors: Miriam Arango, Luisa Arboleda, Yeison Quinto
# @Version: Version 1.0
# @Creation Date: 04 - 01 - 2021
# @Last modify Date: 17 - 01 - 2021
#----------------------------------------------------------------------------------

import tkinter as tk
import tkinter.messagebox as mb
import shareGraphicFunctions as sgf


#----------------------------------------------------------------------------------
# Functions to create the events for each button
#----------------------------------------------------------------------------------

#Function for Pause the simulation

def drawEmptyField(emptyLabelDraw):
    for i in range(100):
        emptyLabelDraw.grid(row=3, column=i, padx=10, pady=2)
        emptyLabelDraw.grid(row=4, column=i, padx=10, pady=2)
        emptyLabelDraw.grid(row=5, column=i, padx=10, pady=2)


def eventPauseButton():
    mb.showinfo(title="Pause Button", message="Estoy en el boton de pausa")
        
#Function for Start the simulation after pause, or since the begining
def eventStartButtonSW():
    mb.showinfo(title="Start Button", message="Estoy en el boton de start")

#Function to finish the simulation and display the final graphic
def eventFinishButton():
    mb.showinfo(title="Finish Button", message="Estoy en el boton de finish")

#Function for Result button, to display window result
def eventResultButton():
    mb.showinfo(title="Result Button", message="Estoy en el boton de result")   

#Function to draw Simulation Window

simulationWindow=tk.Tk()
simulationWindow.title("MLFQ Simulation - Simulation Window")
simulationWindow.resizable(False,False)
simulationWindow.iconbitmap("icon.ico")
simulationWindow.config(bg='#EAF6F5')
#THIS CHANGED TOO
simulationWindow.geometry('1550x600+30+150')

#I HAVE TO CHANGE ALL THIS CODE LIKE IS HERE IN THE SIMULATION WINDOW
#Create the widgets and add them in a grid to add all the widgets needed in the right places
#Labels
tk.Label(simulationWindow,text="Simulation MLFQ", font=("Arial", 18), bg='#EAF6F5').grid(row=0, column=0, sticky="W", columnspan=100, pady=10)
tk.Label(simulationWindow,text="Counter(ms):", font=("Arial", 14), bg='#EAF6F5').grid(row=1, column=0, sticky="E", pady=10, columnspan=96)
tk.Label(simulationWindow,text="Processes graphic", font=("Arial", 14), bg='#EAF6F5', fg="gray").grid(row=2, column=0, columnspan=100, pady=3)

#Label q2, q1, q0
tk.Label(simulationWindow, text="Q2", font=("Arial", 12), bg='#EAF6F5', fg="gray", width=0, height=2).grid(row=3, column=0, padx=2, pady=2)
tk.Label(simulationWindow, text="Q1", font=("Arial", 12), bg='#EAF6F5', fg="gray", width=0, height=2).grid(row=4, column=0, padx=2, pady=2)
tk.Label(simulationWindow, text="Q0", font=("Arial", 12), bg='#EAF6F5', fg="gray", width=0, height=2).grid(row=5, column=0, padx=2, pady=2)

tk.Label(simulationWindow, text="ms", font=("Arial", 12), bg='#EAF6F5', fg="gray", width=0, height=2).grid(row=6, column=0, padx=2, pady=2)
tk.Label(simulationWindow, text="0", font=("Arial", 8), bg='#EAF6F5', fg="gray", width=0, height=2).grid(row=6, column=1, pady=2, sticky="N")
tk.Label(simulationWindow, text="25", font=("Arial", 5), bg='#EAF6F5', fg="gray", width=0, height=2).grid(row=6, column=26, pady=2)
tk.Label(simulationWindow, text="50", font=("Arial", 5), bg='#EAF6F5', fg="gray", width=0, height=2).grid(row=6, column=51, pady=2)
tk.Label(simulationWindow, text="75", font=("Arial", 5), bg='#EAF6F5', fg="gray", width=0, height=2).grid(row=6, column=76, pady=2)
tk.Label(simulationWindow, text="100", font=("Arial", 3), bg='#EAF6F5', fg="gray", width=0, height=2).grid(row=6, column=100, pady=2)

#RoW 7 miliseconds

tk.Label(simulationWindow,text="Color for corresponding processes*", font=("Arial", 14), bg='#EAF6F5', fg="gray").grid(row=8, column=0, columnspan=100, pady=10)
tk.Label(simulationWindow,text="Simulator management*", font=("Arial", 14), bg='#EAF6F5', fg="gray").grid(row=10, column=0, columnspan=100, pady=20)

#Labels to pain the jobs execution
#Draw JobA
jobALabelDraw= tk.Label(simulationWindow, bg='#CB8665', width=0, height=2)
jobALabelDraw.grid(row=9, column=10, pady=2)

tk.Label(simulationWindow, text="JobA", font=("Arial", 12), bg='#EAF6F5', fg="gray").grid(row=9, column=11, pady=2, columnspan=23, sticky="W")

#Draw JobB
jobBLabelDraw= tk.Label(simulationWindow, bg='#FDBCB4', width=0, height=2)
jobBLabelDraw.grid(row=9, column=33, pady=2)

tk.Label(simulationWindow, text="JobB", font=("Arial", 12), bg='#EAF6F5', fg="gray").grid(row=9, column=34, pady=2, columnspan=23, sticky="W")

#Draw JobC
jobCLabelDraw= tk.Label(simulationWindow, bg='#E6D690', width=0, height=2)
jobCLabelDraw.grid(row=9, column=57, pady=2)

tk.Label(simulationWindow, text="JobC", font=("Arial", 12), bg='#EAF6F5', fg="gray").grid(row=9, column=58, pady=2, columnspan=22, sticky="W")

#Draw I/O
ioLabelDraw= tk.Label(simulationWindow, bg="gray", width=0, height=2)
ioLabelDraw.grid(row=9, column=79, pady=2)

tk.Label(simulationWindow, text="I/O", font=("Arial", 12), bg='#EAF6F5', fg="gray").grid(row=9, column=80, pady=2, columnspan=22, sticky="W")

#Field - Entry
resultCounter=tk.Entry(simulationWindow,text="Results", font=("Arial", 12), bg='#EAF6F5', fg="gray", justify="right", width=6, state="disabled")
resultCounter.grid(row=1, column=96, pady=10, sticky="E", columnspan=5)

#Buttons
pauseButton=tk.Button(simulationWindow, text="PAUSE", width=10, height=2, font=("Arial"), command=lambda:eventPauseButton())
pauseButton.grid(row=11, column=0, pady=20, columnspan=33)

startButtonSW=tk.Button(simulationWindow, text="START", width=10, height=2, font=("Arial"), command=lambda:eventStartButtonSW())
startButtonSW.grid(row=11, column=34, pady=20, columnspan=34)

finishButton=tk.Button(simulationWindow, text="FINISH", width=10, height=2, font=("Arial"), command=lambda:eventFinishButton())
finishButton.grid(row=11, column=67, pady=20, columnspan=34)

resultButton=tk.Button(simulationWindow, text="RESULT", width=10, height=2, font=("Arial"), command=lambda:eventResultButton())
resultButton.grid(row=12, column=0, pady=20, columnspan=51)

closeButtonSW=tk.Button(simulationWindow, text="CLOSE", width=10, height=2, font=("Arial"), command=lambda:sgf.eventCloseButton(mainWindow))
closeButtonSW.grid(row=12, column=51, pady=20, columnspan=50)

#Draw empty ms in a queeu
for x in range(3):
    for y in range(100):
        emptyLabelDraw= tk.Label(simulationWindow, bg="red", width=1, height=3)
        emptyLabelDraw.grid(row=x+3, column=y+1)
    
