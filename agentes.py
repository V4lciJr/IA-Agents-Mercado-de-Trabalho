import requests
from bs4 import BeautifulSoup
from googlesearch import search
from datetime import datetime
from chat import chat


class WebScraper:
    """
    Classe para realizar web scraping de informações.
    """

    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/91.0.4472.124 Safari/537.36'
        }

        self.data = datetime.now()

    def obter_estatisticas(self):
        """
        Obtém estatísticas de desemprego do site do IBGE.
        Retorna os elementos BeautifulSoup para 'Pessoas desocupadas' e 'Taxa de desocupação'.
        """
        url = "https://www.ibge.gov.br/explica/desemprego.php"
        try:
            response = requests.get(url, headers=self.headers)
            response.raise_for_status()  # Lança uma exceção para status de erro
            soup = BeautifulSoup(response.content, 'html.parser')

            # Encontra todos os 'div' elementos com a classe 'indicador'
            indicadores = soup.find_all('li', class_='variavel')

            return indicadores

        except requests.exceptions.RequestException as e:
            print(f"Erro ao obter estatísticas do IBGE: {e}")
            return None, None, None, None
        except Exception as e:
            print(f"Erro ao processar HTML do IBGE: {e}")
            return None, None, None, None

    def obter_setores_crescimento(self):
        """
        Obtém os setores com maior crescimento a partir de uma fonte (exemplo: exame.com).
        Esta é uma implementação de exemplo e pode precisar de ajustes significativos
        para funcionar com outros sites ou para ser mais robusta.
        """
        resposta = chat(f"""Faça uma pesquisa e Liste os 5 setores de mercado com o maior crescimento em {self.data} 
                        do mercado brasileiro e suas porcentagens de crescimento. Me devolva apenas os bullets points, 
                        sempre pule uma linha para cada setor, em formato markdown e editado, com os 5 setores, sem 
                        nenhum texto adicional, coloque emojis de acordo com os setores.
                        
                        ### Regras:
                        - Utilize a ferramenta de busca para encontrar.
                        - Não invente informações: extraia dados reais dos sites.
                        - Traga apenas informações atualizadas até a data {self.data} da pesquisa
                        
                        Você está trazendo dados de 2024, não retorne dados desatualizados, apenas dados atualizados da data
                        {self.data}
                        """)

        return resposta

    @staticmethod
    def buscar_manchetes(query, num_resultados=5):
        """
        Realiza uma busca no Google e retorna as URLs das manchetes dos resultados.
        """
        manchetes = []
        try:
            for resultado in search(query, num_results=num_resultados, lang="pt"):
                manchetes.append(resultado)
        except Exception as e:
            print(f"Erro ao buscar manchetes: {e}")
            return []
        return manchetes

    @staticmethod
    def buscar_vagas_google(cargo):
        """
        Realiza uma busca no Google por vagas de emprego e retorna as URLs.
        Passa as urls para os agentes e organiza em tópicos
        retorna o texto formatado
        """

        job_urls = []
        try:
            # Adiciona palavras-chave específicas para tornar a busca mais relevante para vagas
            search_query = f"{cargo} vaga emprego Brasil"
            for url in search(search_query, num_results=15, lang="pt"):
                # Filtro básico para tentar obter URLs relacionadas a vagas
                if ("vagas.com.br" in url or "catho.com.br" in url or "gupy.io" in url or "linkedin.com/jobs" in url
                        or "indeed.com" in url or "99jobs.com" in url or "infojobs.com.br" in url
                        or "glassdoor.com.br/Vaga/index.htm" in url or "Empregos.com.br" in url):

                    job_urls.append(url)
        except Exception as e:
            print(f"Erro ao buscar vagas no Google: {e}")

        resposta = chat(f"""Você é um agente especializado em buscar e resumir vagas de emprego na internet. 
        Sua tarefa é pesquisar **vagas de emprego** com base em um tópico fornecido 
        (ex: "fisioterapeuta", "cientista de dados", etc.) nos seguintes sites: **LinkedIn, Gupy, Catho, Infojobs, 
        Vagas.com, Indeed, Empregos.com.br, Trabalha Brasil, Glassdoor**.

        Sua resposta deve conter as seguintes seções para **cada site individualmente junto com os links de cada vaga
        de acorodo com o site contidos em {job_urls}, se o link for do linkedin, você inclui o link que está em 
        {job_urls} e inclui no tópico:
        
        ---
        
        **Vagas em [NOME DO SITE]:**  
        **Total de Vagas:** X  
        
        **Vagas por Nível:**  
        - Junior – [quantidade]  
        - Pleno – [quantidade]  
        - Sênior – [quantidade]  
        
        **Skills mais comuns nas vagas:**  
        (agrupadas e contadas conforme aparecem nas descrições das vagas)  
        - [Skill 1] – [quantidade]  
        - [Skill 2] – [quantidade]  
        - ...
        
        **Exemplos de Vagas:**  
        (Mostre até 3 exemplos por site)  
        Vaga de [Cargo] – [Plataforma] #[número sequencial] (Nível: [nível]) – Habilidades: [lista de habilidades da vaga]
        
        ---
        
        ### Regras:
        - Utilize a ferramenta de busca para encontrar e resumir vagas reais.
        - Não invente informações: extraia dados reais dos sites.
        - Se algum site não tiver resultados, informe: “Nenhuma vaga encontrada no [nome do site]”.
        - Agrupe habilidades semelhantes (ex: "Python", "python", "PYTHON" devem ser consideradas iguais).
        - Seja claro, objetivo e siga rigorosamente a estrutura de saída.
        - Retorne apenas vagas recentes e relevantes para o tópico.
        
        Tópico de busca: **{cargo}**""")

        return resposta

    def tendencias_de_mercado(self, setores_crescimento):
        """
        Realiza uma busca sobre as maiores tendências de mercado no momento.
        """
        resposta = chat(f"""Pegue os tópicos contidos em {setores_crescimento} do mercado brasileiro, devolva uma 
                        pesquisa detalhada sobre cada tópico retornado atualizados até a data de {self.data}, 
                        edite a resposta em markdown e devolda personalizada, pode ficar à vontade para usar emojis e 
                        e imagens que você encontrar ou gerar, desde que seja relacionada ao assunto e organize tudo como
                        um artigo de um site, retorne apenas as informações e uma conclusão ou considerações finais, 
                        não mostre mais nada depois.
                        
                        ### Regras:
                        - Utilize a ferramenta de busca para encontrar e resumir.
                        - Não invente informações: extraia dados reais dos sites.
                        - Traga apenas informações atualizadas até a data {self.data} da pesquisa
                        - O título e os tópicos da análise devem estar atualizado com a data {self.data}, bem como as notícias
                        - Caso você tenha que gerar uma imagem, devolva apenas a imagem gerada, sem nenhum texto adicional
                        - Mas sempre traga imagens realistas que estjeam relacionadas aos tópicos, que sejam extremamente condizentes com o tópico
                        
                        Você está trazendo dados de 2024, não retorne dados desatualizados, apenas dados atualizados da data
                        {self.data}
                        """)
        return resposta

    def buscar_habilidades(self, vaga):
        """
        Realiza uma busca sobre as habilidades necessárias de acordo com a vaga desejada.
        """
        resposta = chat(f"""Realize uma pesquisa intensa e devolva as habilidades e Skills mais solicitadas no mercado 
                            brasileiro de acordo com a {vaga} até a data {self.data}, devolva a informação de forma organizada, com as quantidades
                            de cada skill que se repetem de acordo com as vagas, retorne apenas habilidades e Skills de 
                            de forma organizada, como se fosse um artigo de um site, bem como utilize emojis, imagens e 
                            caso você não encontre uma imagem sobre o tópico, gere uma, retorne apenas as informações e 
                            uma conclusão ou considerações finais, não mostre mais nada depois
                            
                            ### Regras:
                            - Utilize a ferramenta de busca para encontrar e resumir.
                            - Não invente informações: extraia dados reais dos sites.
                            - Traga apenas informações atualizadas até a data {self.data} da pesquisa
                            - Caso você tenha que gerar uma imagem, devolva apenas a imagem gerada, sem nenhum texto adicional
                            
                            Não traga dados de 2024, não retorne dados desatualizados, apenas dados atualizados da data
                            {self.data}
                            """)
        return resposta
