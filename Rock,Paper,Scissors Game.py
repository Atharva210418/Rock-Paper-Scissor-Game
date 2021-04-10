#!/usr/bin/env python
# coding: utf-8

# In[26]:


import random
user_score=0
computer_score=0
play_count=0
print("Lets play....Rock,Paper,Scissor")
opt=["r", "p" ,"s"]

for i in range(5):
    play_count+=1
    computer_turn= random.choice(opt)
    user_turn= input("Choose your options:\n 'r'-Rock\n 'p'-Paper 's'- Scissor \n")
    
    if user_turn== "s" or user_turn=="S":
        if computer_turn =="r":
            print("Yheee....you loose!")
            computer_score+=1
        elif(computer_turn=="p"):
                print("Ahh...you win this time")
                user_score+=1
        else:
                    print("Ohhh...Its a Tie")
    elif user_turn=="p" or  user_turn=="P":
            if computer_turn =="r":
                print("Ahh...you win this time")
                user_score+=1
            elif(computer_turn =="s"):
                print("Yheee....you loose!")
                computer_score+=1
            else:
                          print("Ohhh...Its a Tie")
    elif user_turn=="r" or  user_turn=="R":
                                
                                if(computer_turn =="s"):
                                    
                
                                    print("Ahh...you win this time")
                                    user_score+=1
                                elif(computer_turn =="p"):
                                                    print("Yheee....you loose!")
                                                    computer_score+=1
                                else:
                                                         print("Ohhh...Its a Tie")
    else:
                                print("Wrong input....! Try entering from given options")
                                
                                print("*"*30)
if computer_score>user_score:
                                print("LOSER....I win and you loose")
                                print("Your score:" + str(user_score) + "\n My score:"+ str(computer_score))
elif computer_score<user_score:
                                    print("OHH Shits...You WIN...but I bet you will not win again")
                                    print("Your score:" + str(user_score) + "\n My score:"+ str(computer_score))
else:
                                            print("Iam shocked....Ahhhhh.....its a TIE")
                                    
                                                   
                                                
                                                
                                            

                                    
                                
                        
                
        


# In[ ]:


R

