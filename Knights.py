import numpy as np
import sys
from random import randint
nodes=list()
for i in range(0,8):
    for j in range(0,8):
        t=[i,j]
        nodes.append(t)
def checkMove(l):
    if 0<=l[0]<8 and 0<=l[1]<8:
        return True
    else:
        return False
    
def getMoves(node):
    m=[[1,2],[-1,2],[1,-2],[-1,-2],[2,1],[-2,1],[2,-1],[-2,-1]]
    moves=list()
    for i in range(0,8):
        x=node[0]+m[i][0]
        y=node[1]+m[i][1]
        if checkMove([x,y]):
            moves.append([x,y])
    return moves

def getStates(history,move):
    moves=getMoves(move)
    states=0
    for m in moves:
        if not m in history:
            states+=1
    return states

def findNextMoves(history):
    moves=getMoves(history[-1])
    ms=list()
    for move in moves:
        if not(move in history):
            e=(move,getStates(history,move))
            ms.append(e)
    return ms

def go(history):
    f=findNextMoves(history)
    if(f==[]):
        return False;
    else:
        moves,states=zip(*findNextMoves(history))
    maximum=max(states)
    if(maximum!=0):
        if(1 in states):
             return moves[states.index(1)]
        else:
              return moves[states.index(min(states))]
    elif(maximum==0 and len(history)==63):
        return moves[states.index(maximum)]
    else:
        return False
    

def drawHistory(history):
    sys.stdout.write("\n\n D R A W I N G\n\n")
    for i in range(0,8):
        for j in range(0,8):
            if(([i,j] in history)):
                sys.stdout.write("%.2d " % (history.index([i,j])))
            else:
                sys.stdout.write(" # ")
        sys.stdout.write('\n')
    sys.stdout.write("\n Number of Moves : "+str(len(history)))

history=list()
start_x=int(input("x"))
start_y=int(input("y"))
start=[start_x,start_y]
history.append(start)
while(True):
    m=go(history)
    if(m==False):
        break
    else:
        history.append(m)
drawHistory(history)
