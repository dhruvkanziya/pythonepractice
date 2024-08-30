def sum_To_N(n):

    #base case 
    if n==1:
        return 1
    
        #recursive case
    ans = n+sum_To_N(n-1)
    return ans

n = int(input("Enter n: "))
print(sum_To_N(n))