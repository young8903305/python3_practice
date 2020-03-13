# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# prevent from stack overflow, use while loop, not recursive
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        dummy = ListNode(None)
        pre = dummy
        
        while (l1 != None) and (l2 != None):
            if l1.val < l2.val:
                pre.next = l1
                l1 = l1.next
            else:
                pre.next = l2
                l2 = l2.next
            pre = pre.next
        
        if l1 == None:
            pre.next = l2
        elif l2 == None:
            pre.next = l1

        return dummy.next
