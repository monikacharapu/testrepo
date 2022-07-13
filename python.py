#My jupyter book on IBM waston studio
##CHARAPU MONIKA
###I am interested in data science because i love to gain insights from data
####the following code tests the factorial of a number
num = int(input("Enter a number: "))    
factorial = 1    
if num < 0:    
   print(" Factorial does not exist for negative numbers")    
elif num == 0:    
   print("The factorial of 0 is 1")    
else:    
   for i in range(1,num + 1):    
       factorial = factorial*i    
   print("The factorial of",num,"is",factorial)  
