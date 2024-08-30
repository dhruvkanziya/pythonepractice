fruits = ["applle","mango","banana","cherry","orange"]
print(fruits)
print(type(fruits))
print(len(fruits))

# if "banana" in fruits:
#     print("Banana is the part of the list")

# #indexing in list
#     print(fruits[1])
#     print(fruits[-3])
#     print(fruits[1:3])

# fruits.insert(2,"watermelon") #insert me hum jahaa chae vaha pe insert  karva sakte hai items ko
# fruits.append("kiwi") #append se sirf end me hi add hote hai
# more_fruits = ["melon","strawberry"]
# fruits.extend(more_fruits)  #fruits me do arrey ko add karva saakte haai or do array merge ho ke ek bada arrayy baan jata hain
# fruits.pop(0)  #pop use to delete elemnt in array
# fruits.remove("banana") #isme jo element me name likha ho vo deleate ho jata hain
# print(fruits)
 

#  #changing items in list
# fruits[3]="watermelon"

# #sorting
# fruits.sort() #by default it sorting in ascending oreder
# fruits.sort(reverse=True) #sorting in desending oreder
# print(fruits)
# fruits.reverse()
# print(fruits)

#list compheration
new_fruits= [fruit for fruit in  fruits if "a" in fruit]
print(new_fruits)

#copy of list
new_fruits =fruits.copy()
print(new_fruits)   