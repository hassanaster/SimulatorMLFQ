#----------------------------------------------------------------------------------
# Result Window: Finishing the simulation, user is avalaible to see the results and the end grafic
# Results display in the siftware for each job (job status, turn around and responsive time)
#----------------------------------------------------------------------------------

#----------------------------------------------------------------------------------
# @Authors: Miriam Arango, Luisa Arboleda, Yeison Quinto
# @Version: Version 1.0
# @Date: 06 - 01 - 2021
# @Last modify Date: 16 - 01 - 2021
#----------------------------------------------------------------------------------

import tkinter as tk
import tkinter.messagebox as mb
import View.shareGraphicFunctions as sgf

#----------------------------------------------------------------------------------
# Functions to create the events for each button
#----------------------------------------------------------------------------------

def drawResultWindow(jobA, jobB, jobC, queue, simulationWindow, mainWindow):
    simulationWindow.withdraw()
    resultWindow=tk.Toplevel()
    resultWindow.title("MLFQ Simulation - Result Window")
    resultWindow.resizable(False,False)
    resultWindow.iconbitmap("/icon.ico")
    resultWindow.config(bg='#EAF6F5')
    resultWindow.geometry('560x690+500+100')

    #Create the widgets and add them in a grid to add all the widgets needed in the right places
    #Labels
    tk.Label(resultWindow,text="Simulation Results ", font=("Arial", 18), bg='#EAF6F5').grid(row=0, column=0, sticky="W", columnspan=4, padx=10, pady=10)
    tk.Label(resultWindow,text="Scheduler Results each milisecond.* ", font=("Arial", 10), bg='#EAF6F5', fg="gray").grid(row=1, column=0, padx=10, columnspan=4)

    tk.Label(resultWindow,text="Final Data results* ", font=("Arial", 10), bg='#EAF6F5', fg="gray").grid(row=3, column=0, padx=10, pady=10, columnspan=4)    
    
    tk.Label(resultWindow,text="Job Status", font=("Arial", 14), bg='#EAF6F5').grid(row=4, column=1, sticky="W", padx=10, pady=10)
    tk.Label(resultWindow,text="Turn Around", font=("Arial", 14), bg='#EAF6F5').grid(row=4, column=2, sticky="W", padx=10, pady=10)
    tk.Label(resultWindow,text="Responsive Time", font=("Arial", 14), bg='#EAF6F5').grid(row=4, column=3, sticky="W", padx=10, pady=10)
    
    tk.Label(resultWindow,text="Job A:", font=("Arial", 14), bg='#EAF6F5').grid(row=5, column=0, sticky="E", padx=10, pady=10)
    tk.Label(resultWindow,text="Job B:", font=("Arial", 14), bg='#EAF6F5').grid(row=6, column=0, sticky="E", padx=10, pady=10)
    tk.Label(resultWindow,text="Job C:", font=("Arial", 14), bg='#EAF6F5').grid(row=7, column=0, sticky="E", padx=10, pady=10)
    tk.Label(resultWindow,text="Average:", font=("Arial", 14), bg='#EAF6F5').grid(row=8, column=0, sticky="E", padx=10, pady=10)

    #Text widget to add results
    textResults=tk.Text(resultWindow, font=("Arial", 14), fg="gray", width=75, height=16, bg='#EAF6F5', cursor="arrow", highlightcolor='#EAF6F5')
    textResults.grid(row=2, column=0, pady=10, padx=10, columnspan=4)
    textResults.insert("insert", "Here we are going to write all data result per ms")

    #Scroll bar
    scrollYTextResults=tk.Scrollbar(resultWindow, command=textResults.yview)
    scrollYTextResults.grid(row=2, column=0, pady=10, sticky="NSE", columnspan=4)
    textResults.config(yscrollcommand=scrollYTextResults.set)
    
    #Fields or Entries
    #JOB A
    statusJobAField=tk.Entry(resultWindow, font=("Arial"), fg="gray", width=10, state="disabled", justify="center", cursor="arrow")
    statusJobAField.grid(row=5, column=1, padx=10, pady=10)

    aroundJobAField=tk.Entry(resultWindow, font=("Arial"), fg="gray", width=10, state="disabled", justify="center", cursor="arrow")
    aroundJobAField.grid(row=5, column=2, padx=10, pady=10)

    responsiveJobAField=tk.Entry(resultWindow, font=("Arial"), fg="gray", width=10, state="disabled", justify="center", cursor="arrow")
    responsiveJobAField.grid(row=5, column=3, padx=10, pady=10)

    #JOB B
    statusJobBField=tk.Entry(resultWindow, font=("Arial"), fg="gray", width=10, state="disabled", justify="center", cursor="arrow")
    statusJobBField.grid(row=6, column=1, padx=10, pady=10)

    aroundJobBField=tk.Entry(resultWindow, font=("Arial"), fg="gray", width=10, state="disabled", justify="center", cursor="arrow")
    aroundJobBField.grid(row=6, column=2, padx=10, pady=10)

    responsiveJobBField=tk.Entry(resultWindow, font=("Arial"), fg="gray", width=10, state="disabled", justify="center", cursor="arrow")
    responsiveJobBField.grid(row=6, column=3, padx=10, pady=10)

    #JOB C
    statusJobCField=tk.Entry(resultWindow, font=("Arial"), fg="gray", width=10, state="disabled", justify="center", cursor="arrow")
    statusJobCField.grid(row=7, column=1, padx=10, pady=10)

    aroundJobCField=tk.Entry(resultWindow, font=("Arial"), fg="gray", width=10, state="disabled", justify="center", cursor="arrow")
    aroundJobCField.grid(row=7, column=2, padx=10, pady=10)

    responsiveJobCField=tk.Entry(resultWindow, font=("Arial"), fg="gray", width=10, state="disabled", justify="center", cursor="arrow")
    responsiveJobCField.grid(row=7, column=3, padx=10, pady=10)

    #Average
    aroundAverage=tk.Entry(resultWindow, font=("Arial"), fg="gray", width=10, state="disabled", justify="center", cursor="arrow")
    aroundAverage.grid(row=8, column=2, padx=10, pady=10)

    responsiveAverage=tk.Entry(resultWindow, font=("Arial"), fg="gray", width=10, state="disabled", justify="center", cursor="arrow")
    responsiveAverage.grid(row=8, column=3, padx=10, pady=10)

    #Buttons
    closeButton=tk.Button(resultWindow, text="CLOSE", width=12, height=2, font=("Arial"), command=lambda:sgf.eventCloseButton(mainWindow))
    closeButton.grid(row=9, column=0, padx=40, pady=20, columnspan=4)