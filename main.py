num=int(input("Enter the number to check:"))

if num>50:
    print("The number is greater than 50")
    if num%2==0:
        print("And the number is even")
    else:
        print("The number is odd")
else:
        print("The number is smaller than 50")