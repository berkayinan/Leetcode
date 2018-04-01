# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry=0
        result_head = ListNode(0)
        cur=result_head
        while l1 is not None and l2 is not None:
            cur.next=ListNode((l1.val+l2.val+carry)%10)
            carry=(l1.val+l2.val+carry)//10
            cur=cur.next
            l1, l2 =l1.next,l2.next
        
        remainder_list = l1 if l1 else l2
        if remainder_list:
            while remainder_list:
                cur.next=ListNode((carry+remainder_list.val)%10)
                carry=(carry+remainder_list.val)//10
                cur=cur.next
                remainder_list=remainder_list.next
        if carry:
            cur.next=ListNode(carry)
        return result_head.next
            
        