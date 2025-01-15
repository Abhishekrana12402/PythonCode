# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Ques Link:https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/
from typing import Optional,ListNode
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow=head
        fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        if slow==fast or not head:
            return None
        temp=head
        # slow fast pointer to find the mid then simply comparing and deleting the middle node 
        while temp:
            if temp.next==slow:
                temp.next=temp.next.next
            temp=temp.next
        return head

