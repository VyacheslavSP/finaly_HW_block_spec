from abc import  abstractmethod
from Animal import Animal

class pets(Animal):
    def __init__(self, Name, Date_birth):
        super().__init__(Name, Date_birth)
        setattr(self, "FlagSmallAnimal", True) ## добавили флаг домашнее животное
        setattr(self,'List_Commands_Pets',[])
    def getCommands(self):
        return self.List_Commands_Pets
