class calculator:
    def __init__(s, n):
        s.n = n

    def square(s):
        print(f"The square is {s.n*s.n}")
    def cube(s):
        print(f"The cube is {s.n*s.n*s.n}")
    def root(s):
        print(f"The squareroot is {s.n**1/2}")

a = calculator(4)
a.square()
a.cube()
a.root()