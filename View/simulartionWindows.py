#----------------------------------------------------------------------------------
# Simulation Window: After get all data needed, user is avalaible to simulate MFLQ 
# This window show graphic the simulation in miliseconds how MFLQ works
#----------------------------------------------------------------------------------

#----------------------------------------------------------------------------------
# @Authors: Miriam Arango, Luisa Arboleda, Yeison Quinto
# @Version: Version 1.0
# @Date: 04 - 01 - 2021
#----------------------------------------------------------------------------------

import tkinter as tk
import tkinter.messagebox as mb

#Window or root: First we should create the root or window
simulationWindow=tk.Tk()
simulationWindow.title("MLFQ Simulation - Simulation Window")
simulationWindow.resizable(False,False)
simulationWindow.iconbitmap("/icon.ico")

#Frame, container or first widget: After this we create the frame where we are going to put the widgets needed for this window
frameSimulationWindow=tk.Frame()
frameSimulationWindow.pack()
frameSimulationWindow.config(width="800", height="800")
frameSimulationWindow['bg']='#EAF6F5'

#Create the widgets and add them in a grid to add all the widgets needed in the right places
#Labels
tk.Label(frameSimulationWindow,text="Simulation MLFQ", font=("Arial", 18), bg='#EAF6F5').grid(row=0, column=0, sticky="W", columnspan=3, padx=10, pady=10)
tk.Label(frameSimulationWindow,text="Counter(ms):", font=("Arial", 14), bg='#EAF6F5').grid(row=1, column=2, sticky="W", padx=10, pady=10)
#---In this part of the grid should display the animation and graphic, it will be uploaded once we arrive to this point
img=tk.PhotoImage(file="mlfq.png")
tk.Label(frameSimulationWindow,image=img).grid(row=2, column=0, sticky="W", padx=20, pady=10, columnspan=3)

#Field - Entry
resultCounter=tk.Entry(frameSimulationWindow,text="Results", font=("Arial", 12), bg='#EAF6F5', fg="gray", justify="right", width=6, state="disabled")
resultCounter.grid(row=1, column=2, padx=10, pady=10, sticky="E")

#Buttons
pauseButton=tk.Button(frameSimulationWindow, text="PAUSE", width=10, height=2, font=("Arial"))
pauseButton.grid(row=3, column=0, padx=10, pady=20)

startButtonSW=tk.Button(frameSimulationWindow, text="START", width=10, height=2, font=("Arial"))
startButtonSW.grid(row=3, column=1, padx=10, pady=20)

finishButton=tk.Button(frameSimulationWindow, text="FINISH", width=10, height=2, font=("Arial"))
finishButton.grid(row=3, column=2, padx=10, pady=20)

#Should be always in the end of the file
simulationWindow.mainloop()