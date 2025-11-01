from pysentimiento import create_analyzer

py_analyzer = create_analyzer(task="sentiment", lang='pt')

class Analyzer:

    def sentiment_analyzer(self, text):
        texto = text
        texto_analisado = py_analyzer.predict(texto)

        return texto_analisado
    
# TESTE

teste = Analyzer()

print(teste.sentiment_analyzer("Jogo Ruim!"))

