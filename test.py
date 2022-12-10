
import math as m

A = 2.414/(100000)
B= 247.8
C = 140
D = 235.8/1000
E = 647.15
F = 1.256
G = -0.625


float(A)
float(B)
float(C)
float(D)
float(E)
float(F)
float(G)



t = input("enter temperature of water")
tk = float(t)+273.15


wsigma = D*m.pow((1-tk/E),F)*(1+G*(1-tk/E))
print(wsigma)
viscpas = A*m.pow(10,(B/(tk-C)))
print(viscpas)