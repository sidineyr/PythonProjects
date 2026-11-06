"""Portal da Descoberta — vinheta original, MIDI + sirene sintetizada.
Python 3, biblioteca padrão. Render: FluidSynth, FluidR3 GM e FFmpeg.
"""
import argparse, array, hashlib, json, math, random, struct, subprocess, wave
from pathlib import Path

ROOT=Path(__file__).resolve().parent
BPM, PPQ, RATE, DURATION=112,960,44100,14.0
STEM='portal_da_descoberta'

def vlq(n):
    out=[n&127]
    while n>>7:
        n>>=7;out.insert(0,(n&127)|128)
    return bytes(out)

def track(events):
    data=bytearray();last=0
    for tick,priority,msg in sorted(events):
        data.extend(vlq(tick-last)+msg);last=tick
    data.extend(b'\x00\xff\x2f\x00')
    return b'MTrk'+struct.pack('>I',len(data))+data

def compose():
    rng=random.Random(6112026);parts=[]
    def part(channel,program,name,volume=90,pan=64):
        raw=name.encode('utf-8');events=[(0,-3,b'\xff\x03'+vlq(len(raw))+raw),(0,-2,bytes([0xc0+channel,program])),(0,-1,bytes([0xb0+channel,7,volume])),(0,-1,bytes([0xb0+channel,10,pan])),(0,-1,bytes([0xb0+channel,91,48]))];parts.append(events);return events
    def note(dst,ch,pitch,t,d,vel):
        start=max(0,round((t+rng.uniform(-.008,.008))*BPM/60*PPQ));end=start+round(d*BPM/60*PPQ)
        dst.extend([(start,1,bytes([0x90+ch,pitch,max(1,min(120,vel+rng.randint(-2,2)))])),(end,0,bytes([0x80+ch,pitch,0]))])
    horn=part(0,60,'Trompas — motivo original',99,56)
    low=part(1,57,'Trombones e graves',88,72)
    strings=part(2,48,'Cordas em expansao',73,46)
    choir=part(3,52,'Coro sem palavras',61,80)
    timp=part(4,47,'Timpanos',86,62)
    bells=part(5,14,'Sinos de descoberta',65,89)
    trumpet=part(6,56,'Metais luminosos',88,69)
    harp=part(7,46,'Arpejos de harpa',61,37)
    drums=part(9,0,'Percussao cinematografica',88,64)
    # Opening tension: E minor + suspended colour, not a quoted logo melody.
    for p in [28,40,47]: note(low,1,p,.04,1.55,72)
    for t,p,d,v in [(.45,59,.24,79),(.82,64,.22,83),(1.13,70,.25,87),(1.62,66,.48,91),(2.28,68,.26,91),(2.61,75,.25,94),(2.95,73,.24,92),(3.38,71,.62,96)]:
        note(horn,0,p,t,d,v)
    chords=[(0.15,2.0,[40,47,54,55]),(2.25,1.9,[36,43,50,52]),(4.35,1.7,[38,45,54,57]),(6.1,1.6,[35,42,49,54]),(7.9,1.65,[45,52,59,63]),(9.65,3.0,[40,47,56,59,66])]
    for t,d,chord in chords:
        for k,p in enumerate(chord):
            note(strings,2,p+12,t+k*.018,d,56+round(t*2))
            if t>=4.35:note(choir,3,p+12,t+.16,d-.12,48+round(t))
        note(low,1,chord[0],t,d*.8,75+round(t))
    # Rising strings and interlocking accents add brief controlled disorientation.
    scale=[52,54,56,58,59,63,64,66,68,70,71,75]
    for i in range(24):
        note(strings,2,scale[i%12]+(12 if i>=12 else 0),3.9+i*.145,.18,55+i)
    for i in range(14):note(harp,7,[64,66,71,75,80,83,87][i%7],6.05+i*.18,.85,62+i)
    for i,t in enumerate([.08,1.6,2.3,3.85,4.35,5.05,5.65,6.1,6.75,7.45,7.9,8.8,9.65]):
        note(timp,4,40 if i%3 else 47,t,.55,66+i*2)
        note(drums,9,36,t,.18,76+i)
    for i in range(18):note(drums,9,38,5.65+i*.105,.09,38+i*2)
    for t in [4.35,7.9,9.65]:note(drums,9,49,t,1.8,72)
    # Original fanfare: E–G#–F#–B–D#–C#–G#–E, asymmetrical phrasing.
    melody=[(7.05,76,.24),(7.38,80,.22),(7.7,78,.32),(8.13,83,.52),(8.85,87,.24),(9.15,85,.28),(9.65,80,.6),(10.42,88,1.5)]
    for t,p,d in melody:
        note(trumpet,6,p,t,d,88 if t<9.65 else 96);note(horn,0,p-12,t+.018,d,88)
    for p in [64,68,71,78]:note(horn,0,p,9.65,2.7,94)
    for t,p in [(9.68,88),(10.15,83),(10.6,90)]:note(bells,5,p,t,2.5,65)
    tempo=[(0,-1,b'\xff\x51\x03'+round(60000000/BPM).to_bytes(3,'big'))]
    for events,ch in zip(parts,[0,1,2,3,4,5,6,7,9]):events.append((round(13.2*BPM/60*PPQ),0,bytes([0xb0+ch,123,0])))
    data=b'MThd'+struct.pack('>IHHH',6,1,len(parts)+1,PPQ)+b''.join(track(x) for x in [tempo]+parts)
    (ROOT/(STEM+'.mid')).write_bytes(data)

def effects():
    rng=random.Random(140611);pcm=array.array('h');phase=0.;brown=0.;last=0.
    for i in range(round(RATE*DURATION)):
        t=i/RATE
        # A musical, sweeping siren, not a sampled emergency alarm.
        env=max(0,min(1,(t-.18)/.9))*max(0,min(1,(6.4-t)/1.8))
        freq=410+82*t+135*math.sin(2*math.pi*(.38*t+.018*t*t))
        phase+=2*math.pi*freq/RATE
        siren=.075*env*(math.sin(phase)+.23*math.sin(2.003*phase))
        noise=rng.uniform(-1,1);brown=.985*brown+.015*noise;air=noise-last;last=noise
        rise=max(0,min(1,(t-3.4)/3.4))*max(0,min(1,(7.1-t)/.3))
        whoosh=.035*rise*air+.8*rise*brown
        impact=0.
        for at in [.03,4.35,7.9,9.65]:
            dt=t-at
            if 0<=dt<.7:impact+=.17*math.exp(-dt*9)*math.sin(2*math.pi*(48*dt+18*(1-math.exp(-dt*8))))
        amp=(siren+whoosh+impact)*min(1,t/.025)*max(0,min(1,(13.6-t)/1.2))
        for pan in [1+.12*math.sin(t*1.4),1-.12*math.sin(t*1.4)]:pcm.append(round(max(-.8,min(.8,amp*pan))*32767))
    with wave.open(str(ROOT/'efeitos.wav'),'wb') as out:
        out.setnchannels(2);out.setsampwidth(2);out.setframerate(RATE);out.writeframes(pcm.tobytes())

def run(args):subprocess.run(args,check=True)

def render(soundfont):
    compose();effects();raw=ROOT/'orquestra.wav';wav=ROOT/(STEM+'.wav');mp3=ROOT/(STEM+'.mp3')
    run(['fluidsynth','-ni','-g','.32','-R','.28','-C','0',soundfont,str(ROOT/(STEM+'.mid')),'-F',str(raw),'-r',str(RATE)])
    run(['ffmpeg','-y','-i',str(raw),'-i',str(ROOT/'efeitos.wav'),'-filter_complex','[0:a][1:a]amix=inputs=2:normalize=0,apad,afade=t=in:st=0:d=0.03,afade=t=out:st=12:d=2,loudnorm=I=-16:TP=-1.5:LRA=9,aresample=44100[a]','-map','[a]','-t',str(DURATION),'-c:a','pcm_s16le',str(wav)])
    run(['ffmpeg','-y','-i',str(wav),'-c:a','libmp3lame','-b:a','192k','-metadata','title=Portal da Descoberta','-metadata','artist=Sidiney Rodrigues — assistencia de IA',str(mp3)])
    with wave.open(str(wav),'rb') as audio:
        data=audio.readframes(audio.getnframes());samples=array.array('h',data)
        duration=audio.getnframes()/audio.getframerate();peak=max(abs(x) for x in samples)/32768;rms=math.sqrt(sum(x*x for x in samples)/len(samples))/32768
        assert duration==DURATION and audio.getnchannels()==2 and rms>.005 and peak<1
    report={'title':'Portal da Descoberta','duration_seconds':duration,'sample_rate':RATE,'channels':2,'bpm':BPM,'peak_dbfs':round(20*math.log10(peak),2),'rms_dbfs':round(20*math.log10(rms),2),'method':'MIDI original, FluidR3 GM, sirene e efeitos sintetizados sem amostras de terceiros','sha256':{p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in [wav,mp3,ROOT/(STEM+'.mid')]}}
    (ROOT/'validacao.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    raw.unlink();(ROOT/'efeitos.wav').unlink()

if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--render',action='store_true');parser.add_argument('--soundfont',default='/usr/share/sounds/sf2/FluidR3_GM.sf2');args=parser.parse_args()
    if args.render:render(args.soundfont)
    else:compose();print('MIDI original criado; use --render para gerar WAV e MP3.')
