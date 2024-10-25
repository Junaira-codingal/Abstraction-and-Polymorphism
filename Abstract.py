from abc import ABC, abstractmethod

#Base Class
class Absclass(ABC):
    
    def print(self,x):
        print(f"Passed value: {x}")
        
    @abstractmethod
    def task(self):
        print("We are inside Absclass task")
        
    
class testClass(Absclass):
    def task(self):
        print("We are inside test_class task")
            
testObj = testClass()
testObj.task()
testObj.print(100)