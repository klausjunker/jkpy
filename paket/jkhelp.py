import sys
import sklearn
import matplotlib
import numpy as np
#import matplotlib.pyplot as plt
def jkversionen():
    print("Python: {}".format(sys.version))
    print("Sklearn: {}".format(sklearn.__version__))
    print("Matplotlib: {}".format(matplotlib.__version__))
    print("NumPy: {}".format(np.__version__))
