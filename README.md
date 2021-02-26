# plotbbox
A package to plot pretty bounding boxes for object detection task





# Install
```python
pip install plotbbox
```

# Example Usage

```python
import cv2
from plotbbox import plotBBox

img = cv2.imread("your_img.png")

label_table = {0: "person", 1: "car"}
color_table = {0: (0, 255, 0), 1: (0, 0, 255)} 

bboxes = your_detection_algorithm(img) # Shape: (N, 5), [:, 0]: class index, [:, 1:]: xmin, ymin, xmax, ymax

for bbox in bboxes:
  
  class_idx = bbox[0]
  xmin, ymin, xmax, ymax = bbox[1:]

  plotBBox(img, xmin, ymin, xmax, ymax, color=color_table[class_idx], thickness=1, label=label_table[class_idx]) # plot bounding box on img

cv2.imwrite("bboxes_plotted_your_img.png", img)
```
