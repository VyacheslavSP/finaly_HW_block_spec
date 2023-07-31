from Pets import pets
class Cat(pets):
    def setName(self,Name):  
        self.Name = Name
    def setCommands(self,command):
        self.getCommands().append(command)