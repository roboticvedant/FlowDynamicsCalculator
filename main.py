import math as m
from openpyxl import workbook
print("Welcome to my liquid lithium water fluid dynamic eqvivalency calculator")
print("All values are to be netered in SI units unless specified")
print("The values of physical properties of Lithium are refrenced from Jeppson, D W, et al.\n “Lithium Literature Review: Lithium's Properties and Interactions.” Lithium Literature Review: Lithium's Properties and Interactions (Technical Report) | OSTI.GOV, 1 Apr. 1978, https://www.osti.gov/servlets/purl/6885395. ")
print("there might be some significant error in calculation of surface tension(+- 5-6%)")
temp = input("Enter the temperature of Liquid Lithium in degree C")
t = int(temp)
rho= (0.515-((1.01*(m.pow(10,-4)))*(t-200)))*1000
eeta = m.pow(10,(1.4936-0.7368*(m.log(t+109.95/t,10))))*0.001
tk=t+273.15
sigma=0.16*(3550-tk)-95
sigma=sigma*0.001
print(rho)
print(eeta)
print(sigma)
vflow = float(input("Enter velocity of flow"))
hd = float(input("Enter the hydraulic diameter of orfice"))
#po = float(input("enter the pressure at orfice"))

print("Calculating equivalence with water flow...")
Re = (rho*vflow*hd)/eeta
#Eu = m.sqrt(rho*vflow*vflow/po)
Fr = m.sqrt(vflow*vflow/(9.81*hd))
We = m.sqrt(rho*hd*vflow*vflow/sigma)
#print(Re)
wrho = 998.02 # 70 F
weeta = 0.00975 # 70 F
wsigma = 72.75*0.001

hdw = float(input("enter hydraulic diameter of orfice for experiment"))
vwr = Re*weeta/(wrho*hdw) # water velcoity req
vwf = Fr*m.sqrt(9.81*hdw)
vww = m.sqrt(We*We*wsigma/(wrho*hdw))
print("Imp results")
print(f"velocity by reynold {vwr},by froude {vwf}, by Waber {vww}")


