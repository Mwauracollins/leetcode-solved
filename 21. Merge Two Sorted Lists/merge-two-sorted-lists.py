# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        l1 = list1
        l2 = list2
        dummy = ListNode()
        current = dummy
        
        while l1 and l2:
            if l1.val < l2.val:
                current.next = l1
                l1 = l1.next
            else:
                current.next = l2
                l2 = l2.next
            current = current.next
            
        if l1:
            current.next = l1
        if l2:
            current.next = l2
            
        return dummy.next


list1 = ListNode(1, ListNode(2, ListNode(4)))
list2 = ListNode(1, ListNode(3, ListNode(4)))

s = Solution()

merge_list = s.mergeTwoLists(list1, list2)
result = []
current = merge_list
while current:
    result.append(current.val)
    current = current.next
print(result)