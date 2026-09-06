# Checklist de revisão — SOMENTE Android v0.1

Este checklist separa o que bloqueia a revisão do código do que será necessário apenas antes de uma futura publicação. Marque um item somente quando houver evidência reproduzível.

## 1. Pronto para solicitar revisão do PR

- [ ] O workflow **SOMENTE Android** conclui em verde no commit mais recente.
- [ ] `testDebugUnitTest`, `lintDebug` e `assembleDebug` passam no GitHub Actions.
- [ ] O APK de depuração instala e abre em um telefone Android 8.0 ou superior.
- [ ] Os três fluxos funcionam no telefone: reconhecer, ler/acompanhar e criar/salvar exercício.
- [ ] O mesmo roteiro é concluído em um tablet, sem conteúdo cortado ou controles inacessíveis.
- [ ] Com TalkBack, todos os controles têm nome compreensível e a ordem de foco permite concluir os três fluxos.
- [ ] Com o maior tamanho de fonte do sistema, o texto permanece legível e os botões continuam utilizáveis.
- [ ] Resultados, aparelho/versão do Android e problemas encontrados estão registrados no PR.

Quando todos os itens desta seção estiverem concluídos, o PR pode sair de rascunho e receber revisão. Isso ainda não autoriza merge nem publicação.

## 2. Somente antes de um teste fechado futuro

- [ ] Confirmar o nome **SOMENTE** e o pacote `br.com.sidineyr.somente`.
- [ ] Definir responsável e contato público na política de privacidade.
- [ ] Criar o ícone 512 × 512, a imagem de destaque 1024 × 500 e capturas de telefone/tablet.
- [ ] Criar e guardar com segurança a chave de upload.
- [ ] Gerar o AAB assinado e testá-lo localmente.
- [ ] Preencher público-alvo, segurança de dados, classificação indicativa e demais campos do Play Console.
- [ ] Executar um teste fechado e corrigir o relatório de pré-lançamento.

## Registro mínimo dos testes manuais

| Ambiente | Versão Android | Tela/fonte | TalkBack | Três fluxos | Resultado/observações |
|---|---|---|---|---|---|
| Telefone |  | Padrão e máxima | Ligado/desligado |  |  |
| Tablet |  | Padrão e máxima | Ligado/desligado |  |  |
