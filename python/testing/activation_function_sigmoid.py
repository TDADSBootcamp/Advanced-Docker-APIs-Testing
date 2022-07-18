# Base on 'Intro to ANNs'
import numpy as np

# Sigmoid function
def sigmoid(x):
    return 1.0/(1.0+np.exp(x))

# Derivation
def dsigmoid(x):
    return sigmoid(x)*(1.0-sigmoid(x))

# This exercise demonstrated the sigmoid function via matplotlib plots
# - How can we be sure we have implemented the functions correctly?
# - How might errors be introduced in the future?
# - How can we help avoid these problems?

