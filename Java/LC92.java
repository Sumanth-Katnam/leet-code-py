public class LC92 {
    public ListNode reverseBetween(ListNode head, int left, int right) {
        if(left == right) return head;

        ListNode dummy = new ListNode(-1, head);
        ListNode curr = dummy;
        ListNode prev = null;
        int count = 0;
        while(curr.next != null && count != left){
            prev = curr;
            curr = curr.next;
            count++;
        }

        ListNode start = prev;

        prev = null;
        ListNode next;
        while(curr != null){
            next = curr.next;
            curr.next = prev;
            prev = curr;
            curr = next;
            count++;
            if(count - 1 == right) break;
        }

        if(start != null){
            ListNode end = start.next;
            start.next = prev;
            end.next = curr;
        }

        return dummy.next;
    }

    public static void main(String[] args) {
        LC92 sol = new LC92();

        ListNode head = new ListNode(3);
        head.next = new ListNode(5);
//        head.next.next = new ListNode(3);
//        head.next.next.next = new ListNode(4);
//        head.next.next.next.next = new ListNode(5);
        System.out.println(sol.reverseBetween(head, 1, 2));
    }
}
