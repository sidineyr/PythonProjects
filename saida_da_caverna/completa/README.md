# Saída da Caverna — composição completa

Instrumental original para piano amostrado e ambientação eletrônica discreta.
88 BPM, 4/4, 54 compassos e aproximadamente **2min33s**, incluindo a cauda final.

## Ouvir

- [Final luminoso — MP3](saida_da_caverna_luminoso.mp3)
- [Final suspenso — MP3](saida_da_caverna_suspenso.mp3)
- [Final sereno — MP3](saida_da_caverna_sereno.mp3)

Os arquivos WAV e MIDI correspondentes ficam nesta pasta após a renderização.

## Narrativa

| Compassos | Momento |
|---|---|
| 1–8 | Introdução íntima, pausas e registro médio-grave |
| 9–24 | Apresentação e desenvolvimento de Dó–Ré–Si–Mi |
| 25–42 | Transformação Mi–Fá–Ré–Sol, expansão e pulsação leve |
| 43–50 | Retorno à serenidade |
| 51–54 | Encerramento e ressonância |

Os primeiros 50 compassos são idênticos nas três versões. Os finais usam F–G–C (Dó), F–G–Am (Lá) e Dm–G–C (Mi). A pulsação aparece apenas nos compassos 25–42. Sem voz.

## Reprodução

Python 3 sem bibliotecas adicionais para gerar os MIDIs:

```bash
python3 compor.py
```

Para áudio, instale FluidSynth, FluidR3 GM e FFmpeg e execute:

```bash
python3 compor.py --render --soundfont /usr/share/sounds/sf2/FluidR3_GM.sf2
```

O workflow `Renderizar Saida da Caverna` renderiza e publica WAV, MP3 e MIDI.
`validacao.json` registra duração e hashes para comparação do corpo musical.

Composição e programação realizadas com assistência de IA a partir da direção musical de Sidiney Rodrigues. Renderização com piano amostrado General MIDI; não é uma gravação de pianista nem uma geração pelo serviço DjIA. O banco de sons não é redistribuído.
