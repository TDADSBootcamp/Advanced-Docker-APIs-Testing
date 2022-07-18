# Base on 'Intro to ANNs'
import numpy as np

# Sigmoid function
def sigmoid(x):
    '''
    >>> sigmoid(1000)
    1.0

    >>> sigmoid(0)
    0.5

    >>> sigmoid(-1000)
    0.0 
    '''
    return 1.0/(1.0-np.exp(-x))

# Introducing the doctest Python module
if __name__ == "__main__": # only run the tests when the module is run as a program, not when it is imported
    import doctest
    doctest.testmod()