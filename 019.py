# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        cur=head
        target=head
        for _ in range(n):
            cur=cur.next
        if not cur:
            return head.next
        cur=cur.next
        while cur:
            cur=cur.next
            target=target.next
        target.next=target.next.next
        return head