# Sparse documentary bed for the Red Lobster pilot: 72 bpm, A minor, low drone + muted piano + soft pulse.
import numpy as np, wave
SR=48000; DUR=86.5; N=int(SR*DUR); L=np.zeros(N); R=np.zeros(N); BPM=72; B=60/BPM
def add(sig,t,g=1,pan=0):
    i=int(t*SR); sig=sig[:max(0,N-i)]; L[i:i+len(sig)]+=sig*g*(1-max(0,pan)); R[i:i+len(sig)]+=sig*g*(1+min(0,pan))
def hz(m): return 440*2**((m-69)/12)
def piano(m,d=2.5):
    n=int(d*SR); x=np.arange(n)/SR; f=hz(m)
    s=sum(a*np.sin(2*np.pi*f*k*x) for k,a in [(1,1),(2,.35),(3,.12),(4,.05)])
    return s*np.minimum(1,x/0.006)*np.exp(-x*2.2)
def drone(m,d):
    n=int(d*SR); x=np.arange(n)/SR; f=hz(m)
    s=np.sin(2*np.pi*f*x)+.5*np.sin(2*np.pi*f*2.003*x)+.25*np.sin(2*np.pi*f*1.5*x)
    return s*np.minimum(1,x/1.5)*np.minimum(1,(d-x)/1.5)
def pulse():
    n=int(.35*SR); x=np.arange(n)/SR
    return np.sin(2*np.pi*(48+40*np.exp(-x*25))*x)*np.exp(-x*9)
chords=[(45,[57,60,64]),(41,[57,60,65]),(48,[55,60,64]),(43,[55,59,62])]  # Am F C G
bar=4*B; t=0; i=0
while t<DUR:
    root,notes=chords[i%4]
    add(drone(root,2*bar+1.5),t,.10)
    for k,b in enumerate([0,1.5,3,4.5,6]):
        add(piano(notes[k%3]+(12 if k==3 else 0)),t+b*B,.11,pan=(-.3 if k%2 else .3))
    if t>18:  # pulse enters with the 2014 deal
        for b in range(8): add(pulse(),t+b*B,.22 if b%4==0 else .12)
    t+=2*bar; i+=1
m=np.max(np.abs(np.r_[L,R])); L/=m/0.6; R/=m/0.6
fo=int(2*SR); L[-fo:]*=np.linspace(1,0,fo); R[-fo:]*=np.linspace(1,0,fo)
w=wave.open('assets/music/bed.wav','wb'); w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR)
w.writeframes((np.c_[L,R]*32767).astype('<i2').tobytes()); w.close(); print('bed ok')
