# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head == None or head.next == None:
            return False
        seen_list = {head : 1}
        cur = head
        while cur.next != None:
            cur = cur.next
            try:
                temp = seen_list[cur] + 1
                return True
            except:
                seen_list[cur] = 1
        return False
        
        