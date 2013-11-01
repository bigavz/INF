from __future__ import division
import numpy as np
import pylab as py

__author__ = 'Avi'


#synapses = np.random.rand(3,3)*0.3

## setup parameters and state variables
dt   = 0.5                   # simulation time step (msec)
T    = np.arange(0,100,dt)           # total time to simulate (msec)
raster = np.zeros(len(T))
test=np.zeros(len(T))


## LIF properties
tau_m   = 10.                       # time constant (msec)
tau_ref = 2.                        # refractory period (msec)
tau_psc = 5.                       # post synaptic current filter time constant
Vth     = 1.                        # spike threshold (V)

## Currents
I    = 0.
Iext = 1.5

V = 0
last_spike=0 #or -tau_ref

#check if in refractory period
#if not, spike
#np.nonzero(last_spike>0) returns proper indices. righteous, so you can call this in spike(V[])

for y,x in enumerate(T): #x is the timestep
    if last_spike>=0: #if time since last spike is positive
        temp = V + (I-V)/tau_m*dt
        V = temp
        if V > Vth: #if we're over the threshold voltage, we want to reset V to resting and enter refractory period of length tau_ref
            last_spike = 0-tau_ref
            V = 0
    last_spike=last_spike+dt
    #print(last_spike, V) keep track of refrac time and corresponding voltage!
    I = Iext + x*np.exp((0-x)/tau_psc)
    raster[y] = V


py.plot(T, np.transpose(raster), 'b.')
py.show()

