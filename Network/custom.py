
def arc_tan(x):
	return 1.0/(1+x**2)

import numpy as np 
np_arc_tan= np.vectorize(arc_tan)

import tensorflow as tf 

from tensorflow.python.framework import ops
np_arc_tan_32 = lambda x: np_arc_tan(x).astype(np.float32)

def tf_arc_tan(x,name=None):
    with ops.op_scope([x], name, "arc_tan") as name:
        y = tf.py_func(np_arc_tan_32,
                        [x],
                        [tf.float32],
                        name=name,
                        stateful=False)
        return y[0]
 def py_func(func, inp, Tout, stateful=True, name=None, grad=None):

    # Need to generate a unique name to avoid duplicates:
    rnd_name = 'PyFuncGrad' + str(np.random.randint(0, 1E+8))

    tf.RegisterGradient(rnd_name)(grad)  # see _MySquareGrad for grad example
    g = tf.get_default_graph()
    with g.gradient_override_map({"PyFunc": rnd_name}):
        return tf.py_func(func, inp, Tout, stateful=stateful, name=name)

def arctangrad(op, grad):
    x = op.inputs[0]

    n_gr = tf_arc_tan(x)
    return grad * n_gr 

np_arc_tan_32 = lambda x: np_arc_tan(x).astype(np.float32)

def tf_arc_tan(x, name=None):

    with ops.op_scope([x], name, "arctan") as name:
        y = py_func(np_spiky_32,
                        [x],
                        [tf.float32],
                        name=name,
                        grad=arctangrad)  
        return y[0]
