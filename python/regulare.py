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