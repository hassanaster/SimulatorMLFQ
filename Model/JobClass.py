#----------------------------------------------------------------------------------
# Class job: this class will manage all jobs, attributes and behaivor during 
# the execution of the scheculer
#----------------------------------------------------------------------------------

#----------------------------------------------------------------------------------
# @Authors: Miriam Arango, Luisa Arboleda, Yeison Quinto
# @Version: Version 1.0
# @Date: 09 - 01 - 2021
#----------------------------------------------------------------------------------

class Job():

    #Builder
    def __init__(self):

        #Initial Attributes
        self.__quantity=0
        self.__priority=3
        self.__arrivalTime=0
        self.__runTime=0
        self.__ioTime=0
        self.__startIoTime=0
        
        #Result Attributes
        self.__jobStatus=2
        self.__turnAround=0.0
        self.__responsiveTime=0.0
    
    #Setters
    def setQuantity(self, data):
        self.__quantity=data

    def setPriority(self, data):
        self.__priority=data

    def setArrivalTime(self, data):
        self.__arrivalTime=data

    def setRunTime(self, data):
        self.__runTime=data

    def setIoTime(self, data):
        self.__ioTime=data

    def setStartIoTime(self, data):
        self.__startIoTime=data
    
    def setJobStatus(self, data):
        self.__jobStatus=data

    def setTurnAround(self, data):
        self.__turnAround=data

    def setResponsiveTime(self, data):
        self.__responsiveTime=data
    
    #Getters
    def getQuantity(self):
        return self.__quantity

    def getPriority(self):
        return self.__priority
    
    def getArrivalTime(self):
        return self.__arrivalTime
    
    def getRunTime(self):
        return self.__runTime
    
    def getIoTime(self):
        return self.__ioTime
    
    def getStartIoTime(self):
        return self.__startIoTime

    def getJobStatus(self):
        return self.__jobStatus

    def getTurnAround(self):
        return self.__turnAround

    def getResponsiveTime(self):
        return self.__responsiveTime


"""Create an object

jobA=Job()
jobA.priority

para poder referirse a un atributo dentro de un metodo 
self.arrivalTime=8"""