class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head):
        if not head:
            return head

        current = head
        while current.next:
            if current.val == current.next.val:
                current.next = current.next.next
            else:
                current = current.next

        return head

# Helper function to print the linked list
def printLinkedList(head):
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")

# Example usage:
# Create a linked list: 1 -> 1 -> 2 -> 3 -> 3
head = ListNode(1, ListNode(1, ListNode(2, ListNode(3, ListNode(3)))))
s = Solution()
result_head = s.deleteDuplicates(head)

# Print the result
printLinkedList(result_head)
