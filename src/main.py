import random

random_num = random.randint(0,2)

choice = ["rock", "paper", "scissors"]

computer_pick = choice[random_num]

#print(computer_pick)

user_win = 0
computer_win = 0

while True:
  user_pick = input("Pick either rock or paper or scissors or q to quit : ").lower()
  
  if user_pick == "q":
    break
    
  if (user_pick not in choice):
    continue
  
    
  if (computer_pick == user_pick):
    print("Draw!")
    print(f"Computer picked {computer_pick}")
  
  elif (computer_pick == "rock" and user_pick == "scissors"):
    print("Computer won!")
    print(f"Computer picked {computer_pick}")
    computer_win += 1
    
  elif (computer_pick == "paper" and user_pick == "rock"):
    print("Computer won!")
    print(f"Computer picked {computer_pick}")
    computer_win += 1
    
  elif (computer_pick == "scissors" and user_pick == "paper"):
    print("Computer won!")
    print(f"Computer picked {computer_pick}")
    computer_win += 1
  
  else:
    print("User won!")
    print(f"Computer picked {computer_pick}.")
    user_win += 1
 
print(f"User won {user_win} times.")
print(f"Computer won {computer_win} times.")
    
  
   
    
  
  