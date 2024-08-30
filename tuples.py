colours = ("red", "green", "yellow")

# fruit= ("orange,")

# print(type(fruit))
# print(len(colours))

# print(colours[-1])
# print(colours[1])

if "green" in colours:
    print("Green is the part of the list")  

more_colors = ("orange", "brown", "violet")
coloore = colours + more_colors 
print(coloore)


#unpacking a tuple
colur1, colours1, colours2 = colours

print(colur1,colours2)