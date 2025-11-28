# creating a list of fruits
fruits = ["pawpaw", "oranges", "ovacodo", "grapes"]
print(fruits)

# add mango to fruits list
fruits.append("mango")
print(fruits)
# remove the second item from the list
fruits.remove("oranges")
print(fruits)

fruits.append("oranges")
print(fruits)

# removing the second item in the list using pop(dynamically)
fruits.pop(1)
print(fruits)

# 
numbers = [1,2,3,4,5,6,6,7,8,8,9,0]
print(numbers[-1],[1])

colors = ["green", "blue", "purple", "white"]
print(colors)
colors[1] = "purple"
print(colors)
print(len(colors))

print(colors[2])

# Write a program that checks if apple is in the fruit list

for i in fruits:
    if fruits == "apple":
        print("apple is  present")
    else:
        print("No apple")





