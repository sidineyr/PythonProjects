# Portal da Descoberta

Vinheta instrumental original para a abertura do portfólio de Sidiney Rodrigues. **14 segundos**, 112 BPM, estéreo, com metais, cordas, coro sem palavras, percussão e sirene musical sintetizada.

- [Ouvir / baixar MP3](portal_da_descoberta.mp3)
- [WAV sem compressão](portal_da_descoberta.wav)
- [MIDI da composição](portal_da_descoberta.mid)
- [Prompt e roteiro musical](PROMPT.md)
- [Código reproduzível](compor.py)
- [Validação técnica e hashes](validacao.json)

## Narrativa

0–3 s: impacto grave, tensão e sirene. 3–7 s: cordas ascendentes e percussões sobrepostas. 7–11 s: revelação em metais e harmonia luminosa. 11–14 s: acorde final, sinos e ressonância.

Composição e programação com assistência de IA a partir da direção musical de Sidiney Rodrigues. Renderização General MIDI com FluidR3 GM; sirene e efeitos calculados por código. Não é gravação de orquestra, nem uma saída de um serviço de geração musical. Não foram utilizadas amostras das vinhetas citadas como inspiração.

Referências documentais: [retrospectiva oficial de Brian Tyler sobre a abertura Universal](https://www.youtube.com/watch?v=UG7x89vX2hk) e [análise acadêmica da linguagem audiovisual do Plantão](https://www.udesc.br/arquivos/ceart/id_cpmenu/5936/Semi_tica_discursiva_aplicada_ao_Jornalismo_an_lise_de_textos_televisivos_1550508869815_5936.pdf). Essas referências orientam escala, crescendo e atenção; não foram transcritas melodias ou arranjos. Não houve audição direta das gravações pela ferramenta.

## Reproduzir a renderização

```sh
sudo apt-get install fluidsynth fluid-soundfont-gm ffmpeg
python3 compor.py --render
```

Somente MIDI: `python3 compor.py`, usando apenas a biblioteca padrão. O workflow `Renderizar abertura do portfolio` gera MP3, WAV e MIDI e registra duração, nível RMS, pico e SHA-256. O banco de sons não é redistribuído.

No portfólio, a vinheta é a primeira faixa após a autorização do visitante, seguida pelas versões de Saída da Caverna.
