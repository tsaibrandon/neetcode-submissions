# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        create a dummy head node
        compare the values at each step
            if it is == then point to list 1
            then which ever one is greater point there
        
        if linked lists are different sizes
            when one hits none then add the rest of the other linked list
        """

        dummy = ListNode()
        tail = dummy

        while list1 and list2:
            if list1.val <= list2.val:
                tail.next = list1
                list1 = list1.next
                tail = tail.next
            else:
                tail.next = list2
                list2 = list2.next
                tail = tail.next
            
        if list1 is None:
            tail.next = list2
            tail = tail.next
        else:
            tail.next = list1
            tail = tail.next
        
        return dummy.next
            

                