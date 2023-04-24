from pyo import *

s= Server().boot()
s.setAmp(0.2)
fmap=SLMap(0,1200,'lin','value',200)
sg= Sig(200)
sg.ctrl(map_list=[fmap],title='LFOs Freq')
l1 = LFO(freq=sg,sharp=1,add=1,type=3)
l2 = LFO(freq=sg,sharp=1,add=1,type=7)

wfmap=SLMap(0,1200,'lin','freq',200)
wtmap=SLMap(0,7,'lin','type',0,res='int',dataOnly=True)
wsmap=SLMap(0,1,'lin','sharp',0.5)
wf = LFO(freq=l1,sharp=0.5,type=0,mul=l2)

wf.ctrl(map_list=[wfmap,wtmap,wsmap],title='Waveform')
o=Pan(wf).out()

sc= Scope([l1,l2,wf])

s.gui(locals())