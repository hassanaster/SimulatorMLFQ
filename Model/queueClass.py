#----------------------------------------------------------------------------------
# Class queue: this class will manage all queues, attributes and behaivor during 
# the execution of the scheculer
#----------------------------------------------------------------------------------

#----------------------------------------------------------------------------------
# @Authors: Miriam Arango, Luisa Arboleda, Yeison Quinto
# @Version: Version 1.0
# @Date: 09 - 01 - 2021
#----------------------------------------------------------------------------------

class Queue():
    
    #Builder

    def __init__(self):
        #Initial Data
        self.__quantum=0
        self.__period=0
        #Result Data - It should be a list of 100 string var
        self.__result=[]
    
    #Setters
    def setQuantum(self, data):
        self.__quantum=data

    def setPeriod(self, data):
        self.__period=data

    def setResult(self, data):
        self.__result.append(data)
    
    #Getters
    def getQuantum(self):
        return self.__quantum
    
    def getPeriod(self):
        return self.__period
    
    def getResult(self, p):
        return self.__result[p]