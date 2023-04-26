from pyo import *
 
s = Server().boot()
s.setAmp(0.2)

env = Adsr(dur=1.5)
env.play()

wf = LFO(freq=200,sharp=1,mul= env)

def loo():
    env.play()
    

p = Pattern(function = loo,time = 1).play()

wf = Pan(wf).out()
sc = Scope([wf,env])

s.gui(locals())