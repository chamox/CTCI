class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class Solution:
    def detectCycle(self, head):
        
        # first we are going to detect the intersection node with f t & h algo

        if not head:
            return None

        slow, fast = head, head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

            if slow == fast:
                break
            
        if fast is None or fast.next is None:
            return None

        slow = head

        while slow != fast:
            slow = slow.next
            fast = fast.next
        
        return fast
    

if __name__ == "__main__":
    node1 = Node(3)
    node2 = Node(2)
    node3 = Node(0)
    node4 = Node(-4)

    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node2  # create cycle

    sol = Solution()
    beginnig = sol.detectCycle(node1)

    if beginnig:
        print("Cycle start at:", beginnig.data)
    else:
        print("There is no cycle.")