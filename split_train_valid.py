import random
import os
import shutil

scr = 'data\\all_clean_data'
dst = 'data\\data_1031\\valid'

cont = os.listdir(scr)
# walk all the paths
for root, dirs, files in os.walk(scr):
    for d in dirs:
        for i in range(0, 2500):
            rand = random.randint(1, 12470)
            tmp = rand
            fileNm = d + '.' + str(rand) + '.jpg'

            scr_path = os.path.join(scr, d, fileNm)
            #print(scr_path)
            dst_path = os.path.join(dst, d)
            #print(dst_path)

            # since we have some outliers deleted, need to check if the file exists or not.
            while not os.path.exists(scr_path):
                tmp = tmp - 1
                fileNm = d + '.' + str(tmp) + '.jpg'
                scr_path = os.path.join(scr, d, fileNm)

            # copy the file from source folder to destination folder
            shutil.copy(scr_path, dst_path)
            os.remove(scr_path)

            print(fileNm)




