import tensorflow as tf

x1 = tf.constant(5)
x2 = tf.constant(6)

result = tf.mul(x1, x2)
print(result)

with tf.Session() as sess:
	print(sess.run(result))

#sess = tf.Session()
#print(sess.run(result))
#sess.close()