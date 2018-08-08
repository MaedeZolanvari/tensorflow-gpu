#Author: Maede Zolanvari
#Date: Aug. 8th 2018


import tensorflow as tf
from tensorflow.python.client import timeline
import time



with tf.device ('/device:GPU:0'):
    time.time()
    timestamp1=time.time()
    for i in range(1000):
        x = tf.random_normal([10000000, 100])
        y = tf.random_normal([100, 10000000])
        res = tf.matmul(x, y)
        #with tf.Session() as sess:
        #    sess.run(res)
        
        x = tf.random_normal([1000000, 100])
        y = tf.random_normal([100, 1000000])
        res = tf.matmul(x, y)
        # with tf.Session() as sess:
        # sess.run(res)
        x = tf.random_normal([10000, 100])
        y = tf.random_normal([100, 10000])
        res = tf.matmul(x, y)
        #with tf.Session() as sess:
        #   sess.run(res)
    """
    # Run the graph with full trace option
    with tf.Session() as sess:
        run_options = tf.RunOptions(trace_level=tf.RunOptions.FULL_TRACE)
        run_metadata = tf.RunMetadata()
        sess.run(res, options=run_options, run_metadata=run_metadata)
    
        # Create the Timeline object, and write it to a json
        tl = timeline.Timeline(run_metadata.step_stats)
        ctf = tl.generate_chrome_trace_format()
        with open('timeline.json', 'w') as f:
            f.write(ctf)
    """
timestamp2=time.time()
exectime=timestamp2-timestamp1
print ('This took seconds =', exectime)

m = divmod(exectime, 60)
print('minutes=',m[0],'seconds=',m[1])
#sess = tf.Session(config=tf.ConfigProto(log_device_placement=True))
#print(sess.run(res))
