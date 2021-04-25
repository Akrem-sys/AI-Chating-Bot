import numpy
import tflearn
from tensorflow.python.framework import ops
import random
import json
import pickle
import nltk
from nltk.stem.lancaster import LancasterStemmer


class Bot:
    def __init__(self):
        self.words = []
        self.labels = []
        self.docs_x = []
        self.docs_y = []
        self.stemmer = LancasterStemmer()
        self.data = []
        self.training = []
        self.output = []
        self.out_empty=[]
        self.model=[]


    def read(self):
        with open("src/intents.json") as f:
            self.data=json.load(f)
    def dump(self):
        with open("src/data.pickle", "wb") as f:
            pickle.dump((self.words, self.labels, self.training, self.output), f)
    def stem(self):
        for intent in self.data["intents"]:
            for pattern in intent["patterns"]:
                wrds = nltk.word_tokenize(pattern)
                self.words.extend(wrds)
                self.docs_x.append(wrds)
                self.docs_y.append(intent["tag"])

            if intent["tag"] not in self.labels:
                self.labels.append(intent["tag"])

        self.words = [self.stemmer.stem(w.lower()) for w in self.words if w != "?"]
        self.words = sorted(list(set(self.words)))
        self.labels = sorted(self.labels)
    def modelsetup(self):
        self.out_empty = [0 for _ in range(len(self.labels))]

        for x, doc in enumerate(self.docs_x):
            bag = []

            wrds = [self.stemmer.stem(w.lower()) for w in doc]

            for w in self.words:
                if w in wrds:
                    bag.append(1)
                else:
                    bag.append(0)

            output_row = self.out_empty[:]
            output_row[self.labels.index(self.docs_y[x])] = 1
            self.training.append(bag)
            self.output.append(output_row)

        self.training = numpy.array(self.training)
        self.output = numpy.array(self.output)
        self.dump()

    def setup(self):
        ops.reset_default_graph()
        net = tflearn.input_data(shape=[None, len(self.training[0])])
        net = tflearn.fully_connected(net, 10)
        net = tflearn.fully_connected(net, 10)
        net = tflearn.fully_connected(net, len(self.output[0]), activation="softmax")
        net = tflearn.regression(net)
        self.model = tflearn.DNN(net)
        self.model.fit(self.training, self.output, n_epoch=1000, batch_size=6, show_metric=True)
        self.model.save("src/model.tflearn")

    def bag_of_words(self,s, words):
        bag = [0 for _ in range(len(words))]

        s_words = nltk.word_tokenize(s)
        s_words = [self.stemmer.stem(word.lower()) for word in s_words]

        for se in s_words:
            for i, w in enumerate(words):
                if w == se:
                    bag[i] = 1

        return numpy.array(bag)
    def chat(self,x,ui):
        results = self.model.predict([self.bag_of_words(x, self.words)])
        results_index = numpy.argmax(results)
        tag = self.labels[results_index]

        if results[0][results_index] > 0.4:
            for tg in self.data["intents"]:
                if tg['tag'] == tag:
                    responses = tg['responses']
            ui.textEdit.setText(random.choice(responses))
        else:
            ui.textEdit.setText("Sorry i can't understand i am still learning try again.")