import spacy
import json
import re
from collections import Counter
from material import text, raw_text, dictionary, non_ingredients, non_culinary_verbs, measurings

class SemanticRecipeExtractor:
    def __init__(self):
        self.nlp = spacy.load("pt_core_news_md")
        ruler = self.nlp.get_pipe("attribute_ruler")

        self.d = dictionary
        self.ni = non_ingredients
        self.ncv = non_culinary_verbs
        self.m = measurings

        ruler.add(
            patterns=[[{"TEXT":"pique"}]],
            attrs={"POS":"VERB", "LEMMA":"picar"}
        )
    
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
                token.text for token in doc if token.pos_ == 'NOUN' and token.text not in self.ni and token.text not in self.m
            )
        )

    def _action_extractor(self, doc):
        return [token.lemma_ for token in doc if token.pos_ == 'VERB' and token.text not in self.ncv]

    def _measurings_extractor(self, doc):
        return list(
            Counter(
                token.text for token in doc if token.text in self.m
            )
        )

    def get_json(self, s):
        doc = self.nlp(self._text_normalizer(s))
        return json.dumps(
            {
                "Ingredients":self._ingredients_extractor(doc),
                "Actions":self._action_extractor(doc),
                "Measures":self._measurings_extractor(doc)
            },
            ensure_ascii=False, indent=4
        )

if __name__ == "__main__":
    print(SemanticRecipeExtractor().get_json(text))