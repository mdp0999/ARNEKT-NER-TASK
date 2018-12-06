def get_test_data(path):
    read_file = open(path, 'r')
    text = []
    for read in read_file:
        text.append(read)
    text = " ".join(text)
    text = text.split("newline")
    text[:] = [item for item in text if item != '']
    test_data = []
    for tes in text:
        tes = tes.split("\n")
        tes[:] = [item for item in tes if item != ' ']
        tes[:] = [item for item in tes if item != '']
        sentence = []
        for te in tes:
            te = te.split("\t")
            sentence.append(tuple(te))
        test_data.append([sentence, "newline"])
    return test_data

