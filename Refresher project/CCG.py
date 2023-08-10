
import random
print("Winning rules of the colors choices Game🕹️ as follows:"  + "\n Enter a number from 1 to 5 and match computer choice to win🏆")
c_score = 0
p_score=0

while True:
    print("red= 1\n yellow= 2\n orange= 3\n green= 4\ntake a turn:")
    p_choice = int(input("user turn:"))

    while p_choice > 5 and p_choice<1:
          p_choice=int(input("enter valid input:"))

    
    if p_choice ==1:
               c_col = "red"
    elif p_choice ==2:
               c_col="yellow"
    elif p_choice ==3:
               c_col = "orange"
    elif p_choice == 4:
               c_col = "green"
    else:
         c_col = "blue"
        
          
    print("user colr choice is:" +c_col)
    print("\n Now its computer turn to choose a color...:")
          
    c_choice = random.randint(1,5)

    while c_choice == p_choice:
          c_choice = random.randint(1,5)


      
    if c_choice ==1:
               c_c_col = "red"
    elif c_choice ==2:
               c_c_col="yellow"
    elif c_choice ==3:
              c_c_col = "orange"
    elif c_choice == 4:
               c_c_col = "green"
    else:
         c_c_col = "blue"    

    print("computer color choice is:" +c_c_col)  

    if(c_col ==c_c_col):
            p_score ==1
            print("playerscore:" + str(p_score)) 
            print("computer score:" + str(c_score))
    else:
            c_score+=1

            print("player score:" +str(p_score))
            print("computer score:" + str(c_score)) 
    
    print("do you want to play again? (y/n):")
    answer = input()

    if answer =='n' or answer =='N':
            break