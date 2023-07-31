from abc import  abstractmethod
from Animal import Animal

class pack_annimal(Animal):
    def __init__(self, Name, Date_birth):
        super().__init__(Name, Date_birth)
        setattr(self, "FlagSmallAnimal", False) ## добавили флаг домашнее животное
        setattr(self,'List_Commands_Pack_Animal',[])
    def getCommands(self):
        return self.List_Commands_Pack_Animal   # а вот списки команд разбиты специально, чтобы когда хомяк вдруг стал ездовым он забыл все свои команды