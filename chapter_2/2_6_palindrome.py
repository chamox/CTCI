class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class Solution:
    def is_palindrome(self, node):
        
        slow = node
        fast = node

        # we are going to find the middle of the linked list
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        # we are going to reverse the second half of the list (returned as prev)
        prev = None
        while slow:
            tmp = slow.next
            slow.next = prev
            prev = slow
            slow = tmp

        # now we check if the list is palindrome or not
        left = node
        right = prev

        while right:
            if right.data != left.data:
                return False
            left = left.next
            right = right.next

        return True


if __name__ == "__main__":
    sol = Solution()

    # Test 1: Palindrome list (1 -> 2 -> 2 -> 1)
    l1 = Node(1)
    l1.next = Node(2)
    l1.next.next = Node(2)
    l1.next.next.next = Node(1)
    print(f"Is palindrome (1 -> 2 -> 2 -> 1): {sol.is_palindrome(l1)}")  # True

    # Test 2: Palindrome list with odd length (1 -> 2 -> 3 -> 2 -> 1)
    l2 = Node(1)
    l2.next = Node(2)
    l2.next.next = Node(3)
    l2.next.next.next = Node(2)
    l2.next.next.next.next = Node(1)
    print(f"Is palindrome (1 -> 2 -> 3 -> 2 -> 1): {sol.is_palindrome(l2)}")  # True

    # Test 3: Non-palindrome list (1 -> 2 -> 3)
    l3 = Node(1)
    l3.next = Node(2)
    l3.next.next = Node(3)
    print(f"Is palindrome (1 -> 2 -> 3): {sol.is_palindrome(l3)}")  # False

    # Test 4: Single element list (1)
    l4 = Node(1)
    print(f"Is palindrome (1): {sol.is_palindrome(l4)}")  # True

    # Test 5: Empty list
    l5 = None
    print(f"Is palindrome (empty list): {sol.is_palindrome(l5)}")  # True