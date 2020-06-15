import numpy
import random
from tensorflow.keras.models import Sequential # RecurrentNeuralNetwork
from tensorflow.keras.layers import Dense # Don't be dense
from tensorflow.keras.layers import Dropout # Prevents Overfitting
from tensorflow.keras.layers import LSTM # Long Short-Term Memory
from tensorflow.keras.layers import BatchNormalization as BatchNorm
from tensorflow.keras.layers import Activation # Activation Function
from keras.utils import np_utils # Categorize Data
from tensorflow.keras.callbacks import ModelCheckpoint # Checkpoint System

# tamanho do n-gram
NGRAM = 3

# carregar frases
sentences = []
with open('./texts/usedSentences.txt', 'r') as sentenceFile:
    for line in sentenceFile:
        sentences.append(line)

# words = []
# with open('./texts/cleanWords.txt', 'r') as wordFile:
#     for line in wordFile:
#         line = line.strip()
#         words.append(line)

vocab = []
for s in sentences:
    words = s.split()
    for w in words:
        vocab.append(w)

# transformar vocabulario em int
vocab = sorted(set(w for w in vocab))
strToInt = dict((w, n) for n, w in enumerate(vocab))
intToStr = dict((n, w) for n, w in enumerate(vocab))

rnnInput = []
rnnOutput = []

# gerar exemplos
for s in sentences:
    words = s.split()
    for i in range(0, len(words) - NGRAM, 1):
        inpSen = words[i:i + NGRAM]
        outSen = words[i + NGRAM]
        rnnInput.append([strToInt[w] for w in inpSen])
        rnnOutput.append(strToInt[outSen])

# formatar input e output
patternNum = len(rnnInput)
# reshape the input into a format compatible with LSTM layers
rnnNormalized = numpy.reshape(rnnInput, (patternNum, NGRAM, 1))
# normalize input
rnnNormalized = rnnNormalized / float(len(vocab))
# one hot enconding the labels
rnnOutput = np_utils.to_categorical(rnnOutput)

# modelo
model = Sequential()
model.add(LSTM(
    512,
    input_shape=(rnnNormalized.shape[1], rnnNormalized.shape[2]),
    recurrent_dropout=0.3,
    return_sequences=True
))
model.add(LSTM(512, return_sequences=True, recurrent_dropout=0.3,))
model.add(LSTM(512))
model.add(BatchNorm())

# overfitting
model.add(Dropout(0.3))
model.add(Dense(256))
model.add(Activation('relu')) # regularization
model.add(BatchNorm())
model.add(Dropout(0.3))

model.add(Dense(len(vocab)))
model.add(Activation('softmax')) # softmax activation / crossentropy loss
model.compile(loss='categorical_crossentropy', optimizer='rmsprop')

model.load_weights('./trainedModels/check-87-0.9973.hdf5')

generatedFile = open('./texts/generatedSentences.txt', 'w')
# generate 100 sentences
for i in range(100):
    start = random.randrange(0, len(rnnInput)-1)
    pattern = rnnInput[start]
    genSentence = [intToStr[n] for n in pattern]
    while True:
        predictionInput = numpy.reshape(pattern, (1, len(pattern), 1))
        predictionInput = predictionInput / float(len(vocab))

        prediction = model.predict(predictionInput, verbose=0)

        index = numpy.argmax(prediction)
        result = intToStr[index]

        genSentence.append(result)

        # restructure pattern
        pattern.append(index)
        pattern = pattern[1:len(pattern)]

        if genSentence[-1] == '<FIM>':
            break
    generatedFile.write(" ".join(genSentence) + '\n')

generatedFile.close()