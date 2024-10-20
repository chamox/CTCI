# Remove Dups: Write code to remove duplicates from an unsorted linked list.
# FOLLOW UP...
# How would you solve this problem if a temporary buffer is not allowed?


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Solution:
    def delete_duplicates_v1(self, head):
        """
            This method removes the duplicate element, but let the element in the linked list
            So, this is a wrong answer, because we need to remove the duplicates elements
        """


        prev = None
        current = head
        seen = dict()

        while current:
            if current.data in seen:
                seen[current.data] += 1
                prev.next = current.next
            else:
                seen[current.data] = 1
                prev = current

            current = current.next

        return head 
    
    def delete_duplicates_v2(self, head):
        # We make a counter dict of the data at the nodes
        data_counter =  dict()


        current = head
        while current:
            if current.data in data_counter:
                data_counter[current.data] += 1
            else:
                data_counter[current.data] = 1
            current = current.next

        # we have the dictionary, so we can start removing the non unique elements of the linked list

        dummy = Node(0)
        dummy.next = head

        prev = dummy
        current = head

        while current:
            if data_counter[current.data] > 1:
                prev.next = current.next
            else:
                prev = current
            current = current.next
        
        return dummy.next

    def delete_duplicates_v3(self, head):
        """
        If we can not make a temporal buffer, we are going to use the 2 pointers technique
        """
        current = head

        while current:
            runner = current

            while runner.next:
                if runner.next.data == current.data:
                    runner.next = runner.next.next
                else:
                    runner = runner.next
            current =  current.next
        return head


if __name__ == "__main__":
    # Test cases
    # make a linked list to test
    linked_list = Node(1)
    linked_list.next = Node(2)
    linked_list.next.next = Node(3)
    linked_list.next.next.next = Node(3)
    linked_list.next.next.next.next = Node(4)
    linked_list.next.next.next.next.next = Node(4)

    current = linked_list
    while current:
        print(current.data)
        current = current.next


    sol = Solution()
    removed_items = sol.delete_duplicates_v3(linked_list)

    print("****")

    current = removed_items
    while current:
        print(current.data)
        current = current.next

