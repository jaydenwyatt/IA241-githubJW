'''
lec 9
define class
'''

#def report_maker(input):
  #  return input 
class car:
    maker= 'toyota'
    
   # def report_maker(self): 
       # return self.maker
       
    
import lec8
print(lec8.cal_abs(-9)) 

import numpy
print(numpy)
    
    def __init__(self,input_model):
            self.model= input_model
        
     def report(self): 
            return self.maker,self.model 
        
my_camry= car('camry')
print(my_camry.maker)
print(my_camry.model)
print(my_camry.report())

my_camry.maker='Ford'
print(my_camry.report())

