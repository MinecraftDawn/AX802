# -*- coding: utf-8 -*-
"""
Created on Sat May  9 08:57:34 2020

@author: Eric
"""

import myList
        
myList = myList.LinkingList()
myList.trace()
for i in range(100):
    myList.append(i)
myList.trace()


#head = Node(100)
#head.next = Node(200)
#head.next.next = Node(300)
#
## Append
#run = head
#while run.next != None:
#    run = run.next
#run.next = Node(400)
#
#
## Trace
#run = head
#while run != None:
#    print(run.value)
#    run = run.next


