import numpy as np
from tensorflow.keras.preprocessing import image

def load_and_preprocess(img_file, target_size=(128, 128)):
    img = image.load_img(img_file, target_size=target_size)
    img_array = image.img_to_array(img)
    img_array = img_array / 255.0
    return np.expand_dims(img_array, axis=0)