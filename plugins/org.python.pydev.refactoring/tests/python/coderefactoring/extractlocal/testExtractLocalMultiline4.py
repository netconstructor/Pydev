class MyClass2(MyClass):
    
    def m1(self, a, b):
        while a > (
                   2+
                   ##|
                   2
                   ##|
                   ):
            new_var = [
                       1, 
                       2
                       ]
    
##r
class MyClass2(MyClass):
    
    def m1(self, a, b):
        extracted_variable = 2
        while a > (
                   2+
                   
                   extracted_variable
                   
                   ):
            new_var = [
                       1, 
                       2
                       ]