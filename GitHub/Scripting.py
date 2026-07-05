# 1] Calculation of 2 Numbers:

# It is mandatory to give datatype as int bcoz while doing sub it takes the value as str.

# No1 = 0
# No2 = 0 - This will Initialize the datatype as Integer
No1 = int(input("Enter the First Number :"))
No2 = int(input("Enter the Second Number :"))

Add = No1 + No2     
# Add = int(No1) + int(No2) - Another method of Initializing DataType as Int.
print("Addition is :", Add)

Sub = No1 - No2
print("Substraction is :", Sub)

Mul = No1 * No2
print("Multiplication is :", Mul)

Div = No1 / No2
print("Division is :", Div)
print("-" * 40)

# Sequence Building blocks :

# If-else :

Age = int(input("Enter Your Age :"))

if(Age < 18):
    print("Sorry you are not allowed!")
else:
    print("Welcome to the movie!")
print("-" * 40)

# If-elif-else :

print("-" * 41)
print("---------Ticket Pricing Software---------")
print("-" * 41)

Age = int(input("Enter Your Age :"))

if(Age <= 5):
    print("Free Entry")
elif(Age > 5 and Age <= 18):
    print("Ticket Price : 900")
elif(Age > 18 and Age <= 40):
    print("Ticket Price : 1200")
else:
    print("Ticket Price : 500")
print("-" * 40)

# Iteration Building blocks :

# while loop :

count = 0

while(count <= 5):
    print("JAY GANESH...!")
    count = count + 1
print("-" * 40)

# for loop(message) :

for i in range(5):
    print("JAY GANESH...!")
print("-" * 40)   

# for loop(Index numbers) :

for i in range(5):
    print(i)
print("-" * 40)





