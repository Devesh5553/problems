# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        prev = None
        curr = head
        i = 0
        points = []
        while curr.next:
            i += 1
            if prev and curr.next:
                if prev.val < curr.val and curr.val > curr.next.val:
                    points.append(i)
                elif prev.val > curr.val and curr.val < curr.next.val:
                    points.append(i)
            prev = curr
            curr = curr.next
        print(points)
        min_dist = float('inf')
        l, r = 0, 1

        while r < len(points):
            tot = points[r] - points[l]
            min_dist = min(min_dist, tot)
            l +=1
            r +=1
        if len(points) > 1:
            return [min_dist, max(points) - min(points)]
        else:
            return [-1, -1]
    