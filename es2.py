from pyo import *

s = Server().boot()
s.setAmp(0.2)

#n = Noise()

mmap= SLMap(0,1000,'lin','mul',1)
fmap=SLMap(0,2,'lin','freq',0)
lfo = LFO(freq=0,sharp=1,type=3,add=1100)
lfo.ctrl(map_list=[mmap,fmap])
sf = Reson(SfPlayer('loop.wav',loop=True),lfo,10)
#sf = Reson(n,lfo,10)
o =Pan(sf,outs=2,pan=0.5).out()



sc =Scope([lfo])
sp= Spectrum(o)

s.gui(locals())