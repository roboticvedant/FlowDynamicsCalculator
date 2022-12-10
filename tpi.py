from tkinter import *
import math as m
import matplotlib.pyplot as plt
import numpy as np
root = Tk()
mlabel = Label(root,width="80",font=('Helvetica', 12), text="Welcome to my liquid lithium water fluid dynamic eqvivalency calculator")
mlabel.pack()

wlabel = Label(root,width="80",font=('Helvetica', 8), text=" The values of physical properties of Lithium are refered from Jeppson, D W, et al.\n “Lithium Literature Review: Lithium's Properties and Interactions.” Lithium Literature Review: Lithium's Properties and Interactions (Technical Report) \n | OSTI.GOV, 1 Apr. 1978, https://www.osti.gov/servlets/purl/6885395. ")
wlabel.pack()


ilabel = Label(root,width="80",font=('Helvetica', 12), text="Enter temperature of liquid lithium ('C)")
ilabel.pack()
elit = Entry(root, width=50, font=('Helvetica', 12))
elit.pack()
elit.insert(0,"")

vlabel = Label(root,width="80",font=('Helvetica', 12), text="Enter velocity of flow (m/s)")
vlabel.pack()
vlit = Entry(root, width=50, font=('Helvetica', 12))
vlit.pack()
vlit.insert(0,"")

olabel = Label(root,width="80",font=('Helvetica', 12), text="Enter the hydraulic diameter of orfice (in m)")
olabel.pack()
olit = Entry(root, width=50, font=('Helvetica', 12))
olit.pack()
olit.insert(0,"")

wlabel = Label(root,width="80",font=('Helvetica', 12), text="Enter diameter of water nozzle in m")
wlabel.pack()
wlit = Entry(root, width=50, font=('Helvetica', 12))
wlit.pack()
wlit.insert(0,"")

def myClick():
    A = 2.414 / (100000)
    B = 247.8
    C = 140
    D = 235.8 / 1000
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

    temp = elit.get()
    t = int(temp)
    rho = (0.515 - ((1.01 * (m.pow(10, -4))) * (t - 200))) * 1000
    eeta = m.pow(10, (1.4936 - 0.7368 * (m.log(t + 109.95 / t, 10)))) * 0.001
    tk = t + 273.15
    sigma = 0.16 * (3550 - tk) - 95
    sigma = sigma * 0.001
    vflow = float(vlit.get())
    hd = float(olit.get())
    Re = (rho*vflow*hd)/eeta
    wrho = 998.02  # 75 F
    #weeta = 0.000875  # 75 F
    #wsigma = 72.75 * 0.001 #75F
    dp = float(wlit.get())
    #tkw = tw+273.15
    pi = 3.14159265359

    x = []
    y = []
    ry = []
    wy = []

    #Fr = m.sqrt(vflow*vflow/(9.81*hd))
    We = m.sqrt(rho*hd*vflow*vflow/sigma)

    #d = (m.pow((Re*weeta/We),2))/(wrho*wsigma)

    for i in range(5,100):
        x.append(i+273.15)
        tkp=i+273.15
        wsigma = D * m.pow((1 - tkp / E), F) * (1 + G * (1 - tkp / E))
        weeta = A * m.pow(10, (B / (tkp - C)))
        di = (m.pow((Re * weeta / We), 2)) / (wrho * wsigma)
        y.append(di)
        vwi = Re * weeta / (wrho * di)
        ri = (wrho*vwi*di)/weeta
        ry.append(ri)
        wi = m.sqrt(wrho*di*vwi*vwi/wsigma)
        wy.append(wi)
    xp = np.array(x)
    yp = np.array(y)
    wyp = np.array(wy)
    ryp = np.array(ry)
    plt.plot(xp, yp)
    #plt.plot(xp, ryp, label="reynold")
    #plt.plot(xp, wyp, label ="weber")
    # naming the x axis
    plt.xlabel('water temperature in Kelvin ')
    # naming the y axis
    plt.ylabel('nozzle diameter')
    #dp = 0.003175
    plt.axhline(y=dp, color='r', linestyle='--',label =f"nozzle diameter={dp}m")
    idx = np.argwhere(np.diff(np.sign(yp-dp))).flatten()
    #idy = np.argwhere(np.diff(np.sign(xp -323.15 ))).flatten()
    print(xp[idx])
    tempreq = float(xp[idx])
    print(tempreq)
    plt.title('Water nozzle diameter vs Water temp ')
    plt.legend()
    wsigma = D * m.pow((1 - tempreq/ E), F) * (1 + G * (1 - tempreq/E))
    weeta = A * m.pow(10, (B / (tempreq-C)))
    print(wsigma)
    print(weeta)
    vwater = Re*weeta/(wrho*dp)
    flowr = pi*(dp/2)*(dp/2)*vwater
    gpm = 15850.3 * flowr
    #pdiff = wrho*vwater*vwater*(1-(dp*dp)/(0.022225*0.022225))
    #print(pdiff*0.000145038)
    flabel = Label(root, width="80", font=('Helvetica', 15), text=f"Physical Parameters Used for the calculations are: \n\n Dynammic viscocity of Lithium at temperature {t}C ={eeta} \n Surface Tension of Lithium at temperature {t}C = {sigma}\n\n Density of water = {wrho} \n Dynamic viscocity of water at temperature {tempreq-273.15}C = {weeta}\n Surface tension of water at temperature {tempreq-273.15}C={wsigma}\n\n\n Reynold Number {Re}  \n Waber Number {We} \n\n\n Veclocity according to calculations \n {vwater} m/s \n and Water Temperature{tempreq-273.15} C \n flow rate in GPM {gpm} GPM")
    flabel.pack()
    plt.show()
    print(x,y)







myButton = Button(root, text="Enter Requested Data", command=myClick)
myButton.pack()



root.mainloop()