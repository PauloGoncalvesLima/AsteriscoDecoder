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
NGRAM = 50

rand_num_array = []
for i in range(100):
    rand_num_array.append(random.randrange(0,36000))

sentencesUsed = open('./texts/usedSentences.txt', 'w')

# carregar frases
sentences = []
with open('./texts/redditSentences.txt', 'r') as sentenceFile:
    i = 0
    for line in sentenceFile:
        if i in rand_num_array:
            sentences.append(line)
            sentencesUsed.write(line)
        i += 1
sentencesUsed.close()

# words = []
# with open('./texts/cleanWords.txt', 'r') as wordFile:
#     for line in wordFile:
#         line = line.strip()
#         words.append(line)

vocab = set()
for s in sentences:
    for c in s:
        vocab.add(c)

# transformar vocabulario em int
vocab = sorted(vocab)
print(vocab)
strToInt = dict((w, n) for n, w in enumerate(vocab))

rnnInput = []
rnnOutput = []

# gerar exemplos
for s in sentences:
    for i in range(0, len(s) - NGRAM, 1):
        inpSen = s[i:i + NGRAM]
        outSen = s[i + NGRAM]
        rnnInput.append([strToInt[c] for c in inpSen])
        rnnOutput.append(strToInt[outSen])

# formatar input e output
patternNum = len(rnnInput)
# reshape the input into a format compatible with LSTM layers
rnnInput = numpy.reshape(rnnInput, (patternNum, NGRAM, 1))
# normalize input
rnnInput = rnnInput / float(len(vocab))
# one hot enconding the labels
rnnOutput = np_utils.to_categorical(rnnOutput)

# modelo
model = Sequential()
model.add(LSTM(
    512,
    input_shape=(rnnInput.shape[1], rnnInput.shape[2]),
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

# checkpoint system
filepath = "./checkpoints/check-{epoch:02d}-{loss:.4f}.hdf5"
checkpoint = ModelCheckpoint(
    filepath,
    monitor='loss',
    verbose=0,
    save_best_only=True,
    mode='min'
)
callbacks_list = [checkpoint]

model.fit(rnnInput, rnnOutput, epochs=200, callbacks=callbacks_list)