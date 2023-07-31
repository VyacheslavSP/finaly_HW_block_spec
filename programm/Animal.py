from abc import ABC, abstractmethod
import uuid

class Animal(ABC):
    def __init__(self,Name,Date_birth):   ## при создание людого ID,Имя,Дата рождения присваевается всем без исключения 
        self.ID = uuid.uuid4()  
        self.Name = Name
        self.Date_birth=Date_birth
    def getName(self):
        return self.Name
    def getDate_birth(self):
        return self.Date_birth
    def getID(self):
        return self.ID

        
        
