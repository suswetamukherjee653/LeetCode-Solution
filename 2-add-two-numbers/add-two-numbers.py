# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        d= ListNode(0)
        cur=d
        carry=0

        while l1 != None or l2 != None or carry>0:
            cursum=carry
            if l1 is not None:
                cursum=cursum+l1.val
                l1=l1.next
            else:
                pass
            if l2 is not None:
                cursum=cursum+l2.val
                l2=l2.next
            else:
                pass
            carry=cursum//10
            n=cursum%10
            cur.next=ListNode(n)
            cur=cur.next
        return d.next