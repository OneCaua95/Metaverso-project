import streamlit as st
import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from analisis import Analisis

st.set_page_config(layout="wide")
from extract import Extractor

data = Extractor()
file = 'data\Twitch_Chat.csv'
analisar = Analisis()

def AnaliseDeSentimento():
    

    col1, col2 = st.columns(2)
    col3, col4 = st.columns(2)

    with col1:
        st.header("Grafico de Sentimento")
        df = pd.read_csv(file, sep= ",")

        df[['Pos', 'Neu', 'Neg']] = df['mensagem'].apply(
            lambda texto: pd.Series(analisar.analisar_sentimento_text(texto), index=['Pos', 'Neu', 'Neg'])
        )

        positive_mean = df["Pos"].mean()
        neutral_mean = df["Neu"].mean()
        negative_mean = df["Neg"].mean()

        colunas = ["Positivo", "Negativo", "Neutro"]
        linhas = [positive_mean, negative_mean, negative_mean]

        dados_dict = {
            'Sentimento': colunas,
            'Valor': linhas
        }

        df_metricas = pd.DataFrame(dados_dict)

        st.bar_chart(df_metricas, x="Sentimento",y="Valor")
    with col2:
        st.header("Top Comentarios")

        df = pd.read_csv(file, sep= ",")

        df = df.groupby("mensagem").value_counts(ascending=False) # TODO
        
        df = df.head(5)

        comentarios = df.index.tolist()

        for i in range(0,len(comentarios)):
            st.write(comentarios[i])
            st.divider()  


    with col3:
        st.header("Usuarios Que mais Participam")

        df = pd.read_csv(file, sep= ",")

        df = df.groupby("user").value_counts(ascending=False) # TODO
        
        df = df.head(5)

        usuarios = df.index.tolist()

        for i in range(0,len(usuarios)):
            st.write(usuarios[i][0])
            st.divider()  

    with col4:
        
        st.header("Nuvem de Palavras")

        df = pd.read_csv(file, sep= ",")

        
        df["mensagem"] = df["mensagem"].apply(lambda texto:analisar.limpar_e_lematizar_texto(texto))

        df["String_nuvem"] = df.apply(lambda row: ' '.join(row.astype(str)), axis=1)

        texto = df["String_nuvem"].to_string()

        wordcloud = WordCloud(width=800, height=400, background_color='white').generate(texto)

        fig, ax = plt.subplots(figsize=(10, 5))
        ax.imshow(wordcloud, interpolation='bilinear')
        ax.axis("off") 
            
        st.pyplot(fig)
    return

def analiseExporatoria():
    
    st.title("Analise Exploratoria")

    col8,col9, = st.columns(2)
    col10,col11 = st.columns(2)

    with col8:
        st.header("Média de Viewer Por Jogo")

        df = analisar.media_de_viewer_por_jogo()

        df = df.head(5)

        st.bar_chart(df, x="Game",y="Avg_viewers")


    with col9:
        st.header("Jogos com mais Streamers")

        df = analisar.jogos_com_mais_streamers()

        df = df.head(5)

        st.bar_chart(df, x="Game",y="Streamers")

        print(df)

    with col11:
        st.header("Jogos com melhor eficiencia Horas Assistidas/ Horas Streamadas")
        df = analisar.eficiencia_de_conteudo()

        df = df.head(5)

        print(df)


        st.bar_chart(df, x="Game",y="Eficiencia_de_conteudo")

    with col10:
        st.header("Grafico de Jogos com maior media de horas")
        df = analisar.media_de_horas()

        df = df.head(5)

        print(df)

        st.bar_chart(df, x="Game",y="Hours_watched")

pages = {
    
    "Menu":[
        st.Page(AnaliseDeSentimento, title="Analise De Sentimento"),
        st.Page(analiseExporatoria)

    ]
}

pg = st.navigation(pages)
pg.run()