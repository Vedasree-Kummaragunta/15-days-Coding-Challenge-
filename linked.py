class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def create_cycle(values, pos):
    head = ListNode(values[0])
    curr = head
    cycle_node = head if pos == 0 else None  # fix: track head if pos == 0

    for i, val in enumerate(values[1:], 1):
        curr.next = ListNode(val)
        curr = curr.next
        if i == pos:
            cycle_node = curr
    if pos != -1:
        curr.next = cycle_node
    return head

class Solution:
    def hasCycle(self, head):
        slow, fast = head, head
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
            if slow == fast:
                return True
        return False


# ✅ Testing
sol = Solution()
head1 = create_cycle([3,2,0,-4], 1)
print(sol.hasCycle(head1))  # True

head2 = create_cycle([1,2], 0)
print(sol.hasCycle(head2))  # True

head3 = create_cycle([1], -1)
print(sol.hasCycle(head3))  # False

