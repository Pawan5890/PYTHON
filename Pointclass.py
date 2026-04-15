#point class
class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    #show method
    def show(self):
        print("Point:",self.x,self.y)
    #change coordinates
    def change(self,x,y):
        self.x=x
        self.y=y
    #Distance between 2 points
    def dist(self,other):
        d=((self.x - other.x)**2+(self.y - other.y)**2)**0.5
        return d
#create 3 points
p1=Point(1,2)
p2=Point(4,6)
p3=Point(0,0)
#Access Methods
p1.show()
p2.show()

p1.change(2,3)
p1.show()
print("Distance p1 and p2",p1.dist(p2))
print("Distance p2 and p3",p2.dist(p3))
