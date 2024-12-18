#linkedlist leri pointerlarla (x ve y) çözmek daha kolaydır.

#O(n) time, O(1) Space
from typing import Optional

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = next

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        firstPointer = headA
        secondPointer = headB
        while firstPointer != secondPointer: #olduğu sürece 
            firstPointer = firstPointer.next if firstPointer != None else headB
            secondPointer = secondPointer.next if secondPointer != None else headA
        return firstPointer #or secondPointer as well