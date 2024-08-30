num1 = int(input("Enter number 1 :"))
num2 = int(input("Enter number 2 :"))
num3 = int(input("Enter number 3 :"))

# if num1>num2 and num1>num3 :
#     print(num1,"Number  is greatest number from your entered number")

# elif num2>num1 and num2>num3:
#     print(num2,"Number  is greatest")

# else:
#     print(num3,"Number  is greatest number")


#another way

if num1 >num2:
    if num1 >num3:
        print(num1,"is greatest element")
    else:
        print(num3,"is the greatest number")

else:
    if num2 > num3:
        print(num2,"is the greatest element")
    else:
        print(num3,"is the greatest element")

