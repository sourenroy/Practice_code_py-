a1 = int(input("Enter a Number :"))
a2 = int(input("Enter a Number :"))
a3 = int(input("Enter a Number :"))
a4 = int(input("Enter a Number :"))

if(a1>a2 and a1>a3 and a1>a4):
    print("The Greatest number is :",a1)

elif(a2>a1 and a2>a3 and a2>a4):
    print("The Greatest number is :",a2)

elif(a3>a2 and a3>a1 and a3>a4):
    print("The Greatest number is :",a3)

elif(a4>a2 and a4>a3 and a4>a1):
    print("The Greatest number is :",a4)
    
else:
    print("Nothing is greater")
