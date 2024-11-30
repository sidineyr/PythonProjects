# README.md  

## Python para Composição Musical com IA  

Este projeto é dedicado a explorar o uso de **Python** como uma ferramenta para composição musical assistida por inteligência artificial (IA). A ideia surgiu da necessidade de aprimorar a criação de músicas livres, utilizando bibliotecas Python específicas para manipulação de sons, geração de melodias e arranjos, além de scripts personalizados para personalizar e enriquecer o processo criativo.

---

## Objetivo do Projeto  

O principal objetivo é construir uma abordagem acessível e dinâmica para a composição musical, onde a programação em Python seja usada para:  

1. **Criar estruturas melódicas e harmônicas**.
2. **Automatizar processos repetitivos**, como geração de padrões rítmicos.
3. **Integrar IA no processo criativo**, usando modelos de aprendizado de máquina para sugestões e refinamentos.
4. **Promover liberdade criativa** com ferramentas abertas e gratuitas.

---

## Histórico do Desenvolvimento  

### **Início do Aprendizado**  
A jornada começou com o estudo de conceitos básicos de Python, como manipulação de listas, estruturas condicionais e loops, já que a composição musical muitas vezes se baseia em padrões repetitivos e combinações criativas de notas e ritmos.  

### **Explorando Bibliotecas Musicais**  
Foram exploradas bibliotecas específicas como:  

- **[MIDIUtil](https://midiutil.readthedocs.io/en/latest/)**: para criar e exportar arquivos MIDI.  
- **[Music21](https://web.mit.edu/music21/)**: para análise e manipulação de notas, escalas e acordes.  
- **[PyDub](https://pypi.org/project/pydub/)**: para processamento de áudio.  
- **[Magenta](https://magenta.tensorflow.org/)**: para geração de músicas com IA.  

Essas ferramentas permitiram criar os primeiros experimentos, como sequências automáticas de notas e arranjos básicos.  

### **Desenvolvimento de Scripts Personalizados**  
Com o progresso do aprendizado, foram criados scripts para:  

- Gerar melodias aleatórias com base em escalas específicas.  
- Adicionar variações rítmicas com diferentes assinaturas de tempo.  
- Combinar padrões melódicos para criar arranjos completos.  

### **Integração com IA**  
A etapa seguinte envolveu a integração com IA para refinar as composições. Ferramentas como o **TensorFlow** e o **Magenta** foram usadas para treinar modelos que sugerem variações harmônicas ou criam arranjos baseados em melodias pré-existentes.

### **Aprimoramento Contínuo**  
Ao longo do desenvolvimento, foi adotado um ciclo contínuo de aprendizado, onde cada composição criada forneceu feedback para ajustes nos scripts e modelos utilizados.  

---

## Exemplos  

1. **Geração de Melodia Simples:**  
```python
from midiutil import MIDIFile  

track = 0  
channel = 0  
time = 0  
duration = 1  
tempo = 120  
volume = 100  

melody = [60, 62, 64, 65, 67, 69, 71, 72]  

midi = MIDIFile(1)  
midi.addTempo(track, time, tempo)  

for note in melody:  
    midi.addNote(track, channel, note, time, duration, volume)  
    time += 1  

with open("melody.mid", "wb") as output_file:  
    midi.writeFile(output_file)  
```

2. **Geração Assistida por IA:**  
Utilizando o **Magenta**, o modelo gera uma melodia com base em dados de treinamento pré-processados, aprimorando a experiência musical.  

---

## Como Contribuir  

1. Clone o repositório:  
```bash
git clone https://github.com/seu-usuario/python-composicao-musical.git
```  

2. Instale as dependências:  
```bash
pip install -r requirements.txt
```  

3. Explore os exemplos e crie sua própria música!

---

## Futuro do Projeto  

O projeto visa expandir o uso de IA para incluir modelos mais avançados, como transformers especializados em geração musical, e explorar novas formas de integração com controladores MIDI e dispositivos físicos para performances ao vivo.

---

**Contribua com sua criatividade e descubra como Python pode transformar a composição musical!** 🎵  
