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

# Complete the findMergeNode function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def findMergeNode(head1, head2):
    '''
    #Method1
    addr = {}   #Creating a dictionary to save addresses of the visited nodes
    start1 = head1 
    start2 = head2
    while(start1): #Run until last node of the first linked list and saving addresses
        addr[start1] = None
        start1 = start1.next
    #print(addr)

    while(start2):
        if(start2 in addr.keys()): #Checking if the current node if exists in the dictionary.
            return start2.data
        start2 = start2.next
    '''
    #Method2: Finding length of both the lists and adjusting the start point
    temp1 = head1 
    temp2 = head2
    len1 = 0
    len2 = 0

    while(temp1):   #Finding the length of linked list 1
        len1 += 1
        temp1 = temp1.next

    while(temp2):   #Finding the length of linked list 2
        len2 += 1
        temp2 = temp2.next

    start1 = head1 
    start2 = head2

    #Adjusting the start point to minimum length
    if(len1<len2):
        diff = len2 - len1
        while(diff):
            start2 = start2.next
            diff -= 1
        while(len1):
            if(start1 == start2):
                return start1.data
            start1 = start1.next
            start2 = start2.next
            len1 -= 1

    elif (len1 == len2):
        while(start1):
            if(start1 == start2):
                return start1.data
            start1 = start1.next
            start2 = start2.next
    
    else:
        diff = len1 - len2
        while(diff):
            start1 = start1.next
            diff -= 1
        while(len2):
            if(start1 == start2):
                return start1.data
            start1 = start1.next
            start2 = start2.next
            len2 -= 1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    tests = int(input())

    for tests_itr in range(tests):
        index = int(input())

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
            
        ptr1 = llist1.head;
        ptr2 = llist2.head;

        for i in range(llist1_count):
            if i < index:
                ptr1 = ptr1.next
                
        for i in range(llist2_count):
            if i != llist2_count-1:
                ptr2 = ptr2.next

        ptr2.next = ptr1

        result = findMergeNode(llist1.head, llist2.head)

        fptr.write(str(result) + '\n')

    fptr.close()