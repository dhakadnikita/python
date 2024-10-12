class Train:
    def book(self):
        print(f"Ticket is booked in train no :{self.trianNo}from {fro} to {to}")

    def getStatus(self,fro,to):
        print(f"Train no {self.trainNo} is running on time")

    def getFare(self,fro,to):
        print(f"Ticket fare is in train no : {self.trainNo} from {fro} to {to} is {randint(222,5555)}")

    t = Train(1234599)
    t.book("Rampur","Delhi")
    t.getStatus()
    t.getFare("")

    
    