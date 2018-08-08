#Author: Maede Zolanvari
#Date: Aug. 8th 2018



from tensorflow.python.client import timeline
import time


import tensorflow as tf
with tf.device ('/device:GPU:0'):
    time.time()
    starttime=time.time()
    for i in range(1000):
        x = tf.random_normal([10000000, 100])
        y = tf.random_normal([100, 10000000])
        res = tf.matmul(x, y)
        
        
        x = tf.random_normal([1000000, 100])
        y = tf.random_normal([100, 1000000])
        res = tf.matmul(x, y)
        
        
        x = tf.random_normal([1000000, 100])
        y = tf.random_normal([100, 1000000])
        res = tf.matmul(x, y)
       

finishtime=time.time()
exectime=finishtime-starttime
print ('This program took seconds =', exectime)

m = divmod(exectime, 60)
print('minutes=',m[0],'seconds=',m[1])
#sess = tf.Session(config=tf.ConfigProto(log_device_placement=True))
#print(sess.run(res))
