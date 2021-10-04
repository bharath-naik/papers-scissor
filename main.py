#!/bin/python3

Import time 
# Rock , Papera and Scissors Game

name = input("Enter your name : \n ")
print(f"Welcome!', {name},lets play rock scissor and paper\n choose from the below list")
player =input('rock(r), paper(p), scissor(s)\n')
print(player, 'vs', end=' ')
choose = randint(1,3)
#print(choose)
"""  1 = rock(r)
     2 = paper(p)
     3 = scissors(s)
"""
if choose == 1:
  computer = '@'
elif choose ==2:
    computer = 'p'
else:
  computer ='s'
print("Predicting The Result ")
time.sleep(1)
if player == computer:
  print('match is DRAW !!')
elif player == 'r' and computer == 's':
  print('PLAYER WIN')
elif player == 's' and computer == 'p':
  print('PLAYER', name, 'WIN')
elif player == 'r' and computer == 'p':
  print('PLAYER ', name, ' WIN')
elif player == 's' and computer == 'r':
  print('YOU LOOSE......')
elif player == 'p' and computer == 's':
  print('YOU LOOSE......')
elif player == 'p' and computer =='r':
  print('PLAYER ', name, ' WIN')

print("Thanks For playing game")
  
