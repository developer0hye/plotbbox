import numpy as np
import cv2
from PIL import ImageFont

import os

__all__ = ["plotBBox"]

TTF_FILE_DIR = os.path.join(os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__))), "Ubuntu-Regular.ttf")

def generate_label_img(label : str, font : ImageFont.FreeTypeFont, text_color=(0, 0, 0), background_color=(255, 255, 255)):
    label_img = font.getmask(label)
    label_img_w, label_img_h = label_img.size
    
    num_img = np.array(label_img).reshape(label_img_h, label_img_w)
    num_img = num_img.astype(np.uint8) # [label_img_h, label_img_w]
    
    text_mask = num_img != 0
    background_mask = num_img == 0
    
    num_img = cv2.cvtColor(num_img, cv2.COLOR_GRAY2BGR) # [label_img_h, label_img_w, 3]

    #change color
    num_img[text_mask] = text_color
    num_img[background_mask] = background_color

    return num_img
    
def plotBBox(img: np.ndarray, 
             xmin: int, ymin: int, xmax: int, ymax: int, color: tuple=(0, 255, 0), thickness: int=1,
             label: str="", font_path: str=TTF_FILE_DIR, font_scale: int=15):
    
    assert type(img) == np.ndarray
    assert len(img.shape) == 3
    assert img.shape[2] == 3

    assert type(xmin) == int
    assert type(ymin) == int
    assert type(xmax) == int
    assert type(ymax) == int

    assert type(color) == tuple
    assert len(color) == 1 or len(color) == 3
    assert all(isinstance(color[i], int) for i in range(len(color)))
    
    assert type(thickness) == int       
    assert type(label) == str

    assert os.path.isfile(font_path)
    
    img_h, img_w = img.shape[:2]
    
    bbox_xmin = np.clip(xmin, 0, img_w-1)
    bbox_ymin = np.clip(ymin, 0, img_h-1)
    bbox_xmax = np.clip(xmax, 0, img_w-1)
    bbox_ymax = np.clip(ymax, 0, img_h-1)
    
    cv2.rectangle(img=img, pt1=(bbox_xmin, bbox_ymin), pt2=(bbox_xmax, bbox_ymax), color=color, thickness=thickness)
    
    if len(label) > 0:
        font = ImageFont.truetype(font_path, font_scale)
        label_img = generate_label_img(label, font, background_color=color)
        
        #paste label_img at top left point of the bounding box
        label_img_h, label_img_w = label_img.shape[:2]
        
        label_xmin = bbox_xmin
        label_ymin = np.clip(bbox_ymin - label_img_h, 0, img_h-1)
        
        label_xmax = np.clip(label_xmin + label_img_w, 0, img_w-1)
        label_ymax = np.clip(label_ymin + label_img_h, 0, img_h-1)
        
        pasted_label_img_h = label_ymax - label_ymin
        pasted_label_img_w = label_xmax - label_xmin
        
        if pasted_label_img_w > 0 and pasted_label_img_h > 0:
            
            if (label_img_h, label_img_w) != (pasted_label_img_h, pasted_label_img_w):
                label_img = cv2.resize(label_img, dsize=(pasted_label_img_w, pasted_label_img_h))

            img[label_ymin:label_ymax, label_xmin:label_xmax] = label_img
