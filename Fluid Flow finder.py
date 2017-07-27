print('Find your fluid flow types')
print('Enter the following variables')
print('Enter the density if you know otherwise put zero')
density=float(input())
print('Enter the velocity of the flow')
velocity=float(input())
print('Enter the length or diameter of the flow')
length=float(input())
print('Enter the absolute viscosity of the flow')
absoluteViscosity=float(input())
print('Enter the kinematics viscosity')
kinematicsViscosity=float(input())
if density==0:
    reynoldsNumber=velocity*length/kinematicsViscosity
    if reynoldsNumber<2000:
        print('Flow is laminar flow')
    else:
        print('Fow is turbulant flow')
else:
    reynoldsNumber=velocity*density*length/absoluteViscosity
    if reynoldsNumber<2000:
        print('Flow is laminar flow')
    else:
            print('Flow is turbulant flow')



