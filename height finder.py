print('Find your vertical distance')
print('How much time taken to reach the bottom in seconds')
time=float(input())
print('enter your intial velocity')
intialVelocity=float(input())
gravity=float(9.81)
verticalDistance=intialVelocity*time+gravity*time**2 /2
print(str(verticalDistance))
