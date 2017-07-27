def spam():
    global eggs
    eggs='spam'
def bacon():
    eggs='bacon'
def ham():
    print(eggs)

eggs=int(45)
spam()
print(str(eggs))
