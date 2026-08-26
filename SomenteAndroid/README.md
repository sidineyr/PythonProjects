# SOMENTE Android

**SOMENTE** (som + mente) é um aplicativo pedagógico para aprender música pela escuta, pela ação e pela criação. O primeiro percurso evita começar pela memorização abstrata: antes de apresentar nomes de notas, trabalha som, silêncio, comparação, altura, intensidade, pulso e ritmo.

## Percurso v0.1

1. som e silêncio;
2. sons iguais e diferentes;
3. grave e agudo;
4. forte e fraco;
5. pulso regular;
6. imitação rítmica;
7. primeira nota — Dó;
8. direção melódica.

O aplicativo sintetiza os sons no próprio aparelho e salva o progresso localmente. Não exige conta, microfone, localização ou acesso aos arquivos.

## Publicidade com limite pedagógico

O build público mantém anúncios desativados por padrão. Quando houver IDs de produção e consentimento configurados, a política permite intersticial apenas após uma aula concluída, nunca na primeira sessão, no máximo a cada quatro conclusões, com 12 minutos de intervalo e limite de três por dia. Áudio e exercício em andamento bloqueiam qualquer exibição.

Durante desenvolvimento, use somente os IDs de teste já incluídos. Antes do lançamento, implemente o fluxo de consentimento UMP, defina corretamente a faixa etária e substitua os IDs por configuração privada de release. Para público infantil ou misto, use exclusivamente anúncios não personalizados e SDKs certificados para famílias.

## Executar

Abra `SomenteAndroid` no Android Studio, aguarde a sincronização e execute `app` em Android 8.0 ou superior.

```bash
./gradlew test
./gradlew bundleRelease
```

O pacote planejado é `br.com.sidineyr.somente`, alvo Android 16/API 36 e versão inicial `0.1.0`.

## Limites da v0.1

Esta versão é um alicerce funcional, ainda não um curso completo. Antes da produção serão necessários: revisão por usuários, validação completa com TalkBack, consentimento, assinatura do AAB, ícone, capturas de tela, ficha de segurança de dados e teste fechado exigido pela conta Play Console.
