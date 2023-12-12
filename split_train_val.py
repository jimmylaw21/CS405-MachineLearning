import os
import random

img_source_path = 'C:\\Users\\Administrator\\Desktop\\cs405\\CS405-MachineLearning\\dataset\\sustech_night_4k60fps'
label_source_path = 'C:\\Users\\Administrator\\Desktop\\cs405\\CS405-MachineLearning\\dataset\\sustech_night_4k60fps_label\\labels'
image_path = 'C:\\Users\\Administrator\\Desktop\\cs405\\CS405-MachineLearning\\dataset\\data2\\image'
label_path = 'C:\\Users\\Administrator\\Desktop\\cs405\\CS405-MachineLearning\\dataset\\data2\\label'

trainval_percent = 0.8
train_percent = 0.9

total_img = os.listdir(img_source_path)
total_txt = os.listdir(label_source_path)
if not os.path.exists(image_path):
    os.makedirs(image_path)
if not os.path.exists(label_path):
    os.makedirs(label_path)
 
num = len(total_img)
list_index = range(num)
tv = int(num * trainval_percent)
tr = int(tv * train_percent)
trainval = random.sample(list_index, tv)
train = random.sample(trainval, tr)

img_file_trainval = open(image_path + '/trainval.txt', 'w')
img_file_test = open(image_path + '/test.txt', 'w')
img_file_train = open(image_path + '/train.txt', 'w')
img_file_val = open(image_path + '/val.txt', 'w')

txt_file_trainval = open(label_path + '/trainval.txt', 'w')
txt_file_test = open(label_path + '/test.txt', 'w')
txt_file_train = open(label_path + '/train.txt', 'w')
txt_file_val = open(label_path + '/val.txt', 'w')
     
for i in list_index:
    img_name = img_source_path + total_img[i][:] + '\n'
    if i in trainval:
        img_file_trainval.write(img_name)
        if i in train:
            img_file_train.write(img_name)
        else:
            img_file_val.write(img_name)
    else:
        img_file_test.write(img_name)
 
img_file_trainval.close()
img_file_train.close()
img_file_val.close()
img_file_test.close()

txt_file_trainval.close()
txt_file_train.close()
txt_file_val.close()
txt_file_test.close()
