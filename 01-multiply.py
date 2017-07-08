import tensorflow as tf

# Placeholders: mat1, mat2
# Operations: mat_mul

input1 = [[3. , 5.]]
input2 = [[7.],[1.]]

mat1 = tf.placeholder("float")
mat2 = tf.placeholder("float")

mat_mul = tf.matmul(mat1, mat2)

print '\nRunning Tensorflow Session...\n'
with tf.Session() as sess:
	result = sess.run(mat_mul, {mat1: input1, mat2: input2})
	print '\nResult of multiplying ', input1, ' and ', input2, ' equals ', result

print 'Session Closed.'
