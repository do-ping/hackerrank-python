#!/bin/python3
import sys


class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node

        self.tail = node


def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)


# Complete the mergeLists function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def mergeLists(head1: SinglyLinkedListNode, head2: SinglyLinkedListNode):
    if not head1:
        return head2
    if not head2:
        return head1

    dummy = SinglyLinkedListNode(0)
    current = dummy

    while head1 and head2:
        if head1.data <= head2.data:
            current.next = head1
            head1 = head1.next
        else:
            current.next = head2
            head2 = head2.next

        current = current.next

    if head1:
        current.next = head1
    elif head2:
        current.next = head2

    return dummy.next

    # while head2:
    #     digit = head2.data
    #
    #     previous = None
    #     current = head1
    #     while current:
    #         if current.data <= digit:
    #             if not current.next:
    #                 current.next = SinglyLinkedListNode(digit)
    #                 break
    #         elif current.data > digit:
    #             temp = SinglyLinkedListNode(digit)
    #             temp.next = current
    #             if previous:
    #                 previous.next = temp
    #             else:
    #                 head1 = temp
    #             break
    #
    #         previous = current
    #         current = current.next
    #
    #     head2 = head2.next
    #
    # return head1


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    #
    # tests = int(input())
    #
    # for tests_itr in range(tests):
    #     llist1_count = int(input())
    #
    #     llist1 = SinglyLinkedList()
    #
    #     for _ in range(llist1_count):
    #         llist1_item = int(input())
    #         llist1.insert_node(llist1_item)
    #
    #     llist2_count = int(input())
    #
    #     llist2 = SinglyLinkedList()
    #
    #     for _ in range(llist2_count):
    #         llist2_item = int(input())
    #         llist2.insert_node(llist2_item)
    #
    #     llist3 = mergeLists(llist1.head, llist2.head)
    #
    #     print_singly_linked_list(llist3, ' ', fptr)
    #     fptr.write('\n')
    #
    # fptr.close()
    for data in [
        ([1, 2, 3], [3, 4]),
        ([1, 5, 6], [3, 4])
    ]:
        data1 = data[0]
        l1 = SinglyLinkedList()
        for i in data1:
            l1.insert_node(i)

        data2 = data[1]
        l2 = SinglyLinkedList()
        for i in data2:
            l2.insert_node(i)

        result = mergeLists(l1.head, l2.head)
        print(data)
        print_singly_linked_list(result, " ", sys.stdout)
        print()
