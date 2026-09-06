"""
Problem: Circular Linked List
Pattern: Linked List (Floyd's cycle detection)
Time: O(n) | Space: O(1)

Detect whether a linked list contains a cycle, using the classic
slow/fast ("tortoise and hare") pointer technique.

Input:  a list where the last node's `next` points back into the list
Output: True
"""

def is_circular_linked_list(linked_list):
    slow = linked_list.head
    fast = linked_list.head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            return True
    return False


# Alternative: track visited nodes in a set instead of Floyd's slow/fast
# pointers. Time: O(n) same, but Space: O(n) instead of O(1).
def is_circular_linked_list_set(linked_list):
    visited = set()
    current = linked_list.head
    while current:
        if id(current) in visited:
            return True
        visited.add(id(current))
        current = current.next
    return False


if __name__ == "__main__":
    from linked_list import LinkedList
    l = LinkedList()
    l.insert_last('a')
    l.insert_last('b')
    print(is_circular_linked_list(l))  # False
