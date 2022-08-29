import random

random_num = random.randint(0,2)

choice = ["rock", "paper", "scissors"]

computer_pick = choice[random_num]

#print(computer_pick)

while True:
  user_pick = input("Pick either rock or paper or scissors or q to quit : ").lower()
  if user_pick == "q":
    quit()
    
  
  