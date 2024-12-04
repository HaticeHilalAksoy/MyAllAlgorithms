# stack O(1) O(1)     Queue  O(1) O(n)-> time 
# pop da q dan çıkartıp geri ekleyeceğiz. en sonuncu da çıkartacağız ama eklemeyip direkt döndürücez.
# soldan pop edeceğiz sağ dan geri ekleyeceğiz yani
from collections import deque
class Stack:
    def __init__(self):
        self.stack = deque()

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        for i in range(len(self.stack)-1):
            self.stack.append(self.stack.popleft())
        return self.stack.popleft()

    def top(self):
        return self.stack[-1]

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)
Mystack= Stack()
Mystack.push(10)
Mystack.push(20)


"""
        class MyStack:

    def __init__(self):
        self.q = deque()

    def push(self, x: int) -> None:
        self.q.append(x)

    def pop(self) -> int:
        for i in range(len(self.q)-1):
            self.q.append(self.q.popleft()) #we pop everything but the last one (and also we append them back)
        return self.q.popleft() #we pop the last one and not append it back

    def top(self) -> int:
        return self.q[-1]

    def empty(self) -> bool:
        return len(self.q) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
"""