# Partition: Write code to partition a linked list around a value x, such that all nodes less than x come
# before all nodes greater than or equal to x. If x is contained within the list, the values of x only need
# to be after the elements less than x (see below). The partition element x can appear anywhere in the
# "right partition"; it does not need to appear between the left and right partitions.
# EXAMPLE
# Input:
# Output:
# 3 -> 5 -> 8 -> 5 -> 10 -> 2 -> 1 [partition= 5]
# 3 -> 1 -> 2 -> 10 -> 5 -> 5 -> 8

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class Solution:
    def partition(self, node, k):
        head = node
        tail = node

        while node:
            next_node = node.next  # we store the value to avoid reference problem
            node.next = None
            if node.data < k:
                # add at the beginning
                node.next = head
                head = node
                
            else:
                # add at the final
                tail.next = node
                tail = node
                

            node = next_node  # we traverse the list

        tail.next = None  # close the list
        return head
if __name__ == "__main__":
    # linked list: 3 -> 5 -> 8 -> 5 -> 10 -> 2 -> 1
    head = Node(3)
    head.next = Node(5)
    head.next.next = Node(8)
    head.next.next.next = Node(5)
    head.next.next.next.next = Node(10)
    head.next.next.next.next.next = Node(2)
    head.next.next.next.next.next.next = Node(1)

    # k = 5
    solution = Solution()
    new_head = solution.partition(head, 5)

    current = new_head
    while current:
        print(current.data, end=" -> " if current.next else "")
        current = current.next