# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

from heapq import heapify,heappop,heappush
class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        dummy=ListNode(None)
        cur=dummy
        heap=[(l.val,i) for i,l in enumerate(lists) if l]
        heapify(heap)
        while heap:
            value,list_id= heappop(heap)
            cur.next=ListNode(value)
            cur=cur.next
            if lists[list_id].next:
                lists[list_id]=lists[list_id].next
                heappush(heap,(lists[list_id].val,list_id))
        return dummy.next
            
        