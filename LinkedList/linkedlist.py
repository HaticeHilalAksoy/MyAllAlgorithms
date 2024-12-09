#araya soka yapabiliriz. iki pointer değişken değiştirerek sabit zamanda ekleme yapabiliriz.
#bir şey eklerken kolay okurken daha zor. bir şey alma O(n) bir şe ekleme o(1)
# asıl amacı sabit zamanda bir ekleme yapabilmemize olanak tanımak.
#singly linkedlist  öncekini bilmez sonrasını bilir  için silip etmek zordur.
# doubly linkedlist bir önceki bir sonraki bir de kendi değerini kayıt edebiliyor bir node da 

#single 
class Node():
    def __init__(self, value):
        self.value = value
        self.nextNode = None
firstNode = Node(10)
secondNode = Node(20)
thirdNode= Node(30)
firstNode.nextNode = secondNode
secondNode.nextNode = thirdNode

print(firstNode.nextNode) #2.node
print(firstNode.nextNode.value)
print(firstNode.nextNode.nextNode.value) 
#doubly
class DoublyNode():
    def __init__(self, value):
        self.value = value
        self.nextNode = None
        self.prevNode = None
x=DoublyNode(5)
y=DoublyNode(10)
z=DoublyNode(15)
x.nextNode = y
y.prevNode = x
y.nextNode = z
z.prevNode = y
print(x.nextNode.value) #10
print(z.prevNode.value) #10
print(y.prevNode.value) #5
print(y.nextNode.value) #15
print(y.prevNode.nextNode.value) #10