# Mini Curso CI/CD

Projeto educacional em português focado em fundamentos de CI/CD, versionamento, qualidade, artefatos e desenho de pipelines. O conteúdo é publicado como um site estático com Marmite e deploy automático no GitHub Pages.

## Visão Geral

O objetivo deste repositório é ensinar CI/CD com ênfase em base conceitual. Em vez de começar por ferramenta, o curso organiza a aprendizagem em torno de decisões, práticas e trade-offs que sustentam pipelines confiáveis.

O projeto entrega:

- um site estático com navegação entre aulas e páginas auxiliares
- conteúdo em Markdown versionado no próprio repositório
- assets visuais usados nas aulas
- customizações simples de estilo e comportamento
- publicação contínua via GitHub Actions

## Acesse o Conteúdo

- Site publicado: [waltenne.github.io/mini-curso-cicd](https://waltenne.github.io/mini-curso-cicd)
- Repositório: [github.com/waltenne/mini-curso-cicd](https://github.com/waltenne/mini-curso-cicd)

## Estrutura do Curso

O curso está dividido em cinco dias:

1. Day 01: Os Alicerces - Por que CI/CD importa?
2. Day 02: Controlando a Bagunça - Versionamento e Colaboração
3. Day 03: Garantia de Qualidade - O Coração do CI
4. Day 04: Do CI ao CD - Artefatos, Entrega e Deploy Contínuo
5. Day 05: Construindo Pipelines CI/CD - Do Conceito à Prática

Ao longo dos módulos, o conteúdo aborda temas como:

- integração contínua, entrega contínua e implantação contínua
- Git Flow, Trunk-Based Development, SemVer e Conventional Commits
- pirâmide de testes, fail fast, SAST, SCA e scan de secrets
- artefatos imutáveis, estratégias de deploy e qualidade de release
- modelagem de pipelines, cache, templates e boas práticas de automação

## Stack do Projeto

- Gerador de site estático: Marmite
- Conteúdo: Markdown
- Publicação: GitHub Pages
- Automação de deploy: GitHub Actions
- Customização visual: custom.css
- Customização de comportamento: custom.js

## Estrutura do Repositório

Principais diretórios e arquivos:

- content: páginas do curso, páginas auxiliares e mídia
- content/media/course/index: imagens usadas na vitrine dos dias
- content/media/course/assets: imagens de apoio das aulas
- .github/workflows/ci.yaml: build e deploy para GitHub Pages
- marmite.yaml: configuração do site
- custom.css: ajustes visuais do conteúdo
- custom.js: ponto de extensão para scripts customizados

Arquivos relevantes dentro de content:

- home.md: página inicial do curso
- 01.md até 05.md: aulas principais
- authors.md: página do autor
- contributors.md: página de contribuidores
- arquivos iniciados com _: páginas auxiliares e blocos adicionais do site

## Como Executar Localmente

### Pré-requisitos

Você precisa ter o Rust e o Cargo disponíveis na máquina para instalar o Marmite.

Importante: versões antigas do Cargo podem falhar ao instalar o Marmite porque dependências mais recentes já exigem suporte a edition2024. A recomendação é usar uma toolchain estável atual instalada com rustup.

Ambiente recomendado:

- Rust estável recente
- Cargo compatível com edition2024
- rustup para gerenciar atualizações da toolchain

Se você ainda não usa rustup, instale com:

```bash
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
source "$HOME/.cargo/env"
rustup update stable
rustup default stable
```

Se já tem Rust instalado, confirme a versão antes de instalar o Marmite:

```bash
cargo --version
rustc --version
```

### Instalação do Marmite

```bash
cargo install --git https://github.com/rochacbruno/marmite --branch main
```

Se aparecer erro relacionado a edition2024, atualize a toolchain e tente novamente.

### Gerar o site

Na raiz do projeto, execute:

```bash
marmite . site --debug
```

O comando gera o site estático no diretório site.

### Servir localmente

Depois de gerar o conteúdo, você pode subir um servidor estático simples:

```bash
python3 -m http.server 8000 -d site
```

Depois, acesse [localhost:8000](http://localhost:8000).

## Publicação

O deploy é feito automaticamente pelo workflow em .github/workflows/ci.yaml.

Fluxo atual:

1. checkout do repositório
2. instalação do Marmite via Cargo
3. geração do site na pasta site
4. upload do artefato para GitHub Pages
5. deploy ao publicar mudanças na branch main

Também é possível disparar a publicação manualmente via workflow_dispatch.

## Como Atualizar o Conteúdo

Para evoluir o curso:

1. edite os arquivos Markdown em content
2. adicione ou atualize imagens em content/media
3. ajuste metadados e navegação em marmite.yaml quando necessário
4. gere o site localmente para validar a navegação
5. envie as alterações para a branch main para publicar

## Personalização

O projeto mantém a customização enxuta:

- custom.css reduz largura máxima e ajusta margens do conteúdo
- custom.js é carregado em todas as páginas e pode ser usado para integrações como analytics
- marmite.yaml concentra nome, descrição, menu, busca, paginação e demais opções globais

## Analytics

O GitHub Pages não oferece analytics nativo para sites estáticos. A forma mais simples é carregar um script de terceiros no site.

Este projeto já está preparado para isso em [mini-curso-cicd/custom.js](mini-curso-cicd/custom.js).

Provedores suportados no arquivo:

- Plausible
- GoatCounter
- Google Analytics 4

Para ativar, edite o bloco analyticsConfig em [mini-curso-cicd/custom.js](mini-curso-cicd/custom.js) e preencha apenas o provedor desejado.

Exemplos:

Para Plausible:

```js
const analyticsConfig = {
  provider: "plausible",
  plausibleDomain: "waltenne.github.io",
  goatCounterEndpoint: "",
  gaMeasurementId: "",
};
```

Para GoatCounter:

```js
const analyticsConfig = {
  provider: "goatcounter",
  plausibleDomain: "",
  goatCounterEndpoint: "https://seu-projeto.goatcounter.com",
  gaMeasurementId: "",
};
```

Para Google Analytics 4:

```js
const analyticsConfig = {
  provider: "ga4",
  plausibleDomain: "",
  goatCounterEndpoint: "",
  gaMeasurementId: "G-XXXXXXXXXX",
};
```

Depois disso:

1. gere o site novamente
2. publique na branch main
3. valide o carregamento do script em produção

Se a prioridade for simplicidade e privacidade, Plausible ou GoatCounter costumam ser escolhas melhores que GA4 para GitHub Pages.

## Público-Alvo

Este material é útil para:

- pessoas iniciando em DevOps e CI/CD
- desenvolvedores que querem entender o porquê por trás dos pipelines
- times que precisam nivelar conceitos antes de escolher ferramentas
- instrutores e comunidades que desejam reutilizar conteúdo introdutório sobre entrega contínua

## Contribuição

Contribuições de conteúdo, correções textuais, melhorias visuais e ajustes estruturais são bem-vindas.

Sugestões práticas:

- corrigir ortografia e clareza didática
- expandir exemplos práticos e diagramas
- revisar consistência entre os módulos
- melhorar estilos e experiência de leitura

## Autor

O conteúdo foi criado por Waltenne Carvalho, com foco em compartilhar conhecimento sobre automação, CI/CD, infraestrutura e práticas de qualidade em software.
