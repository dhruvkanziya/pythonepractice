names = {"sia","tia","mia"}
print(names)

print(len(names))
print(type(names))

#print(names[0])  indexing is not supported
for x in names:
     print(x)


if "sia" in names:
    print("sia in name available")


names.add("ria")
print(names)


#updating function
names_list = ["ria","kia"]
names.update(names_list)
print(names)

# #removeing function
# names.remove("ria")
# print(names)

#joining sets
s1={'d','e','f','g','h',}
s2={'a','b','c',}
# print(s2,s1)

# s3=s2.union(s1)
# print(s3)
# s2.update(s1)
# print(s2)


#keep only duplicates while joining sets
s1.intersection_update(s2)
print(s1)

#keep only duplicates while joining sets
s1.symmetric_difference_update(s2)
print(s1)