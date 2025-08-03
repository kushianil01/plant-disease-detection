import os
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.callbacks import ModelCheckpoint, EarlyStopping

# Paths
DATA_DIR = "PlantVillage"
MODEL_PATH = "plant_disease_app/model/plant_disease_model.keras"
CLASSES_PATH = "plant_disease_app/model/classes.txt"
IMG_SIZE = 128
BATCH_SIZE = 32
EPOCHS = 20

# Data loading
datagen = ImageDataGenerator(rescale=1./255, validation_split=0.2,
                             rotation_range=20, zoom_range=0.2,
                             width_shift_range=0.1, height_shift_range=0.1,
                             shear_range=0.1, horizontal_flip=True)

train_gen = datagen.flow_from_directory(
    DATA_DIR, target_size=(IMG_SIZE, IMG_SIZE), batch_size=BATCH_SIZE,
    class_mode='categorical', subset='training', shuffle=True)

val_gen = datagen.flow_from_directory(
    DATA_DIR, target_size=(IMG_SIZE, IMG_SIZE), batch_size=BATCH_SIZE,
    class_mode='categorical', subset='validation')

model = Sequential([
    Conv2D(32, (3,3), activation='relu', input_shape=(IMG_SIZE, IMG_SIZE, 3)),
    MaxPooling2D(2,2),
    Conv2D(64, (3,3), activation='relu'),
    MaxPooling2D(2,2),
    Conv2D(128, (3,3), activation='relu'),
    MaxPooling2D(2,2),
    Flatten(),
    Dropout(0.5),
    Dense(128, activation='relu'),
    Dense(train_gen.num_classes, activation='softmax')
])

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

os.makedirs(os.path.dirname(MODEL_PATH), exist_ok=True)

model.fit(train_gen, validation_data=val_gen, epochs=EPOCHS,
          callbacks=[ModelCheckpoint(MODEL_PATH, save_best_only=True, monitor='val_accuracy'),
                     EarlyStopping(patience=5, restore_best_weights=True)])

# Save class names
with open(CLASSES_PATH, "w") as f:
    f.write("\n".join(train_gen.class_indices.keys()))
