# Delete Middle Node: Implement an algorithm to delete a node in the middle (i.e., any node but
# the first and last node, not necessarily the exact middle) of a singly linked list, given only access to
# that node.
# EXAMPLE
# lnput:the node c from the linked lista->b->c->d->e->f
# Result: nothing is returned, but the new linked list looks likea->b->d->e->f

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class Solution:
    def delete_middle_node(self, middle):
        next_node = middle.next
        middle.data = next_node.data
        middle.next = next_node.next
        return True
    

    
if __name__ == "__main__":

    head = Node('a')
    head.next = Node('b')
    middle = head.next.next = Node('c')  # we are going to delete this node
    head.next.next.next = Node('d')
    head.next.next.next.next = Node('e')
    head.next.next.next.next.next = Node('f')

    current = head
    while current:
        print(current.data, end=" -> " if current.next else "")
        current = current.next

    print("")

    solution = Solution()

    solution.delete_middle_node(middle)


    current = head
    while current:
        print(current.data, end=" -> " if current.next else "")
        current = current.next