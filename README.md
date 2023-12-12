# CS405-MachineLearning
This is a repository of CS405-Machine Learning project, relative to SUStech, object detection for traffic and yolo.

### 文件结构

**datasets/**

放置数据源（images和labels，使用x-anylabeling标注），命名举例：sustech_night_4k60fps，sustech_night_4k60fps_label

可训练的数据集（images和labels，train，val，test），命名举例：data1

**document/**

放置各种项目文档，报告展示文档

**models/**

放置模型

**some scripts...**

split_train_val.py 将数据源制作成数据集

video2img.py 将视频转为图像集，默认1秒2张
