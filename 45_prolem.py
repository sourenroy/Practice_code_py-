from random import randint

class train:

    def __init__(s, trainNo):
        s.trainNo = trainNo

    def book(s, fro , to):
        print(f"Ticket is booked in train no:{s.trainNo} from {fro} to {to}")
      

    def getstatus(s):
        print(f"Train no.{s.trainNo} is running on time")

    def getFare(s, fro, to):
        print(f"Ticket is booked in train no:{s.trainNo} from {fro} to {to} is {randint(222, 555)}")
    

t = train(12399)
t.book("DB", "Delhi")
t.getstatus()
t.getFare("DB", "Delhi")

