import java.util.ArrayList;

/**
 * Definition for singly-linked list.
 */
  class ListNode {
      int val;
      ListNode next;
      ListNode() {}
      ListNode(int val) { this.val = val; }
      ListNode(int val, ListNode next) { this.val = val; this.next = next; }
  }

public class LC725 {
      private int getSize(ListNode head){
          int length = 0;
          ListNode curr = head;

          while(curr != null){
              curr = curr.next;
              length++;
          }
          return length;
      }
    public ListNode[] splitListToParts(ListNode head, int k) {
        int length = getSize(head);
        int subSetSize = length/k, remainder = length % k;

        ArrayList<ListNode> res = new ArrayList<>();

        ListNode curr = head;
        for(int i = 0; i < k; i++){
            res.add(curr);

            for(int j = 0; j < subSetSize - 1 + (remainder != 0 ? 1: 0); j++){
                if(curr == null) break;
                curr = curr.next;
            }

            remainder -= (remainder != 0 ? 1: 0);

            if(curr != null){
                ListNode temp = curr.next;
                curr.next = null;
                curr = temp;
            }
        }
        return res.toArray(ListNode[]::new);
    }
}
