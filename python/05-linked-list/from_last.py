"""
Problem: Nth From Last
Pattern: Linked List (two-pointer / runner technique)
Time: O(n) | Space: O(1)

Given a linked list, return the node n spaces from the last node.
Do not call the list's size() method. Assumes n is always less than the
length of the list.

Input:  list = a -> b -> c -> d, from_last(list, 2)
Output: node with data 'b'
"""

def from_last(linked_list, n):
    slow = linked_list.head
    fast = linked_list.head

    while n > 0:
        fast = fast.next
        n -= 1

    while fast.next:
        slow = slow.next
        fast = fast.next

    return slow


# Alternative: two-pass approach -- walk once to get the length, then walk
# again to the target index. Same O(n) time, but two passes, and needs the
# length up front (the one-pass version above doesn't).
def from_last_two_pass(linked_list, n):
    length = 0
    current = linked_list.head
    while current:
        length += 1
        current = current.next

    target_index = length - 1 - n
    current = linked_list.head
    for _ in range(target_index):
        current = current.next
    return current


if __name__ == "__main__":
    from linked_list import LinkedList
    l = LinkedList()
    for x in ['a', 'b', 'c', 'd']:
        l.insert_last(x)
    print(from_last(l, 2).data)  # b
