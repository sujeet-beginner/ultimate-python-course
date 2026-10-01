# Can you change the self.paramter inside a class to something else (say "harry"). Try changing self to "slf" or "harry" and see the effects
 # yes it works ; the program stil execute without error even if "self" is change "slf" or even by the other name " Harry" but mostly you used self to mantain readablility


from random import randint

class Train:

    def __init__(slf, trainNo):
        slf.trainNo = trainNo

    def book(self, fro, to):
        print(f"Ticket is booked in train no : {self.trainNo} from {fro} to {to}")
        
    def getStatus(self):
        print(f"Train no: {self.trainNo} is running on time")
        
    def getFare(self, fro, to):
        print(f"Ticket fare in train no: {self.trainNo} from {fro} to {to} is {randint(222, 5555)}")


t = Train(12399)
t.book("Latur", "Pune")
t.getStatus()
t.getFare("Latur", "Pune")
        