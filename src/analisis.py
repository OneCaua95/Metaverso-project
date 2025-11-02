from extract import Extractor
import pandas as pd
from texttransform import TextTransformation
from sentiment import Analyzer

data = Extractor()
transformation = TextTransformation()
sentimentos = Analyzer()
df = data.get_data()

class Analisis:

    def media_de_viewer_por_jogo(self):
        df_media_de_viewer_por_jogo = df.groupby("Game").mean("Avg_viewers")

        df_media_de_viewer_por_jogo = df_media_de_viewer_por_jogo.sort_values("Avg_viewers", ascending = False)

        df_media_de_viewer_por_jogo = df_media_de_viewer_por_jogo.reset_index()

        return df_media_de_viewer_por_jogo
    
    def jogos_com_mais_streamers(self):
        df_jogos_com_mais_streamers = df.groupby("Game").sum("Streamers")

        df_jogos_com_mais_streamers = df_jogos_com_mais_streamers.sort_values("Streamers", ascending = False)

        df_jogos_com_mais_streamers = df_jogos_com_mais_streamers.reset_index()

        return df_jogos_com_mais_streamers
    
    def eficiencia_de_conteudo(self):
        df = self.jogos_com_mais_streamers()
        df["Eficiencia_de_conteudo"] = df.apply(lambda x: x['Hours_watched'] / x['Hours_streamed'], axis=1)

        df = df.sort_values("Eficiencia_de_conteudo", ascending= False)

        df = df.reset_index()

        return df
    
    def media_de_horas(self):
        df_media_de_horas = df.groupby("Game").mean("Hours_watched")

        df_media_de_horas = df_media_de_horas.sort_values("Hours_watched", ascending = False)

        df_media_de_horas = df_media_de_horas.reset_index()

        return df_media_de_horas
    
    
    def consultar_jogo_por_mes_ano(self, mes, ano):
        
        query_str = f"Year == {ano} and Month == {mes}"
        filtered_data = df.query(query_str)
    
        if filtered_data.empty:  
            print(f"Nenhum dado encontrado para o Ano {ano} e Mês {mes}.")
            return
        
        monthly_hours = filtered_data.groupby("Game")["Hours_watched"].sum()
        
        game = monthly_hours.sort_values(ascending=False).head(1)

        return game
        
    def analisar_sentimento_text(self, text : str):

        text = transformation.limpeza_do_texto(text)

        analise_sentimentos_text = sentimentos.sentiment_analyzer(text)

        Positivo = analise_sentimentos_text['POS']
        Neutro = analise_sentimentos_text['NEU']
        Negative = analise_sentimentos_text['NEG']

        return Positivo, Neutro, Negative
    
    def limpar_e_lematizar_texto(self, text : str):
        text = transformation.limpeza_do_texto(text)
        text = transformation.lematizacao(text)

        return text



# TESTES

teste = Analisis()


print(teste.media_de_viewer_por_jogo())