class abc:
    def add(self,a,b):
        print(a+b)
    def add(self,a,b,c=0):
        print(a+b+c)
c=abc()
c.add(3,4)
c.add(3,4,5)