# Detecção de Ameaças Cibernéticas com Aprendizado de Máquina

---

# Introdução

A segurança da informação tornou-se um dos maiores desafios da era digital. Com o crescimento exponencial da conectividade e da dependência de sistemas digitais por parte de empresas, governos e cidadãos, os ataques cibernéticos tornaram-se mais frequentes, sofisticados e prejudiciais. Organizações de todos os portes são alvos constantes de ameaças como ataques de força bruta, injeção de SQL, varreduras de portas, negação de serviço (DDoS) e comunicações com servidores de comando e controle (C2).

Este projeto propõe o desenvolvimento de um sistema de detecção de ameaças cibernéticas baseado em aprendizado de máquina, capaz de analisar o tráfego de rede e classificar automaticamente conexões como legítimas ou maliciosas. A iniciativa se insere no contexto da segurança cibernética aplicada, área de atuação crescente tanto no mercado profissional quanto na pesquisa acadêmica.

**Objetivos gerais:** desenvolver um modelos de Aprendizado Supervisionado para classificação automática de ameaças em tráfego de rede, aplicando um pipeline completo de ciência de dados — da preparação dos dados até a avaliação dos modelos.

**Justificativa:** o avanço das ameaças cibernéticas torna inviável a detecção exclusivamente manual. Sistemas baseados em IA conseguem identificar padrões complexos em grandes volumes de dados em tempo real, complementando e potencializando as capacidades das equipes de segurança.

**Público-alvo:** equipes de segurança da informação, administradores de redes, pesquisadores da área e gestores de TI que precisam de ferramentas automatizadas para monitoramento e resposta a incidentes.

---

## Problema

Nesta seção, você deve apresentar o problema que a sua investigação/experimentação busca resolver. Por exemplo, caso o _dataset_ selecionado, seja um _dataset_ que contenha uma série temporal com o preço de diversas ações da bolsa de valores, o problema pode estar relacionado a dificuldade em saber a melhor hora (hora certa??) de comprar ou então, de executar a venda de uma determinada ação.

Descreva ainda o contexto em que essa aplicação será usada, se houver: empresa parceira, tecnologias etc. Novamente, descreva apenas o que de fato existir, pois ainda não é a hora de apresentar requisitos  detalhados ou projetos.

**Atenção:** Nesta etapa, apresente apenas informações reais e já confirmadas. Não antecipe requisitos técnicos detalhados, funcionalidades específicas ou desenhos de projeto — essa parte será desenvolvida posteriormente.

> **Links Úteis**:
> - [Objetivos, Problema de pesquisa e Justificativa](https://medium.com/@versioparole/objetivos-problema-de-pesquisa-e-justificativa-c98c8233b9c3)
> - [Matriz Certezas, Suposições e Dúvidas](https://medium.com/educa%C3%A7%C3%A3o-fora-da-caixa/matriz-certezas-suposi%C3%A7%C3%B5es-e-d%C3%BAvidas-fa2263633655)
> - [Brainstorming](https://www.euax.com.br/2018/09/brainstorming/)

## Questão de pesquisa

A questão de pesquisa é o ponto de partida e a base orientadora de todo o trabalho a ser desenvolvido. Ela deve estar diretamente alinhada ao problema identificado e expressar, de forma clara, o que se deseja investigar ou comprovar.

O papel da questão de pesquisa é guiar todas as etapas do projeto — desde a definição da metodologia até a análise e interpretação dos resultados. Ao término da investigação ou experimentação, o objetivo é que seja possível responder a essa questão de forma fundamentada, utilizando evidências obtidas ao longo do processo.

**Dica:** Formule a questão de pesquisa de forma específica e objetiva, evitando perguntas muito amplas ou genéricas. Pergunte-se: "Ao final do trabalho, minha pesquisa terá condições de responder claramente a essa pergunta?"

> **Links Úteis**:
> - [Questão de pesquisa](https://www.enago.com.br/academy/how-to-develop-good-research-question-types-examples/)
> - [Problema de pesquisa](https://blog.even3.com.br/problema-de-pesquisa/)

## Objetivos preliminares

Nesta seção, você deve apresentar os objetivos preliminares do trabalho, deixando claro que o objetivo geral é experimentar modelos de aprendizado de máquina adequados para solucionar o problema descrito anteriormente.

Além do objetivo geral, é importante definir pelo menos dois objetivos específicos, que direcionem a investigação de acordo com o foco que o grupo pretende adotar. Esses objetivos específicos podem envolver: 
* Explorar um determinado tipo de modelagem ou técnica de aprendizado de máquina;
* Comparar diferentes abordagens para resolver o mesmo problema;
* Aplicar o modelo em um cenário real ou simulado;
* Otimizar parâmetros para melhorar métricas específicas de desempenho.

Exemplo:
Objetivo específico 1: Predizer a tendência de alta, estabilidade ou queda de uma determinada ação em uma janela de tempo definida.
Objetivo específico 2: Estimar o valor exato da ação ao final do período analisado.

**Importante:** À medida que a pesquisa/experimentação avança, os objetivos podem ser ajustados ou refinados. Mantenha essa seção atualizada no repositório para refletir o andamento e as novas decisões do projeto.
 
> **Links Úteis**:
> - [Objetivo geral e objetivo específico: como fazer e quais verbos utilizar](https://blog.mettzer.com/diferenca-entre-objetivo-geral-e-objetivo-especifico/)

## Justificativa

Nesta seção, apresente a importância e a motivação para trabalhar com o conjunto de dados escolhido. Explique por que esse dataset é relevante e como ele se conecta ao problema identificado anteriormente.

Indique:
* Razões para a escolha dos objetivos específicos – Justifique por que decidiu aprofundar sua investigação nessas metas, relacionando-as ao potencial de solução ou melhoria para o problema.
* Relevância do estudo do problema – Mostre a importância de compreender e tratar a questão apresentada, tanto no contexto acadêmico quanto no profissional.
* Impacto social, econômico ou ambiental – Descreva como o problema afeta a sociedade ou um setor específico, buscando sempre quantificar o impacto por meio de dados reais.

**Importante:**
* Apresente números, estatísticas e informações concretas, citando as fontes (relatórios, artigos científicos, portais oficiais etc.).
* Mantenha a objetividade e a clareza, evitando argumentos genéricos.
* Construa um texto coeso que conecte o problema, os objetivos e a relevância do trabalho.

> **Links Úteis**:
> - [Como montar a justificativa](https://guiadamonografia.com.br/como-montar-justificativa-do-tcc/)

## Público-Alvo

Nesta seção, descreva quem poderá se beneficiar com a sua investigação, apresentando os diferentes perfis de pessoas ou grupos impactados.

O objetivo aqui não é definir clientes específicos ou papéis exatos dentro da aplicação, mas sim compreender o perfil dos usuários e partes interessadas. Para isso, considere:
* Conhecimentos prévios relacionados ao domínio do problema e ao uso de tecnologia;
* Nível de familiaridade com recursos digitais e possíveis barreiras de uso;
* Contexto profissional e hierárquico, quando aplicável (ex.: nível de decisão, responsabilidades, área de atuação);
* Necessidades e expectativas que podem ser atendidas pelo projeto.

**Dica:** Seja objetivo e baseie suas descrições em informações reais ou plausíveis para o contexto escolhido. Isso ajudará a manter o foco no desenvolvimento de soluções relevantes e aplicáveis.

> **Links Úteis**:
> - [Público-alvo](https://blog.hotmart.com/pt-br/publico-alvo/)
> - [Como definir o público alvo](https://exame.com/pme/5-dicas-essenciais-para-definir-o-publico-alvo-do-seu-negocio/)
> - [Público-alvo: o que é, tipos, como definir seu público e exemplos](https://klickpages.com.br/blog/publico-alvo-o-que-e/)
> - [Qual a diferença entre público-alvo e persona?](https://rockcontent.com/blog/diferenca-publico-alvo-e-persona/)

## Estado da arte

Nesta seção, descreva abordagens da literatura que tratam problemas semelhantes ao seu. Seu objetivo é documentar métodos, dados, métricas e resultados.

### O que levantar (mínimo 5 trabalhos)
Para **cada estudo encontrado** aderente à temática do grupo, registre de forma objetiva:
* Problema e contexto: que problema o trabalho buscou resolver e em qual domínio/cenário foi aplicado.
* Dados (dataset): origem, tamanho, período, variáveis/atributos, pré-processamentos relevantes (faltantes, balanceamento, normalização).
* Abordagem/algoritmos: algoritmos utilizados e parâmetros principais (quando informados).
* Métricas de avaliação: quais e por quê (ex.: Acurácia, F1, AUC, RMSE, MAE, etc.).
* Resultados: principais números, comparações internas, limitações citadas e conclusões.

* Texto-síntese crítico (2–4 parágrafos) respondendo:
- O que os estudos concordam? Onde divergem?
- Quais lacunas permanecem (dados, métricas, cenários, limitações técnicas/éticas)?
- Como seu projeto se alinha aos estudos identificados?

**Dica:** Prefira artigos dos últimos 5 anos ou referências clássicas indispensáveis.

### Ferramentas inteligentes permitidas
Você pode utilizar: Perplexity, SciSpace, Elicit, Research Rabbit, Litmaps.
Use-as para descoberta, organização e triagem de literatura. 

**Atenção:** 
* Sempre acesse a fonte original (PDF/artigo) antes de citar; verifique números e conclusões.
* Registre DOI/URL oficial e dados bibliográficos completos.
* Evite “alucinações” das ferramentas: desconfie de referências sem DOI ou que você não consiga localizar oficialmente.
* Use as ferramentas inteligentes para mapear redes de citação (Research Rabbit), mapas de tópicos (Litmaps), filtrar por período e gerar resumos iniciais (Perplexity/SciSpace/Elicit).
* Leia os trabalhos mais promissores e descarte estudos fora de escopo.

> **Links Úteis**:
> - [Google Scholar](https://scholar.google.com/)
> - [IEEE Xplore](https://ieeexplore.ieee.org/Xplore/home.jsp)
> - [Science Direct](https://www.sciencedirect.com/)
> - [ACM Digital Library](https://dl.acm.org/)

# Descrição do Dataset Selecionado

## Identificação e Origem

| Atributo | Informação |
|---|---|
| **Nome** | Cybersecurity Threat Detection Dataset |
| **Fonte** | Kaggle — usuário dhrubangtalukdar |
| **URL** | https://www.kaggle.com/datasets/dhrubangtalukdar/cybersecurity-threat-detection-dataset |
| **Licença** | Verificar na página do Kaggle |
| **Formato** | CSV único (cybersecurity.csv) |
| **Tamanho** | ~2 MB |

## Visão Geral

O dataset contém registros de conexões de rede rotulados entre tráfego benigno e diferentes tipos de ataques cibernéticos. Cada registro representa uma única conexão de rede com informações sobre origem, destino, protocolo, volume de dados transferidos e classificação de segurança.

| Métrica | Valor |
|---|---|
| **Total de registros** | 10.000 |
| **Total de atributos** | 13 colunas |
| **Tráfego benigno (label = 0)** | 9.600 registros (96%) |
| **Tráfego malicioso (label = 1)** | 400 registros (4%) |
| **Valores nulos** | 3.232 (apenas na coluna `url`) |
| **Duplicatas** | Nenhuma |
| **Período** | Outubro de 2025 (dado sintético/simulado) |

## Distribuição dos Tipos de Ataque

| Tipo de Ataque | Registros | Descrição |
|---|---|---|
| benign | 9.600 | Tráfego legítimo normal |
| brute-force | 108 | Tentativas repetidas de autenticação |
| port-scan | 81 | Varredura de portas abertas |
| sql-injection | 64 | Injeção de comandos SQL maliciosos |
| xss | 34 | Cross-Site Scripting |
| credential-stuffing | 28 | Uso de credenciais vazadas |
| ddos | 27 | Negação de serviço distribuída |
| command-injection | 26 | Injeção de comandos no sistema |
| exploit-attempt | 22 | Tentativa de exploração de vulnerabilidades |
| c2 | 10 | Comunicação com servidor Command & Control |

## Descrição dos Atributos

| Coluna | Tipo | Descrição | Valores Ausentes | Exemplos |
|---|---|---|---|---|
| `timestamp` | String (datetime) | Data e hora da conexão. Permite extração de features temporais como hora do dia e dia da semana. | Nenhum | 2025-10-01 00:12:54 |
| `src_ip` | String | Endereço IP de origem da conexão. Identificador de rede, não utilizado diretamente como feature preditiva. | Nenhum | 188.176.27.165 |
| `dst_ip` | String | Endereço IP de destino da conexão. | Nenhum | 10.0.0.5 |
| `src_port` | Inteiro | Porta de origem da conexão. Varia de 21 a 65.524. | Nenhum | 45231 |
| `dst_port` | Inteiro | Porta de destino da conexão. Portas como 80 (HTTP), 443 (HTTPS) e 22 (SSH) são comuns. | Nenhum | 443 |
| `protocol` | String | Protocolo de comunicação utilizado: TCP, UDP ou ICMP. | Nenhum | TCP (77,65%), UDP (19,1%), ICMP (3,25%) |
| `bytes_sent` | Inteiro | Volume de bytes enviados na conexão. Varia de 17 a 139.170.400. | Nenhum | 22.000 |
| `bytes_received` | Inteiro | Volume de bytes recebidos na conexão. Varia de 3 a 291.483.000. | Nenhum | 37.473 |
| `user_agent` | String | Agente de usuário HTTP da conexão. Indica o navegador ou ferramenta utilizada. | Nenhum | Mozilla/5.0 (Windows NT 10.0...) |
| `url` | String | URL acessada na conexão. Ausente para conexões UDP e ICMP que não geram requisições HTTP. | **3.232 (32,32%)** | https://webmail.corp/login |
| `is_internal_traffic` | Booleano | Indica se a conexão é interna à rede (True) ou externa (False). | Nenhum | False (84,66%), True (15,34%) |
| `label` | Inteiro (0 ou 1) | **Variável-alvo binária.** 0 = tráfego legítimo, 1 = ataque cibernético. | Nenhum | 0, 1 |
| `attack_type` | String | **Variável-alvo multiclasse.** Especifica o tipo de ataque ou "benign". Usada para análise, não como feature preditiva. | Nenhum | benign, brute-force, ddos... |

## Qualidade dos Dados

**Pontos positivos:**
- Nenhuma duplicata identificada.
- Apenas uma coluna com valores ausentes (`url`), com justificativa técnica clara, já que algumas conexões não geram URL.
- Variáveis-alvo, label e attack_type, bem definida em duas granularidades (binária e multiclasse).
- Distribuição de protocolos realista (TCP dominante, seguido de UDP e ICMP).

**Desafios identificados e tratamentos planejados:**

| Problema | Descrição | Tratamento Planejado |
|---|---|---|
| **Valores nulos em `url`** | 3.232 registros sem URL (conexões UDP/ICMP) | Substituir por `'sem_url'` — ausência de URL é informação relevante |
| **Colunas textuais não numéricas** | `src_ip`, `dst_ip`, `user_agent`, `url` | Tranformar os valores correspondentes em features numéricas |
| **`timestamp` não numérico** | Data/hora em formato string | Extração de `hora` e `dia_semana` como features numéricas |
| **`is_internal_traffic` booleano** | True/False | Conversão para 1/0 |
| **`attack_type` como feature** | Seria vazamento de informação (data leakage) | Utilizada apenas para análise exploratória, removida do modelo |

## Critérios de Qualidade Atendidos

| Critério (orientações do projeto) | Avaliação |
|---|---|
| **Representatividade** | Cobre 9 tipos de ataque relevantes e modernos |
| **Qualidade dos dados** | Sem duplicatas; único problema de nulos tem solução clara |
| **Contexto e significado** | Todas as colunas têm significado técnico claro em segurança de redes |
| **Ética e privacidade** | IPs e dados de usuário são sintéticos/simulados; sem dados pessoais reais |
| **Atualidade e relevância** | Tipos de ataque modernos (C2, credential-stuffing, XSS) |
| **Tamanho do dataset** | 10.000 registros — atende ao mínimo exigido |

---
# Canvas analítico

Nesta seção, você deverá estruturar e preencher o seu Canvas Analítico, que tem como objetivo registrar a organização das ideias e apresentar o modelo de negócio do projeto.

O Canvas deve ser preenchido integralmente, mesmo que algumas informações ainda não estejam totalmente definidas. Nessa etapa inicial, é aceitável trabalhar com hipóteses ou estimativas, desde que sejam coerentes com o problema e o contexto definidos.

**Dica:** O Canvas Analítico serve como guia visual para alinhar expectativas e direcionar o desenvolvimento. Ele poderá (e deverá) ser revisitado e atualizado ao longo do projeto.

> **Links Úteis**:
> - [Modelo do Canvas Analítico](https://github.com/ICEI-PUC-Minas-PMV-SI/PesquisaExperimentacao-Template/blob/main/help/Software-Analtics-Canvas-v1.0.pdf)

# Vídeo de apresentação da Etapa 01

Nesta etapa, o grupo deverá produzir um vídeo de 5 a 8 minutos apresentando o trabalho realizado, no qual cada integrante deve dizer seu nome e apresentar uma parte do conteúdo desenvolvido, garantindo que todos participem ativamente da gravação. A ausência de participação de qualquer membro resultará em penalização na nota final desta etapa. Recomenda-se que o grupo elabore previamente um roteiro para organizar a ordem das falas, distribuir o tempo de forma equilibrada e assegurar que todos os tópicos relevantes sejam apresentados de maneira clara e objetiva.

# Referências

Inclua todas as referências (livros, artigos, sites, etc) utilizados no desenvolvimento do trabalho utilizando o padrão ABNT.

> **Links Úteis**:
> - [Padrão ABNT PUC Minas](https://portal.pucminas.br/biblioteca/index_padrao.php?pagina=5886)
