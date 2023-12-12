from ultralytics import YOLO

model = YOLO('ultralytics/cfg/models/v8/yolov8-linearAttention.yaml')
model.train(cfg='ultralytics/cfg/automaticDriver.yaml', data='ultralytics/cfg/datasets/mydata.yaml')
