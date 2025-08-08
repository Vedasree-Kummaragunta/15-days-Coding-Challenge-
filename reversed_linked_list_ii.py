class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        
        # Move `prev` to the node before `left`
        for _ in range(left - 1):
            prev = prev.next
        
        curr = prev.next  # The first node of the sublist to reverse
        
        # Reverse the sublist
        for _ in range(right - left):
            temp = curr.next
            curr.next = temp.next
            temp.next = prev.next
            prev.next = temp

        return dummy.next
head = [1, 2, 3, 4, 5]
left = 2
right = 4
sol=Solution()
print(sol.reverseBetween())