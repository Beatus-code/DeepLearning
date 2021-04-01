# DeepLearning
Deep Learning in Convolution Neural Network
The aim of the experiment was to investigated the following:
1. Data Scaling using Mean Subtraction vs Normalization
2. Weight Initialization( Xavier vs He Initialization)
3. Layer Architecture
4. Gradient Optimization
5. Activation Function and
6. Regularization

from keras.datasets import fashion_mnist
from keras.utils import to_categorical
from keras.models import Sequential
from keras.layers import Conv2D
from keras.layers import MaxPooling2D
from keras.layers import Dense
from keras.layers import Flatten
import tensorflow as tf
from keras.preprocessing.image import ImageDataGenerator
# load dataset  datasets..load_data()
(trainX, trainY), (testX, testY) = fashion_mnist.load_data()
