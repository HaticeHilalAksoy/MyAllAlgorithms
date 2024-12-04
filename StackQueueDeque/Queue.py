#listeleri kullanarak queue yaptık.
class Queue():
    def __init__(self):
        self.queue = []
    def isEmpty(self):
        return self.queue==[]
    def enqueue(self, item):
        #self.queue.append(item) sona eklemiş olursun bu stack olur.
        self.queue.insert(0,item) #en başa ekledim.
    def dequeue(self):
        return self.queue.pop() #eğer pop(0) yaparsam baştan çıkarmaya başlarım.
    def size(self):
        return len(self.queue)
myQueue = Queue()
myQueue.isEmpty()
myQueue.enqueue(10)
myQueue.enqueue(20)
myQueue.enqueue(30)
print(myQueue.size())
print(myQueue.dequeue())
print(myQueue.dequeue())
print(myQueue.size())
print(myQueue.isEmpty())