#list kullanarak stack yazmak

class Stack():
    def __init__(self):
        self.elements=[]
    def isEmpty(self):
        return self.elements==[]
    def push(self,item):
        self.elements.append(item)
    def pop(self):
        return self.elements.pop()
    def showLast(self):
        return self.elements[len(self.elements)-1]
    def size(self):
        return len(self.elements)
myStack = Stack()
print(myStack.isEmpty())
print(myStack.push(10))
print(myStack.push(20))
print(myStack.showLast())
print(myStack.pop())
print(myStack.pop())
print(myStack.size())

#stack nasıl ters çevrilir: push ettikten sonra pop ettiğimizde o popu başka bir stack e eklersek (push edersek) ters çevirmiş oluruz