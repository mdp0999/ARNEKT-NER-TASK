import pycrfsuite
from word2features import *
test = open("/home/mdp/PycharmProjects/FInal_NER_Task/arnekt-iecsil-baseline_task_a/data/arnekt-iecsil-ie-corpus_test_1/task_a/v1_test1.te", "r").read().split("newline")
test[:] = [item for item in test if item != '']
test_data = []

#Generate predictions
tagger = pycrfsuite.Tagger()
tagger.open('crf_te.model')
lang_code = 'te'
write_file = open('v1_test1_tagged.' + lang_code, 'w')
test_data = []
a = 0
for tes in test:
    tes = tes.split("\n")
    tes[:] = [item for item in tes if item != '']
    sentence = []
    for te in tes:
        te = te.split("\t")
        sentence.append(tuple(te))
    test_data.append([sentence,"newline"])

#print(test_data[0])

for doc in test_data:
    if doc[1] == "newline":
        X_test = [extract_features(doc[0])]
        y_pred = [tagger.tag(xseq) for xseq in X_test][0]
        print(doc[1], y_pred)
        for y_p in y_pred:
            write_file.write(y_p + '\n')
        write_file.write("newline" + '\n')
