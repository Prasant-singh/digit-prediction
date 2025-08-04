import os
import random

path = 'digit0to9/test/images'
images = os.listdir(path)


image_files = [f for f in images ]

if not image_files:
    print(f"No image files found in {path}")
else:
   
    random_image_filename = random.choice(image_files)
    full_image_path = os.path.join(path, random_image_filename)

full_image_path="download.webp"  # Use the downloaded image path directly

from ultralytics import YOLO

model = YOLO("runs/detect/yolo_custom_model/weights/best.pt")

model.predict(
    source=f"{full_image_path}",
    save=True
)