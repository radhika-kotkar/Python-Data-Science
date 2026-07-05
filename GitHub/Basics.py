print("JAY GANESH...!")

# Number DataType :

x = 11
y = 21.0
z = 8 + 6j

print(x)    
print(type(x))      # Int
print(id(x))
print("-" * 40)

print("Value of y is :", y) 
print("Type of y is :",type(y))      # Float
print("ID of y is :",id(y))
print("-" * 40)

print(z)   
print(type(z))      # Complex - "j" Imaginary Constant
print(id(z))
print("-" * 40)

# Sequence DataType :

Data1 = [20,40,60,80]
Data2 = (20,40,60,80)
Data3 = {20,40,60,80}
student = {"Name" : "Radhika", "Age" : 23, "Marks" : 91.03}

print(type(Data1))      # List
print(type(Data2))      # Tuple
print(type(Data3))      # Set 
print(type(student))    # Dict
print("-" * 40)

print(len(Data1))
print(len(Data2))
print(len(Data3))     
print(len(student))
print("-" * 40)

# Text DataType :

ClassName = "Marvellous Infosystems"

print(ClassName)
print(type(ClassName))      # str
print(len(ClassName))
print(id(ClassName))
print("-" * 40)

# Boolean DataType :

Flag = True

print(Flag)
print(type(Flag))       # bool
print(id(Flag))
print("-" * 40)
# print(len(Flag)) - No len() will apply on bool bcoz there is only true or False value.

# None DataType :

Age = None

print(Age)
print(type(Age))        # NoneType
print(id(Age))
print("-" * 40)
# print(len(Age)) - No len() will apply on None bcoz it is not holding any value of any datatype.

# Print & Input :

Name = input("Enter Your Name : ")
print("Heyy!",Name)
print("-" * 40)
# print("Enter your name : ")
# name = input()

# Range DataType/Function :

R = range(5)        
R1 = range(1,7)      
R2 = range(3,9,2)   

print(R)    # range(0,5)
print(R1)   # range(1,7)
print(R2)   # range(3,9,2)
print("-" * 40)

print(len(R))
print(len(R1))
print(len(R2))
print("-" * 40)

print(type(R))      # range
print("-" * 40)

