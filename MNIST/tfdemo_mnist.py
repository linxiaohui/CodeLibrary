# -*- coding:utf-8 -*-

from data_input import *
import tensorflow as tf
import numpy as np

dataset = MNISTDataSet('mnist')

# Create the model
x = tf.placeholder(tf.float32, [None, 784])
W = tf.Variable(tf.zeros([784, 10]))
b = tf.Variable(tf.zeros([10]))
y = tf.nn.softmax(tf.matmul(x, W) + b)

# Define loss and optimizer
y_ = tf.placeholder(tf.float32, [None, 10])
cross_entropy = -tf.reduce_sum(y_ * tf.log(y))
train_step = tf.train.GradientDescentOptimizer(0.01).minimize(cross_entropy)

correct_prediction = tf.equal(tf.argmax(y, 1), tf.argmax(y_, 1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

sess = tf.InteractiveSession()
# Train
tf.global_variables_initializer().run()

for i in range(500):
      train_images, train_labels = dataset.next_train_batch(50)
      train_step.run({x: train_images, y_: train_labels})
      if i%50 == 0 :
            print(sess.run(accuracy, feed_dict={x: train_images, y_: train_labels}))
            #print(sess.run(W),sess.run(b))

# Test trained model
images, labels = dataset.get_test_data()
print("Result correct prediction:")
print(sess.run(accuracy, feed_dict={x: images, y_: labels}))