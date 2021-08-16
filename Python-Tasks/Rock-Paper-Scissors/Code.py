"""
0-Rock
1-Paper
2-Scissor
"""
import random
import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')
    
Options={0:"Rock",1:"Paper",2:"Scissor"}
# Created Dictionary of available choices 
poss={(0, 1):1,(0, 2):0,(1, 2):2}
# Dictionary of possibilities and the winner value
# print("Hi User!")
player=int(input("Please enter your choice: 0-Rock | 1-Paper | 2-Scissor : "))
# User input
while player not in Options.keys():
    cls()
    player=int(input("Please enter your choice: 0-Rock | 1-Paper | 2-Scissor : "))

print("you choose "+Options[player] )
computer=random.randrange(0,3)
# Comuters random choice

print("computer choose "+Options[computer] )
res=[player,computer]
res.sort()
res=tuple(res)

# Below is the if else loop to decide winner
if player==computer:
    print(" It is a tie !!...")
elif poss[res]==computer:
    print("Computer won the game by choosing "+Options[computer] )
elif poss[res]==player:
    print("You won the game by choosing "+Options[player] )