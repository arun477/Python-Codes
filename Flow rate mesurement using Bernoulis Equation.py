print('Flow rate measurement by using Bernoulis equation')
print('p1,v1,z1 are flow properties at inlet')
print('p2,v2,z2 are flow properties at outlet')
print('where rho,g are density and gravity of the flowing fluid')
print('All units are in'+'SI'+'units')
g=9.81
print('Enter what kind of mesuring instrument used in the flow measurement i.e. venturimeter or orificemeter or nozzle')
instrument=input()
if instrument=='venturimeter':
    import venturies
     venturi()
    

