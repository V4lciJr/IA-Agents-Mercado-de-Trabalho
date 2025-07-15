import streamlit as st
from agentes import WebScraper


class PainelMercadoTrabalho:
    """
    Classe principal para o painel de análise do mercado de trabalho.
    """

    def __init__(self):
        self.scraper = WebScraper()
        self.setores_crescimento = self.scraper.obter_setores_crescimento()

    def exibir_visao_geral(self):
        """
        Exibe a seção de visão geral do painel.
        """
        st.write("""
            ### Resumo do Painel de Análise de Mercado de Trabalho
            Bem-vindo ao Painel de Análise de Mercado de Trabalho, uma ferramenta interativa desenvolvida para fornecer insights relevantes e acessíveis sobre o cenário profissional brasileiro. Nosso objetivo é auxiliar na tomada de decisões de carreira e educação, mantendo você atualizado sobre as dinâmicas do mercado.

            ##### Como Funciona:
            Este painel é alimentado por agentes de inteligência artificial que coletam dados de diversas fontes online, incluindo sites de emprego, redes sociais profissionais e pesquisas setoriais. Além disso, utilizamos modelos de aprendizado de máquina para analisar esses dados, identificar tendências atuais e prever futuras demandas por habilidades e profissões.

            ##### Principais Seções:
            **Visão Geral:** Obtenha um panorama rápido do mercado de trabalho, incluindo a taxa de desemprego mais recente e os setores com maior crescimento, atualizados por meio de web scraping.

            **Tendências:** Explore análises aprofundadas sobre tendências por área profissional e setor, ajudando a identificar onde estão as maiores oportunidades.

            **Habilidades e Skills:** Descubra as habilidades técnicas e comportamentais mais demandadas pelo mercado brasileiro, com informações para guiar seu desenvolvimento profissional.

            **Pesquisa Personalizada:** Realize buscas específicas por vagas, com integração de agentes inteligentes para refinar os resultados e oferecer recomendações.

            Nosso compromisso é com a clareza e a acessibilidade, transformando dados complexos em informações compreensíveis para todos. Fique atento às atualizações, pois continuaremos a aprimorar este painel com novas funcionalidades e dados para apoiar sua jornada profissional.
        """)

        st.markdown("<h1 style='color: #4CAF50;'>Visão Geral do Mercado de Trabalho Brasileiro</h1>",
                    unsafe_allow_html=True)

        # Taxa de Desemprego (Web Scraping)
        # O scraper.obter_estatisticas() agora retorna os objetos BeautifulSoup Tag
        # Taxa de Desemprego (Web Scraping)

        desempregados, taxa, desalentados, subutilizacao = self.scraper.obter_estatisticas()

        if desempregados:

            st.markdown(f"<h2 style='color: #1E88E5;'>Estatísticas (IBGE) - {desempregados.find(class_='variavel-periodo').text}</h2>", unsafe_allow_html=True)

            col1, col2, col3, col4 = st.columns(4)
            with col1:
                st.metric(label=desempregados.h3.text, value=desempregados.find(class_='variavel-dado').text, border=True)

            with col2:
                st.metric(label=taxa.h3.text, value=taxa.find(class_='variavel-dado').text, border=True)

            with col3:
                st.metric(label=desalentados.h3.text, value=desalentados.find(class_='variavel-dado').text, border=True)

            with col4:
                st.metric(label=subutilizacao.h3.text, value=subutilizacao.find(class_='variavel-dado').text, border=True)

        else:
            st.write("Não foi possível obter a taxa de desemprego no momento.")

        # Setores com Maior Crescimento (Web Scraping)
        if self.setores_crescimento:
            st.markdown("<h2 style='color: #1E88E5;'>Setores com Maior Crescimento</h2>", unsafe_allow_html=True)

            st.markdown(
                f"<div style='padding: 10px; border-radius: 5px; background-color: #A9A9A9; margin-bottom: 5px;'>- {self.setores_crescimento}</div>",
                unsafe_allow_html=True)
        else:
            st.write("Não foi possível obter os setores em crescimento no momento.")

        # Busca e exibição de manchetes
        st.markdown("<h2 style='color: #1E88E5;'>Manchetes Recentes</h2>",
                    unsafe_allow_html=True)  # Cor alterada para combinar com as outras
        manchetes = self.scraper.buscar_manchetes("mercado de trabalho brasileiro atual", num_resultados=5)
        if manchetes:
            for manchete in manchetes:
                st.markdown(f"- {manchete}")
        else:
            st.write("Não foi possível obter as manchetes no momento.")

    def exibir_tendencias(self):
        st.markdown("<h1 style='color: #4CAF50;'>Tendências por Área Profissional/Setor</h1>", unsafe_allow_html=True)
        tendencias = self.scraper.tendencias_de_mercado(self.setores_crescimento)
        st.write(tendencias)

    def exibir_pesquisa(self):
        st.markdown("<h1 style='color: #4CAF50;'>Pesquisa Personalizada de Vagas</h1>", unsafe_allow_html=True)
        st.write("Realize buscas específicas por vagas, com a futura integração de agentes inteligentes para refinar "
                 "os resultados e oferecer recomendações.")
        pesquisa_vaga = st.text_input("Pesquisar Vaga (Ex: Desenvolvedor Python, Analista de Dados, Fisioterapeuta...):", "")

        if st.button("Buscar Vagas"):
            if pesquisa_vaga:
                st.subheader(f"Resultados da Pesquisa para: **{pesquisa_vaga}**")

                with st.spinner("Buscando vagas na Internet..."):
                    job_sites = self.scraper.buscar_vagas_google(pesquisa_vaga)
                    st.write(job_sites)

    def exibir_habilidades(self):
        st.markdown("<h1 style='color: #4CAF50;'>Habilidades e Skills Demandadas</h1>", unsafe_allow_html=True)
        st.write("Descubra as habilidades técnicas e comportamentais mais demandadas pelo mercado, com informações "
                 "para guiar seu desenvolvimento profissional.")
        pesquisa_habilidades = st.text_input("Pesquisar habilidades do Cargo desejado (Ex: Desenvolvedor Python, Analista de Dados, Fisioterapeuta):", "")

        if st.button("Buscar Habilidades"):
            if pesquisa_habilidades:
                st.subheader(f"Resultados das habilidades e Skills mais solicitadas para: **{pesquisa_habilidades}**")

                with st.spinner("Buscando habilidades e Skills na Internet..."):
                    job_sites = self.scraper.buscar_habilidades(pesquisa_habilidades)
                    st.write(job_sites)

    def run(self):
        """
        Executa o painel.
        """
        st.markdown(f"<h1 style='color: #1E88E5;'>Painel de Análise de Mercado de Trabalho</h1>",
                    unsafe_allow_html=True)
        # Define o tema do Streamlit
        st.markdown(
            """
            <style>
            .sidebar .sidebar-content {
                background-color: #e0f7fa;
                color: black;
            }
            .css-1aumxhk {
                background-color: #f5f5f5;
                color: black;
            }
            .stButton>button {
                color: black;
                background-color: #4CAF50;
                border: 2px solid #4CAF50;
                border-radius: 5px;
            }
            .stButton>button:hover {
                color: black;
                background-color: #f5f5f5;
                border: 2px solid #4CAF50;
            }
            </style>
            """,
            unsafe_allow_html=True,
        )
        secao = st.sidebar.radio("Selecione a Seção",
                                 ("Visão Geral", "Pesquisa Personalizada", "Tendências", "Habilidades e Skills"))
        if secao == "Visão Geral":
            self.exibir_visao_geral()
        elif secao == "Tendências":
            self.exibir_tendencias()
        elif secao == "Habilidades e Skills":
            self.exibir_habilidades()
        elif secao == "Pesquisa Personalizada":
            self.exibir_pesquisa()


if __name__ == "__main__":
    painel = PainelMercadoTrabalho()
    painel.run()
