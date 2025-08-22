class animals:
    pass

class pets(animals):
    pass

class dog:
    @staticmethod
    def barks():
        print("Bhow Bhow")

d = dog()

d.barks()