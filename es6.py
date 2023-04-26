from pyo import *
s = Server().boot()
s.setAmp(0.2)

ns= Notein(scale=1)
ns.keyboard()

env=MidiAdsr(ns["velocity"])
env.ctrl()

mm1=SLMap(4,8,'lin','freq',4)
mf1=SLMap(0,0.5,'lin','mul',0.01)

mm2=SLMap(1,10,'lin','freq',4)
mf2=SLMap(0,0.8,'lin','mul',0.01)

l1=LFO(type=3,mul=.1,add=1)
l2=LFO(type=3,mul=.4,add=1)
l1.ctrl(map_list=[mm1,mf1],title="vibrato")
l2.ctrl(map_list=[mm2,mf2],title='tremolo')


wf = LFO(freq = l1*ns["pitch"],mul = env*l2)
wf.ctrl(title='waveform')

wfm1 =SLMap(20,20000,'log','freq',12000)
wfm2 =SLMap(0,5,'lin','res',0.5)
wff = MoogLP(wf)
wff.ctrl(map_list=[wfm1,wfm2],title='LP Filter')

smap=SLMap(0,1,'lin','value',0.5)
set=Sig(0.5)
set.ctrl(map_list=[smap],title='Dry/Wet')

o = Selector(inputs=[wf,wff],voice=set)
o = Pan(o).out()

sc=Scope(o)

s.gui(locals())