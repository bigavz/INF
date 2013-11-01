from __future__ import division
import numpy as np
import pylab as py

__author__ = 'Avi'


#synapses = np.random.rand(3,3)*0.3

## setup parameters and state variables
population  = 10                      # number of neurons
T    = 5                     # total time to simulate (msec)
dt   = 0.125                   # simulation time step (msec)
#time = [0,4]  # time array [0..tau_ref]


## LIF properties
tau_m   = 10                       # time constant (msec)
tau_ref = 4                        # refractory period (msec)
tau_psc = 5                        # post synaptic current filter time constant
Vth     = 1                        # spike threshold (V)

## Currents
I    = np.zeros(population)
Iext = np.zeros(population) # externally applied stimulus
Iext[0] = 1.5

V =np.zeros(population) #initial voltage trace
last_spike=np.zeros(population) #initial last spike filter
for i,x in enumerate(last_spike):
    last_spike[i] = last_spike[i]-tau_ref

#check if in refractory period
#if not, spike
#when spike, set matrix indeces in last_spike to -tau_ref

#np.nonzero(last_spike>0) returns proper indeces. righteous, so you can call this in spike(V[])

#def spike(V, last_spike):
#    '''we gotta integrate the V, fire by resetting the last_spike, and playing some music'''
#    active = np.nonzero(last_spike>0)
#    temp=np.zeros(len(V))
#    temp[active] = V[active] + (I[active] - V[active]))/tau_m*dt

#I = Iext + synapses.dot(Isyn(t - last_spike))