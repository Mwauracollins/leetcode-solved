/**
 * Definition for singly-linked list. */
public class MergeTwoSortedLists {
    public class ListNode {
        int val;
        ListNode next;
        ListNode() {}
        ListNode(int val) { this.val = val; }
        ListNode(int val, ListNode next) { this.val = val; this.next = next; }
    }

    public class Solution {
        public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
            ListNode l1 = list1;
            ListNode l2 = list2;
            ListNode dummy = new ListNode(-1);
            ListNode current = dummy;

            while (l1 != null && l2 != null){
                if (l1.val < l2.val){
                    current.next = l1;
                    l1 = l1.next;
                } else {
                    current.next = l2;
                    l2 = l2.next;
                }
                current = current.next;
            }
            if (l1 != null){
                current.next = l1;
            }
            if (l2 != null){
                current.next = l2;
            }
            return dummy.next;
        }

        public void printList(ListNode head){
            ListNode current = head;
            while (current != null){
                System.out.print(current.val + " -> ");
                current = current.next;
            }
        }
    }

    public static void main(String[] args) {
        MergeTwoSortedLists outerInstance = new MergeTwoSortedLists();
        Solution solution = outerInstance.new Solution();

        ListNode list1 = outerInstance.new ListNode(1);
        list1.next = outerInstance.new ListNode(2);
        list1.next.next = outerInstance.new ListNode(4);

        ListNode list2 = outerInstance.new ListNode(1);
        list2.next = outerInstance.new ListNode(3);
        list2.next.next = outerInstance.new ListNode(4);

        ListNode mergedList = solution.mergeTwoLists(list1, list2);
        solution.printList(mergedList);
    }
}
