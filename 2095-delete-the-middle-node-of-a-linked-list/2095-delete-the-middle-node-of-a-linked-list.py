# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        length = 0
        while curr:
            curr = curr.next
            length += 1
        n = length // 2
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        curr = head
        for i in range(n + 1):
            if i == n:
                prev.next = curr.next
            else:
                curr = curr.next
                prev = prev.next
        return dummy.next