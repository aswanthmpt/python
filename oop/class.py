# class vehicle:
#     wheel=2
#     mirror=2
#     def start(self):
#          print("engine start")
# bike=vehicle()
# bike.start()

# class vehicle:
#     wheel=2
#     mirror=2
#     def start(self,a,b):
#          print(a,b)
# bike=vehicle()
# bike.start("engine","cc")


# class vehicle:
#     color="red"
#     def start(self):
#          print("color is",self.color)
# car=vehicle()
# car.start()


# class vehicle:
#     def setcolor(self,color):
#         self.color=color
#     def start(self):
#          print("color is",self.color)
# car=vehicle()
# car.setcolor("yellow")
# car.start()


# class vehicle:
#     def __init__(self,color,tyre):
#         self.color=color
#         self.tyre=tyre
#     def start(self):
#          print("color is",self.color,"tyre is",self.tyre)
# car=vehicle("red",4)
# car.start()

# class animal:
#     def __init__(self,eye,leg,tail):
#         self.eye=eye
#         self.leg=leg
#         self.tail=tail
#     def eyee(self):
#         print("it has",self.eye,"eyes")
#     def legg(self):
#         print("it has",self.leg,"legs")
#     def taill(self):
#         print("it has",self.tail,"tail")
    
# petanimal=animal(2,4,1)
# petanimal.eyee()
# petanimal.legg()
# petanimal.taill()
# wildanimal=animal(2,4,1)
# wildanimal.eyee()
# wildanimal.legg()
# wildanimal.taill()



####
# class vehicle:
#     def engine(self):
#         print("all vehicles have engine")
# class car(vehicle):
#     def fourwheeler(self):
#         print("car have 4 wheels")
# class bike(vehicle):
#     def twowheeler():
#         print("bike have 2 wheel")
# c=car()
# c.fourwheeler()
# c.engine()

# ##
# class granpa:
#     def farmer(self):
#         print("farmer") 
#     def driver(self):
#         print("driver")
# class father(granpa):
#     def reader(self):
#         print("reader")
# class me(father):
#     def engineer(self):
#         print("engineer")
# c=me()
# c.driver()
# c.reader()
# c.engineer()
# ######


class libraryitem:
    def title(self):
        print("wings of fire")
    def author(self):
        print("APJ Abdhul kalam")
    def id(self):
        print("1000")
class book(libraryitem):
    def numpages(self):
        print("500d")
    def readbook(self):
        print("reading the book")
    
class dvd(libraryitem):
    def duration(self):
        print("3:00 hours")
    def dvdplay(self):
        print("playing the dvd")
c=book()
c.title()
c.author()
c.id()
c.numpages()
c.readbook()

d=dvd()
d.title()
d.author()
d.id()
d.duration()
d.dvdplay()

    
