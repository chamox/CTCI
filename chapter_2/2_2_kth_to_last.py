# Return Kth to Last: Implement an algorithm to find the kth to last element of a singly linked list.

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class Solution:
    def find_kth_to_last(self, head, k):
        slow = head
        fast = head

        for _ in range(k):
            if fast is None:
                return None
            fast = fast.next
        
        while fast:
            slow = slow.next
            fast = fast.next

        if slow is not None:
            return slow.data
        else:
            return None
    
if __name__ == "__main__":
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)

    solution = Solution()

    # Find k° node from final
    k = 3
    result = solution.find_kth_to_last(head, k)

    print(f"the node value at position {k} from the final is: {result}")