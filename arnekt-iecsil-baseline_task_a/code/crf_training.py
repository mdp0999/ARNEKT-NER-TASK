import numpy as np
import pycrfsuite
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import pickle
from word2features import *

#Read data file
language = "hi"
with open("../data/arnekt-iecsil-ie-corpus_train/task_a/v1_train."+language, "rb") as fp:
    data = pickle.load(fp)

X_train = [extract_features(doc) for doc in data]
y_train = [get_labels(doc) for doc in data]

#split data into train and test
# # X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1)

trainer = pycrfsuite.Trainer(verbose=True)

# Submit training data to the trainer
for xseq, yseq in zip(X_train, y_train):
    trainer.append(xseq, yseq)

# Set the parameters of the model
trainer.set_params({
    # coefficient for L1 penalty
    'c1': 0.1,

    # coefficient for L2 penalty
    'c2': 0.01,

    # maximum number of iterations
    'max_iterations': 200,

    # whether to include transitions that
    # are possible, but not observed
    'feature.possible_transitions': True
})

# Provide a file name as a parameter to the train function, such that
# the model will be saved to the file when training is finished
trainer.train('new_crf_hi.model')

# Generate predictions
tagger = pycrfsuite.Tagger()
tagger.open('crf_'+language+'.model')