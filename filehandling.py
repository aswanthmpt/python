# file=open("demo.txt","r")
# s=file.read()
# print(s)
# file.close()

with open ("demo.txt","w")as file:
    file.write("hai")
    

with open ("demo.txt","r")as file:
    s=file.read()
    print(s)