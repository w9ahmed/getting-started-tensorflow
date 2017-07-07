import tensorflow as tf

node1 = tf.constant(3.0, dtype=tf.float32)
node2 = tf.constant(4.0, dtype=tf.float32)

node3 = tf.constant(2, dtype=tf.int32)

print node1, node2, node3

session = tf.Session()

print session.run(node1)
print session.run([node2, node3])


################################
# combining Tensor nodes with operations (Operations are also nodes.)
################################

operation_node = tf.add(node1, node2)
print operation_node
print session.run(operation_node)



#################################
# A graph can be parameterized to accept external inputs, known as placeholders.
#################################

placeholder_a = tf.placeholder(dtype=tf.float32)
placeholder_b = tf.placeholder(dtype=tf.float32)

# adder_node = a + b
adder_node = tf.add(placeholder_a, placeholder_b)

# names are important
print session.run(adder_node, {placeholder_a: 4.0, placeholder_b: 6.0})
print session.run(adder_node, {placeholder_a: [1, 3], placeholder_b: [4, 3]})


################################
# Adding 1 to value
################################
print '\n While Loop Stuff \n'

i = tf.constant(0, dtype=tf.int32)

r = tf.while_loop(
	lambda i: tf.less(i, 10),
	lambda i: tf.add(i, 1),
	[i])

print session.run(r)



