class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class Solution:
    def getIntersectionNode(self, headA, headB):
        l1 = headA
        l2 = headB

        while l1 != l2:
            if l1:
                l1 = l1.next
            else:
                l1 = headB

            if l2:
                l2 = l2.next
            else:
                l2 = headA
        return l1

# Tests
if __name__ == "__main__":
    sol = Solution()

    # Test 1: Lists intersect at node with data 8
    # List A: 1 -> 3
    #                \
    #                 8 -> 10
    #                /
    # List B:      2
    intersecting_node = Node(8)
    intersecting_node.next = Node(10)

    l1 = Node(1)
    l1.next = Node(3)
    l1.next.next = intersecting_node

    l2 = Node(2)
    l2.next = intersecting_node

    print(f"Intersection at node with data: {sol.getIntersectionNode(l1, l2).data}")  # Expected: 8

    # Test 2: Lists do not intersect
    # List A: 1 -> 3 -> 5
    # List B: 2 -> 4 -> 6
    l1 = Node(1)
    l1.next = Node(3)
    l1.next.next = Node(5)

    l2 = Node(2)
    l2.next = Node(4)
    l2.next.next = Node(6)

    result = sol.getIntersectionNode(l1, l2)
    print(f"Intersection: {result}")  # Expected: None

    # Test 3: One list is empty
    # List A: 1 -> 3 -> 5
    # List B: (empty)
    l1 = Node(1)
    l1.next = Node(3)
    l1.next.next = Node(5)

    l2 = None  # Empty list

    result = sol.getIntersectionNode(l1, l2)
    print(f"Intersection with empty list: {result}")  # Expected: None

    # Test 4: Both lists are empty
    # List A: (empty)
    # List B: (empty)
    l1 = None  # Empty list
    l2 = None  # Empty list

    result = sol.getIntersectionNode(l1, l2)
    print(f"Intersection with both lists empty: {result}")  # Expected: None