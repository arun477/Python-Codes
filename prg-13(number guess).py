def guessing():
    import random
    print('I am going to think number randomly between 1 to 10')
    print('you have to enter any number between 1 to 10')
    print('if your number match with the my random number your are the winner buddy!!, and you have three chances to get the right answer')
    
    g=0
    while g!=3:
        print('Now please enter your guess bellow')
        g=g+1
        guess=int(input())
        r=random.randint(1,10)
        if  guess<r :
          print('your guess is too low buddy try one more time!')
        elif guess>r:
          print('your guess is too high buddy try one more time!')
        elif guess==r:
          print('your guess'+str(guess)+' correct buddy cooool!!!')
    print('see you later')
         
    
    

        
    
print('Are you ready to play the number guess game')
print('enter yes to play the game otherwise enter no')
enter=input()
if enter=='yes':
    print('lets go into the game')
    guessing()


else:
       print('see you later')
