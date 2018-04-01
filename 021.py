#Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        cur=ListNode(None)
        dummy_head=cur
        while l1 is not None or l2 is not None:
            print(l1 is None,l2 is None)
            if l2 is None or (l1 and l1.val<=l2.val):
                cur.next=ListNode(l1.val)
                l1=l1.next
            else:
                cur.next=ListNode(l2.val)
                l2=l2.next
            cur=cur.next
        return dummy_head.next
        
            
            