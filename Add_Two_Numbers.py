# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        extra = 0
        empty = ListNode(0)
        answer = None
        while l1!=empty or l2!=empty or extra:
            current = l1.val + l2.val + extra if l1.val + l2.val + extra < 10 else l1.val + l2.val +extra -10
            if answer:
                answer.next = ListNode(current)
                answer = answer.next
            else:
                answer = ListNode(current)
                head = answer
            extra = 0 if l1.val + l2.val + extra < 10 else 1
            l1 = l1.next if l1.next else empty
            l2 = l2.next if l2.next else empty
        return head