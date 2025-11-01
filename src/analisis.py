from extract import Extractor

data = Extractor()

df = data.get_data()

class Analisis:

    def media_de_viewer_por_jogo(self):
        df_media_de_viewer_por_jogo = df.groupby("Game").mean("Avg_viewers")

        return df_media_de_viewer_por_jogo.sort_values("Avg_viewers", ascending = False)
    
    def jogos_com_mais_streamers(self):
        df_jogos_com_mais_streamers = df.groupby("Game").sum("Streamers")

        return df_jogos_com_mais_streamers.sort_values("Streamers", ascending = False)
    
    def eficiencia_de_conteudo(self):
        df = self.jogos_com_mais_streamers()
        df["Eficiencia_de_conteudo"] = df.apply(lambda x: x['Hours_watched'] / x['Hours_streamed'], axis=1)

        return df.sort_values("Eficiencia_de_conteudo", ascending= False)
    
    def media_de_horas(self):
        df_media_de_horas = df.groupby("Game").mean("Hours_watched")

        return df_media_de_horas.sort_values("Hours_watched", ascending = False)

# TESTES

teste = Analisis()

print(teste.media_de_horas())