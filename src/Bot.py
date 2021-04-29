from tensorflow.python.framework import ops
from pickle import dump
from tflearn import fully_connected,regression,DNN,input_data
from json import load
from nltk import word_tokenize
from numpy import array,argmax
from random import choice
from nltk.stem.lancaster import LancasterStemmer
from os.path import exists

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
        self.count=-1
        self.say=""

    def read(self):
        with open("src/models/intents.json") as f:
            self.data=load(f)
    def dump(self):
        with open("src/models/data.pickle", "wb") as f:
            dump((self.words, self.labels, self.training, self.output), f)
    def stem(self):
        for intent in self.data["intents"]:
            for pattern in intent["patterns"]:
                wrds = word_tokenize(pattern)
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

        self.training = array(self.training)
        self.output = array(self.output)
        self.dump()

    def setup(self):
        ops.reset_default_graph()
        net = input_data(shape=[None, len(self.training[0])])
        net = fully_connected(net, 10)
        net = fully_connected(net, 10)
        net = fully_connected(net, len(self.output[0]), activation="softmax")
        net = regression(net)
        self.model = DNN(net)
        if exists("src/models/model.tflearn.index"):
            self.model.load("src/models/model.tflearn")
        else:
            self.model.fit(self.training, self.output, n_epoch=1000, batch_size=8, show_metric=True)
            self.model.save("src/models/model.tflearn")

    def bag_of_words(self,s, words):
        bag = [0 for _ in range(len(words))]

        s_words = word_tokenize(s)
        s_words = [self.stemmer.stem(word.lower()) for word in s_words]

        for se in s_words:
            for i, w in enumerate(words):
                if w == se:
                    bag[i] = 1

        return array(bag)
    def chat(self,x,ui):
        self.count+=1
        results = self.model.predict([self.bag_of_words(x, self.words)])
        results_index = argmax(results)
        tag = self.labels[results_index]
        try:
            if results[0][results_index] > 0.4:
                for tg in self.data["intents"]:
                    if tg['tag'] == tag:
                        responses = tg['responses']
                self.say=choice(responses)
                ui.textEdit.setText(self.say)
            else:
                self.say="Sorry i can't understand i am still learning try again."
                ui.textEdit.setText(self.say)
        except Exception as e:
            print(e)