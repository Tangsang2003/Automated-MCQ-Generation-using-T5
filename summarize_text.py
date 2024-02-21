import spacy
from gensim.summarization import summarize


def extract_relevant_information(text):
    # Load spaCy model
    nlp = spacy.load("en_core_web_sm")

    # Process the text with spaCy
    doc = nlp(text)

    # Extract named entities
    named_entities = [ent.text for ent in doc.ents]

    # Extract keywords (nouns and proper nouns)
    keywords = [token.text for token in doc if token.pos_ in ["NOUN", "PROPN"]]

    # Summarize the text
    summary = summarize(text)

    return named_entities, keywords, summary

# Example text
# input_text = """
# Artificial intelligence (AI) is intelligence demonstrated by machines, in contrast to the natural intelligence displayed by humans and animals. Leading AI textbooks define the field as the study of "intelligent agents": any device that perceives its environment and takes actions that maximize its chance of successfully achieving its goals.
# """


input_text = '''

 Question and Answer Generation: To create the questionanswer pairs,
 we combined the two tasks into a single multi-task model. We ne-tuned the
 small version of the T5 Transformer, which has 220M parameters, and we used
 the SQuAD1.1 dataset [37], which includes 100,000 questionanswer pairs. We
 trained the model to output the question and the answer and to accept the
 passage and the answer with a 30% probability for the answer to be replaced by
 the [MASK] token. This allows us to generate an answer for the input question
 by providing the [MASK] token instead of the target answer. We trained the
 model for ve epochs, and we achieved the best validation cross-entropy loss of
 1.17 in the fourth epoch. We used a learning rate of 0.0001, a batch size of 16,
 and a source and a target maximum token lengths of 300 and 80, respectively.
 For question generation, we used the same data split and evaluation scripts as
 in [9]. For answer generation, we trained on the modi ed SQuAD1.1 Question
 Answering dataset as proposed in our previous work [45], achieving an Exact
 Match of 41.51 and an F1 score of 53.26 on the development set.
 Distractor Generation: To create contextual distractors for the question
 answer pairs, we used the RACE dataset [19] and the small pre-trained T5 model.
 Weprovided the question, the answer, and the context as an input, and obtained
 three distractors separated by a [SEP] token as an output. We trained the model
 for ve epochs, achieving a validation cross-entropy loss of 2.19. We used a
 learning rate of 0.0001, a batch size of 16, and a source and a target maximum
 token lengths of 512 and 64, respectively. The rst, the second, and the third
 distractor had BLEU1 scores of 46.37, 32.19, and 34.47, respectively. We further
 extended the variety of distractors with context-independent proposals, using
 sense2vec [43] to generate words or multi-word phrases that are semantically
 similar to the answer
'''
input_text.replace("\n", "")
entities, keywords, summary = extract_relevant_information(input_text)

# Print the results
print("Named Entities:", entities)
print("Keywords:", keywords)
# print("------------------Summary------------------\n", summary)
