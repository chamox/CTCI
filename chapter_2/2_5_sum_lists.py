class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class Solution:
    def sum_lists(self, l1, l2):
        result = Node(0)
        current = result
        carry = False

        while l1 or l2 or carry:
            new_node = Node(0)

            if l1:
                new_node.data += l1.data
                l1 = l1.next
            if l2:
                new_node.data += l2.data
                l2 = l2.next
            if carry:
                new_node.data += 1
                carry = False
            
            if new_node.data // 10 > 0:
                new_node.data = new_node.data % 10
                carry = True

            current.next = new_node
            current = current.next

        return result.next

                


if __name__ == "__main__":
    # Create lists (7 -> 1 -> 6) y (5 -> 9 -> 2)
    l1 = Node(7)
    l1.next = Node(1)
    l1.next.next = Node(6)

    l2 = Node(5)
    l2.next = Node(9)
    l2.next.next = Node(2)

    # Sum lists
    sol = Solution()
    result = sol.sum_lists(l1, l2)

    # aux function to print
    def print_linked_list(node):
        while node:
            print(node.data, end=" -> " if node.next else "\n")
            node = node.next

    print_linked_list(result)  # this sould be: 2 -> 1 -> 9