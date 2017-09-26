import math

a=[0.0,0.0]
b=[10.0,10.0]

#COEFICIENTE ANGULAR DA RETA
m=(b[1] - a[1])/(b[0] - a[0])

#ANGULO EM GRAUS
mA = math.degrees(math.atan(m))

disTotal=math.sqrt((b[0] - a[0])**2+(b[1] - a[0])**2)

c=[4.0,4.0]
disPercorrida=math.sqrt((c[0] - a[0])**2+(c[1] - a[0])**2)

'''
print(math.cos(math.radians(mA)))
print(math.sin(math.radians(mA)))
'''

x=disPercorrida*math.cos(math.radians(mA))
y=disPercorrida*math.sin(math.radians(mA))

print("{0:.6f}".format(x))
print("{0:.6f}".format(y))

#print("( " + str(x) + ", " + str(y) + " )") 








