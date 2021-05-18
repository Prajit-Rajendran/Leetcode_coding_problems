# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        def reassign_last(head):
            prev = head
            cur = prev.next
            while cur.next != None:
                prev = cur
                cur = cur.next
            prev.next = None
            cur.next = head
            return cur
        
        if head == None:
            return head
        if head.next == None:
            return head
        cur = head
        count = 0
        while cur!= None:
            cur = cur.next
            count += 1
        for i in range(min(k, k%count)):
            head = reassign_last(head)
        return head