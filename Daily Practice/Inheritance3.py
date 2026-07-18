class Base:
    def __init__(self):
        print("Inside Base Constructor.")
    
class Derived(Base):
    def __init__(self):
        super().__init__()      # Calling the parents constructor or any function using super method.
        print("Inside Derived Constructor.")

dobj = Derived()