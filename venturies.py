def venturi():
    g=9.81
    print('a1,v1,p1,z1 are area,velocity,pressure,datum of the tube')
    print('a2,v2,p2,z2 are area,velocity,pressure,datum of the throat')
    print('Enter the a1')
    a1=float(input())
    a2=0.5*a1
    print('Enter the density of the fluid')
    rho=float(input())
    print('Enter the velocity at the tube or inlet velocity')
    v1=float(input())
    print('Enter the manometric readings')
    print('Enter the p1')
    p1=float(input())
    print('Enter the p2')
    p2=float(input())
    print('Enter the z1')
    z1=float(input())
    print('Enter the z2')
    z2=float(input())
    p11=p1/rho*g
    p12=p2/rho*g
    h1=p11+z1
    h2=p12+z2
    a12=a1**2
    a22=a2**2
    a=(1-a22/a12)**0.5
    h=h1-h2
    h12=(2*g*h)
    v2=h12/a
    q=a2*v2
    print('Volume flow rate through the tube')
    print(str(q)+'cubic meter per kg of fluid')
    
    
    
    
          

