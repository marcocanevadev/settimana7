from pyo import *
s = Server().boot()
s.setAmp(0.2)

ns= Notein(scale=1)
ns.keyboard()

env=MidiAdsr(ns["velocity"])
env.ctrl()

l1=LFO(mul=.1,add=1)
l2=LFO(mul=.4,add=1)
l1.ctrl()
l2.ctrl()


wf = LFO(freq = l1*ns["pitch"],mul = env*l2)
wf.ctrl()

wff = MoogLP(wf)

o = Pan(wf).out()

s.gui(locals())