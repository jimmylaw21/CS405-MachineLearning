import cv2
import os

IMG_PER_SEC = 2
VIDEO_NAME = 'sustech_night_4k60fps'

video_path = 'dataset/' + VIDEO_NAME + '.mp4'
output_folder = 'dataset/' + VIDEO_NAME


os.makedirs(output_folder, exist_ok=True)

cap = cv2.VideoCapture(video_path)

fps = int(cap.get(cv2.CAP_PROP_FPS))

feq = fps // IMG_PER_SEC

frame_count = 0

while True:
    ret, frame = cap.read()

    if not ret:
        break

    if frame_count % feq == 0:
        frame_filename = os.path.join(output_folder, f"frame_{frame_count // feq}.jpg")
        cv2.imwrite(frame_filename, frame)

    frame_count += 1

# 释放视频对象
cap.release()

print(f"抽取了 {frame_count // feq} 帧到 {output_folder} 文件夹中。")

