# Saída da Caverna

Miniatura original para piano, com oito compassos em Dó maior, criada como
exercício de composição musical com Python. Em cerca de 22 segundos, um motivo
hesitante é apresentado, transformado e conduzido à cadência luminosa `F–G–C`.

## Estrutura musical

| Compassos | Função | Material |
|---|---|---|
| 1–2 | Apresentação | motivo `C–D–B–E` |
| 3–4 | Variação | repetição com a última nota em `G` |
| 5–6 | Transformação | motivo elevado uma terça: `E–F–D–G` |
| 7–8 | Chegada | cadência `F–G–C` |

A melodia tem pequenas respirações e intensidades variáveis. A segunda voz é
uma harmonia grave e discreta, sem efeitos de áudio.

## Arquivos

- `saida_da_caverna.py`: composição reprodutível com `music21`;
- `saida_da_caverna.mid`: partitura MIDI;
- `saida_da_caverna.wav`: piano renderizado com FluidSynth e FluidR3 GM;
- `renderizar.sh`: regeneração do MIDI e do WAV no Linux.

## Como reproduzir

```bash
python3 -m pip install music21
sudo apt install fluidsynth fluid-soundfont-gm
chmod +x renderizar.sh
./renderizar.sh
```

Para usar outra SoundFont:

```bash
SOUNDFONT=/caminho/para/piano.sf2 ./renderizar.sh
```

## Critério de conclusão

O MIDI e o WAV devem ter menos de 30 segundos e permitir reconhecer, apenas
pela audição, apresentação, transformação e chegada.

Composição: **Sidiney Rodrigues**. Desenvolvimento realizado com assistência de IA.
