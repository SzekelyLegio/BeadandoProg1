# -*- coding: utf-8 -*-
"""
Created on Wed May  1 13:07:07 2019

@author: SzekelyLegio
"""
import numpy as np
print("--------------------------------Első feladat-----------------------------------------")
def islowertriangular(M): 
    for i in range(0, len(M)): 
        for j in range(i + 1, len(M)): 
            if(M[i][j] != 0):  
                    return False
    return True
      

M = [[1,0,0,0], 
     [1,4,0,0], 
     [4,6,2,0], 
     [0,4,7,6]] 
  
if islowertriangular(M): 
    print ("Yes") 
else: 
    print ("No") 
    
print("--------------------------------Második feladat-----------------------------------------")

from math import sqrt
from itertools import count, islice

def isPrime(n):
    if n < 2:
        return False

    for number in islice(count(2), int(sqrt(n) - 1)):
        if n % number == 0:
            return False

    return True


def computeGCD(x, y): 
  
    if x > y: 
        small = y 
    else: 
        small = x 
    for i in range(1, small+1): 
        if((x % i == 0) and (y % i == 0) and isPrime(i) == True):
            gcd = i 
       
              
    return gcd
  
a = 1230
b= 1530
  
# prints 12 

print (computeGCD(1230345,1530345)) 



print("--------------------------------Harmadik feladat-----------------------------------------")
import re

class Validator(object):

    def __init__(self, email):
        self.email = email
        
    
            
 
    def checkCharacter(self):

        symbols = {'~', ':', "'", '+', '[', '\\', '^', '{', '%', '(', '"', '*', '|', ',', '&', '<', '`', '}', '=', ']', '!', '>', ';', '?', '#', '$', ')', '/'}
        myEmail = self.email
        for i in symbols:
            if i in myEmail:
                return False
            else:
                return True
        

    def check_for_symbol(self):
        if re.search("[@.]", self.email) is None:
            return False
        else:
            return True

    def check_length(self):
        if len(self.email) >= 12:
            return True
        else:
            return False
        
    def check_ending(self):
        a=self.email.rfind(".")
        MyEmail= self.email[a:]
        if(MyEmail.find(".-")==-1| MyEmail.find("._")==-1 | MyEmail.find(".,")==-1 | MyEmail.find(".+")==-1 | MyEmail.find("./")==-1 | MyEmail.find(".-")==-1):
            return True
        else:
            return False 
    def check_endingPoints(self):
        a=self.email.rfind(".")
        MyEmail= self.email[a:]
        if(MyEmail.rfind(".-")<2):
            return True
        else:
            return False 
    def check_endingCaracters(self):
        
        a=[".",""]
        MyEmail= self.email[a:]
        if(MyEmail.rfind(".-")<2):
            return True
        else:
            return False 
        
    def check_twoPoints(self):
        if(self.email.find("..")== -1):
            return True
        else:
            return False
        
    
        


def email_to_verify():
   a =input("Type your email: ")
   return a


def check_email(email):
    validator = Validator(email)
    symbol = validator.check_for_symbol()
    if symbol is False:
        print ("Your email address is not valid. Failed symbols..")

    length = validator.check_length()
    if length is False:
        print ("Your email is not valid. Failed length")
        
    points =validator.check_twoPoints()
    if points is False:
        print("Your email has two points next to eachother")
        
    ending=validator.check_ending()
    if ending is False:
        print("Your email has a bad end")
        
    endingPoints=validator.check_endingPoints()
    if endingPoints is False:
        print("Your email has too many points")
        
    CheckCaracters=validator.checkCharacter()
    if CheckCaracters is False:
        print("no caracters allowed")
        
    if length and symbol and points and ending and endingPoints and CheckCaracters is True :
        print ("Email is a valid email address.")


if __name__ == '__main__':
    e = email_to_verify()
    check_email(e) 
    









   
    




  


