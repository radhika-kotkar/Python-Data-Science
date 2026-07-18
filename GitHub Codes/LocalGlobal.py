no = 11     # Global Variable

def Display():
    print("From Display :",no)
def Demo():
    print("From Demo :",no)
Display()
Demo()
print("-" * 40)

no = 11     # Global Variable

def Display():
    L = 21
    print("From Display :",no)
    print("From Display :",L)
def Demo():
    print("From Demo :",no)
    # print("From Display :",L)    # Error
Display()
Demo()
print("-" * 40)

# Changing Global variable value inside function so it is only applicable to Local function.

no = 11   

def Display():
    no = 21     # Locally changed not affected global value.
    print("From Display :",no)

print("Before :",no)
Display()
print("After :",no)
print("-" * 40)

# If we want to change Global Value then use global keyword.

no = 11   

def Display():
    global no
    no = 21     
    print("From Display :",no)

print("Before :",no)
Display()
print("After :",no)
print("-" * 40)



