import re
import spacy

nlp = spacy.load("pt_core_news_sm")

class TextTransformation:

    def limpeza_do_texto(self, text : str):
        text = text.lower()

        text = re.sub(r'http\S+|@\w+|#[\w-]+', '', text) # limpar links, e caracteres especiais.
        text = re.sub(r'[^a-záéíóúâêîôûãõç\s]', '', text) # Limpar caracteres não alfabeticos
        text = re.sub(r'\s+', ' ', text).strip() # remover espaço em branco continuo

        return text

    def lematizacao(self, text: str):

        doc = nlp(text)
        lemmas = [t.lemma_ for t in doc if t.is_alpha and not t.is_stop]
        print(lemmas)

        return ' '.join(lemmas)

# Teste 

        
"wordcloud = text.limpeza_do_texto -> lematização"
"analise de sentimento = text.limpeza_do_texo -> sentiment_analyzer"