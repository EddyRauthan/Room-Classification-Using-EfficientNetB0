import random
import shutil 
import os

VALID_EXTS = {".jpg", ".jpeg", ".png", ".bmp", ".webp"}

# def collect_image(class:path):
#     return sorted([p for p in class.iterdir() if p.suffix.lower() in VALID_EXTS])

random.seed(42)

source = "room dataset"
destination = "split_dataset"

train_ratio = 0.7
test_ratio = 0.15
val_ratio = 0.15

dirs = [d for d in os.listdir(source) if os.path.isdir(os.path.join(source, d))]

for dir in dirs:
    
    images = [i for i in os.listdir(os.path.join(source, dir)) if os.path.splitext(i)[1].lower() in VALID_EXTS]
    random.shuffle(images)
    
    total = len(images)
    
    train_count = int(total * train_ratio)
    val_count = train_count + int(total * val_ratio)
    
    split = {
        
        "train": images[:train_count],
        "val": images[train_count:val_count],
        "test": images[val_count:]
    }
    
    for name, images in split.items():
        dest_dir = os.path.join(destination, name, dir)
        os.makedirs(dest_dir, exist_ok=True)
        
        for image in images:
            src_path = os.path.join(source, dir, image)
            dest_path = os.path.join(dest_dir, image)
            shutil.copy(src_path, dest_path)
            
            
print(f"{dir:15s} train={len(split['train']):4d} val={len(split['val']):4d} test={len(split['test']):4d}")