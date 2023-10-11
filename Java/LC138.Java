// Definition for a Node.
class Node {
    int val;
    Node next;
    Node random;

    public Node(int val) {
        this.val = val;
        this.next = null;
        this.random = null;
    }
}


class Solution {
    public Node copyRandomList(Node head) {
        if(head == null) 
            return null;
        
        // Inserting duplicates next to original
        Node curr = head;
        while(curr != null){
            Node curr_copy = new Node(curr.val);
            curr_copy.next = curr.next;
            curr.next = curr_copy;
            curr = curr_copy.next;
        }

        // Attaching random links
        curr = head;
        while(curr != null){
            curr.next.random = (curr.random != null) ? curr.random.next : null;
            curr = curr.next.next;
        }

        // re-establishing original next links between original and copy
        Node prev = new Node(-1);
        Node copy = head.next;
        prev.next = head.next;

        while (head != null && head.next != null){
            head.next = copy.next;
            copy.next = (copy.next != null) ? copy.next.next : null;
            head = head.next;
            copy = copy.next;
        }
        return prev.next;
    }
}