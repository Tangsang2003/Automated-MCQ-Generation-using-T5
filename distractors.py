# This is just a test file. Don't mind this. heehee

from sense2vec import Sense2Vec
s2v = Sense2Vec().from_disk('./app/ml_models/sense2vec_distractor_generation/data/s2v_old')
word = '600'
word = word.lower()
word = word.replace(' ', '_')
print(word)
sense = s2v.get_best_sense(word)
# Get the sense
print("Best Sense", sense)
most_similar = s2v.most_similar(sense, n=12)
print(most_similar)