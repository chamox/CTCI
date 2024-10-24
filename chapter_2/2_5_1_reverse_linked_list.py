class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class Solution:
    def reverse_list(self, node):
        prev = None
        current = node

        while current:
            tmp = current.next
            current.next = prev
            prev = current
            current = tmp
        
        return prev
    

def print_linked_list(node):
    while node:
        print(node.data, end=" -> " if node.next else "\n")
        node = node.next

if __name__ == "__main__":
    # Create linked list 1 -> 2 -> 3 -> 4
    l1 = Node(1)
    l1.next = Node(2)
    l1.next.next = Node(3)
    l1.next.next.next = Node(4)

    print("Lista original:")
    print_linked_list(l1)  # Should be: 1 -> 2 -> 3 -> 4

    sol = Solution()
    reversed_list = sol.reverse_list(l1)

    print("Lista invertida:")
    print_linked_list(reversed_list)  # Should be: 4 -> 3 -> 2 -> 1