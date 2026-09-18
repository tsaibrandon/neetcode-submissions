# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        first reverse the second half of the list
            use a fast and slow pointer to find the center
        
        then have two pointers 
            one at the front and one at the back 
            walk through the linked list and arrange the pointers accordingly
        """

        fast, slow = head, head

        # find the halfway point
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse the second half
        prev = None
        curr = slow.next
        slow.next = None

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        # reorder the linked list
        while head and prev:
            nxt1 = head.next
            head.next = prev
            head = nxt1
            nxt2 = prev.next
            prev.next = head
            prev = nxt2
        
