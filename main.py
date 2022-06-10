import random

play = True
possible_actions = ["R", "P", "S"]

while play == True:
    print('this is a Rock, Paper and Scissors game')
    print('Enter R for rock, P for paper and S for scissors')
    user_action = input("Enter a choice (R, P, S): ")
    if user_action in possible_actions:
        print('Player  ' + user_action )
        break
    else:
        print("please choose a correct option")
        continue

computer_action = random.choice(possible_actions)
print('CPU  ' + computer_action) 


if computer_action == 'R' and user_action.upper() == 'S':     
   
    print ("Scissors beats rock, I win! ")

elif computer_action == 'P' and user_action.upper() == 'S':     
   
    print ("Scissors beats paper, I win! ")
    
elif computer_action == 'S' and user_action.upper() == 'P':   
       
         print ("Scissors beats paper! I win! ")
        
elif computer_action == 'P' and user_action.upper() == 'R':    
    
       print  ("Paper beat rock, I win! ")
else:       
        print ("its a tie")
play = True