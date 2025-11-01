from pysentimiento import create_analyzer

analyzer = create_analyzer(model_name='pysentimiento/bertweet-pt-sentiment', lang='pt')

class Analyzer:

    def sentiment_analyzer(text):
        texto_analisado = analyzer.predict(text)

        return texto_analisado



# TESTE

teste = Analyzer()

print(teste.sentiment_analyzer("Jogo Ruim!"))