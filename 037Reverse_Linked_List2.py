# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

"""
use list to implement stack.
push items into stack and pop them, will reverse their order

connect m-1, reverse list, n+1 
"""

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if m==n:
            return head
        
        stack = []
        left, iterator = None, head
        if m != 1:
            for i in range(1, m-1):    # care about the range, begin with 1
                iterator = iterator.next
            left = iterator
            iterator = iterator.next    # position is on m
        
        for i in range(m, n+1):   # need to include the n's item, n+1
            stack.append(iterator)    # in reverse range, push itmes into stack
            iterator = iterator.next

        temp1, temp2 = stack.pop(), None
        if m == 1:
            head = temp1
        else:
            left.next = temp1    # connect left and the reverse-list-head

        # pop stack item as the reversed list
        while stack:
            temp2 = stack.pop()
            temp1.next = temp2
            temp1 = temp2
        
        # connect reverse list and the rest  
        temp1.next = iterator
        return head
