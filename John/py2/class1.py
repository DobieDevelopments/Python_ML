import cv2
import tensorflow as tf, os
from PIL import Image


def write_jpeg(data, filepath):
    g = tf.Graph()
    with g.as_default():
        data_t = tf.placeholder(tf.uint8)
        op = tf.image.encode_jpeg(data_t, format='rgb', quality=100)
        init = tf.initialize_all_variables()

    with tf.Session(graph=g) as sess:
        sess.run(init)
        data_np = sess.run(op, feed_dict={ data_t: data })

    with open(filepath, 'wb') as fd: 
        fd.write(data_np)

def load_data(data_directory):

    labels = []
    images = []

    file_names = [os.path.join(data_directory, f) 
    for f in os.listdir(data_directory) 
        if f.endswith(".jpg")]
    for f in file_names:
        img = cv2.imread(f) #Image.open(f)
        print(len(img.size))
        images.append( img) 
        print(f)
    return images

import numpy as np

R = np.zeros([128 * 128])
G = np.ones([128 * 128]) * 100
B = np.ones([128 * 128]) * 200

data = np.array(list(zip(R, G, B)), dtype=np.uint8).reshape(128, 128, 3)

assert data.shape == (128, 128, 3)


ROOT_PATH = "N:\\Sunfl\\Downloads"
train_data_directory = os.path.join(ROOT_PATH, "train_images")
test_data_directory = os.path.join(ROOT_PATH, "small_test_data") #"test_images")

images = load_data(test_data_directory)
i = 1
for img in images:
    write_jpeg(img, "test_save/" + str(i) + "_test.jpeg")
    i += 1