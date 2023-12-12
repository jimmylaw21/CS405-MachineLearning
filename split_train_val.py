import os
import shutil
import numpy as np

def split_data(source_images, source_labels, target_root, train_size=0.7, val_size=0.2):
    # 获取所有图像文件的名称
    files = os.listdir(source_images)
    np.random.shuffle(files)

    # 计算训练集、验证集和测试集的大小
    train_end = int(train_size * len(files))
    val_end = int(val_size * len(files)) + train_end

    # 分配文件到训练集、验证集和测试集
    subsets = {'train': files[:train_end], 'val': files[train_end:val_end], 'test': files[val_end:]}

    for subset, filenames in subsets.items():
        for filename in filenames:
            # 构建源文件和目标文件的路径
            source_image_path = os.path.join(source_images, filename)
            source_label_path = os.path.join(source_labels, filename.replace('.jpg', '.txt'))

            target_image_path = os.path.join(target_root, 'images', subset, filename)
            target_label_path = os.path.join(target_root, 'labels', subset, filename.replace('.jpg', '.txt'))

            # 创建目标文件夹（如果不存在）
            os.makedirs(os.path.dirname(target_image_path), exist_ok=True)
            os.makedirs(os.path.dirname(target_label_path), exist_ok=True)

            # 复制图像文件到目标文件夹
            shutil.copy(source_image_path, target_image_path)

            # 检查标签文件是否存在，如果不存在，则创建一个空文件
            if os.path.exists(source_label_path):
                shutil.copy(source_label_path, target_label_path)
            else:
                open(target_label_path, 'a').close()

# 使用示例
source_images_folder = 'datasets\sustech_night_4k60fps'
source_labels_folder = 'datasets\sustech_night_4k60fps_label\labels'
target_folder = 'datasets\data2'

split_data(source_images_folder, source_labels_folder, target_folder)



# import os
# import random

# img_source_path = 'C:/Users/Administrator/Desktop/cs405/CS405-MachineLearning/datasets/sustech_night_4k60fps/'
# label_source_path = 'C:/Users/Administrator/Desktop/cs405/CS405-MachineLearning/datasets/sustech_night_4k60fps_label/labels/'
# image_path = 'C:/Users/Administrator/Desktop/cs405/CS405-MachineLearning/datasets/data2/images/'
# label_path = 'C:/Users/Administrator/Desktop/cs405/CS405-MachineLearning/datasets/data2/labels/'

# trainval_percent = 0.8
# train_percent = 0.9

# total_img = os.listdir(img_source_path)
# total_txt = os.listdir(label_source_path)
# if not os.path.exists(image_path):
#     os.makedirs(image_path)
# if not os.path.exists(label_path):
#     os.makedirs(label_path)
 
# num = len(total_img)
# list_index = range(num)
# tv = int(num * trainval_percent)
# tr = int(tv * train_percent)
# trainval = random.sample(list_index, tv)
# train = random.sample(trainval, tr)

# img_file_trainval = open(image_path + '/trainval.txt', 'w')
# img_file_test = open(image_path + '/test.txt', 'w')
# img_file_train = open(image_path + '/train.txt', 'w')
# img_file_val = open(image_path + '/val.txt', 'w')

# txt_file_trainval = open(label_path + '/trainval.txt', 'w')
# txt_file_test = open(label_path + '/test.txt', 'w')
# txt_file_train = open(label_path + '/train.txt', 'w')
# txt_file_val = open(label_path + '/val.txt', 'w')
     
# for i in list_index:
#     img_name = img_source_path + total_img[i][:] + '\n'
#     label_name = label_source_path + total_txt[i][:-4] + '.txt\n'
#     if i in trainval:
#         img_file_trainval.write(img_name)
#         if i in train:
#             img_file_train.write(img_name)
#         else:
#             img_file_val.write(img_name)
#     else:
#         img_file_test.write(img_name)
 
# img_file_trainval.close()
# img_file_train.close()
# img_file_val.close()
# img_file_test.close()

# txt_file_trainval.close()
# txt_file_train.close()
# txt_file_val.close()
# txt_file_test.close()

