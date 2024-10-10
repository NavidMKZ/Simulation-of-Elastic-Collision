#Navid Markazi & Ali kashkouli,Isfahan University of Technology,January 2021
from vpython import *
import math
scene = canvas(width=1300, height=500)
choose={"choose":0}

def program_mode(m):
    choose["choose"]=m.index
scene.append_to_caption("program modes:")
menu(text="program modes",choices=['','LAB System','CM System'],bind=program_mode)
scene.append_to_caption("\t\t--Radius of Sphere One:2\tRadius of Sphere Two:1--")
scene.append_to_caption("\n\n")
scene.append_to_caption("Impact parameter:")
imp_p={"imp_p":0}
radius1={"r1":0}
radius2={"r2":0}
def T(s):
    imp_p["imp_p"]=s.text
winput( bind=T )
scene.append_to_caption("\t\t--The Impact parameter is allowed to choose between -3 and 3--")
scene.append_to_caption("\n\n")
while True:
    rate(1)
    if choose["choose"]!=0 and imp_p["imp_p"]!=0:
        break
    else:
        pass

def runner(r):
    global run
    run=r.checked
checkbox(bind=runner,text='Start',checked=False)
run=False

b=float(imp_p["imp_p"])          #impact parameter
r1=2
r2=1
D=r1+r2
M=(r2/r1)**3
N=(2*(b/D)*math.sqrt(1-(b/D)**2))/(M-1+2*(b/D)**2)
phi=math.asin(b/D)                                 #Calculate the angle of the first object with the horizon
v2i=0.2                                            
if M>=1-2*(b/D)**2:                                #Calculate the angle of the second object with the horizon
    theta=math.atan(N)
else:
    if b>0:
        theta=math.pi-math.atan((2*(b/D)*math.sqrt(1-(b/D)**2))/(1-M-2*(b/D)**2))
    else:
        theta=-math.pi+math.pi-math.atan((2*(b/D)*math.sqrt(1-(b/D)**2))/(1-M-2*(b/D)**2))   

if choose["choose"]==1:

    object1=sphere(pos=vector(0,0,0),radius=r1,color=color.red,make_trail=True,interval=10,retain=100)
    object2=sphere(pos=vector(-24,b,0),radius=r2,color=color.blue,make_trail=True,interval=10,retain=100)

    scene.append_to_caption("\nphi:\t\t",phi*180/math.pi,"\n\n")
    scene.append_to_caption("theta:\t\t",theta*180/math.pi,"\n\n")

    t=0
    delta_t=0.0001
    while True:                             #Calculate the position of the objects
        if run:
            rate(500)
            t=t+delta_t
            object2.pos.x=object2.pos.x+v2i*t
            if object2.pos.x+D*math.cos(phi)>object1.pos.x:
                break

    delta_t2=0.5
    time_z=0
    while True:                             #Calculate the position of the objects
        if run:
            time_z=delta_t2+time_z
            rate(60)
            t=t+delta_t2
            object2.pos.x=((math.sin(phi)*math.cos(theta)*v2i*t)/(math.sin(theta+phi)))-D*math.sin(phi)
            object2.pos.y=((math.sin(phi)*math.sin(theta)*v2i*t)/(math.sin(theta+phi)))+b
            X1=M*((math.sin(theta)*math.cos(phi)*v2i*t)/(math.sin(phi+theta)))
            object1.pos.x=X1
            object1.pos.y=-M*((math.sin(theta)*math.sin(phi)*v2i*t))/(math.sin(phi+theta))
            if time_z>=211:
                break
else:

    object1=sphere(pos=vector(0,0,0),radius=r1,color=color.red,make_trail=True,interval=10,retain=100)
    object2=sphere(pos=vector(-24,b,0),radius=r2,color=color.blue,make_trail=True,interval=10,retain=100)

    u1i=-M*v2i/(M+1)                          #The initial velocity of the first object at the center of mass
    u2i=v2i/(M+1)                         #The initial velocity of the second object at the center of mass

    t=0
    delta_t=0.001
    while True:                             #Calculate the position of the objects
        if run:
            rate(100)
            t=t+delta_t
            object2.pos.x=object2.pos.x+u2i*t
            object1.pos.x=object1.pos.x+u1i*t
            if object2.pos.x+D*cos(phi)>=object1.pos.x:
                break
    if b>0:
        x=-(M*((sin(theta))**2)+math.sqrt(1-(-1+M**2)*(sin(theta))**2))/(1+(sin(theta))**2)
        y=-sin(theta)*(M-math.sqrt(1-(-1+M**2)*(sin(theta))**2))/(1+(sin(theta))**2)
    else:
        x=-(M*((sin(theta))**2)+math.sqrt(1-(-1+M**2)*(sin(theta))**2))/(1+(sin(theta))**2)
        y=sin(theta)*(M-math.sqrt(1-(-1+M**2)*(sin(theta))**2))/(1+(sin(theta))**2)

    theta2=math.atan2(y,x)

    scene.append_to_caption("\n")
    scene.append_to_caption("theta2:\t\t",theta2*180/math.pi,"\n\n")

    delta_t2=0.001
    time_z=0
    while True:                                 #Calculate the position of the objects
        if run:
            rate(10)
            t=t+delta_t2
            time_z=time_z+delta_t2
            if b>0:
                object2.pos.x=object2.pos.x+u2i*cos(theta2)*t
                object2.pos.y=object2.pos.y+u2i*sin(theta2)*t
                object1.pos.x=object1.pos.x+u1i*cos(theta2)*t
                object1.pos.y=object1.pos.y+u1i*sin(theta2)*t
            else:
                object2.pos.x=object2.pos.x+u2i*cos(theta2)*t
                object2.pos.y=object2.pos.y-u2i*sin(theta2)*t
                object1.pos.x=object1.pos.x+u1i*cos(theta2)*t
                object1.pos.y=object1.pos.y-u1i*sin(theta2)*t
            if time_z>0.245:
                break