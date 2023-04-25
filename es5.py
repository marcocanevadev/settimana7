from pyo import *
 
s = Server().boot()
s.setAmp(0.2)

env = Adsr(dur=1.5)
env.ctrl()

wf = LFO(freq=200,sharp=1,mul= env).mix(2).out()

def loo():
    env.play()

p = Pattern(function = loo,time = 1)
sc = Scope([wf])

s.gui(locals())