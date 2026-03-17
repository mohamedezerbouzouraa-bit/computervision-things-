from PIL import Image
import numpy as np

img = Image.open("ezerpic.jpg")
img = img.convert('L')
pixels = np.array(img) / 255.0
pixels = pixels ** 2
pixels = (pixels * 255).astype(np.float32)
new_img = Image.fromarray(pixels)

new_img.save("finalresult.jpg")
