#Problem Statement at: https://www.hackerrank.com/challenges/merge-two-sorted-linked-lists

#!/bin/python3

import math
import os
import random
import re
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
'''
def print_linked_list(llist):
    head = llist.head
    while(head):
        print(head.data,'->',end='')
        head = head.next
'''
def mergeLists(head1, head2):
    llist = SinglyLinkedList() #Temporary Linked List
    if(head1 == None and head2 == None): #if Both linked lists are empty, return None
        return None
    elif(head2 == None): #If either one the list is empty return the other list.
        return head1
    elif(head1 == None):
        return head2
    else:
        while( head1 and head2 ):
            
            if(head1.data < head2.data): #if linked list1 data is less then linked list2 data.
                llist.insert_node(head1.data)
                head1 = head1.next
                
            elif (head1.data == head2.data):
                llist.insert_node(head1.data)
                head1 = head1.next
                llist.insert_node(head2.data)
                head2 = head2.next
                
            else:
                llist.insert_node(head2.data)
                head2 = head2.next
                
        #print_linked_list(llist)      
        if(head1 == None):
            #print('Linked list 1 finished')
            llist.tail.next = head2 #Our linked list 'llist' have two pointers head and tail. tail points to last Node. Last Node.next points to the remaining list.
            #print_linked_list(llist)
        else:
            #print('Linked list 2 finished')
            llist.tail.next = head1
            #print_linked_list(llist)
    return llist.head

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

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

        llist3 = mergeLists(llist1.head, llist2.head)

        print_singly_linked_list(llist3, ' ', fptr)
        fptr.write('\n')

    fptr.close()
