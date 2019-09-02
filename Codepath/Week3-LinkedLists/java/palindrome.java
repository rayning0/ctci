/**
 * Given a singly linked list, determine if it is a palindrome.
 *
 * Example 1:
 * Input: 1->2
 * Output: false
 *
 * Example 2:
 * Input: 1->2->2->1
 * Output: true
 *
 **/
public class Main {
    public static void main(String[] args) {

        ListNode n1_1 = new ListNode(1);
        System.out.println("Test cases 1 passed: " + isPalindrome(n1_1));

        ListNode n2_1 = new ListNode(1);
        ListNode n2_2 = new ListNode(2);
        n2_1.next = n2_2;
        System.out.println("test case 2 passed: " + !isPalindrome(n2_1));

        ListNode n3_1 = new ListNode(1);
        ListNode n3_2 = new ListNode(2);
        ListNode n3_3 = new ListNode(3);
        n3_1.next = n3_2;
        n3_2.next = n3_3;
        System.out.println("test case 3 passed: " + !isPalindrome(n3_1));

        ListNode n4_1 = new ListNode(1);
        ListNode n4_2 = new ListNode(2);
        ListNode n4_3 = new ListNode(1);
        n4_1.next = n4_2;
        n4_2.next = n4_3;
        System.out.println("test case 4 passed: " + isPalindrome(n4_1));
    }

    public static boolean isPalindrome(ListNode node) {
        int fullLength = getLength(node);

        int[] firstHalf = new int[fullLength / 2];
        int currentNode = 0;
        while (currentNode < (fullLength / 2)) {
            firstHalf[currentNode] = node.data;
            node = node.next;
            currentNode++;
        }

        // Skip the middle node if the list has an odd number of nodes
        if (fullLength % 2 == 1) {
            node = node.next;
        }

        while (currentNode > 0) {
            if (node.data != firstHalf[currentNode - 1]) {
                return false;
            }
            node = node.next;
            currentNode--;
        }

        if (currentNode != 0) {
            return false;
        }

        return true;
    }

    public static int getLength(ListNode node) {
        int length = 0;
        while (node != null) {
            length++;
            if (node.next == null) {
                return length;
            }
            node = node.next;
        }
        return length;
    }

    public static class ListNode {
        int data;
        ListNode next;

        ListNode(int data) {
            this.data = data;
        }
    }
}
