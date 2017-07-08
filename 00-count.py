import tensorflow as tf

# Constants: one
# Variables: num
# Operations: Add, Assign

one = tf.constant(1)

num = tf.Variable(0)

add = tf.add(num, one)

assign = tf.assign(num, add)

init = tf.global_variables_initializer()

print '\nRunning Tensorflow Session...\n'
with tf.Session() as sess:
	sess.run(init)

	print '\nInitial Value of NUM: ', sess.run(num)

	print '\nIterating 10 times...\n'
	for i in range(10):
		result = sess.run(assign)
		print 'New result of NUM: ', result



