#----------------------------------------------------------------------------------
# Module main.py: Here we use package frome View, Controllers and Model package
#----------------------------------------------------------------------------------

#----------------------------------------------------------------------------------
# @Authors: Miriam Arango, Luisa Arboleda, Yeison Quinto
# @Version: Version 1.0
# @Date: 08 - 01 - 2021
#----------------------------------------------------------------------------------

from View.mainWindow import *

#We draw the first window to obtain the main data
drawMainWindow()

#We obtain the quantity of job and queue that user is needing to simulate
queue=getQueue()
job=getJob()

#We set initial data in "" for the main window
print(queue, job, sep= ", ")
setInit()

#We draw the second window
