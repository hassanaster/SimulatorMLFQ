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
        self.__quantity=0
        self.__quantum=0
        self.__period=0
        #Result Data - It should be a list of 100 string var
        self.__result={}
    
    #Setters

    def setQuantity(self, data):
        self.__quantity=data

    def setQuantum(self, data):
        self.__quantum=data

    def setPeriod(self, data):
        self.__period=data

    def setResult(self, data):
        self.__result=data
    
    #Getters
    def getQuantity(self):
        return self.__quantity

    def getQuantum(self):
        return self.__quantum
    
    def getPeriod(self):
        return self.__period
    
    def getResult(self):
        return self.__result