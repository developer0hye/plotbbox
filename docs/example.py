import cv2
import numpy as np
from plotbbox import plotBBox

import os
from pathlib import Path

np.random.seed(7777)

def load_dataset(root):
    imgs_path = []
    labels_path = []

    for r, d, f in os.walk(root):
        for file in f:
            if file.lower().endswith((".png", ".jpg", ".bmp")):
                img_path = os.path.join(r, file).replace(os.sep, '/')
                label_path = Path(img_path).with_suffix('.txt')
                
                if os.path.isfile(img_path) and os.path.isfile(label_path):                                    
                    imgs_path.append(img_path)
                    labels_path.append(label_path)
            
    return imgs_path, labels_path


VOC_CLASSES = (  # always index 0
    'aeroplane', 'bicycle', 'bird', 'boat',
    'bottle', 'bus', 'car', 'cat', 'chair',
    'cow', 'diningtable', 'dog', 'horse',
    'motorbike', 'person', 'pottedplant',
    'sheep', 'sofa', 'train', 'tvmonitor')

class_label_table = {}
color_table = {}

for idx, label in enumerate(VOC_CLASSES):
    class_label_table[idx] = label
    color_table[idx] = np.random.randint(0, 256, size=3).tolist()

imgs_path, labels_path = load_dataset("./images")
labels = [np.loadtxt(label_path, dtype=np.float32, delimiter=' ').reshape(-1, 5) for label_path in labels_path]

for idx_img, (img_path, label) in enumerate(zip(imgs_path, labels)):
    img = cv2.imread(img_path)
    img_h, img_w = img.shape[:2]
    bboxes = label
    # bboxes[0]: class_idx
    # bboxes[1:]: normalized xywh
    
    bboxes[:, [1, 3]] *= img_w
    bboxes[:, [2, 4]] *= img_h
    
    for bbox in bboxes:
        c = int(bbox[0])
        
        x, y, w, h = bbox[1:]
        
        xmin = int(x - w / 2)
        ymin = int(y - h / 2)
        xmax = int(x + w / 2)
        ymax = int(y + h / 2)

        class_label = class_label_table[c]
        color = color_table[c]
        
        plotBBox(img, 
                 xmin, ymin, xmax, ymax, color=tuple(color), thickness=3, 
                 label=class_label, font_scale=20)
    
    cv2.imwrite(str(idx_img).zfill(3)+".png", img)