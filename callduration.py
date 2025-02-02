call_dur=int(input("enter the call duration in seconds:"))
if(call_dur<=500):
    x=500*0.01
    print(x)
elif(501<=call_dur<=800):
    y=500*0.01+call_dur*0.008
    print(y)
elif(call_dur>=801):
    z=500*0.01+299*0.008+1*.005
    print(z)
