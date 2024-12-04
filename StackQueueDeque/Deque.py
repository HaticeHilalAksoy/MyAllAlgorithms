#list kullaranarak yazdım. 

class Deque():
    def __init__(self):
        self.deque = []
    def isEmpty(self):
        return self.deque==[]
    def addFront(self, item):
        self.deque.insert(0,item)
    def addRear(self, item):
        self.deque.append(item)
    def removeFront(self):
        return self.deque.pop(0)
    def removeRear(self):
        return self.deque.pop()
    def size(self):
        return len(self.deque)
    
myDeque = Deque()
print(myDeque.isEmpty())
myDeque.addFront(10)
myDeque.addFront(20)
myDeque.addRear(30)
#20,10,30
print(myDeque.removeFront())
#10,30
print(myDeque.removeRear())
print(myDeque.isEmpty())