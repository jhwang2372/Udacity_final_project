import os
#from keras.applications.resnet50 import ResNet50, preprocess_input
#from keras.applications.inception_v3 import InceptionV3, preprocess_input
from keras.applications.xception import xception, preprocess_input
from keras.models import load_model
from scipy.misc import imread
import cv2
import numpy as np
from os.path import basename, splitext


DATASET_PATH  = './data/whole_data/test'
IMAGE_SIZE    = (299, 299)
NUM_CLASSES   = 2
BATCH_SIZE    = 16
#WEIGHTS_FINAL = 'final-resnet50-final.h5'
WEIGHTS_FINAL = 'finetuned-best_Xcpt_more_layer.hdf5'
CLASSES = ['cats', 'dogs']


#labels = []
preds = np.zeros(12500)
prob = np.zeros(12500)

# testing model
model = load_model(WEIGHTS_FINAL)

# load weights into new model
model.load_weights(WEIGHTS_FINAL)


# for i, layer in enumerate(model.layers):
#    print(i, layer.name)

for root, dirs, files in os.walk(DATASET_PATH):
    for file in files:
        photo_path = os.path.join(DATASET_PATH, file)  # photo path
        #print(photo_path)

        base = os.path.basename(file)
        ind = int(splitext(base)[0]) - 1

        if not ind % 1000:
            print(photo_path)

        img = (imread(photo_path)[:, :, :3]).astype(np.float32)  # read to ndarray
        x = cv2.resize(img, IMAGE_SIZE)

        # predict the category of the image
        x = preprocess_input(x)
        x = np.expand_dims(x, axis=0)
        y = model.predict(x)[0]
        y_max = y.argsort()[::-1][:5]
        #preds.append(y_max[0])
        preds[ind] = y_max[0]

        # we set the smallest probability to 0.0005
        # to avoid the significantly impact in case of wrong predictions
        if y[1] < 0.0005:
            prob[ind] = 0.0005
        else:
            prob[ind] = y[1]
        prob[ind] = y[1]


        if idx % 500 == 0:
            print("Reading the %sth image" % idx)

        idx = idx + 1

#print("labels:", labels)
#print("preds:", preds)

nd_preds = np.array(preds)
nd_prob = np.array(prob)
np.save('preds.npy', nd_preds)
np.save('prob_org.npy', nd_prob)

