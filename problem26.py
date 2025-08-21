n = int(input("Enter a Num :"))

for i in range(2,n):
    if(n%i) == 0:
        print("Number is not prime")
        break
else:
    print("It's a Prime Number")