import os
import cv2

def load_images_from_directory(data_dir):

    image_files = [f for f in os.listdir(data_dir) if f.endswith(".jpg") or f.endswith(".png")]

    images = []

    for filename in image_files:

        path = os.path.join(data_dir, filename)

        img = cv2.imread(path)

        img = cv2.resize(img, (224, 224))

        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        images.append(img)

    return images
