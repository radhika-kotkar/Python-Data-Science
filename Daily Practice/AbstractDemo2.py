# abc - module , ABC - class
from abc import ABC , abstractmethod      # Abstract Base Class

class Base(ABC):
    @abstractmethod
    def Addition(self,No1,No2):     # Abstract = Method without body
        pass

class Derived(Base):
    def Addition(self,No1,No2):      # Concrete = Method with body
        return No1 + No2

dobj = Derived()

Ret = dobj.Addition(10,11)
print("Addition is :",Ret)

