# SOMENTE Android

**SOMENTE** (som + mente) é um laboratório pedagógico gratuito para iniciantes de qualquer idade. A experiência reúne escuta, leitura e criação sem exigir conta, internet, anúncios, microfone ou conhecimento prévio de partitura.

## Três modos de aula

1. **Escutar e reconhecer** — o estudante ouve uma nota, escolhe seu nome e vê a resposta na pauta.
2. **Ler e ouvir** — uma sequência curta é reproduzida enquanto a nota atual é destacada.
3. **Criar exercício** — professor ou estudante monta até 16 notas, ouve o resultado e salva a atividade localmente.

O desenho se inspira na clareza de aplicativos de partitura para Android, mas segue uma progressão própria: ouvir → reconhecer → visualizar → criar. Os exemplos são originais e não incluem repertório protegido.

## Executar

Abra a pasta `SomenteAndroid` no Android Studio, aguarde a sincronização do Gradle e execute o módulo `app` em Android 8.0 ou superior. Na linha de comando, com Gradle 8.14.3 instalado:

```bash
gradle testDebugUnitTest lintDebug assembleDebug
```

O pacote é `br.com.sidineyr.somente`, com alvo Android 16/API 36 e versão `0.1.0`.

## Uso responsável

- use volume confortável, especialmente com fones;
- o nome das notas segue a nomenclatura em português;
- o exercício salvo permanece apenas neste aparelho;
- valide contraste, tamanhos de toque e TalkBack em aparelho real antes de publicar.

## Limites da v0.1

O MVP usa ondas senoidais e valores rítmicos iguais. Compassos, figuras rítmicas, claves adicionais, transposição e exportação ficam para versões posteriores. Antes da Google Play ainda são necessários ícone, capturas, AAB assinado e teste fechado.
