# 🚀 Painel Interativo de Análise do Mercado de Trabalho Brasileiro 📊

## ✨ Visão Geral do Projeto

Bem-vindo ao repositório do **Painel Interativo de Análise do Mercado de Trabalho Brasileiro**\! Este projeto é uma ação de extensão universitária que visa democratizar o acesso a informações cruciais sobre o cenário profissional do Brasil. Desenvolvido com base em Ciência de Dados e Inteligência Artificial, nosso painel transforma dados complexos e dispersos em insights claros e acionáveis para estudantes, profissionais, educadores e empresas.

Em um mercado de trabalho em constante evolução, o acesso a dados atualizados e interpretáveis é um diferencial. Nosso objetivo é capacitar o público com as ferramentas necessárias para tomar decisões de carreira e educacionais mais informadas.

## 📸 Demonstração

<img width="1346" height="602" alt="apresentação" src="https://github.com/user-attachments/assets/0df422bf-782b-4fc2-a0b1-96e8cb98b14e" />


-----

## 💡 Motivação

O mercado de trabalho brasileiro é dinâmico e complexo, mas a informação sobre ele muitas vezes é fragmentada, de difícil acesso ou complexa demais para ser interpretada rapidamente. Identificamos uma lacuna na democratização desses dados, o que dificulta o planejamento de carreira e a tomada de decisões estratégicas. Nosso projeto nasceu da necessidade de preencher essa lacuna, oferecendo uma plataforma intuitiva que utiliza o poder da IA para compilar, analisar e apresentar essas informações de forma compreensível a todos.

## 🔍 Funcionalidades Principais

Nosso painel é dividido em seções interativas, cada uma impulsionada por agentes de Inteligência Artificial dedicados:

  * **1. Visão Geral do Mercado:** 🇧🇷

      * Um panorama rápido e atualizado das estatísticas do mercado de trabalho brasileiro (taxa de desemprego, subutilização, desalentados) diretamente do IBGE via web scraping.
      * Manchetes recentes sobre o cenário de empregos, coletadas via busca inteligente no Google.
      * Identificação dos setores com maior crescimento.

  * **2. Tendências por Área Profissional/Setor:** 📈

      * Análises aprofundadas sobre as tendências emergentes em diversas áreas e setores, ajudando a identificar onde estão as maiores oportunidades e para onde o mercado está se movendo.

  * **3. Pesquisa Personalizada de Vagas:** 🕵️‍♀️

      * Permite que o usuário pesquise uma vaga específica (ex: "Desenvolvedor Python", "Analista de Dados").
      * Agentes de IA realizam buscas inteligentes na web para encontrar vagas relevantes e apresentam os resultados.
      * *(Em desenvolvimento: futuras implementações incluirão métricas como percentual de vagas júnior/pleno/sênior e um "score" de compatibilidade com o perfil do usuário.)*

  * **4. Habilidades e Skills Demandadas:** 🎯

      * Com base na vaga pesquisada pelo usuário, esta seção lista as habilidades técnicas e comportamentais (soft skills) mais procuradas pelo mercado.
      * Um guia prático para direcionar o desenvolvimento profissional e a aquisição de novas competências.

## 🛠️ Tecnologias Utilizadas

Este projeto foi construído com as seguintes tecnologias e bibliotecas:

  * **Python 🐍:** Linguagem de programação principal.
  * **Streamlit 🚀:** Framework para a construção da interface do painel web interativo.
  * **LangChain 🔗:** Framework para orquestração de agentes de IA, permitindo a interação com Large Language Models (LLMs) e ferramentas externas.
  * **ChatOpenAI (GPT-4.1-mini) 🤖:** Utilizado como LLM para capacidades de processamento de linguagem natural e raciocínio dos agentes.
  * **GoogleSerperAPIWrapper 🌐:** Ferramenta integrada ao LangChain para realizar buscas avançadas na internet.
  * **Beautiful Soup 🧺:** Biblioteca para web scraping, usada para extrair dados de websites como o IBGE.
  * **Pandas 🐼:** Biblioteca para manipulação e análise de dados.
  * **NLTK & spaCy 💬:** Bibliotecas para Processamento de Linguagem Natural (PLN), utilizadas na análise de textos de vagas.
  * **Dotenv 🔑:** Para gerenciamento seguro de variáveis de ambiente (como chaves de API).

## 🏗️ Arquitetura e Design

A arquitetura do painel adota uma abordagem baseada em agentes e serviços. Uma classe `WebScraper` é responsável pela coleta de dados específicos (como os do IBGE), enquanto agentes mais sofisticados, orquestrados pelo `LangChain`, lidam com buscas inteligentes e processamento de informações textuais. O Streamlit atua como a camada de apresentação, integrando as saídas desses agentes e visualizando-as de forma interativa. Essa modularidade permite escalabilidade e facilita a adição de novas funcionalidades e fontes de dados.

## 🚀 Como Executar o Projeto

Siga os passos abaixo para configurar e executar o painel em seu ambiente local:

### Pré-requisitos

  * Python 3.9+
  * Conta OpenAI (para acesso à API, se necessário)
  * Chave de API Serper (para GoogleSerperAPIWrapper)

### 1\. Clonar o Repositório

```bash
git clone https://github.com/seu-usuario/painel-mercado-trabalho-ia.git
cd painel-mercado-trabalho-ia
```

### 2\. Configurar o Ambiente Virtual

Recomendamos o uso de um ambiente virtual para gerenciar as dependências.

```bash
python -m venv venv
source venv/bin/activate  # No Linux/macOS
# venv\Scripts\activate   # No Windows
```

### 3\. Instalar as Dependências

```bash
pip install -r requirements.txt
```

*(Certifique-se de que o `requirements.txt` contenha todas as bibliotecas listadas na seção "Tecnologias Utilizadas").*

### 4\. Configurar Variáveis de Ambiente

Crie um arquivo `.env` na raiz do projeto e adicione suas chaves de API:

```
OPENAI_API_KEY="sua_chave_api_openai"
SERPER_API_KEY="sua_chave_api_serper"
```

### 5\. Executar o Painel

```bash
streamlit run painel.py
```

O painel será aberto automaticamente no seu navegador padrão (geralmente em `http://localhost:8501`).

## ✅ Resultados e Contribuições

Com o desenvolvimento das atividades, alcançamos um protótipo funcional que demonstra o potencial da **Inteligência Artificial** na democratização de informações complexas do mercado de trabalho. Conseguimos integrar web scraping de fontes como o IBGE com agentes de IA avançados baseados em LLMs, apresentando os dados em um painel interativo e intuitivo.

Este trabalho contribui significativamente para o contexto de pesquisa ao aplicar conceitos de Ciência de Dados e IA na resolução de um problema social relevante. Para a comunidade, oferece uma ferramenta valiosa para o planejamento de carreira e educação, transformando dados brutos em conhecimento acionável.

## 🚧 Desafios Enfrentados

Durante o desenvolvimento, enfrentamos alguns desafios notáveis:

  * **Escassez de APIs Abertas:** A maioria das grandes plataformas de emprego não oferece APIs públicas e gratuitas, o que nos forçou a depender fortemente do web scraping.
  * **Bloqueios de Web Scraping:** Sites como o LinkedIn possuem robustos sistemas de detecção e bloqueio de requisições automatizadas. Isso exigiu um aprendizado contínuo sobre técnicas de *rate limiting*, *user-agent rotation* e outras estratégias para evitar o bloqueio e garantir a coleta de dados de forma ética e eficiente. Essas dificuldades ressaltam a importância de sempre considerar as políticas de uso e a conformidade legal ao realizar web scraping.

## ⏭️ Próximos Passos

O projeto está em constante evolução\! As próximas etapas incluem:

  * Aprimorar os modelos de Aprendizado de Máquina (ML) para previsões de tendências e salários.
  * Implementar a funcionalidade de percentual de vagas júnior/pleno/sênior e "match" na pesquisa personalizada.
  * Realizar testes de usabilidade aprofundados com a comunidade para coletar feedback e refinar a interface.
  * Desenvolver materiais educativos complementares sobre como interpretar e usar os dados do painel.
  * Expandir as fontes de dados para abranger um espectro ainda maior do mercado de trabalho.

## 🤝 Como Contribuir

Aceitamos contribuições\! Se você deseja ajudar a aprimorar este projeto, sinta-se à vontade para:

1.  Fazer um *fork* do repositório.
2.  Criar uma nova *branch* para sua funcionalidade (`git checkout -b feature/sua-feature`).
3.  Fazer suas alterações e *commits* (`git commit -m 'feat: Adiciona nova funcionalidade X'`).
4.  Fazer *push* para sua *branch* (`git push origin feature/sua-feature`).
5.  Abrir um *Pull Request* detalhando suas mudanças.

## 🧑‍💻 Time do Projeto

  * Valci Júnior
  * [LinkedIn](https://www.linkedin.com/in/valci-junior/)


## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

-----
