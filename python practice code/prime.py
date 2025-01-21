n=int(input("enter the n1:"))

if (n==1):
    print("it is not a prime number")
    
if n>1:
    for i in range(2,n):
        if (n % i == 0):
            print("this is not a prime number")
            break
    else:
        print("it is a prime number")

