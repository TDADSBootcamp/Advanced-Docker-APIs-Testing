# Base on 'Intro to ANNs'
import numpy as np

# Sigmoid function
def sigmoid(x):
    return 1.0/(1.0+np.exp(x))

# Introducing the assert Python keyword
assert sigmoid(1) < sigmoid(2), 'Assert sigmoid increases between two poibts'
assert sigmoid(1000) == 1.0, 'Assert sigmoid value at high values'
assert sigmoid(0) == 0.5, 'Assert sigmoid value at 0'
assert sigmoid(-1000) == 0.0, 'Assert sigmoid value at low values'