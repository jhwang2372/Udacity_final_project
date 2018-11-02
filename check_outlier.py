import os
from keras.applications.resnet50 import ResNet50, preprocess_input, decode_predictions
from os.path import basename, splitext
from scipy.misc import imread
import cv2
import numpy as np


DATASET_PATH  = '../final_project_classify/all/train/train'
IMAGE_SIZE    = (224, 224)

# define all the classes that exists in imagenet that belongs to dogs and cats
DOGS = ['n02085620','n02085782','n02085936','n02086079','n02086240','n02086646','n02086910','n02087046','n02087394','n02088094','n02088238',
        'n02088364','n02088466','n02088632','n02089078','n02089867','n02089973','n02090379','n02090622','n02090721','n02091032','n02091134',
        'n02091244','n02091467','n02091635','n02091831','n02092002','n02092339','n02093256','n02093428','n02093647','n02093754','n02093859',
        'n02093991','n02094114','n02094258','n02094433','n02095314','n02095570','n02095889','n02096051','n02096177','n02096294','n02096437',
        'n02096585','n02097047','n02097130','n02097209','n02097298','n02097474','n02097658','n02098105','n02098286','n02098413','n02099267',
        'n02099429','n02099601','n02099712','n02099849','n02100236','n02100583','n02100735','n02100877','n02101006','n02101388','n02101556',
        'n02102040','n02102177','n02102318','n02102480','n02102973','n02104029','n02104365','n02105056','n02105162','n02105251','n02105412',
        'n02105505','n02105641','n02105855','n02106030','n02106166','n02106382','n02106550','n02106662','n02107142','n02107312','n02107574',
        'n02107683','n02107908','n02108000','n02108089','n02108422','n02108551','n02108915','n02109047','n02109525','n02109961','n02110063',
        'n02110185','n02110341','n02110627','n02110806','n02110958','n02111129','n02111277','n02111500','n02111889','n02112018','n02112137',
        'n02112350','n02112706','n02113023','n02113186','n02113624','n02113712','n02113799','n02113978']
CATS=['n02123045','n02123159','n02123394','n02123597','n02124075','n02125311','n02127052']


base_model = ResNet50(include_top=True, weights='imagenet', input_tensor=None,
               input_shape=(IMAGE_SIZE[0],IMAGE_SIZE[1],3))
#
# for i, layer in enumerate(base_model.layers):
#    print(i, layer.name)

for root, dirs, files in os.walk(DATASET_PATH):
    for file in files:
        photo_path = os.path.join(DATASET_PATH, file)  # photo path
        #print(photo_path)

        img = (imread(photo_path)[:, :, :3]).astype(np.float32)  # read to ndarray
        x = cv2.resize(img, IMAGE_SIZE)

        # predict the category of the image
        x = preprocess_input(x)
        x = np.expand_dims(x, axis=0)
        y = base_model.predict(x)
        y_top50 = decode_predictions(y, top=50)[0]


        # check if the predicted class belongs to the 108 kinds of dogs or 7 kinds of cats
        # if yes, it's normal image; if not, maybe it's outlier
        for i, cont in enumerate(y_top50):
            if cont[0] in DOGS or cont[0] in CATS:
                break
            if i == 50:
                print("Outlier found:", file)

