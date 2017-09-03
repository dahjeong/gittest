import tensorflow as tf
x_data = [[73., 80., 75],[93., 88., 93.], [89., 91., 90.], [96., 98., 100.], [73., 66., 70.]]
y_data = [[152.], [185.], [180.], [196.], [142.]]
#
X = tf.placeholder(tf.float32, shape=[None, 3])
Y = tf.placeholder(tf.floar32, shape=[None, 1])

W = tf.Variable(tf.random_normal([3, 1]), name='weight')
b = tf.Variable(tf.random_normal([1]), name='bias')

# Hypothesis
hypothesis = tf.matmul(X, W) + b
