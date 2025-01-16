#Write a Python program to check whether a number entered by the user is greater than 50 or not. Also, if it is greater than 50, then check whether it is odd or even.

num=int(input("Enter a number"))

if num<50:
    print("The number is small")


else:
    print("The number is bigger than 50")
    if num%2==0:
        print(" and is even")
    else:
        print(" andthe number is odd")
