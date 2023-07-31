
class Counter():
    Count=0
    Count=int(Count)
    flagCorrectAcsess=False
    def __init__(self):
        self.Count=0
        self.flagCorrectAcsess=False
    def add(self):
        try:
            if self.flagCorrectAcsess:
                self.Count+=1
            else:
                raise ValueError
        finally:
             self.flagCorrectAcsess=False
    def printCount(self):
        return self.Count
    def Acsess(self,boolean):
        self.flagCorrectAcsess=boolean


