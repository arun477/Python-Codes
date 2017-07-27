print('Analysis of strength of the materials')
print('what is your material')
material=input()
print('Enter the yeild point of the material in Newton/square meter')
yeildStress=float(input())
print('Enter the load on the material Newton')
load=float(input())
print('Enter the diameter of the material in meter')
diameter=float(input())
print('Enter the bredth of the material in meter')
breadth=float(input())
print('Enter the width of the material in meter')
width=float(input())
if diameter='':
    area=width*breadth/2
else:
    area=0.785*diameter**2
    break

stress=load/area
del(length)=float(input())
original(length)=float(input())
strain=del(length)/original(length)
youngsModulus=stress/strain
