import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from sense2vec import Sense2Vec
import random
# nltk.download('punkt')
# nltk.download('stopwords')


def is_float(value):
    try:
        float(value)
        return True
    except ValueError:
        return False


def extract_significant_words(sentence_arg):
    # Tokenize the sentence
    tokens = word_tokenize(sentence_arg)

    # Remove non-alphabetic characters and convert to lowercase
    words = [word.lower() for word in tokens if word.isalpha() or word.isnumeric() or is_float(word)]

    # Remove stop words (optional)
    stop_words = set(stopwords.words('english'))
    words = [word for word in words if word not in stop_words]

    return words


# Example usage
s2v = Sense2Vec().from_disk('./app/ml_models/sense2vec_distractor_generation/data/s2v_old')
# sentence = "This is an example sentence with irrelevant characters and punctuation!"
# sentence = " Squad 2.0"
# sentence = "2007 AD"
sentence = "The police have the right to defend their lives"
significant_words = extract_significant_words(sentence)
print(significant_words)
distractors_candidates = []
for word_itr in significant_words:
    word = word_itr
    word = word.lower()
    sense = s2v.get_best_sense(word)
    if not sense:
        continue
    most_similar = s2v.most_similar(sense, 3)
    for phrase in most_similar:
        normalized_phrase = phrase[0].split("|")[0].replace("_", " ").lower()
        if normalized_phrase != word_itr:
            modified_sentence = sentence.replace(word_itr, normalized_phrase)
            if modified_sentence not in distractors_candidates:
                distractors_candidates.append(modified_sentence)
print("----------------- Distractors: ---------------------")
print(distractors_candidates)



print ("-----upto here---------------------")
print("-----------Selected Distractors-------------------")
indices = []
selected = []
random_num = 0
if len(distractors_candidates) >= 3:
    for i in range(3):
        while True:
            random_num = random.randint(0, len(distractors_candidates) - 1)
            if random_num not in indices:
                indices.append(random_num)
                break

for i in range(len(indices)):
    selected.append(distractors_candidates[indices[i]])
for i in range(len(selected)):
    print("-------------------------")
    print(selected[i])

word = '600'
word = word.lower()
word = word.replace(' ', '_')
print(word)
sense = s2v.get_best_sense(word)
# Get the sense
print("Best Sense", sense)
most_similar = s2v.most_similar(sense, n=12)
print(most_similar)