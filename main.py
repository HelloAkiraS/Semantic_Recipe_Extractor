import spacy
import json
import re
from collections import Counter
from material import text, raw_text, dictionary, non_ingredients

class SemanticRecipeExtractor:
    def __init__(self):
        self.nlp = spacy.load("pt_core_news_md")
        self.d = dictionary
        self.ni = non_ingredients
    
    def _text_normalizer(self, string):
        string = re.sub(
            r'\b(' + '|'.join(self.d.keys()) + r')\b',
            lambda repl: self.d[repl.group(0)],
            string.lower()
        )
        return re.sub(r'[!?,.]{2,}','.', string)

    def _ingredients_extractor(self, doc):
        return list(
            Counter(
                token.text for token in doc if token.pos_ == 'NOUN' and token.text not in self.ni
            )
        )

    def _action_extractor(self, doc):
        pass

    def _measurings_extractor(self, doc):
        pass

    def get_json(self, raw_text):
        doc = self.nlp(self._text_normalizer(raw_text))
        return self._ingredients_extractor(doc)

if __name__ == "__main__":
    print(SemanticRecipeExtractor().get_json(raw_text))