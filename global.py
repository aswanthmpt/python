##local
# def asd():
#     a=10
#     print(a)
# asd()
# print(a)

##global
# a=10
# def asd():
#     print(a)
# asd()
# print(a)

#enclosed

# def asd():
#     a=10
#     def bsd():
#         print(a)
#     bsd()
# asd()

##recurtion
# a=1
# def asd(b):
#     b=b+1
#     print(b)
#     asd(b)
    
    
# asd(a)


# a=1
# def asd(b):
#     if b<=10:
#         print(b)
#         b=b+1
#         asd(b)
    
    
# asd(a)

##factorial 

def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)
res=fact(0)
print(res)
    
    
    ##
# a=100
# def asd(n):
#     if n>=1:
#         print(n)
#         n=n-1
#         asd(n)
        
# asd(a)
    
    

