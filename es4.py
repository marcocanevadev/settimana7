from pyo import *

s= Server().boot()
s.setAmp(0.2)

fmap=SLMap(0,1200,'lin','value',200)
sg= Sig(200)
sg.ctrl(map_list=[fmap],title='LFOs Freq')
l1 = LFO(freq=sg,sharp=1,add=1,type=3)
l2 = LFO(freq=sg,sharp=1,add=1,type=7)

lfmap=SLMap(1,5,'lin','freq',1)
l3 = LFO(freq=1,sharp=1,type=7).range(0,1)
l3.ctrl(map_list=[lfmap],title='Auto Panner')

wfmap=SLMap(0,1200,'lin','freq',200)
wtmap=SLMap(0,7,'lin','type',0,res='int',dataOnly=True)
wsmap=SLMap(0,1,'lin','sharp',0.5)

wf = LFO(freq=l1,sharp=0.5,type=0,mul=l2)
wf.ctrl(map_list=[wfmap,wtmap,wsmap],title='Waveform')

wf= MoogLP(wf,2100,0.5)
wf.ctrl(title='LP Filter')



o=SPan(wf,outs=2,pan=l3).out()

sc= Scope([l1,l2,l3,wf])

s.gui(locals())