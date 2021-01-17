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
import View.shareGraphicFunctions as sgf
from View.resultWindows import *
from Controller.mlfq import *

result=[]
avgResponse=0.0
avgTurnAroundTime=0.0

#----------------------------------------------------------------------------------
# Functions to create the events for each button
#----------------------------------------------------------------------------------

#Function for Pause the simulation
def eventPauseButton():
    mb.showinfo(title="Pause Button", message="Estoy en el boton de pausa")
        
#Function for Start the simulation after pause, or since the begining
def eventStartButtonSW(jobA, jobB, jobC, queueQuantity, quantum, period):
    global result
    global avgResponse
    global avgTurnAroundTime

    #Taking Data
    #---This is just for now because this is additional data recover in the aditional windows
    jobA.setRunTime(30)
    jobB.setRunTime(20)
    jobC.setRunTime(50)

    #Create a JobList to execute the scheduler and the list to draw the graphic
    joblist={}
    joblist[0]=jobA
    joblist[1]=jobB
    joblist[2]=jobC
    timeList=[]
    jobList=[]
    queueList=[]
    
    #print("Cantidad de colas: ", queueQuantity, "Periodo S: ", period, "Quantum: ", quantum, sep=',')
    
    #Executing the scheduler
    scheduler=mlfq()
    scheduler.RunMLFQ(joblist, queueQuantity, period, quantum) #numero de cuotas, S y quantum 

    #Create the file to capture the result
    scheduler.statistics()
    avgResponse=scheduler.getResponseTimeAvg()
    avgTurnAroundTime=scheduler.getTurnAroundAvg()
    scheduler.infGraficaList(timeList, jobList, queueList)
    print(timeList[:])
    #scheduler.infGrafica(timeList, jobList, queueList)
    result=scheduler.getResults()

    #---After results we have to call the function wich draw the simulation with the pause, and finish button 



#Function to finish the simulation and display the final graphic
def eventFinishButton():
    mb.showinfo(title="Finish Button", message="Estoy en el boton de finish")

#Function for Result button, to display window result
def eventResultButton(jobA, jobB, jobC, simulationWindow, mainWindow):
    global result
    global avgResponse
    global avgTurnAroundTime
    drawResultWindow(jobA, jobB, jobC, simulationWindow, mainWindow, result, avgResponse, avgTurnAroundTime)

#Function to draw Simulation Window
def drawSimulationWindow(jobA, jobB, jobC, queueQuantity, quantum, period, aditionalDataWindow, mainWindow):
    aditionalDataWindow.withdraw()
    simulationWindow=tk.Toplevel()
    simulationWindow.title("MLFQ Simulation - Simulation Window")
    simulationWindow.resizable(False,False)
    simulationWindow.iconbitmap("icon.ico")
    simulationWindow.config(bg='#EAF6F5')
    simulationWindow.geometry('490x450+500+250')

    #Create the widgets and add them in a grid to add all the widgets needed in the right places
    #Labels
    tk.Label(simulationWindow,text="Simulation MLFQ", font=("Arial", 18), bg='#EAF6F5').grid(row=0, column=0, sticky="W", columnspan=3, padx=10, pady=10)
    tk.Label(simulationWindow,text="Counter(ms):", font=("Arial", 14), bg='#EAF6F5').grid(row=1, column=2, sticky="W", padx=10, pady=10)
    
    #---In this part of the grid should display the animation and graphic, it will be uploaded once we arrive to this point
    img=tk.PhotoImage(file="mlfq.png")
    tk.Label(simulationWindow,image=img).grid(row=2, column=0, sticky="W", padx=20, pady=10, columnspan=3)

    #Field - Entry
    resultCounter=tk.Entry(simulationWindow,text="Results", font=("Arial", 12), bg='#EAF6F5', fg="gray", justify="right", width=6, state="disabled")
    resultCounter.grid(row=1, column=2, padx=10, pady=10, sticky="E")

    #Buttons
    pauseButton=tk.Button(simulationWindow, text="PAUSE", width=10, height=2, font=("Arial"), command=lambda:eventPauseButton())
    pauseButton.grid(row=3, column=0, padx=10, pady=20)

    startButtonSW=tk.Button(simulationWindow, text="START", width=10, height=2, font=("Arial"), command=lambda:eventStartButtonSW(jobA, jobB, jobC, queueQuantity, quantum, period))
    startButtonSW.grid(row=3, column=1, padx=10, pady=20)

    finishButton=tk.Button(simulationWindow, text="FINISH", width=10, height=2, font=("Arial"), command=lambda:eventFinishButton())
    finishButton.grid(row=3, column=2, padx=10, pady=20)

    resultButton=tk.Button(simulationWindow, text="RESULT", width=10, height=2, font=("Arial"), command=lambda:eventResultButton(jobA, jobB, jobC, simulationWindow, mainWindow))
    resultButton.grid(row=4, column=0, padx=10, pady=20, columnspan=2)

    closeButtonSW=tk.Button(simulationWindow, text="CLOSE", width=10, height=2, font=("Arial"), command=lambda:sgf.eventCloseButton(mainWindow))
    closeButtonSW.grid(row=4, column=2, pady=20, sticky="W")