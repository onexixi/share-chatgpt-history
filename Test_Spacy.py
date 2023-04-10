import spacy
from spacy import displacy
from collections import Counter
import en_core_web_sm
nlp = en_core_web_sm.load()

doc = nlp("The cat sat on the mat. The dog sat on the log.")
for token in doc:
    print(token.text, token.pos_, token.dep_)

displacy.serve(doc, style="dep")