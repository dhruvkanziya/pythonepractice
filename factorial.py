#function for caluclating  factorial of number 
def factorial(n):
    ans = 1
    if n == 0:
        ans = 1
    else:
        for i in range(1,n+1):
            ans*= i
    return ans


n = int(input("Ente the number :"))

output= factorial(n)
print("then factorial is :", output)