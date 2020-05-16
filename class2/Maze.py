# -*- coding: utf-8 -*-
"""
Created on Sat May 16 10:20:15 2020

@author: Eric
"""


MAZE = [[0,0,1,1,1,0,1,1,1],
        [1,0,1,1,1,0,1,1,1],
        [1,0,0,0,0,0,0,0,1],
        [1,1,1,0,1,1,1,0,1],
        [1,0,0,0,1,1,1,0,1],
        [1,0,1,0,1,0,1,0,1],
        [1,0,0,0,1,0,0,0,1],
        [1,1,1,1,0,1,1,0,1],
        [1,1,1,1,0,0,0,0,0]]

START = [0,0]
END = [8,8]
#-------------------------------#

visited = [[0 for _ in range(len(MAZE))] for _ in range(len(MAZE[0]))]
pathStack = [[START[0],START[1]]]

def run(x, y):
    if [x, y] == END:
        print(pathStack)
        print("曾經抵達終點")
    
    if x+1 < len(MAZE[0]) and MAZE[y][x+1] == 0 and visited[y][x+1] == 0:
        visited[y][x+1] = 1
        
        pathStack.append([x+1,y])
        run(x+1,y)
        pathStack.pop()
        
        
    if y-1 >= 0 and MAZE[y-1][x] == 0 and visited[y-1][x] == 0:
        visited[y-1][x] = 1
        
        pathStack.append([x,y-1])
        run(x,y-1)
        pathStack.pop()
        
    if x-1 >= 0 and MAZE[y][x-1] == 0 and visited[y][x-1] == 0:
        visited[y][x-1] = 1
        
        pathStack.append([x-1,y])
        run(x-1,y)
        pathStack.pop()
        
    if y+1 < len(MAZE) and MAZE[y+1][x] == 0 and visited[y+1][x] == 0:
        visited[y+1][x] = 1
        
        pathStack.append([x,y+1])
        run(x,y+1)
        pathStack.pop()
        

run(START[0],START[1])




