l1 = [0, 2, 3, 4, 5]
l2 = [7, 6, 0, 4, 5]
l3 = [10, 0, 8, 4, 5]

#type casting into sets

s1 =  set(l1)
s2 = set(l2)
s3 = set(l3)

print(s1)

#join intersection
s1s2 =s1.intersection(s2)
final_set=s1s2.intersection(s3)

final_list=list(final_set)
print(final_list)