# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        visited = []
        cur = head
        if head == None:
            return True
        if head.next == None:
            return True
        while cur!=None:
            visited.append(cur.val)
            cur = cur.next
        if list(reversed(visited)) == visited:
            return True
        return False
        