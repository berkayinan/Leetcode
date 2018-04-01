# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy=ListNode(None)
        dummy.next=head
        cur=dummy
        while cur.next and cur.next.next:
            temp=cur.next.next
            cur.next.next=cur.next.next.next
            temp.next=cur.next
            cur.next=temp
            cur=cur.next.next
        return dummy.next
        