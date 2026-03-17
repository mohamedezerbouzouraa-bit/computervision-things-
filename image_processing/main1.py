from image_processing.load_images import load_images_from_directory
from image_processing.tensor_conversion import images_to_tensor
from image_processing.tensor_conversion import tensor_to_numpy
from image_processing.tensor_conversion import tensor_to_gpu

data_dir = "images"

images = load_images_from_directory(data_dir)

batch_tensor = images_to_tensor(images)

batch_numpy = tensor_to_numpy(batch_tensor)

batch_gpu = tensor_to_gpu(batch_tensor)

print("Tensor shape:", batch_tensor.shape)

print("Numpy shape:", batch_numpy.shape)

print("Device:", batch_gpu.device)
