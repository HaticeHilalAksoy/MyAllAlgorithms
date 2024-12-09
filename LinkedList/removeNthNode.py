#time O(N) Space O(1)

#single linkedlist
#slayding window
from typing import Optional

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        leftPointer = head
        rightPointer = head
        
        while n > 0 and rightPointer:  # there is n gap between two pointers
            rightPointer = rightPointer.next
            n -= 1
        
        while rightPointer and rightPointer.next:  # stop when rightPointer.next is None
            leftPointer = leftPointer.next
            rightPointer = rightPointer.next
                
        if leftPointer == head and not rightPointer:  # edge case: single node list
            return head.next

        leftPointer.next = leftPointer.next.next  # skip the leftPointer.next so it would be out of LinkedList
        
        return head
