# Recebimento sem desembolso — 16/10/2026

Limite autorizado: zero gastos. O monitor não usa carteira assinante, não cria
trustlines, não paga gas, não converte ativos e não contrata serviços.
`payout_assessment` distingue oportunidade de renda efetivamente recebida.
Não há pagamento automático habilitado nem rendimento garantido.

## Caminho pesquisado: Superteam Earn

Fonte oficial: https://superteam.fun/earn/agents
FAQ: https://docs.superteam.fun/the-superteam-handbook/community/faqs/superteam-earn-faq

A plataforma tem API oficial para agentes, com anúncios AGENT_ALLOWED e AGENT_ONLY.
Permite descobrir trabalho e entregar resultados. O patrocinador seleciona vencedores;
um operador humano deve vincular o agente e completar perfil para receber.
Alguns patrocinadores exigem KYC. Isso não é renda passiva nem depósito incondicional.

O adaptador de descoberta está preparado, mas BLOQUEADO por falta de credencial.
Seu schema foi testado com fixtures, não com uma resposta autenticada real.
É necessário cadastrar um agente no serviço e armazenar sua chave em
Actions Secrets como SUPERTEAM_API_KEY. Não colocar a chave nem claimCode no
repositório, logs ou SQLite. Nunca fornecer seed da carteira.
O cadastro externo, aceite de termos, vínculo humano e submissões não foram realizados.
O endpoint é apenas GET; esta implementação não entrega trabalhos automaticamente.

## Correções da triagem anterior

- https://github.com/oll4com/spaceapp/issues/65: US$450, primeira solução aceita,
  pagamento por PayPal, Wise ou banco em até sete dias após merge. Não é rota
  comprovada de depósito cripto; concorrência já identificada.
- https://github.com/paraloom-labs/paraloom-wallet/issues/89: relatório de falhas
  apresentado por outro pesquisador; a menção a US$150 USDC não comprova tarefa
  remunerada disponível para nós. O detector agora exclui esse padrão da triagem.
- Claimable balances Stellar: patrocínio da reserva do registro não implica
  patrocínio da transação de claim nem de uma trustline. Não executar sob limite
  zero sem identificar quem assume todos os custos.

Fontes Stellar:
https://developers.stellar.org/docs/build/guides/transactions/sponsored-reserves
https://developers.stellar.org/docs/build/guides/transactions/fee-sponsorship

Algora oficial (algora.io) anuncia pagamentos bancários via seu fluxo de payouts;
não confundir com sites de investimento de nome semelhante.
https://algora.io/swift

## O que falta para lucro

Uma oportunidade válida, trabalho original aceito, beneficiário verificado, termos
de pagamento e custos confirmados. Receber exige um pagador; scripts não criam
esse direito. O monitor continua a cada seis horas, sem iniciar gastos ou assinar
transações quando nenhuma rota elegível existe. Custos tributários pessoais não
podem ser certificados como zero por este software.
