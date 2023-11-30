# import re
# terms="hello"
# # x=re.split(terms,"hello world hello")
# x=re.match(terms,"hello world hello")
# # x=re.findall(terms,"hello world hello")
# # x=re.search(terms," world hello")

# print(x)


# import re
# terms="aswanth"
# x=re.match(terms,"aswanth")
# if x:
#     print("matched")
# else:
#     print("not matched")


# import re
# terms="[a-zA-Z0-9]swanth"
# x=re.match(terms,"4swanth")
# if x:
#     print("matched")
# else:
#     print("not matched")
    
# import re
# terms="[a-zA-Z0-9]......"
# x=re.match(terms,"4swanth")
# if x:
#     print("matched")
# else:
#     print("not matched")


# import re    **^ for starting
# terms="^aswanth"
# x=re.match(terms,"aswanth hello")
# if x:
#     print("matched")
# else:
#     print("not matched")
    
    
# import re   **$for ending
# terms="aswanth$"
# x=re.search(terms,"hello aswanth")
# if x:
#     print("matched")
# else:
#     print("not matched")
    
# import re ** *for last letter 0-many
# terms="aswanth*"
# x=re.search(terms,"aswanthhhhhhh")
# if x:
#     print("matched")
# else:
#     print("not matched")

# import re  ** +for one to many
# terms="aswanth+"
# x=re.search(terms,"aswanthhhhhhh")
# if x:
#     print("matched")
# else:
#     print("not matched")

# import re   ** ?for 0 or one
# terms="aswanth?$"
# x=re.search(terms,"aswanthh")
# if x:
#     print("matched")
# else:
#     print("not matched")


# import re
# terms="hel{2}o"
# x=re.search(terms,"hello world")
# if x:
#     print("matched")
# else:
#     print("not matched")
    
    

# import re
# terms="[a-z]el{2}o|[A-Z]llo"
# x=re.search(terms,"hello world")
# if x:
#     print("matched")
# else:
#     print("not matched")


# import re
# terms=("[a-z]el{2}o|[A-Z]llo")
# x=re.search(terms,"hello world")
# if x:
#     print("matched")
# else:
#     print("not matched")


# import re
# terms="\dello"
# x=re.search(terms,"1ello world")
# if x:
#     print("matched")
# else:
#     print("not matched")



# import re
# terms="\Dello"
# x=re.search(terms,"hello world")
# if x:
#     print("matched")
# else:
#     print("not matched")


# import re
# terms="\shello"
# x=re.search(terms," hello world")
# if x:
#     print("matched")
# else:
#     print("not matched")


# import re
# terms="\Sello"
# x=re.search(terms,"hello world")
# if x:
#     print("matched")
# else:
#     print("not matched")

# import re
# terms="\wello"
# x=re.search(terms,"9ello world")
# if x:
#     print("matched")
# else:
#     print("not matched")
    
    
# import re
# terms="\Wello"
# x=re.search(terms,"#ello world")
# if x:
#     print("matched")
# else:
#     print("not matched")


# import re
# terms="^[^h]ello"
# x=re.search(terms,"hello world")
# if x:
#     print("matched")
# else:
#     print("not matched")




# import re
# terms="^[5-9]\d{9}$"
# x=re.search(terms,"9048642860")
# if x:
#     print("validate")
# else:
#     print("not validate")

# import re
# asd=str(input("enter the user name : "))
# terms="^[a-zA-Z]\w{3,25}$"
# x=re.search(terms,asd)
# if x:
#     print("validate")
# else:
#     print("not validate")

# import re
# asd=str(input("enter the date :"))
# terms="^([012][1-9]|3[01]|[12]0)(.|\|-)([0][1-9]|1[012])(.|\|-)(\d{3}[1-9]|[1-9]{3}[0-9])$"
# x=re.search(terms,asd)
# if x:
#     print("validate")
# else:
#     print("not validate")
    
    
    
import re
terms="^[a-zA-Z]\w{3,25}@[a-z][com]|^[a-zA-Z]\w{3,25}@[a-z][in]"
x=re.search(terms,"ase23@com")
if x:
    print("vallid")
else:
    print("not valid")