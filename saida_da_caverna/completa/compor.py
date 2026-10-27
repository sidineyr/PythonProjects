"""Saída da Caverna: composição original reprodutível, sem dependências Python.

python compor.py --render --soundfont /usr/share/sounds/sf2/FluidR3_GM.sf2
Requer FluidSynth e FFmpeg para renderizar; somente MIDI usa biblioteca padrão.
"""
import argparse
import hashlib
import json
import random
import struct
import subprocess
from pathlib import Path

BPM, PPQ, BARS = 88, 480, 54
CHORDS = {'C': [48,52,55], 'Am': [45,48,52], 'F': [41,45,48],
          'G': [43,47,50], 'Dm': [50,53,57], 'Em': [40,43,47]}

def vlq(n):
    out = [n & 127]
    while n >> 7:
        n >>= 7
        out.insert(0, (n & 127) | 128)
    return bytes(out)

def meta(kind, text):
    raw = text.encode('utf-8')
    return bytes([255, kind]) + vlq(len(raw)) + raw

def track(events):
    data, previous = bytearray(), 0
    for tick, priority, message in sorted(events):
        data.extend(vlq(tick - previous) + message)
        previous = tick
    data.extend(b'\x00\xff\x2f\x00')
    return b'MTrk' + struct.pack('>I', len(data)) + data

def compose(ending):
    rng = random.Random(88054)
    piano, pad, pulse = [], [], []
    def note(dst, channel, pitch, beat, duration, velocity, human=True):
        offset = rng.uniform(-0.018, 0.018) if human else 0
        start = max(0, round((beat + offset) * PPQ))
        vel = max(1, min(127, velocity + (rng.randint(-3,3) if human else 0)))
        dst.extend([(start, 1, bytes([0x90+channel,pitch,vel])),
                    (start+round(duration*PPQ), 0, bytes([0x80+channel,pitch,0]))])
    piano.extend([(0,0,meta(3,'Piano acustico')), (0,0,b'\xc0\x00'),
                  (0,0,b'\xb0\x07\x64'), (0,0,b'\xb0\x5b\x24')])
    pad.extend([(0,0,meta(3,'Textura suave')), (0,0,b'\xc1\x59'), (0,0,b'\xb1\x07\x26')])
    pulse.extend([(0,0,meta(3,'Pulsacao central')), (0,0,b'\xc2\x50'), (0,0,b'\xb2\x07\x1c')])
    progression = ['Am','Em','F','C','Am','Em','Dm','G']
    progression += ['C','Am','F','G'] * 4
    progression += ['C','Em','F','G','Am','F','Dm','G'] * 2 + ['F','G']
    progression += ['C','Am','F','G','C','Am','Dm','G']
    progression += {'luminoso':['F','G','C','C'],
                    'suspenso':['F','G','Am','Am'],
                    'sereno':['Dm','G','C','C']}[ending]
    assert len(progression) == BARS
    for bar, chord in enumerate(progression):
        base, notes = bar*4, CHORDS[chord]
        if bar < 8:
            strength, rhythm = 43, [(0,1.35),(2.3,1.1)]
        elif bar < 24:
            strength, rhythm = 55, [(0,.8),(1,.7),(2,.8),(3,.65)]
        elif bar < 42:
            strength, rhythm = 66, [(0,.7),(.9,.6),(1.6,.7),(2.5,1.1)]
        else:
            strength, rhythm = 54 - (bar-42)//2, [(0,1.25),(1.6,.9),(3,.7)]
        note(piano,0,notes[0]-12,base,3.5,strength-17)
        for k,p in enumerate(notes[1:]+[notes[0]+12]):
            note(piano,0,p,base+.08+k*.06,3.15,strength-21)
        motif = [60,62,59,64] if bar < 24 else [64,65,62,67]
        if bar < 8:
            melody = motif[(bar%2)*2:(bar%2)*2+2]
        else:
            melody = [p + (12 if 32<=bar<40 else 0) for p in motif]
            if bar%4 == 3:
                melody[-1] = 67 if bar<24 else 72
        if bar >= 50:
            final = {'luminoso':72,'suspenso':69,'sereno':76}[ending]
            melody = {50:[69,72,69],51:[71,74,67],52:[final],53:[]}[bar]
            rhythm = [(0,3.8)] if bar == 52 else [(0,1),(1.5,1),(3,.8)]
        for (offset,duration), pitch in zip(rhythm,melody):
            note(piano,0,pitch,base+offset,duration,strength)
        if 8<=bar<50 and bar%2==0:
            for pitch in notes:
                note(pad,1,pitch+12,base,7.5,35 if bar<24 else 44,False)
        if 24<=bar<42:
            for offset in [0,1,2,3]:
                note(pulse,2,notes[0]+12,base+offset,.12,38 if offset%2==0 else 28,False)
    end = round((BARS*4 + 8)*PPQ)
    for dst,ch in [(piano,0),(pad,1),(pulse,2)]:
        dst.append((end,0,bytes([0xb0+ch,123,0])))
    tempo = [(0,0,meta(3,'Saida da Caverna - '+ending)),
             (0,0,b'\xff\x51\x03'+round(60000000/BPM).to_bytes(3,'big')),
             (0,0,b'\xff\x58\x04\x04\x02\x18\x08')]
    for bar,label in [(0,'Introducao'),(8,'Descoberta do motivo'),(24,'Expansao luminosa'),(42,'Serenidade'),(50,'Encerramento')]:
        tempo.append((bar*4*PPQ,0,meta(6,label)))
    tempo.append((end,0,meta(1,'Fim')))
    data = b'MThd'+struct.pack('>IHHH',6,1,4,PPQ)
    data += b''.join(track(t) for t in [tempo,piano,pad,pulse])
    common = sorted(e for t in [piano,pad,pulse] for e in t if e[0]<50*4*PPQ)
    return data, hashlib.sha256(repr(common).encode()).hexdigest()

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--render',action='store_true')
    parser.add_argument('--soundfont',default='/usr/share/sounds/sf2/FluidR3_GM.sf2')
    args = parser.parse_args()
    root = Path(__file__).resolve().parent
    hashes = []
    report = {'bpm':BPM,'compasso':'4/4','compassos':BARS,'duracao_audio_segundos':153,'versoes':[]}
    for ending in ['luminoso','suspenso','sereno']:
        midi, common_hash = compose(ending)
        hashes.append(common_hash)
        stem = root / ('saida_da_caverna_'+ending)
        stem.with_suffix('.mid').write_bytes(midi)
        if args.render:
            raw = root / ('temporario_'+ending+'.wav')
            subprocess.run(['fluidsynth','-ni','-g','0.65','-R','0.24','-C','0',args.soundfont,str(stem.with_suffix('.mid')),'-F',str(raw),'-r','44100'],check=True)
            subprocess.run(['ffmpeg','-y','-i',str(raw),'-af','apad,afade=t=out:st=149:d=4','-t','153','-c:a','pcm_s16le',str(stem.with_suffix('.wav'))],check=True)
            subprocess.run(['ffmpeg','-y','-i',str(stem.with_suffix('.wav')),'-codec:a','libmp3lame','-b:a','192k',str(stem.with_suffix('.mp3'))],check=True)
            raw.unlink()
            import wave
            with wave.open(str(stem.with_suffix('.wav')),'rb') as wav:
                assert abs(wav.getnframes()/wav.getframerate()-153)<.01
                assert wav.getnchannels()==2
        report['versoes'].append({'nome':ending,'sha256_midi':hashlib.sha256(midi).hexdigest(),'sha256_corpo_comum':common_hash})
    assert len(set(hashes))==1, 'Os primeiros 50 compassos devem ser identicos'
    (root/'validacao.json').write_text(json.dumps(report,indent=2,ensure_ascii=False),encoding='utf-8')
    print(json.dumps(report,indent=2,ensure_ascii=False))

if __name__ == '__main__':
    main()

