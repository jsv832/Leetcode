def hasCycle(self, head: Optional[ListNode]) -> bool:

    fast = head
    slow = head

    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next

        if slow is fast:
            return True

    return False
    