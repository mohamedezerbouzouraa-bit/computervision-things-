import torch
import numpy as np

def images_to_tensor(images):
    num_images = len(images)
    batch = torch.zeros(num_images, 3, 224, 224, dtype=torch.float32)

    for i, img in enumerate(images):
        img_t = torch.from_numpy(img)
        img_t = img_t.permute(2, 0, 1)
        img_t = img_t.float() / 255.0
        batch[i] = img_t

    return batch


def tensor_to_numpy(tensor):
     return tensor.numpy()


def tensor_to_gpu(tensor):
    if torch.cuda.is_available():
        return tensor.to("cuda")
    return tensor
