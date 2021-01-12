#----------------------------------------------------------------------------------
# Result Window: Finishing the simulation, user is avalaible to see the results and the end grafic
# Results display in the siftware for each job (job status, turn around and responsive time)
#----------------------------------------------------------------------------------

#----------------------------------------------------------------------------------
# @Authors: Miriam Arango, Luisa Arboleda, Yeison Quinto
# @Version: Version 1.0
# @Date: 06 - 01 - 2021
#----------------------------------------------------------------------------------

import tkinter as tk
import tkinter.messagebox as mb

#Window or root: First we should create the root or window
resultWindow=tk.Tk()
resultWindow.title("MLFQ Simulation - Result Window")
resultWindow.resizable(False,False)
resultWindow.iconbitmap("/icon.ico")

#Frame, container or first widget: After this we create the frame where we are going to put the widgets needed for this window
frameresultWindow=tk.Frame()
frameresultWindow.pack()
frameresultWindow.config(width="800", height="800")
frameresultWindow['bg']='#EAF6F5'

#Create the widgets and add them in a grid to add all the widgets needed in the right places
#Labels
tk.Label(frameresultWindow,text="Simulation MLFQ", font=("Arial", 18), bg='#EAF6F5').grid(row=0, column=0, sticky="W", columnspan=4, padx=10, pady=10)
tk.Label(frameresultWindow,text="Counter(ms):", font=("Arial", 14), bg='#EAF6F5').grid(row=1, column=2, sticky="E", padx=10, pady=10)

#---In this part of the grid should display the animation and graphic, it will be uploaded once we arrive to this point
img=tk.PhotoImage(file="mlfq.png")
tk.Label(frameresultWindow,image=img).grid(row=2, column=0, sticky="W", padx=20, pady=10, columnspan=4)

tk.Label(frameresultWindow,text="Job Status", font=("Arial", 14), bg='#EAF6F5').grid(row=3, column=1, sticky="W", padx=10, pady=10)
tk.Label(frameresultWindow,text="Turn Around", font=("Arial", 14), bg='#EAF6F5').grid(row=3, column=2, sticky="W", padx=10, pady=10)
tk.Label(frameresultWindow,text="Responsive Time", font=("Arial", 14), bg='#EAF6F5').grid(row=3, column=3, sticky="W", padx=10, pady=10)
tk.Label(frameresultWindow,text="Job A:", font=("Arial", 14), bg='#EAF6F5').grid(row=4, column=0, sticky="E", padx=10, pady=10)
tk.Label(frameresultWindow,text="Job B:", font=("Arial", 14), bg='#EAF6F5').grid(row=5, column=0, sticky="E", padx=10, pady=10)
tk.Label(frameresultWindow,text="Job C:", font=("Arial", 14), bg='#EAF6F5').grid(row=6, column=0, sticky="E", padx=10, pady=10)

#Field - Entry
resultCounter=tk.Entry(frameresultWindow, state="disabled", font=("Arial", 12), bg='#EAF6F5', fg="gray", justify="right", width=6)
resultCounter.grid(row=1, column=3, padx=10, pady=10, sticky="W")

#JOB A
statusJobAField=tk.Entry(frameresultWindow, font=("Arial"), fg="gray", width=10, state="disabled", justify="center")
statusJobAField.grid(row=4, column=1, padx=10, pady=10)

aroundJobAField=tk.Entry(frameresultWindow, font=("Arial"), fg="gray", width=10, state="disabled", justify="center")
aroundJobAField.grid(row=4, column=2, padx=10, pady=10)

responsiveJobAField=tk.Entry(frameresultWindow, font=("Arial"), fg="gray", width=10, state="disabled", justify="center")
responsiveJobAField.grid(row=4, column=3, padx=10, pady=10)

#JOB B
statusJobBField=tk.Entry(frameresultWindow, font=("Arial"), fg="gray", width=10, state="disabled", justify="center")
statusJobBField.grid(row=5, column=1, padx=10, pady=10)

aroundJobBField=tk.Entry(frameresultWindow, font=("Arial"), fg="gray", width=10, state="disabled", justify="center")
aroundJobBField.grid(row=5, column=2, padx=10, pady=10)

responsiveJobBField=tk.Entry(frameresultWindow, font=("Arial"), fg="gray", width=10, state="disabled", justify="center")
responsiveJobBField.grid(row=5, column=3, padx=10, pady=10)

#JOB C
statusJobCField=tk.Entry(frameresultWindow, font=("Arial"), fg="gray", width=10, state="disabled", justify="center")
statusJobCField.grid(row=6, column=1, padx=10, pady=10)

aroundJobCField=tk.Entry(frameresultWindow, font=("Arial"), fg="gray", width=10, state="disabled", justify="center")
aroundJobCField.grid(row=6, column=2, padx=10, pady=10)

responsiveJobCField=tk.Entry(frameresultWindow, font=("Arial"), fg="gray", width=10, state="disabled", justify="center")
responsiveJobCField.grid(row=6, column=3, padx=10, pady=10)

#Buttons
begginingButton=tk.Button(frameresultWindow, text="GO TO MAIN", width=14, height=3, font=("Arial"))
begginingButton.grid(row=7, column=0, padx=10, pady=20, columnspan=2, sticky="E")

closeButton=tk.Button(frameresultWindow, text="CLOSE", width=14, height=3, font=("Arial"))
closeButton.grid(row=7, column=2, padx=40, pady=20, columnspan=2, sticky="W")

#Should be always in the end of the file
resultWindow.mainloop()