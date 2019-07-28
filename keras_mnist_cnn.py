import tensorflow as tf
import keras
import matplotlib.pyplot as plt

class myCallbacks(keras.callbacks.Callback):
  def on_epoch_end(self,epoch,logs={}):
    if(logs.get('acc')>0.95):
      print('\nStopping operation! Exceeded 95% accuracy!')
      self.model.stop_training = True

callbacks = myCallbacks()

mnist = keras.datasets.mnist

(x_train, y_train), (x_test, y_test) = mnist.load_data()

x_train = x_train/255.0
x_test = x_test/255.0

model = keras.models.Sequential([
  keras.layers.Conv2D(64, (3,3), activation='relu', input_shape=(28,28,1))


])
