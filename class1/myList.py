# -*- coding: utf-8 -*-
"""
Created on Sat May  9 11:17:26 2020

@author: Eric
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkingList:
    def __init__(self):
        self.head = Node(-1)
        
    def trace(self):
        run = self.head.next
        while run:
            print(run.value)
            run = run.next
            
    def append(self, value):
        run = self.head
        while run.next:
            run = run.next
        run.next = Node(value)