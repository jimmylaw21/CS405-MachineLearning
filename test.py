from ultralytics import YOLO
import torch

if __name__ == '__main__':
    print(torch.__version__)
    print(torch.cuda.is_available())

    model = YOLO("models/yolov8n.pt")
    results = model.train(data="datasets/data1/mydata.yaml", epochs=3)  # train the model
    val = model.val()  # evaluate model performance on the validation set
    predict = model("https://ultralytics.com/images/bus.jpg")  # predict on an image
