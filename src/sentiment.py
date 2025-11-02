from pysentimiento import create_analyzer
import pandas as pd

py_analyzer = create_analyzer(task="sentiment", lang='pt')

class Analyzer:

    def sentiment_analyzer(self, text):
        texto = text
        texto_analisado = py_analyzer.predict(texto)

        return texto_analisado.probas
    
# TESTE

