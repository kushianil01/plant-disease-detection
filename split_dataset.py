import os
import shutil
import random
from tqdm import tqdm

# === CONFIG ===
SOURCE_DIR = 'PlantVillage'  # the original folder with 9 class folders
DEST_DIR = 'PlantVillageSplit'  # will contain train/val/test subfolders
SPLIT_RATIOS = (0.7, 0.15, 0.15)  # train, val, test

# === START ===
def create_dirs(base, class_names):
    for split in ['train', 'val', 'test']:
        for cls in class_names:
            os.makedirs(os.path.join(base, split, cls), exist_ok=True)

def split_class_images(class_path, train_ratio, val_ratio, test_ratio):
    images = os.listdir(class_path)
    images = [img for img in images if img.lower().endswith(('.jpg', '.jpeg', '.png'))]
    random.shuffle(images)
    
    total = len(images)
    train_end = int(total * train_ratio)
    val_end = train_end + int(total * val_ratio)
    
    return images[:train_end], images[train_end:val_end], images[val_end:]

def main():
    random.seed(42)
    class_names = [folder for folder in os.listdir(SOURCE_DIR) 
                   if os.path.isdir(os.path.join(SOURCE_DIR, folder))]

    print("Found classes:", class_names)

    create_dirs(DEST_DIR, class_names)

    for cls in tqdm(class_names, desc="Splitting classes"):
        src_path = os.path.join(SOURCE_DIR, cls)
        train_imgs, val_imgs, test_imgs = split_class_images(src_path, *SPLIT_RATIOS)

        for img in train_imgs:
            shutil.copy(os.path.join(src_path, img), os.path.join(DEST_DIR, 'train', cls, img))
        for img in val_imgs:
            shutil.copy(os.path.join(src_path, img), os.path.join(DEST_DIR, 'val', cls, img))
        for img in test_imgs:
            shutil.copy(os.path.join(src_path, img), os.path.join(DEST_DIR, 'test', cls, img))

    print("\n✅ Dataset split complete. Check the 'PlantVillageSplit' folder.")

if __name__ == "__main__":
    main()
