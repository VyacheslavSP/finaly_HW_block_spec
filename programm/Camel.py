from PackAnimal import pack_annimal
class Camel(pack_annimal):
    def setName(self,Name):  
        self.Name = Name
    def setCommands(self,command):
        self.getCommands().append(command)