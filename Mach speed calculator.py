print('The Mach Number of the Aircraft ')
print('Fill the required variables')
print('what is the medium of the flow')
medium=input()
print('Temperature of the'+str(medium))
Temperature=float(input())
print('adiabatic index of the'+str(medium))
adiabaticIndex=float(input())
print('characteristic specific constant'+str(medium)+'in KJ')
gasConstant=float(input())
soundSpeed=float((gasConstant*adiabaticIndex*Temperature)**0.5)
print(str(soundSpeed))
print('what is the velocity of the Aircraft')
aircraftVelocity=float(input())
machNumber=float(aircraftVelocity/soundSpeed)
print('machNumber'+str(float(machNumber)))
if machNumber<1:
    print('Aircraft flying with subsonic speed')
elif machNumber==1:
    print('Aircraft flying with sonic speed')
elif 1>machNumber<5:
    print('Aircraft flying with supersonic speed')
elif machNumber>5:
    print('Aircraft flying with hypersonic speed')


      



