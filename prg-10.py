import random
def getAnswer(answer):
    if answer==1:
        return 'it is certain'
    elif answer==2:
        return 'it is decidedly so'
    elif answer==3:
        return 'yes'

r=random.randint(1,3)
fortune=getAnswer(r)
print(fortune)
