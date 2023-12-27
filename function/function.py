# def fun():
#     print("%%%%%%%%%%%%%%%%%%")
#     print("~~~~~~~~~~~~~~~~~~~")
    
# print("hai")
# fun()


# def fun():
#     a=8
#     b=6
#     print(a+b)
  
    
# print("hai")
# fun()

# q=int(input("enter the number: "))
# def add(a,b):
#     print(a*b)
# for i in range(1,11):
#     print(i,"x",q,"=",end=" ")
#     add(q,i)       

##function with return
# def asw():
#     a,d=1,2
#     return a+d
# print(asw())

# def asw():
#     a,d=1,2
#     return a+d
# x=asw()
# print(x)

# def asw():
#     a,d=1,2
#     return a+d
# print(type(asw()))

##function with argument and return

# def asw(a,b):
    
#     return a*b

# x=asw(3,2)
# print(x)


    
def recur_factorial(n):
   if n == 1:
       return n
   else:
       return n*recur_factorial(n-1)

num = 7

# check if the number is negative
if num < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   print("The factorial of", num, "is", recur_factorial(num))
    
  
    
