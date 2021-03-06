import numpy as np

from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
import string
import keras


# TODO: fill out the function below that transforms the input series 
# and window-size into a set of input/output pairs for use with our RNN model
def window_transform_series(series,window_size):
    # containers for input/output pairs
    X = [[series[i+j] for j in range(0,window_size)] for i, val in enumerate(series) if i<(len(series)-window_size)]
    y = [val for i, val in enumerate(series) if i>window_size-1]

    # reshape each 
    X = np.asarray(X)
    X.shape = (np.shape(X)[0:2])
    y = np.asarray(y)
    y.shape = (len(y),1)
    
    return X,y

# TODO: build an RNN to perform regression on our time series input/output data
def build_part1_RNN(step_size, window_size):
    model = Sequential()
    model.add(LSTM(5, input_shape=(window_size, 1)))
    model.add(Dense(1))
    return model


### TODO: list all unique characters in the text and remove any non-english ones
def clean_text(text):
    # find all unique characters in the text

    uniques = list(set(text))
    # print(uniques)

    # Remove any non-ascii characters, except necessary punctuation marks
    for char in uniques:
        if char not in string.ascii_lowercase+',.?!:;':
            text = text.replace(char,' ')
        
    # shorten any extra dead space created above
    text = text.replace('  ',' ')

    return text


    # remove as many non-english characters and character sequences as you can 


### TODO: fill out the function below that transforms the input text and window-size into a set of input/output pairs for use with our RNN model
def window_transform_text(text,window_size,step_size):
    # containers for input/output pairs
    
    inputs = [text[i:i+window_size] for i in range(0,len(text),step_size) if i<(len(text)-window_size)]
    outputs = [text[i] for i in range(0,len(text), step_size) if i>window_size-1]
    
    return inputs,outputs
