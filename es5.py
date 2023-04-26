from pyo import *
 
s = Server().boot()
s.setAmp(0.2)



t = Sig(1)
t.ctrl(title='tempo')

env = Adsr(0.01,0.1,0.3,2.6,1.5)
env.ctrl()

freqs= [261.63, 293.66,329.63,349.23,392.0,440.0,493.88]

wf = LFO(freq=Choice(freqs,freq=1/t),sharp=1,mul= env)

def loo():
    env.play()
    

p = Pattern(function = loo,time = t ).play()

wf = Pan(wf).out()
sc = Scope([wf,env])

s.gui(locals())