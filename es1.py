from pyo import *

s = Server().boot()

s.setAmp(0.2)

mmap=SLMap(0.1,0.5,'lin','mul',0.1)
fmap=SLMap(0,0.5,'lin','freq',0)
tmap=SLMap(0,7,'lin','type',0,res='int',dataOnly=True)
playbackspeed = LFO(freq=0,sharp=1,type=0,add=0.96)
playbackspeed.ctrl(map_list=[mmap,fmap,tmap])
sc = Scope(playbackspeed)

sf = SfPlayer(path='.\loop.wav',speed=playbackspeed,loop = True)

sf.out()

s.gui(locals())