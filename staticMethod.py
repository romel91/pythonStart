class Math:
    def __init__(self, num):
        self.num =num

    def addtonum(self,n):
        self.num=self.num + n

    @staticmethod
    def add(a,b):
        return a+b 

a=Math(4)
# print(Math.add(1,2))
print(a.add(2,4))
a.addtonum(6)
print(a.num)


        