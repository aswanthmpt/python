###1

# ls=[1,8,4,5,6,9]
# lss=[0]

# def asd(a):
#     lss[0]
    
#     for i in ls:
#         if i%2==0:
#             lss.append(i)
#     return lss
# x=asd(ls)
# print(x)


###2
# astr = "malayalam"
# out = {x : astr.count(x) for x in set(astr )}
# print ( str(out))


###3

# a=int(input("enter the number"))
# b=int(input("enter the divisor"))
# try:
   
#     print(a/b)
    
# except:
#     print("cant divisible by zero")
#     a=int(input("enter the number"))
#     b=int(input("enter the divisor"))
#     print(a/b)

###4

# class dep:
#    def deposit(self):
#       self.c=0
#       a=int(input("enter the deposit amount:"))
#       self.c=self.c+a

#    def withdraw(self):
#       b=int(input("enter the withdrawal amount:"))
#       if self.c>=b:
#          print("tour withdrawal amount is",b)
#       else:
#          print("insufficient balance")
#       self.c=self.c-b

#    def balance(self):
#       print("your balance is :",self.c)
      
# d=dep()
# d.deposit()
# d.withdraw()
# d.balance()
      
   
###5

# lss=[1,2,3,4,5,6,7,8,9,10]
# ls=[i**2 for i in lss]
# print(lss)
# print(ls)

    
##6
# a=int(input("enter a number"))
# def fact(n):
#    if n == 1:
#        return n
#    else:
#        return n*fact(n-1)
# num=a
# if num == 0:
#    print("The factorial of 0 is 1")
# else:
#    print("The factorial of", num, "is", fact(num))

###7
# dict={'aa':10,'bb':30,'cc':20,'dd':50,'dd':60,}