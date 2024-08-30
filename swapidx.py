n = int(input("Enter size of list :"))

list = []

for i in range(n):
    num = int(input())
    list.append(num)

idx1 = int(input("Enter index 1 which you want to swap:"))
idx2 = int(input("Enter index 2 which you want to swap:"))
print(list)

#swapping values
temp = list[idx1]
list[idx1] = list[idx2]
list[idx2] = temp

print(list)