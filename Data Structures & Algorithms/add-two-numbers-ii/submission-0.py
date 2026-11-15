
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        stack1 = []
        stack2 = []

        while l1:
            stack1.append(l1.val)
            l1 = l1.next

        while l2:
            stack2.append(l2.val)
            l2 = l2.next

        carry = 0
        head = None

        while stack1 or stack2 or carry:
            total = carry

            if stack1:
                total += stack1.pop()

            if stack2:
                total += stack2.pop()

            carry = total // 10
            digit = total % 10

            head = ListNode(digit, head)

        return head
        #time and space is O(m+n) and O(m+n) respectively
