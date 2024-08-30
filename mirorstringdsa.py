input_string = input("Enter string :")
n = int(input("Enter n :"))

#creating the dictionary for mirror operations
alphabates ="abcdefghijklmnopqrstuvwxyz"
reverse_alphabates = alphabates[::-1]   
dict1 = dict(zip(alphabates, reverse_alphabates))

#creating the part of string which we will do mirror operation
prefix = input_string[0:n-1]
suffix = input_string[n-1:]

#finding the mirror string
mirror = ""
for i in range(0,len(suffix)):
    mirror = mirror + dict1[suffix[i]]

#creating the final string
res = prefix + mirror
print("The result is: ",res)
