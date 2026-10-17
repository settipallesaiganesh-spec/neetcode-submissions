import math

class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head

        while curr and curr.next:
            gcd_val = math.gcd(curr.val, curr.next.val)

            new_node = ListNode(gcd_val)
            new_node.next = curr.next
            curr.next = new_node

            curr = new_node.next

        return head 
        #Time and space is O(n) and O(1) respectively