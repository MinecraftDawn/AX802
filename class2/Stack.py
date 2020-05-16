# -*- coding: utf-8 -*-
"""
Created on Sat May  9 11:17:26 2020

@author: Eric
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class Stack:
    def __init__(self):
        self.head = Node(-1)
        
    def trace(self):
        run = self.head.next
        while run:
            print(run.value)
            run = run.next
            
    def push(self, value):
        run = self.head
        while run.next:
            run = run.next
        run.next = Node(value)
        
    def pop(self):
        pre = self.head
        run = self.head.next
        
        while run.next:
            pre = pre.next
            run = run.next
            
        pre.next = None
        
        return run.value
        
        
    # def delete(self, value):
    #     pre = self.head
    #     run = self.head.next
        
    #     while run:
    #         if run.value == value:
    #             pre.next = run.next
    #             run = run.next
    #         else:
    #             pre = pre.next
    #             run = run.next
        
    
        
        
        