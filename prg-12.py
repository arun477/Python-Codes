import random
print('I am thinking of a number between 1 and 20')
guess=int(input())
r=random.randint(1,20)
while guess==r:
    print('your guess'+str(guess)+' is righ you won')
if guess<r:
    print('your guess is too low')
elif guess>r:
    print('your guess is too high')
     continue
    
