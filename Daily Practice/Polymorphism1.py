# Same fun name in both class(overriding)
class Base:
    def fun(self):
        print("Inside Base fun")

class Derived(Base):
    def fun(self):
        print("Inside Derived fun") 

dobj = Derived()
dobj.fun()
