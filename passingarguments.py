#pass by value

def addOne(x):
    x = x + 1
    print("Inside function :",x) 


x = 5
addOne(x)
print("Outside function:",x)

#pass by reference
def modifylist(lst):
    lst.append(4)
    print("inside function list",lst)

lst = [1, 2, 3]
modifylist(lst)
print("outside function list:",lst)  