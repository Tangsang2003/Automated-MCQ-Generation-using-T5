import nltk
from nltk.tokenize import word_tokenize
from nltk.translate.bleu_score import sentence_bleu, SmoothingFunction
from nltk import pos_tag, ne_chunk
from collections import Counter
from nltk.corpus import stopwords
from collections import OrderedDict
from sense2vec import Sense2Vec
# import random
# nltk.download('punkt')
# nltk.download('stopwords')
# s2v = Sense2Vec().from_disk('./app/ml_models/sense2vec_distractor_generation/data/s2v_old')

import warnings
warnings.filterwarnings("ignore", message="floor_divide is deprecated", category=UserWarning)


def character_bleu(hypothesis, reference):
    smoothing = SmoothingFunction().method1
    bleu_score = sentence_bleu([list(reference)], list(hypothesis),
                               smoothing_function=smoothing, weights=(1, 0, 0, 0))
    return bleu_score


def is_float(value):
    try:
        float(value)
        return True
    except ValueError:
        return False


def extract_named_entities(sentence_arg):
    tokens = word_tokenize(sentence_arg)
    pos_tags = pos_tag(tokens)  # Part of Speech tagging.
    # assigning a part-of-speech category (such as noun, verb, adjective, etc.) to each word in a text.
    # Named Entity Recognition using NLTK's ne_chunk
    # identify named entities in a given text and classify
    # them into categories such as persons, organizations, locations, etc.
    tree = ne_chunk(pos_tags)

    # Extract named entities
    named_entities = []
    for subtree in tree:
        if isinstance(subtree, nltk.Tree):
            entity = " ".join([word for word, tag in subtree.leaves()])
            label = subtree.label()
            named_entities.append((entity, label))

    # Remove stop words
    stop_words = set(stopwords.words('english'))
    filtered_tokens = [word.lower() for word in tokens if word.isalnum() and word.lower() not in stop_words]

    # Extract keywords using Counter
    keywords = [word for word, count in Counter(filtered_tokens).most_common(5)]
    return named_entities, keywords


# def extract_significant_words(sentence_arg):
#     # Tokenize the sentence
#     tokens = word_tokenize(sentence_arg)
#
#     # Remove non-alphabetic characters and convert to lowercase
#     words = [word.lower() for word in tokens if word.isalpha() or word.isnumeric() or
#              is_float(word)]
#
#     # Remove stop words (optional)
#     stop_words = set(stopwords.words('english'))
#     words = [word for word in words if word not in stop_words]
#
#     return words


# Example usage
# sentence = "This is an example sentence with irrelevant characters and punctuation!"
# sentence = " Squad 2.0"
# sentence = "Highlighting the consequences of greed"


def generate_distractors(sentence, count, s2v):
    distractors = []
    answer = sentence.lower()
    answer = answer.replace(" ", "_")
    sense = s2v.get_best_sense(answer)
    if not sense:
        # print(f"Correct Answer: {sentence}")
        named_ent, kwords = extract_named_entities(sentence)
        ne_list = []
        for i in range(len(named_ent)):
            ne_list.append(named_ent[i][0])
        # print(ne_list)
        for i in range(len(ne_list)):
            word = ne_list[i]
            word = word.replace(" ", "_")
            ne_list[i] = word

        # print(kwords)
        distractors_candidates = []
        for word_itr in ne_list:
            if len(distractors_candidates) >= count:
                break
            # print(word_itr)
            word = word_itr
            word = word.lower()
            sense = s2v.get_best_sense(word)
            if not sense:
                continue
            most_similar = s2v.most_similar(sense, count)
            for phrase, prob in most_similar:
                normalized_phrase = phrase.split("|")[0].replace("_", " ").lower()
                if prob < 0.6:
                    # print("Continue because low prob!")
                    continue
                if normalized_phrase.lower() != word_itr.lower():
                    if character_bleu(normalized_phrase, word_itr) >= 0.5 and word_itr.isalpha():
                        # print(f"Too similar {normalized_phrase} and {word}")
                        continue
                    modified_sentence = sentence.lower().replace(word, normalized_phrase)
                    if modified_sentence not in distractors_candidates:
                        # print(f"Added {modified_sentence} from NE")
                        distractors_candidates.append(modified_sentence)
                        if len(distractors_candidates) > count:
                            break

        if len(distractors_candidates) < count:
            for word_itr in kwords:
                # print(word_itr)
                if len(distractors_candidates) >= count:
                    break
                word = word_itr
                word = word.lower()
                # print(f"Processing word: {word}")
                sense = s2v.get_best_sense(word)
                # print(f"Best sense for {word}: {sense}")
                if not sense:
                    # print("No sense found. Skipping.")
                    continue
                most_similar = s2v.most_similar(sense, 3)
                # print(f"Most similar phrases: {most_similar}")
                for phrase, prob in most_similar:
                    # print(phrase)
                    normalized_phrase = phrase.split("|")[0].replace("_", " ").lower()
                    # print(normalized_phrase)
                    if float(prob) < 0.6:
                        # print("Continue... because low prob")
                        continue

                    if normalized_phrase != word:
                        if character_bleu(word_itr.lower(), normalized_phrase) >= 0.5 and word_itr.isalpha():
                            # print(f"Too similar {normalized_phrase} and {word_itr}")
                            continue
                        modified_sentence = sentence.lower().replace(word_itr, normalized_phrase)
                        # print(modified_sentence)
                        # print(sentence)
                        if modified_sentence not in distractors_candidates:
                            # print(f"Adding to list: {modified_sentence}")
                            distractors_candidates.append(modified_sentence)
                            if len(distractors_candidates) >= count:
                                break
                    elif normalized_phrase == word_itr:
                        # print(f"Skipping {normalized_phrase}")
                        continue
        # print("----------------- Distractors: ---------------------")
        # print(distractors_candidates)

        # print("-----Up to here---------------------")
        # print("-----------Selected Distractors-------------------")
        # indices = []
        # selected = []
        # if len(distractors_candidates) >= count:
        #     for i in range(count):
        #         while True:
        #             random_num = random.randint(0, len(distractors_candidates) - 1)
        #             if random_num not in indices:
        #                 indices.append(random_num)
        #                 break
        #
        # for i in range(len(indices)):
        #     selected.append(distractors_candidates[indices[i]])
        # for i in range(len(selected)):
        #     print("-------------------------")
        #     print(selected[i])
        return distractors_candidates

    else:
        most_similar = s2v.most_similar(sense, count)

        for phrase in most_similar:
            normalized_phrase = phrase[0].split("|")[0].replace("_", " ").lower()

            if normalized_phrase.lower() != answer:
                distractors.append(normalized_phrase.capitalize())

        return list(OrderedDict.fromkeys(distractors))


# sentence = "Five"
# generate_distractors(sentence, 4)


# word = word.lower()
# word = word.replace(' ', '_')
# print(word)
# sense = s2v.get_best_sense(word)
# # Get the sense
# print("Best Sense", sense)
# most_similar = s2v.most_similar(sense, n=12)
# print(most_similar)

# sentence = "New York"
# print(generate_distractors(sentence, 3, s2v))