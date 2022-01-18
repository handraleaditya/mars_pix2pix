import numpy as np
import os
from PIL import Image

path = "./mars/train/"


for file in os.listdir(path):
    img = Image.open(path + file)
    arr = np.array(img)
    new_arr = np.stack((arr,)*3, axis=-1)
    print(new_arr.shape)
    new_img = Image.fromarray(new_arr)
    new_img.save(f"./mars/rgb_train/{file}")


