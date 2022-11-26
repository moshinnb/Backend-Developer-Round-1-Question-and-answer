import re
list=["2124567890","212-456-7890","(212)456-7890","(212)-456-7890","212.456.7890","212 456 7890","+12124567890","+12124567890","+1 212.456.7890","+212-456-7890","1-212-456-7890"]
def validatNo(number):

    pat="^\+|(\+\d)?\s?\(?\d\d\d\)?[\s.-]?\d\d\d[\s.-]?\d\d\d\d$"
    
    if(re.search(pat,number)!=None):
        return "Valid"
    else:
        return "Not Valid"
    
for i in list:    
   print(i,"---->",validatNo(i))
   
