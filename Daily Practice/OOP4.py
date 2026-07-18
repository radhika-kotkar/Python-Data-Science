class Demo():
    # class variables
    Value1 = 10
    Value2 = 20

    def __init__(self):
        # Instance variables
        self.No1 = 11
        self.No2 = 21

    # Instance Method
    def fun(self):
        print("Inside Instance Method named as fun.")

        # Accessing Instance Variable in Instance Method.
        print(self.No1)
        print(self.No2)

        # Accessing Class Variable in Instance Method.
        print(Demo.Value1)
        print(Demo.Value2)

    @classmethod
    def gun(cls):
        print("Inside class method named as gun.")

        # Accessing Instance Variable in Class Method is not allowed.
        # print(Demo.No1)     
        # print(Demo.No2)

        print(Demo.Value1)  # Accessing Class Variable in Class Method.
        print(Demo.Value2)

# Call with Object 
dobj = Demo()
dobj.gun()