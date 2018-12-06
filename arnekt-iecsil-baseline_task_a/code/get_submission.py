import os
from load_data import *
import numpy as np
import pycrfsuite
from sklearn.metrics import classification_report
from word2features import *


# tamil - ta, malayalam - ml, telugu = te, kannada - kn, hindi - hi
lang_code = 'te'

# getting root directories
test_root_dir = '../data/arnekt-iecsil-ie-corpus_test_1/task_a/'

# getting test1 file paths
test1_path = os.path.join(test_root_dir, 'v1_test1.'  + lang_code)

# loading data
test_data = get_test_data(test1_path)
print(test_data[0])
#load crf models
tagger = pycrfsuite.Tagger()
tagger.open('crf_'+lang_code+'.model')

#define write file
write_file = open('v1_test1_tagged.' + lang_code, 'w')

#work on test data
for doc in test_data:
    if doc[1] == "newline":
        X_test = [extract_features(doc[0])]
        y_pred = [tagger.tag(xseq) for xseq in X_test][0]
        for y_p in y_pred:
            write_file.write(y_p + '\n')
        write_file.write("newline" + '\n')
