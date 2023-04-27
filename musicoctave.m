pkg load mxml

% Cria um arquivo MIDI
midi = Midi();

% Define o tempo da música (120 bpm)
midi.setTempo(120);

% Define a faixa para um piano
track = midi.addTrack();
track.setInstrument(1);

% Define a progressão de acordes
chords = [69 71 73 74; 76 78 80 81; 83 85 87 88];
r = randi([1 3], 1, 4);
notes = chords(r, :);

% Define os valores para a duração e volume das notas
durations = [2 2 4 4];
velocities = [80 80 100 100];

% Adiciona as notas ao arquivo MIDI
for i = 1:4
  for j = 1:4
    note = Note();
    note.setChannel(1);
    note.setPitch(notes(i, j));
    note.setDuration(durations(j));
    note.setVelocity(velocities(j));
    track.addEvent(note);
  endfor
endfor

% Escreve o arquivo MIDI em disco
midi.write('mymusicmath.mid');
