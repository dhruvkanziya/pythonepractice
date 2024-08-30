def sumOneToN(n):
    sum = 0
    for i in range(1,n+1):
        sum = sum + i
    return sum

n = int(input("Enter n: "))
output =sumOneToN(n)
print("Sum of all numbers till n is ",output)
n1 = int(input("Enter n1: "))
output2 =sumOneToN(n1)
print("Sum of all numbers till N is ",output2)