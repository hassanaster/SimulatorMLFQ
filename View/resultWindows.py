#----------------------------------------------------------------------------------
# Result Window: Finishing the simulation, user is avalaible to see the results and the end grafic
# Results display in the siftware for each job (job status, turn around and responsive time)
#----------------------------------------------------------------------------------

#----------------------------------------------------------------------------------
# @Authors: Miriam Arango, Luisa Arboleda, Yeison Quinto
# @Version: Version 1.0
# @Date: 06 - 01 - 2021
# @Last modify Date: 14 - 01 - 2021
#----------------------------------------------------------------------------------

import tkinter as tk
import tkinter.messagebox as mb
import View.shareGraphicFunctions as sgf

#----------------------------------------------------------------------------------
# Functions to create the events for each button
#----------------------------------------------------------------------------------

def drawResultWindow(jobA, jobB, jobC, queueA, queueB, queueC, simulationWindow, mainWindow):
    simulationWindow.withdraw()
    resultWindow=tk.Toplevel()
    resultWindow.title("MLFQ Simulation - Result Window")
    resultWindow.resizable(False,False)
    resultWindow.iconbitmap("/icon.ico")
    resultWindow.config(bg='#EAF6F5')
    resultWindow.geometry('480x600+500+150')

    #Create the widgets and add them in a grid to add all the widgets needed in the right places
    #Labels
    tk.Label(resultWindow,text="Simulation MLFQ", font=("Arial", 18), bg='#EAF6F5').grid(row=0, column=0, sticky="W", columnspan=4, padx=10, pady=10)
    tk.Label(resultWindow,text="Counter(ms):", font=("Arial", 14), bg='#EAF6F5').grid(row=1, column=2, sticky="E", padx=10, pady=10)

    #---In this part of the grid should display the animation and graphic, it will be uploaded once we arrive to this point
    img=tk.PhotoImage(file="mlfq.png")
    tk.Label(resultWindow,image=img).grid(row=2, column=0, sticky="W", padx=20, pady=10, columnspan=4)

    tk.Label(resultWindow,text="Job Status", font=("Arial", 14), bg='#EAF6F5').grid(row=3, column=1, sticky="W", padx=10, pady=10)
    tk.Label(resultWindow,text="Turn Around", font=("Arial", 14), bg='#EAF6F5').grid(row=3, column=2, sticky="W", padx=10, pady=10)
    tk.Label(resultWindow,text="Responsive Time", font=("Arial", 14), bg='#EAF6F5').grid(row=3, column=3, sticky="W", padx=10, pady=10)
    tk.Label(resultWindow,text="Job A:", font=("Arial", 14), bg='#EAF6F5').grid(row=4, column=0, sticky="E", padx=10, pady=10)
    tk.Label(resultWindow,text="Job B:", font=("Arial", 14), bg='#EAF6F5').grid(row=5, column=0, sticky="E", padx=10, pady=10)
    tk.Label(resultWindow,text="Job C:", font=("Arial", 14), bg='#EAF6F5').grid(row=6, column=0, sticky="E", padx=10, pady=10)

    #Field - Entry
    resultCounter=tk.Entry(resultWindow, state="disabled", font=("Arial", 12), bg='#EAF6F5', fg="gray", justify="right", width=6)
    resultCounter.grid(row=1, column=3, padx=10, pady=10, sticky="W")

    #JOB A
    statusJobAField=tk.Entry(resultWindow, font=("Arial"), fg="gray", width=10, state="disabled", justify="center")
    statusJobAField.grid(row=4, column=1, padx=10, pady=10)

    aroundJobAField=tk.Entry(resultWindow, font=("Arial"), fg="gray", width=10, state="disabled", justify="center")
    aroundJobAField.grid(row=4, column=2, padx=10, pady=10)

    responsiveJobAField=tk.Entry(resultWindow, font=("Arial"), fg="gray", width=10, state="disabled", justify="center")
    responsiveJobAField.grid(row=4, column=3, padx=10, pady=10)

    #JOB B
    statusJobBField=tk.Entry(resultWindow, font=("Arial"), fg="gray", width=10, state="disabled", justify="center")
    statusJobBField.grid(row=5, column=1, padx=10, pady=10)

    aroundJobBField=tk.Entry(resultWindow, font=("Arial"), fg="gray", width=10, state="disabled", justify="center")
    aroundJobBField.grid(row=5, column=2, padx=10, pady=10)

    responsiveJobBField=tk.Entry(resultWindow, font=("Arial"), fg="gray", width=10, state="disabled", justify="center")
    responsiveJobBField.grid(row=5, column=3, padx=10, pady=10)

    #JOB C
    statusJobCField=tk.Entry(resultWindow, font=("Arial"), fg="gray", width=10, state="disabled", justify="center")
    statusJobCField.grid(row=6, column=1, padx=10, pady=10)

    aroundJobCField=tk.Entry(resultWindow, font=("Arial"), fg="gray", width=10, state="disabled", justify="center")
    aroundJobCField.grid(row=6, column=2, padx=10, pady=10)

    responsiveJobCField=tk.Entry(resultWindow, font=("Arial"), fg="gray", width=10, state="disabled", justify="center")
    responsiveJobCField.grid(row=6, column=3, padx=10, pady=10)

    #Buttons
    closeButton=tk.Button(resultWindow, text="CLOSE", width=12, height=2, font=("Arial"), command=lambda:sgf.eventCloseButton(mainWindow))
    closeButton.grid(row=7, column=0, padx=40, pady=20, columnspan=4)