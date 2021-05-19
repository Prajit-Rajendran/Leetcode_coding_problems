# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return head
        if head.next == None:
            return head
        prev = head
        cur = head.next
        while 1:
            print(prev.val, cur.val)
            if prev.val == cur.val:
                prev.next = cur.next
                if prev.next == None:
                    return head
                cur = prev.next
            else:
                prev = cur
                cur = cur.next
                if cur == None:
                    return head
                
            
        