#Problem Statement at: https://www.hackerrank.com/challenges/compare-two-linked-lists/
#!/bin/python3

import os
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

# Complete the compare_lists function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
'''
def compare_lists(llist1, llist2):
    count1 = 0
    count2 = 0
    head1 = llist1
    head2 = llist2
    if (llist1 == None and llist2 == None):
        return 1
    else:
        while (head1): #Counting elements in List 1
            count1 += 1
            head1 = head1.next
        while (head2): #Counting elements in List 2
            count2 += 1
            head2 = head2.next
        #print('Linked list 1 length:',count1)
        #print('Linked list 2 length:',count2)
        if(count1 == count2):
            #print('count equal')
            while(llist1.next != None and llist2.next != None):
                if(llist1.data == llist2.data):
                    llist1 = llist1.next
                    llist2 = llist2.next
                else:
                    #print('Not Identical')
                    return 0
            #print('Identical')
            return 1
        else:
            #print('Not Identical')
            return 0
'''
#Alternate Approach
def compare_lists(llist1, llist2):
    while llist1 and llist2:
        if llist1.data != llist2.data:
            return 0
        llist1 = llist1.next
        llist2 = llist2.next

    if llist1 is None and llist2 is None:
        return 1
    else:
        return 0

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    tests = int(input())

    for tests_itr in range(tests):
        llist1_count = int(input())

        llist1 = SinglyLinkedList()

        for _ in range(llist1_count):
            llist1_item = int(input())
            llist1.insert_node(llist1_item)
            
        llist2_count = int(input())

        llist2 = SinglyLinkedList()

        for _ in range(llist2_count):
            llist2_item = int(input())
            llist2.insert_node(llist2_item)

        result = compare_lists(llist1.head, llist2.head)

        #fptr.write(str(int(result)) + '\n')

    #fptr.close()
