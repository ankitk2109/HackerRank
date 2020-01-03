#!/bin/python3

import math
import os
import random
import re
import sys

class DoublyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = DoublyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node
            node.prev = self.tail


        self.tail = node

def print_doubly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)

def reverse(head):
    if(head == None):
        return
    if(head.next == None):
        return head
    else:
        p = None    #Pointing to None for start
        c = head    #Pointing to current Node 
        
        while(c != None): #Loop should run until current points to None
            n = c.next  #Initializing next pointer inside the loop so that next will always point to a valid value. i,e when current is pointing to last node next will point to None and when current is pointing to None the loop will break and avoid error on n=c.next as None doesnot have 'next'.
            c.next = p  #Pointing current.next to previous
            c.prev = n  #Pointing current.prev to next
            p = c   #Changing previous pointer to current
            c = n   #Changing current pointer to next
    
    head = p    #Previous pointer is pointing to last node at last
    return head


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        llist_count = int(input())

        llist = DoublyLinkedList()

        for _ in range(llist_count):
            llist_item = int(input())
            llist.insert_node(llist_item)

        llist1 = reverse(llist.head)

        print_doubly_linked_list(llist1, ' ', fptr)
        fptr.write('\n')

    fptr.close()
