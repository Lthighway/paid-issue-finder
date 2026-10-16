# OMNIA Treasure Hunter

Monitor de leitura para carteiras do proprietário. Python 3.12+, SQLite, GitHub Actions, painel HTML em português. Sem IA paga, sem chaves privadas, sem assinatura e sem execução de claims. Integrado ao Paid Issue Finder com reutilização de `scripts/analyze_issues.py` e `scripts/run_finder.py` (commit inicial `a86330209119caa9a8a976515d8ad24c41916ddb`).

## Relatório e painel

- [Último relatório](https://github.com/Lthighway/paid-issue-finder/blob/treasure-data/REPORT.md)
- [Resultados JSON](https://github.com/Lthighway/paid-issue-finder/blob/treasure-data/results.json)
- [Execuções e download do painel](https://github.com/Lthighway/paid-issue-finder/actions/workflows/treasure-hunter.yml)

Baixe o artefato `omnia-treasure-hunter`, extraia e abra `index.html`. Funciona offline, sem servidor ou dependência JavaScript externa. O painel é uma fotografia: baixe novamente para ver a próxima auditoria. Não há hospedagem web contínua configurada.

## Executar

Na raiz do repositório:

```bash
python -m pip install -r treasure_hunter/requirements.txt
python -m unittest discover -s treasure_hunter/tests -v
python -m treasure_hunter scan --state treasure-state
python -m treasure_hunter notify --state treasure-state
```

`scan` não envia mensagens. `notify` só envia se os Secrets/variáveis existirem. `.sqlite` inclui cache das respostas, histórico de auditorias, estado de comparação e fila de notificações.

Carteiras são declaradas em `treasure_hunter/config/wallets.json`; é possível editá-las no GitHub sem alterar código. CLI:

```bash
python -m treasure_hunter wallet --action list
python -m treasure_hunter wallet --action add --network evm --address 0xSEU_ENDERECO
python -m treasure_hunter wallet --action remove --network evm --address 0xSEU_ENDERECO
```

Cadastre somente endereços públicos próprios. Nenhuma chave é necessária. Bitcoin (Bech32/Bech32m/Base58Check) e Stellar têm checksum validado; Solana valida Base58/32 bytes. EVM aceita hex de 20 bytes, sem exigir checksum de maiúsculas EIP-55. Não corrige endereços automaticamente.

## Cobertura real

| Integração | O que consulta | Limites |
|---|---|---|
| Bitcoin / mempool.space | saldo confirmado, saldo em mempool separado, últimas transações | 25 transações; sem Runes/Ordinals |
| Ethereum, Base, Arbitrum, Optimism, Polygon | saldo e nonce por RPC; tokens e transações Blockscout | até 3 páginas por consulta; ETH/POL não convertidos em USD |
| BNB Chain | saldo e nonce por RPC | enumeração de tokens e histórico indisponíveis sem indexador adicional |
| Solana | SOL finalizado, últimas 100 assinaturas, contas SPL e Token-2022 | sem NFTs comprimidos e sem todos os saldos em protocolos DeFi |
| Stellar / Horizon | saldos, últimas 100 transações, até 200 claimable balances e livros XLM dos ativos encontrados | total XLM não desconta reserva/passivos; predicados relativos desconhecidos não são confirmados |
| Merkl | recompensas por endereço nas seis redes e 20 campanhas (filtradas às redes monitoradas) | prova retornada pela API não equivale a verificação on-chain; positivo fica POTENCIAL |
| Aave Rescue Phase 1 | quatro listas oficiais fixadas por commit, prova Merkle, root e isClaimed via eth_call | apenas esse programa de restituição; não cobre incidentes arbitrários |
| GitHub e Algora via issues | 12 issues novas e revisão de até 30 registros anteriores, fonte original, metadata, concorrência e sinais de termos | amostra limitada; Algora não tem integração direta autenticada; texto de issue não prova valor/pagamento |

A ausência na lista oficial Aave só significa NÃO ELEGÍVEL nessa distribuição específica. Nenhum resultado vazio prova ausência universal de ativos ou oportunidades. Novos programas exigem adaptadores oficiais revisados; não há descoberta universal de todos os airdrops existentes.

### Significado dos resultados

- **CONFIRMADO**: fato demonstrado pela fonte indicada; em categoria saldo significa saldo, não recompensa. Em cobertura significa consulta concluída. Em recompensa/recuperação significa direito técnico verificado, não dinheiro recebido.
- **POTENCIAL**: evidência incompleta, token sem liquidez comprovada, campanha sem direito pessoal, ou anúncio de bounty.
- **NÃO ELEGÍVEL**: negativa restrita ao método/programa consultado, ou recompensa já reivindicada.
- **EXPIRADO**: prazo explícito do programa encerrado.
- **SUSPEITO**: prova inconsistente, sinal explícito de spam ou heurística do Paid Issue Finder.
- **INDISPONÍVEL**: erro HTTP/RPC, schema incompatível, ou cobertura não implementada.

Valores usam Decimal, nunca float para saldos. USD de bounty é valor anunciado, não patrimônio. Nenhuma soma entre ativos diferentes. Preço/liquidez não verificados ficam desconhecidos; token chamado USDT não é automaticamente tratado como dólar. Inatividade >=180 dias é só indício de esquecimento. Probabilidades de conclusão/pagamento ficam `null`: não há amostra calibrada para atribuir percentuais honestos. Reputação por estrelas não comprova histórico de pagamentos.

## Operação autônoma e custos

Workflow `OMNIA Treasure Hunter`: manual, ao alterar código/configuração, e cron `17 */6 * * *` (UTC; aproximadamente 03:17, 09:17, 15:17 e 21:17 de Brasília). GitHub pode atrasar ou omitir execuções; não é SLA de seis horas. Agendamento usa branch padrão. Repositórios públicos inativos por 60 dias podem ter o cron suspenso: verifique a aba Actions se pararem as atualizações.

Branch **treasure-data** mantém o SQLite e os relatórios entre runners. O workflow restaura a branch, faz auditoria, persiste a fila antes do envio e persiste confirmações depois. Concorrência serializada, sem force push. Falha ao salvar impede notificações. O relatório também é artefato por 30 dias. O banco e commits históricos aumentam ao longo do tempo; não há limpeza destrutiva automática. As carteiras e seus resultados são públicos neste repositório público.

Não há serviço pago obrigatório. RPCs/REST públicos podem bloquear, limitar ou mudar esquema. Cache de 5 minutos, intervalo mínimo de 350 ms, 3 tentativas em erros transitórios, backoff, timeout e limite de resposta. Quantidade limitada de resultados controla cotas. Execuções em repositórios privados consomem a franquia Actions do plano; evite habilitar cobrança automática. Consulta é gratuita; eventual claim manual pode exigir gas e não faz parte deste monitor.

### Notificações

Configure no GitHub: Settings → Secrets and variables → Actions:

- Telegram: `TELEGRAM_BOT_TOKEN`, `TELEGRAM_CHAT_ID`.
- E-mail: `SMTP_HOST`, `SMTP_PORT` (465 por padrão), `SMTP_USER`, `SMTP_PASSWORD`, `NOTIFY_EMAIL`. SMTP SSL, senha de aplicativo quando exigida pelo provedor.

Não coloque esses valores em arquivos. Alertas para recompensa, recuperação e bounty; mudanças de saldo/cobertura ficam no relatório. Cada oportunidade usa ID estável e fingerprint sem timestamps/preço. Falhas de entrega são tentadas novamente; entrega confirmada não repete nas execuções normais. Uma interrupção entre aceitação pelo provedor e persistência remota pode duplicar uma mensagem: exatamente uma entrega não é garantível sem suporte idempotente do provedor. Se mudar de destinatário/canal depois, as mensagens já concluídas não são reenviadas automaticamente.

## Fontes e contratos de leitura

- Bitcoin: https://mempool.space/docs/api/rest e BIP-173/BIP-350.
- RPC EVM: https://ethereum.org/en/developers/docs/apis/json-rpc/ ; endpoints definidos em `chains.py`, com verificação de chainId.
- Blockscout: https://docs.blockscout.com/devs/apis ; `/api/v2/addresses/{address}/transactions` e `/tokens`.
- Solana: https://solana.com/docs/rpc/http/getbalance , `getSignaturesForAddress`, `getTokenAccountsByOwner`.
- Stellar: https://developers.stellar.org/docs/data/apis/horizon/api-reference/resources/claimablebalances .
- Merkl: https://api.merkl.xyz/docs ; https://docs.morpho.org/developers/rewards/tutorials/fetch-rewards-data/ . `amount - claimed` exclui `pending`; API legada Morpho foi descontinuada e não foi usada.
- Aave/BGD: https://github.com/bgd-labs/rescue-mission-phase-1 ; mapas fixados no commit `2c15e1b1fbcf72aa3834e63f2efcd71f4f91a28f`; distribuidor em https://github.com/bgd-labs/aave-address-book/blob/main/src/MiscEthereum.sol .
- GitHub: https://docs.github.com/en/rest/search/search#search-issues-and-pull-requests .
- Algora: https://api.docs.algora.io/ ; integração atual é indireta por issues públicas.
- Actions: https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows#schedule .

## Validação

`tests/` cobre checksums, unidades, falha RPC sem saldo zero, diferença entre pending/claimable, schema incompatível, predicados Stellar, spam, prova Merkle real de referência e adulteração, persistência em conexões isoladas, deduplicação e retry por canal, bloqueio de RPC de escrita e escape HTML.

Relatórios reais são produzidos por consultas, sem fixtures no modo scan. Testes simulados de notificações não substituem envio real: nenhum envio a Telegram/SMTP foi testado sem credenciais. Veja `VALIDATION.md` para o estado verificado da entrega inicial.

Livros de ofertas Stellar: https://developers.stellar.org/docs/data/apis/horizon/api-reference/retrieve-an-order-book . Ausência de bids XLM não exclui pools AMM, outras contrapartes ou outras bolsas. Presença de bids não valida lastro nem garante conversão.
