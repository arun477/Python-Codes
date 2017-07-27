import random
guessesTaken=0
print('Hello! What is your name?')
myName=input()
number=random.randint(1,20)
print('Well' +myName+ 'Iam thinking of a number between 1 and 20 try to find it bout you have only 6 chances to guess')
while guessesTaken<6:
    print('Take a guess')
    guess=int(input())
    guessesTaken=guessesTaken+1
    if guess<number:
        print('Your guess is too low.')
    if guess>number:
        print('your guess is too high.')
    if guess==number:
        break
    if guess!=number:
     guessesTaken=str(guessesTaken)
     print('cool'+myName+'your guess'+guessesTaken+'correct')
    if guess!=number:
        print('sorry dude try one more time')
