# import nltk
# from nltk import word_tokenize, pos_tag, ne_chunk
# from nltk.corpus import stopwords
# from collections import Counter
#
# # Download NLTK resources (if not already downloaded)
# # Sample text
# text = "Tangsang is an awesome person."
#
# # Tokenize and part-of-speech tagging using NLTK
# tokens = word_tokenize(text)
# pos_tags = pos_tag(tokens)  # Part of Speech tagging.
# # assigning a part-of-speech category (such as noun, verb, adjective, etc.) to each word in a text.
#
# # Named Entity Recognition using NLTK's ne_chunk
# # identify named entities in a given text and classify
# # them into categories such as persons, organizations, locations, etc.
# tree = ne_chunk(pos_tags)
#
# # Extract named entities
# named_entities = []
# for subtree in tree:
#     if isinstance(subtree, nltk.Tree):
#         entity = " ".join([word for word, tag in subtree.leaves()])
#         label = subtree.label()
#         named_entities.append((entity, label))
#
# # Remove stop words
# stop_words = set(stopwords.words('english'))
# filtered_tokens = [word.lower() for word in tokens if word.isalnum() and word.lower() not in stop_words]
#
# # Extract keywords using Counter
# keywords = [word for word, count in Counter(filtered_tokens).most_common(5)]
#
# # Perform Named Entity Recognition using spaCy
# # nlp = spacy.load('en_core_web_sm')
# # doc = nlp(text)
# # spacy_named_entities = [(ent.text, ent.label_) for ent in doc.ents]
#
# # Display results
# print("Named Entities (NLTK):", named_entities)
# print("Keywords (NLTK):", keywords)
# # print("Named Entities (spaCy):", spacy_named_entities)

from sense2vec import Sense2Vec
from collections import OrderedDict
from typing import List


class Sense2VecDistractorGeneration:
    def __init__(self):
        self.s2v = Sense2Vec().from_disk('app/ml_models/sense2vec_distractor_generation/data/s2v_old')

    def generate(self, answer: str, desired_count: int) -> List[str]:
        distractors = []
        answer = answer.lower()
        answer = answer.replace(" ", "_")

        sense = self.s2v.get_best_sense(answer)

        if not sense:
            return []

        most_similar = self.s2v.most_similar(sense, n=desired_count)

        for phrase in most_similar:
            normalized_phrase = phrase[0].split("|")[0].replace("_", " ").lower()

            if normalized_phrase.lower() != answer:  # TODO: compare the stem of the words (e.g. wrote, writing)
                distractors.append(normalized_phrase.capitalize())

        return list(OrderedDict.fromkeys(distractors))


s2v = Sense2VecDistractorGeneration()
print(Sense2VecDistractorGeneration.generate(s2v, 'las vegas', 4))
