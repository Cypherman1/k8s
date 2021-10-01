import tensorflow as tf
import numpy as np


fileDir = "/usr/mydata/version.txt"

f = open(fileDir, "w+")
f.writelines("Tensorflow version is: " + tf.__version__)
f.write("\n")
f.write("Numpy version is:" + np.__version__)
f.close()
