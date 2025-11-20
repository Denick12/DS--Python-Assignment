# variables
name = 'Denick'
print(name)
a = 10
b = 3.14
print(a)
is_student = True 
print("Am I a student?", is_student)
print(is_student)
x = None
print(x)
print(type(x))
m = 5
n = 8 
print(m)
print(n)

m =8
print(m)

# conditional_statements
num = int(input('Enter a Number: '))
if num > 0:
    print('Its Positive')
else:
    print('Its Negative')

dgt = int(input('Enter a number: '))
if dgt % 2 == 0:
    print("Its Even Number")
else:
   print("Its Odd Number") 

age = int(input('Please Enter your age: '))
if age >= 18:
    print('You are eligible to vote')
else:
    print('You are under age')

temp = int(input('Enter the temperature readings on the thermometer: '))
if temp > 30:
    print('Hot')
elif 15 <=temp <=30:
    print('Warm')
else:
    print('Cold')

# lists
fruits = ['apple', 'banana','cherry']
print(fruits)
print(fruits[2])

fruits.append('Oranges')
print(fruits)
fruits.remove('banana')
print(fruits)

numbers = [1,2,3,4,5,6]
print(sum(numbers))
