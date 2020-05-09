# -*- coding: utf-8 -*-
"""
Created on Sat May  9 08:57:34 2020

@author: Eric
"""

import myList
myList = myList.LinkingList()

myList.trace()
for i in range(10):
    myList.append(i)
myList.delete(5)
myList.trace()

